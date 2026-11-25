---
title: s-ui科学上网面板进阶玩法|一键脚本搭建教程|可视化S-UI面板
date: '2025-11-18 12:00:00'
tags:
- 节点分享
categories:
- 节点分享
description: 、下载SSH连接工具Finalshell：【 点击进入 】 2、域名解析：【 点击进入 】 3、开源项目地址：【 点击进入 】 4、关闭防火墙（ 注意：不同平台/系统，关闭防火墙的设置有所不一样，请根据实际情况来 ） sudo ufw disable Copy 5、一键申请SSL
---
、下载SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

2、域名解析：【[点击进入](https://dash.cloudflare.com/)】

3、开源项目地址：【[点击进入](https://github.com/alireza0/s-ui)】

4、关闭防火墙（注意：不同平台/系统，关闭防火墙的设置有所不一样，请根据实际情况来）
[code]
    sudo ufw disableCopy
[/code]

5、一键申请SSL证书
[code]
    bash <(curl -fsSL https://raw.githubusercontent.com/slobys/SSL-Renewal/main/acme.sh)Copy
[/code]

6、一键搭建脚本
[code]
    bash <(curl -Ls https://raw.githubusercontent.com/alireza0/s-ui/master/install.sh)Copy
[/code]

7、设置路径（特别需要注意：每次设置完之后，记得点击右上角的保存，很容易遗漏，没保存会导致连接不上）

  * 设置——TLS设置——入站管理——用户管理

  * 进阶玩法：出站管理——路由列表
    * 中转玩法
    * 不同出站玩法

  * 注意要点：
    * 用户管理中可以重置节点参数
    * VLESS协议要注意要删除流控
    * 出站节点尽量简单，不要添加加密（加密会导致延迟增加）
