---
title: 一键搭建 Argo Tunnel + Xray科学上网（支持 Reality、VLESS/VMESS/Trojan/SS+WS）｜不暴露端口更安全｜订阅自适配多客户端
date: '2025-11-11 12:00:00'
tags:
- 科学上网
categories:
- 科学上网
description: 1、下载并安装SSH连接工具Finalshell：【 点击进入 】 2、登录Cloudflare：【 点击进入 】 3、开源项目：【 点击进入 】 bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/argox/
---
1、下载并安装SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

2、登录Cloudflare：【[点击进入](https://dash.cloudflare.com/login)】

3、开源项目：【[点击进入](https://github.com/fscarmen/ArgoX)】
[code]
    bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/argox/main/argox.sh)Copy
[/code]

  * 修改配置文件：/etc/argox
    * 修改path路径，根据inbound.json的配置更改
    * /-vl?ed=2048改成/argox-vl
    * /-vm?ed=2048改成/argox-vm
    * /-tr?ed=2048改成/argox-tr
