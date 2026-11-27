---
title: Quick软件共享热点给iOS教程
date: '2022-02-20 12:00:00'
cover: /img/covers/quickios.jpg
tags:
- 免流搭建安卓
categories:
- 免流搭建安卓
description: 安装socks5代理软件 本教程需要iOS安装socks5代理软件：Brook、Shadowrocket、Shiliew等软件，本教程以Brook软件为例 iOS使用海外账号登录App Store - 搜索socks - 找到Brook软件并下载安装 首次启动和关闭智能分流 首次
---
1. 安装socks5代理软件  
本教程需要iOS安装socks5代理软件：Brook、Shadowrocket、Shiliew等软件，本教程以Brook软件为例  
iOS使用海外账号登录App Store - 搜索socks - 找到Brook软件并下载安装  
![](https://quick-connect.top/quickAppShare/iOS/appStore.png)

* * *

  2. 首次启动和关闭智能分流  
首次打开Brook会申请所需要的权限，请允许所申请的权限  
权限申请完成后打开[侧边栏] - 点击 [Bypass] - 选择 [否]，完成  
![](https://quick-connect.top/quickAppShare/iOS/sidebar.png)  
![](https://quick-connect.top/quickAppShare/iOS/bypass.png)

* * *

  3. 连接热点并查看热点机的IP  
Android手机连接Quick软件里的线路，然后iOS连接热点  
iOS打开wifi设置 - 点击热点名称后面的叹号[!] - 记下路由器一行的IP  
![](https://quick-connect.top/quickAppShare/iOS/selectWifi.png)  
![](https://quick-connect.top/quickAppShare/iOS/wifiInfo.png)

* * *

  4. 添加socks5服务器  
再打开Brook软件，点击右上角的 [+] - 选择 [socks5 server]，[Server]一栏填上刚刚记录的路由器后面的IP，然后IP后面再加上“:10800”，如图所示，最后点击添加，完成操作  
![](https://quick-connect.top/quickAppShare/iOS/addSocks5Server.png)  
![](https://quick-connect.top/quickAppShare/iOS/selectSocks5.png)  
![](https://quick-connect.top/quickAppShare/iOS/socks5Addr.png)

* * *

  5. 启动Socks5  
回到Brook软件主页，点击开启，然后给予相应的权限，给完权限后回到软件主页，如果还是未开启状态，就再点击一次开启  
开启成功后如下图  
![](https://quick-connect.top/quickAppShare/iOS/VPNstarted.png)

* * *

  6. 检查是否成功  
进入浏览器，输入http://myip.ipip.net/，查看IP是否为quick节点的出口IP，如果是则表示成功，不是或者无网则表示不成功  
![](https://quick-connect.top/quickAppShare/iOS/myip.png)
