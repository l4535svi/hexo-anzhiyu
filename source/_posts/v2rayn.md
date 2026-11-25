---
title: 最新 v2rayN 使用教程快速入门篇
date: '2025-03-05 12:00:00'
cover: https://picsum.photos/seed/v2rayn/800/450
tags:
- 节点分享
categories:
- 节点分享
description: v2rayN是Windows系统下的代理软件客户端，功能强大且支持多种代理协议，如VMess、VLESS、Trojan、Socks、Shadowsocks、Hysteria2、Tuic等代理协议。通过本文2025最新使用教程快速入门篇所掌握的技巧，能快速方便配置代理协议进行代理访
---
v2rayN是Windows系统下的代理软件客户端，功能强大且支持多种代理协议，如VMess、VLESS、Trojan、Socks、Shadowsocks、Hysteria2、Tuic等代理协议。通过本文2025最新使用教程快速入门篇所掌握的技巧，能快速方便配置代理协议进行代理访问。

![v2rayN从入门到精通](https://v2rayn.org/wp-content/uploads/2022/06/1656267342-v2rayN-1024x538.jpg)v2rayN从入门到精通

Table of Contents

[](https://v2rayn.org/#)

  * [界面预览](https://v2rayn.org/# "界面预览")
  * [下载](https://v2rayn.org/# "下载")
    * [官网下载](https://v2rayn.org/# "官网下载")
  * [安装教程](https://v2rayn.org/# "安装教程")
    * [软件目录](https://v2rayn.org/# "软件目录")
    * [图标说明](https://v2rayn.org/# "图标说明")
  * [节点](https://v2rayn.org/# "节点")
    * [免费节点](https://v2rayn.org/# "免费节点")
    * [收费节点](https://v2rayn.org/# "收费节点")
    * [自己搭建节点](https://v2rayn.org/# "自己搭建节点")
  * [添加服务器](https://v2rayn.org/# "添加服务器")
    * [订阅设置教程](https://v2rayn.org/# "订阅设置教程")
    * [剪贴板导入教程](https://v2rayn.org/# "剪贴板导入教程")
    * [扫描屏幕二维码教程](https://v2rayn.org/# "扫描屏幕二维码教程")
    * [配置V2Ray节点](https://v2rayn.org/# "配置V2Ray节点")
    * [配置Xray节点](https://v2rayn.org/# "配置Xray节点")
    * [配置Shadowsocks节点](https://v2rayn.org/# "配置Shadowsocks节点")
    * [配置Socks节点](https://v2rayn.org/# "配置Socks节点")
    * [配置Trojan节点](https://v2rayn.org/# "配置Trojan节点")
    * [配置Hysteria2节点](https://v2rayn.org/# "配置Hysteria2节点")
    * [配置Tuic节点](https://v2rayn.org/# "配置Tuic节点")
  * [使用教程](https://v2rayn.org/# "使用教程")
    * [选择节点](https://v2rayn.org/# "选择节点")
    * [系统代理](https://v2rayn.org/# "系统代理")
    * [路由模式](https://v2rayn.org/# "路由模式")
    * [开机自动启动](https://v2rayn.org/# "开机自动启动")
  * [更新教程](https://v2rayn.org/# "更新教程")
  * [常见问题](https://v2rayn.org/# "常见问题")
    * [core类型的区别是什么？](https://v2rayn.org/# "core类型的区别是什么？")
    * [支持哪些协议？](https://v2rayn.org/# "支持哪些协议？")
    * [与 v2rayNG 的关系？](https://v2rayn.org/# "与 v2rayNG 的关系？")
  * [最新更新](https://v2rayn.org/# "最新更新")

## 界面预览

[![v2rayN主界面](https://v2rayn.org/wp-content/uploads/2024/01/1706544977-v2rayN-interface-cn.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706544977-v2rayN-interface-cn.jpg)主界面

## 下载

### 官网下载

v2rayN官网下载地址：<https://github.com/2dust/v2rayN/releases> 新手使用建议下载稳定版本，即版本号后标记为 `Latest` 的版本。

## 安装教程

### 软件目录

下载完成后，找到合适的目录，推荐安装在非系统盘，解压压缩包，解压后的目录如下图所示。

[![v2rayN安装目录文件](https://v2rayn.org/wp-content/uploads/2024/01/1706546502-v2rayN-Floder.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706546502-v2rayN-Floder.jpg)安装目录

找到软件主程序 `v2rayN.exe` 双击鼠标左键即可开始使用，程序启动后会最小化到任务右小角的托盘，鼠标双击蓝色的 `V` 字小图标，即可打开软件的主界面。

### 图标说明

不同状态下软件的图标颜色是不一样的，参考下表图标颜色说明。

图标| 软件状态| 说明  
---|---|---  
![1706696938 v2rayN Notify Icon 1](https://v2rayn.org/wp-content/uploads/2024/01/1706696938-v2rayN-Notify-Icon-1-32px.jpg)| 清除系统代理| 每次启动/重启服务的时候，强制把windows系统(ie)的代理清除掉。  
![1706696935 v2rayN Notify Icon 2](https://v2rayn.org/wp-content/uploads/2024/01/1706696935-v2rayN-Notify-Icon-2-32px.jpg)| 自动配置系统代理| 每次启动/重启服务的时候，强制设定windows系统(ie)的代理。  
![1706696937 v2rayN Notify Icon 3](https://v2rayn.org/wp-content/uploads/2024/01/1706696937-v2rayN-Notify-Icon-3-32px.jpg)| 不改变系统代理| 每次启动/重启服务的时候，什么都不做。作用就是保留其他软件设定的代理。  
图标状态说明

## 节点

节点即软件中的服务器，在使用之前，首先需要添加一个v2rayN节点即服务端才能使用代理上网功能，更多节点可参考本站[节点订阅地址](https://v2rayn.org/v2rayn-node/)或[好用的v2rayN节点购买机场推荐](https://v2rayn.org/node/)。

### 免费节点

由于软件支持VMess、VLESS、Trojan、Socks、Shadowsocks、Hysteria2、Tuic等代理协议，如需免费节点可以使用搜索引擎搜索。

### 收费节点

免费节点资源少或者觉得免费节点不稳定的话可以考虑购买收费节点。推荐搬瓦工官方机场 [Just My Socks](https://jmsnode.com/)，支持 Shadowsocks 及 V2Ray 协议，并且多个数据中心及套餐可选。

技术小白建议购买机场，无需编写配置文件，直接导入节点订阅地址链接即可使用，机场推荐购买：[大哥云机场 (注册可免费试用！国内高速中转加密隧道，价格低至19.99元！)](https://v2rayn.org/dageyun/)

### 自己搭建节点

如果对稳定性要求高且有一定的技术基础，推荐自己搭建节点，速度有保证且安全性也最高，具体搭建教程可参考下面的链接。

  * [V2Ray 搭建](https://www.linuxv2ray.com/) (VMess)
  * [Xray 搭建](https://www.linuxxray.com/) (VLESS)
  * [Trojan 搭建](https://www.linuxtrojan.com/)
  * [Shadowsocks 搭建](https://www.linuxsss.com/) (SS)

## 添加服务器

获取节点服务器信息后，就可以开始添加服务器了，点击软件主界面的`服务器`，根据不同的节点添加不同的节点服务器。

[![v2rayN添加服务器主界面](https://v2rayn.org/wp-content/uploads/2024/01/1706686582-v2rayN-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706686582-v2rayN-Server.jpg)服务器设置

### 订阅设置教程

一些代理机场往往会提供一个订阅地址，就可以使用订阅方式导入节点信息，点击软件主界面的`订阅分组`，`点击订阅分组设置`，如下图所示：

[![v2rayN订阅分组](https://v2rayn.org/wp-content/uploads/2024/01/1706686626-v2rayN-Subscription-Group.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706686626-v2rayN-Subscription-Group.jpg)订阅分组

在弹出的窗口中点击添加，如下图所示：

[![v2rayN添加订阅分组](https://v2rayn.org/wp-content/uploads/2024/01/1706686733-v2rayN-Subscription-Group-Settings.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706686733-v2rayN-Subscription-Group-Settings.jpg)添加订阅分组

随后在弹窗的窗口中，输入别名，在`可选地址(Url)`部分粘贴订阅地址，点击添加，然后点击确定，如下图所示：

[![v2rayN订阅分组设置](https://v2rayn.org/wp-content/uploads/2024/01/1706686836-v2rayN-Subscription-Group-Settings-add-Subcription.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706686836-v2rayN-Subscription-Group-Settings-add-Subcription.jpg)订阅分组设置

添加完成后，点击软件主界面的`订阅分组`，然后点击更新全部订阅(不通过代理)即可成功使用订阅地址添加节点信息，如下图所示：

[![v2rayN更新全部订阅](https://v2rayn.org/wp-content/uploads/2024/01/1706687443-v2rayN-Subscription-Group-Update-Subscription-without-Proxy.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706687443-v2rayN-Subscription-Group-Update-Subscription-without-Proxy.jpg)更新全部订阅

### 剪贴板导入教程

首先复制节点服务器的连接地址，不同协议的地址如下所示。

  * VMESS服务器即v2Ray节点地址：`vmess://`
  * VLESS服务器即Xray节点地址：`vless://`
  * Shadowsock服务器节点地址：`ss://`
  * Socks服务器节点地址：`socks5://`
  * Trojan服务器节点地址：`trojan://`

单机鼠标右键复制或者使用键盘快捷键 `Ctrl+C` 复制节点地址，注意一定要复制全。

[![从剪贴板导入批量URL](https://v2rayn.org/wp-content/uploads/2024/01/1706694515-v2rayN-add-Server-from-Clipboard.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694515-v2rayN-add-Server-from-Clipboard.jpg)从剪贴板导入批量URL

然后点击软件主界面的`服务器`，选择从剪贴板导入批量URL即可导入节点信息，如上图所示。

### 扫描屏幕二维码教程

首先打开服务器节点的二维码图片，然后打开软件，点击软件主界面的`服务器`，选择扫描屏幕上的二维码即可导入节点信息，如下图所示。

[![扫描屏幕上的二维码](https://v2rayn.org/wp-content/uploads/2024/01/1706694536-v2rayN-add-Server-from-QRcode.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694536-v2rayN-add-Server-from-QRcode.jpg)扫描屏幕上的二维码

### 配置V2Ray节点

点击软件主界面的`服务器`，选择 `添加[VMess]服务器`，如下图所示。

[![v2rayN添加服务器添加V2Ray节点](https://v2rayn.org/wp-content/uploads/2024/01/1706694653-v2rayN-add-Server-VMess-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694653-v2rayN-add-Server-VMess-Server.jpg)添加V2Ray节点

在添加窗口输入V2Ray节点信息，即可配置V2Ray服务器信息，然后点击确定保存，如下图所示。

[![配置V2Ray节点信息](https://v2rayn.org/wp-content/uploads/2024/01/1706694683-v2rayN-add-Server-VMess-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694683-v2rayN-add-Server-VMess-Server-Config.jpg)配置V2Ray节点信息

### 配置Xray节点

点击软件主界面的`服务器`，选择 `添加[VLESS]服务器`，如下图所示。

[![v2rayN添加服务器添加Xray节点](https://v2rayn.org/wp-content/uploads/2024/01/1706694725-v2rayN-add-Server-VLESS-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694725-v2rayN-add-Server-VLESS-Server.jpg)添加Xray节点

在添加窗口输入Xray节点信息，即可配置Xray服务器信息，然后点击确定保存，如下图所示。

[![配置Xray节点信息](https://v2rayn.org/wp-content/uploads/2024/01/1706694750-v2rayN-add-Server-VLESS-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694750-v2rayN-add-Server-VLESS-Server-Config.jpg)配置Xray节点信息

### 配置Shadowsocks节点

点击软件主界面的`服务器`，选择 `添加[Shadowsocks]服务器`，如下图所示。

[![v2rayN添加服务器添加Shadowsocks节点](https://v2rayn.org/wp-content/uploads/2024/01/1706694824-v2rayN-add-Server-Shadowsocks-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694824-v2rayN-add-Server-Shadowsocks-Server.jpg)添加Shadowsocks节点

在添加窗口输入Shadowsocks节点信息，即可配置Shadowsocks服务器信息，然后点击确定保存，如下图所示。

[![配置Shadowsocks节点信息](https://v2rayn.org/wp-content/uploads/2024/01/1706694852-v2rayN-add-Server-Shadowsocks-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694852-v2rayN-add-Server-Shadowsocks-Server-Config.jpg)配置Shadowsocks节点信息

### 配置Socks节点

点击软件主界面的`服务器`，选择 `添加[Socks]服务器`，如下图所示。

[![v2rayN添加服务器添加Socks节点](https://v2rayn.org/wp-content/uploads/2024/01/1706694909-v2rayN-add-Server-Socks-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694909-v2rayN-add-Server-Socks-Server.jpg)添加Socks节点

在添加窗口输入Socks节点信息，即可配置Socks服务器信息，然后点击确定保存，如下图所示。

[![配置Socks节点](https://v2rayn.org/wp-content/uploads/2024/01/1706694992-v2rayN-add-Server-Socks-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706694992-v2rayN-add-Server-Socks-Server-Config.jpg)配置Socks节点信息

### 配置Trojan节点

点击软件主界面的`服务器`，选择 `添加[Trojan]服务器`，如下图所示。

[![v2rayN添加服务器添加Trojan节点](https://v2rayn.org/wp-content/uploads/2024/01/1706695047-v2rayN-add-Server-Trojan-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695047-v2rayN-add-Server-Trojan-Server.jpg)添加Trojan节点

在添加窗口输入Trojan节点信息，即可配置Trojan服务器信息，然后点击确定保存，如下图所示。

[![配置Trojan节点信息](https://v2rayn.org/wp-content/uploads/2024/01/1706695072-v2rayN-add-Server-Trojan-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695072-v2rayN-add-Server-Trojan-Server-Config.jpg)配置Trojan节点信息

### 配置Hysteria2节点

点击软件主界面的`服务器`，选择 `添加[Hysteria2]服务器`，如下图所示。

[![v2rayN添加服务器添加Hysteria2节点](https://v2rayn.org/wp-content/uploads/2024/01/1706695494-v2rayN-add-Server-Hysteria2-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695494-v2rayN-add-Server-Hysteria2-Server.jpg)添加Hysteria2节点

在添加窗口输入Hysteria2节点信息，即可配置Hysteria2服务器信息，然后点击确定保存，如下图所示。

[![配置Hysteria2节点信息](https://v2rayn.org/wp-content/uploads/2024/01/1706695780-v2rayN-add-Server-Hysteria2-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695780-v2rayN-add-Server-Hysteria2-Server-Config.jpg)配置Hysteria2节点信息

### 配置Tuic节点

点击软件主界面的`服务器`，选择 `添加[Tuic]服务器`，如下图所示。

[![v2rayN添加服务器添加Tuic节点](https://v2rayn.org/wp-content/uploads/2024/01/1706696325-v2rayN-add-Server-Tuic-Server.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706696325-v2rayN-add-Server-Tuic-Server.jpg)添加Tuic节点

在添加窗口输入Tuic节点信息，即可配置Tuic服务器信息，然后点击确定保存，如下图所示。

[![配置Tuic节点信息](https://v2rayn.org/wp-content/uploads/2024/01/1706696358-v2rayN-add-Server-Tuic-Server-Config.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706696358-v2rayN-add-Server-Tuic-Server-Config.jpg)配置Tuic节点信息

## 使用教程

在添加完节点信息后，开启系统代理并选择路由模式，即可开始使用代理服务器上网了，如下面系统代理及路由模式章节所述。

### 选择节点

在软件主界面选择任意节点，单击鼠标右键，在弹出的窗口中扎到设为活动服务器即可选择节点，如下图所示，然后开启系统代理即可，也可以选择任意节点，双击鼠标左键选择节点。

![v2rayN选择节点](https://v2rayn.org/wp-content/uploads/2024/02/1707289273-v2rayN-Choose-Node.jpg)选择节点

### 系统代理

按照上面的配置教程配置完服务器（节点）后，需要设置系统代理才能让浏览器支持科学上网功能，在任务栏右下角系统托盘找到软件的图标，在图标上单击鼠标右键，点击自动配置系统代理，此时软件的图标会标称红色，至此就可以开始使用了，打开 [Google](https://www.google.com/) 试试能不能访问吧。

[![v2rayN自动配置系统代理](https://v2rayn.org/wp-content/uploads/2024/01/1706695100-v2rayN-enable-System-Proxy.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695100-v2rayN-enable-System-Proxy.jpg)自动配置系统代理

### 路由模式

路由的功能是将入站数据按需求由不同的出站连接发出，以达到按需代理的目的。这一功能的常见用法是分流国内外流量，可以通过内部机制判断不同地区的流量，然后将它们发送到不同的出站代理，有以下三种路由模式可以选择。

  * 绕过大陆(Whitelist)模式：即原先版本里的白名单，只是白名单内的网站通过节点服务器代理上网
  * 黑名单(Blacklist)模式：除了黑名单内的网站，其余网站都通过节点服务器代理上网
  * 全局(Global)模式：所有网站通过节点服务器代理上网

根据不同的需求选择合适的路由模式，一般选择白名单模式。

[![v2rayN路由模式](https://v2rayn.org/wp-content/uploads/2024/01/1706695132-v2rayN-enable-Router-Mode.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695132-v2rayN-enable-Router-Mode.jpg)路由模式

### 开机自动启动

在点击软件主界面的`设置`，点击`设置`然后点击`参数设置`进入参数设置页面，如下图所示：

![v2rayN设置参数设置](https://v2rayn.org/wp-content/uploads/2024/01/1706695247-v2rayN-Settings-OptionSetting.jpg)参数设置

进入参数设置后，选择`v2rayN设置`标签页，勾选上开机自动启动复选框，然后点击确认，如下图所示。

[![v2rayN设置开机自启动](https://v2rayn.org/wp-content/uploads/2024/01/1706695342-v2rayN-Settings-OptionSetting-v2rayN-Settings.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695342-v2rayN-Settings-OptionSetting-v2rayN-Settings.jpg)设置开机自启动

## 更新教程

可在线自动更新软件、Xray-Core、sing-box Core、Geo files，通过点击软件主界面的`检查更新`进行在线更新，如下图所示。

[![v2rayN检查更新](https://v2rayn.org/wp-content/uploads/2024/01/1706695368-v2rayN-Update.jpg)](https://v2rayn.org/wp-content/uploads/2024/01/1706695368-v2rayN-Update.jpg)检查更新
