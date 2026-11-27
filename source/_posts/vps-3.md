---
title: 一键查路由：自研脚本带你从家宽到 VPS、再到目标网站做全链路追踪
date: '2025-11-25 12:00:00'
cover: /img/covers/vps-3.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 1、下载并安装SSH连接工具Finalshell：【 点击进入 】 2、客户端——VPS路由信息查询 IP地址查询：【 点击进入 】 电脑端——VPS 路由 tracert -w 3000 -h 30 VPS_IP Copy 归属/地理/ASN查询 curl.exe -s htt
---
1、下载并安装SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】  
  
2、客户端——VPS路由信息查询

  * IP地址查询：【[点击进入](https://ss.sloby.cn/#/)】

  * 电脑端——VPS 路由

[code]
    tracert -w 3000 -h 30 VPS_IPCopy
[/code]

  * 归属/地理/ASN查询

[code]
    curl.exe -s https://ipinfo.io/路由IPCopy
[/code]

  * 一键查询所有路由信息（用终端管理员执行）

[code]
    $target = 'VPS_IP'   # 目标：可以填你 VPS 或网站 IP
    $raw = tracert -d -w 3000 -h 30 $target
    
    $rows = @()
    foreach ($line in $raw) {
      if ($line -match '^\s*(\d+)\s+.*?(\d{1,3}(?:\.\d{1,3}){3})') {
        $hop = [int]$matches[1]
        $ip  = $matches[2]
    
        # 抓三次时延（如果有 * 则忽略）
        $rtts = ([regex]::Matches($line, '(\d+)\s*ms') | ForEach-Object { [int]$_.Groups[1].Value })
        $rttAvg = if ($rtts.Count -gt 0) { [math]::Round(($rtts | Measure-Object -Average).Average,1) } else { $null }
    
        # 查询 ip-api
        try {
          $a = Invoke-RestMethod -Uri ("http://ip-api.com/json/{0}?lang=zh-CN&fields=country,regionName,city,as,isp,org" -f $ip) -TimeoutSec 5
          $a_loc = "{0} {1} {2}" -f $a.country,$a.regionName,$a.city
          $a_asn = $a.as; $a_isp = $a.isp; $a_org = $a.org
        } catch { $a_loc='?'; $a_asn='?'; $a_isp='?'; $a_org='?' }
    
        # 查询 ipinfo
        try {
          $b = Invoke-RestMethod -Uri ("https://ipinfo.io/{0}/json" -f $ip) -TimeoutSec 5
          $b_loc = $b.country
          if ($b.city) { $b_loc = "$($b.country) $($b.region) $($b.city)" }
          $b_asn = if ($b.org) { $b.org } else { '?' }
        } catch { $b_loc='?'; $b_asn='?' }
    
        # 反向解析 PTR（公共DNS）
        try {
          $ptr = (Resolve-DnsName -Type PTR -Server 8.8.8.8 $ip -ErrorAction Stop).NameHost
        } catch { $ptr = $null }
    
        $rows += [pscustomobject]@{
          跳数 = $hop
          IP   = $ip
          平均RTTms = $rttAvg
          ASN1 = $a_asn
          ISP1 = $a_isp
          位置1 = $a_loc
          ASN2_orORG = $b_asn
          位置2 = $b_loc
          PTR  = $ptr
        }
      }
    }
    $rows | Sort-Object 跳数 | Format-Table -AutoSize
    Copy
[/code]

3、VPS（Linux）——目标网站路由信息查询

  * 安装依赖

[code]
    sudo apt update && sudo apt install -y mtr-tiny curl jq dnsutils tracerouteCopy
[/code]

  * 一键查询VPS——目标网站的所有路由信息
    * 把下面整段在 VPS 上粘贴执行（会生成 `routeview.sh`，覆盖旧的）

[code]
    cat > routeview.sh <<'BASH'
    #!/usr/bin/env bash
    set -euo pipefail
    
    usage() {
      echo "用法: $0 [--tcp PORT]|[--icmp] [--debug] <目标域名或IP>"
      echo "示例: $0 google.com"
      echo "      $0 --tcp 443 google.com"
    }
    
    PROTO="tcp"; PORT="443"; TARGET=""; DEBUG=0
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --tcp)  PROTO="tcp"; PORT="${2:-443}"; shift 2;;
        --icmp) PROTO="icmp"; shift;;
        --debug) DEBUG=1; shift;;
        -h|--help) usage; exit 0;;
        *) TARGET="$1"; shift;;
      esac
    done
    [[ -z "${TARGET}" ]] && { usage; exit 1; }
    
    need=()
    for t in mtr curl jq dig awk sed grep traceroute; do
      command -v "$t" >/dev/null 2>&1 || need+=("$t")
    done
    if [[ ${#need[@]} -gt 0 ]]; then
      echo "缺少依赖: ${need[*]}"
      echo "Debian/Ubuntu: sudo apt install -y mtr-tiny curl jq dnsutils traceroute"
      exit 2
    fi
    
    tmp="$(mktemp)"
    if [[ "$PROTO" == "tcp" ]]; then
      echo ">>> 正在用 TCP:${PORT} 方式探测: ${TARGET}"
      # 不同版本 mtr 的 report 宽度/列位会变化，使用 -n 仅数字，-r 报告模式
      mtr -n -r -w -z -c 20 --tcp -P "$PORT" "$TARGET" > "$tmp" || true
    else
      echo ">>> 正在用 ICMP 方式探测: ${TARGET}"
      mtr -n -r -w -z -c 20 "$TARGET" > "$tmp" || true
    fi
    [[ $DEBUG -eq 1 ]] && { echo "---- RAW MTR ----"; cat "$tmp"; echo "-----------------"; }
    
    # 尝试从 mtr 报告抽取：hop ip avg
    # 兼容两种常见行：
    #  1) " 1.|-- 1.1.1.1  0.0%  20  1.0  1.5  0.8  3.2  0.5"
    #  2) " 1.  1.1.1.1  ... Avg"
    mapfile -t LINES < <(awk '
      /^\s*[0-9]+(\.\|\-\-|\.)/ {
        hop=$1
        gsub(/\..*/,"",hop)  # 提取数字
        # 找第一个 IPv4
        ip=""
        for(i=1;i<=NF;i++){ if($i ~ /^([0-9]{1,3}\.){3}[0-9]{1,3}$/){ ip=$i; break } }
        # 找 Avg 列（mtr 报告第7列通常是 Avg；为了保险，从右向左找一个小数）
        avg=""
        for(i=NF;i>=1;i--){ if($i ~ /^[0-9]+(\.[0-9]+)?$/){ avg=$i; break } }
        if(ip!=""){ print hop, ip, avg }
      }
    ' "$tmp")
    
    if [[ ${#LINES[@]} -eq 0 ]]; then
      echo ">>> mtr 没抽到 hop，改用 traceroute 兜底 ..."
      trf="$(mktemp)"
      traceroute -n -w 2 -q 1 "$TARGET" > "$trf" || true
      [[ $DEBUG -eq 1 ]] && { echo "---- RAW TRACEROUTE ----"; cat "$trf"; echo "------------------------"; }
      mapfile -t LINES < <(awk '
        /^[ ]*[0-9]+[ ]+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ {
          hop=$1; ip=$2;
          avg="-";
          for(i=3;i<=NF;i++){ if($i ~ /ms$/){ gsub(/ms/,"",$i); avg=$i; break } }
          print hop, ip, avg
        }
      ' "$trf")
    fi
    
    printf "\n%-4s %-16s %-8s %-18s %-18s %-26s %-28s %-40s\n" "跳数" "IP" "Avg(ms)" "ASN(ip-api)" "ISP(ip-api)" "位置(ip-api)" "ORG(ipinfo)" "PTR"
    printf "%0.s-" {1..160}; echo
    
    for row in "${LINES[@]}"; do
      hop="$(awk '{print $1}' <<<"$row")"
      ip="$(awk '{print $2}' <<<"$row")"
      avg="$(awk '{print $3}' <<<"$row")"
    
      # ip-api
      a_json="$(curl -s "http://ip-api.com/json/${ip}?lang=zh-CN&fields=status,country,regionName,city,as,isp,org")"
      a_ok="$(jq -r '.status // "fail"' <<<"$a_json")"
      if [[ "$a_ok" == "success" ]]; then
        ASN="$(jq -r '.as // "?"' <<<"$a_json")"
        ISP="$(jq -r '.isp // "?"' <<<"$a_json")"
        LOC="$(jq -r '[.country,.regionName,.city]|map(select(.!=null and .!=""))|join(" ")' <<<"$a_json")"
      else
        ASN="?" ; ISP="?" ; LOC="?"
      fi
    
      # ipinfo
      b_json="$(curl -s "https://ipinfo.io/${ip}/json")"
      ORG="$(jq -r '.org // "?"' <<<"$b_json")"
    
      PTR="$(dig +short -x "$ip" @8.8.8.8 | sed -n '1p')"
      [[ -z "$PTR" ]] && PTR="-"
    
      printf "%-4s %-16s %-8s %-18s %-18s %-26s %-28s %-40s\n" "$hop" "$ip" "$avg" "$ASN" "$ISP" "$LOC" "$ORG" "$PTR"
    done
    
    echo -e "\n提示：\n- 看“跳数”顺序来理解路由拓扑；\n- 位置字段为多源数据库估算，仅作参考；\n- 以 ASN/运营商 + 时延增量判断区域更可靠。"
    BASH
    chmod +x routeview.sh
    echo "已生成 ./routeview.sh"
    Copy
[/code]

  * 用法（如查询VPS——Google的路由信息）
    * 红色部分替换成自己想要查询的网站

[code]
    #TCP 443（推荐，贴近浏览器访问）
    ./routeview.sh --tcp 443 google.com
    
    #ICMP（传统 ping/trace）
    ./routeview.sh google.com
    Copy
[/code]

  * 路由信息查询（适合查询机场节点）：【[点击进入](https://tools.ipip.net/traceroute.php)】
