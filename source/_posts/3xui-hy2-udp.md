---
title: 3XUI 搭建 HY2 节点：UDP 端口跳跃配置与不生效排障
date: '2026-11-08 12:00:00'
cover: https://picsum.photos/seed/3xui-hy2-udp/800/450
tags:
- 节点搭建
categories:
- 节点搭建
description: '# HY2 # 3XUI # VPS 之前多是 VLESS 加 Reality，走 TCP，晚高峰丢包严重时速度会受影响。这期用 3XUI 面板搭 Hysteria2：UDP 的 QUIC 传输、自带拥塞控制，重点是把 UDP 端口跳跃配通——配完发现不生效，问题出在 v2ray'
---
#

HY2

#

3XUI

#

VPS

之前多是 VLESS 加 Reality，走 TCP，晚高峰丢包严重时速度会受影响。这期用 3XUI 面板搭 Hysteria2：UDP 的 QUIC 传输、自带拥塞控制，重点是把 UDP 端口跳跃配通——配完发现不生效，问题出在 v2rayN 的核心类型，换成 sing-box 再做端口转发才算真通。

![3XUI 搭建 HY2 节点：UDP 端口跳跃配置与不生效排障-1](https://www.cunzhangblog.com/api/blob/images/a930d476b84db4ecedd2af83260d893e186f6b3e.webp)

Hysteria2，简称 HY2，是一种基于 UDP 的 QUIC 传输代理协议，自带拥塞控制机制。在高延迟、丢包比较严重的网络环境下，它的传输表现往往比走 TCP 的协议更好，不过也不是在所有场景下都一定更快。

这篇讲的是用 3XUI 面板搭建一个 HY2 节点，重点是把 UDP 端口跳跃配通，以及跳跃不生效时的排查办法。

之前多是 VLESS 加 Reality 的方案，走的是 TCP，搭建相对简单、日常使用也比较稳定。这期换成 HY2，看看它在不太理想的网络环境下表现怎么样。

## 准备：搬瓦工 VPS 与重装系统

我用的是一台搬瓦工的 VPS。搬瓦工官网：<https://bandwagonhost.com/aff.php?aff=85093>

先在搬瓦工后台把服务器停掉，然后重装系统，我这里选的是 Debian 12。重装完成后会给出新的密码和端口，记下来备用。

BandwagonHost Basic 基础型（2GB / 3核）

年付 洛杉矶 入门

  * 机房：美国洛杉矶
  * CPU：3 核
  * 内存：2GB RAM
  * 硬盘：40GB SSD
  * 流量：2TB / 月（1Gbps）
  * 特点：年付约合每月 8.33 美元，长期自建的入门档

$99.99 / 年

[🔗 立即订购 →](https://bandwagonhost.com/aff.php?aff=85093)

适合：个人 / 几人小团队长期自建节点

## 安装 3XUI 面板

[WEBSHARE代理 IP快速可靠的代理，免费领 10 个✓无需信用卡✓99.7% 成功率✓8000 万+ 全球 IPWEBSHARE1,000 Proxies Available31.87.93.32连接11.07.21.53连接67.73.17.29连接免费领取 ↗](https://www.webshare.io/?referral_code=s0mgk1vw9ggr)

用 FinalShell 以 root 身份 SSH 连上 VPS。FinalShell官网：<https://www.hostbuf.com/>

面板的一键安装命令如下：
[code]
    bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)
[/code]

安装时数据库选 1，面板端口保持默认不自定义，证书选第一个。面板需要绑定一个域名并申请 https，我是在 Cloudflare 里加一条 A 记录，名称随便写一个，指向搬瓦工的 IP，并把代理状态关掉。

Cloudflare官网：<https://www.cloudflare.com/>

域名填进安装程序后，默认用 80 端口，证书选自动续期并应用。装好后把登录 URL、用户名和密码记录下来，用它们登录 3XUI 面板。

## 新建 HY2 入站并开启端口跳跃

在面板的入站里新建一条规则，备注写 HY2，协议选 Hysteria，端口保持默认，传输保持默认，把 QUIC 打开，再把 UDP Hop 打开。

UDP Hop 就是 UDP 端口跳跃。正常情况下 HY2 节点用的是固定的 UDP 端口，客户端每次连接都走这个端口，一旦这个端口受到针对性的限制，就可能连接失败或者不稳定。

端口跳跃是让客户端可以在指定范围内切换端口，我这里设的是 30000 到 31000，一共 1001 个端口。服务器通过端口转发规则，把收到的数据交给真正监听固定端口的 HY2 服务。这样即使某一个端口受限，其他端口也能正常工作。

需要注意的是，开启了端口跳跃，不代表 HY2 要同时监听这 1001 个端口。HY2 服务仍然只监听前面入站的固定端口，我这里是 15843。

安全设置里，SNI 填上面绑定的域名，ALPN 在默认的 H3 后面再加上 H2 和 HTTP/1.1，证书从面板设置里自动填入公钥和私钥，然后创建。

## 添加客户端并导入 v2rayN

入站建好后添加一个客户端，备注写 HY2，关联入站选刚刚搭建的 HY2，创建后打开二维码，把节点信息复制出来，导入 v2rayN 就可以用了。

v2rayN下载：<https://github.com/2dust/v2rayN>

## 排查：端口跳跃没生效

导入之后我先测了一下延迟，结果不太对。按理说这个时候还没有做端口转发，应该是测不通的，但它却显示有延迟，说明流量根本没走跳跃端口。

先在 VPS 上装一个抓包工具：（如果已经安装，则跳过这一步）
[code]
    apt update && apt install tcpdump -y
[/code]

装好后监控跳跃端口范围：
[code]
    tcpdump -ni any 'udp portrange 30000-31000'
[/code]

跑起来没有任何反应。再换一条命令，同时监控固定端口和跳跃端口：
[code]
    tcpdump -ni any 'udp port 15843 or udp portrange 30000-31000'
[/code]

这下能看到，流量一直在走固定端口 15843，说明前面设置的跳跃规则压根没有生效。

温馨提示：上面这条监控命令如果不是 root 账户登录，也可以用 sudo 执行，效果完全相同：
[code]
    sudo tcpdump -ni any 'udp portrange 30000-31000'
[/code]

我去查了一下，GitHub 上有个情况和我一样的 issue：端口跳跃不生效，是 Xray、sing-box 内核这边的问题。v2rayN 里核心类型默认用的是 Xray，哪怕设置了端口跳跃，它还是走固定端口联网，跳跃功能等于没开。

解决办法是把核心类型改成 sing-box。再测一次延迟，变成 -1 了，这才是对的：因为 VPS 上还没做端口转发，连不上网是正常的。如果没做转发之前就能连上网，那反而说明不正常。

## 端口转发：把跳跃范围指到 15843(重要)

接下来去 VPS 上做端口转发，核心命令是把 UDP 30000 到 31000 的流量统一转发到 HY2 实际监听的 15843：
[code]
    iptables -t nat -A PREROUTING -p udp --dport 30000:31000 -j REDIRECT --to-ports 15843
[/code]

转发完回到 v2rayN 再测，延迟能测通了，这才算端口转发完成。端口按你自己的实际配置来改，不用照抄我的数字。

## 验证转发确实生效

转发通了之后，还要确认它真的在走跳跃端口，而不是又回到了固定端口。先看转发规则的计数器，每隔 1 秒刷新一次：
[code]
    watch -n 1 'iptables -t nat -L PREROUTING -n -v -x --line-numbers'
[/code]

随便打开几个网站，能看到计数一直在增加，说明转发规则已经生效。再换一条命令，直接看客户端实际访问的目标端口变化：
[code]
    tcpdump -ni any 'udp dst portrange 30000-31000'
[/code]

能看到很多端口在跑，比如 30097，这就确认客户端正在使用跳跃范围内的端口，而不是最开始那个固定端口 15843。

## 给 Clash 开订阅

很多伙伴习惯用 Clash 客户端。面板的订阅链接页面默认只有一个订阅，没有 Clash 的订阅，需要去面板设置里开通。

面板设置——订阅设置——打开“Clash/Mihomo订阅”——Clash/Mihomo——打开“启用路由”

回到订阅链接页面刷新，就能看到多出来了一个 Clash 的订阅，复制链接导入自己的 Clash 客户端就可以用了。

本文为实测记录，操作请遵守相关平台服务条款。
