---
title: 2026年3X-UI 最新版 Hysteria2 歇斯底里2 端口跳跃实战 保姆级教程
date: '2026-08-04 12:00:00'
cover: /img/covers/20263x-ui-hysteria2-2.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 视频 项目地址 https://github.com/MHSanaei/3x-ui Final shell 下载 https://www.hostbuf.com/t/988.html 3X-UI脚本 bash <(curl -Ls https://raw.githubuserco
---
视频

项目地址  
https://github.com/MHSanaei/3x-ui

Final shell 下载  
https://www.hostbuf.com/t/988.html

3X-UI脚本  
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)

cloudflare  
https://dash.cloudflare.com/

clash-verge-rev  
https://github.com/clash-verge-rev/clash-verge-rev

v2rayn  
https://github.com/2dust/v2rayN

假设节点端口 35406 跳跃端口 48000:50000 你的多少就修改一下相对应的端口即可

# 更新软件源

 ______
[code]
    apt update -y 
[/code]

# 安装 iptables、ip6tables 及规则持久化工具

 ______
[code]
    apt install -y iptables iptables-persistent
[/code]

转发命令

 ______
[code]
    iptables -t nat - A PREROUTING -p udp --dport 48000:50000 -j REDIRECT --to-ports 35406  
    ---  
    ip6tables -t nat -A PREROUTING -p udp --dport 48000:50000 -j REDIRECT --to-ports 35406
[/code]  
  
观看是不是真正成功端口跳跃  
tcpdump -ni any udp port 26142 or portrange 48000-50000
