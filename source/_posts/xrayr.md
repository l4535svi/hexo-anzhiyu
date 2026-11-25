---
title: XrayR开源项目地址
date: '2025-07-01 12:00:00'
tags:
- 建站
categories:
- 建站
description: 1、XrayR开源项目地址： 【 点击进入 】 XrayR一键安装 wget -N https://raw.githubusercontent.com/XrayR-project/XrayR-release/master/install.sh && bash install.sh
---
1、XrayR开源项目地址：【[点击进入](https://github.com/XrayR-project/XrayR)】

  * XrayR一键安装

[code]
    wget -N https://raw.githubusercontent.com/XrayR-project/XrayR-release/master/install.sh && bash install.shCopy
[/code]

  * 配置文件路径：/etc/XrayR/config.yml

2、权限组——订阅管理——节点管理的逻辑关系

  * 权限组只是举例说明，小伙伴可以根据实际情况设置

![](https://naiyous.com/wp-content/uploads/2023/09/v2board%E8%AE%BE%E7%BD%AE%E9%80%BB%E8%BE%91%E6%80%9D%E8%B7%AF-1024x373.jpg)

  * 订阅管理的配置模板

[code]
    <style>
        .no-wrap {
            white-space:pre-wrap;;
        }
    </style>
    
    <div class="no-wrap">
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)更快的网络
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)流媒体解锁
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)享有IPLC游戏专线
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)不限制设备数
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)1000 GB 流量/月
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)500 Mpbs 限速
    ![✅](https://s.w.org/images/core/emoji/15.1.0/svg/2705.svg)在线客服售后保障
    </div>
    Copy
[/code]

3、SSL设置参考资料：【[点击进入](https://go-acme.github.io/lego/dns/cloudflare/)】
[code]
    CLOUDFLARE_EMAIL=you@example.com \
    CLOUDFLARE_API_KEY=b9841238feb177a84330febba8a83208921177bffe733 \Copy
[/code]

4、节点配置，参考XrayR详细教程：【[点击进入](https://xrayr-project.github.io/XrayR-doc/dui-jie-v2board/v2board.html)】

  * 放行端口

[code]
    ufw allow 需要放行的端口
[/code]
