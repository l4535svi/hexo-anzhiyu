---
title: 最新 OpenClash 使用教程快速入门篇
date: '2025-01-10 12:00:00'
cover: /img/covers/openclash.jpg
tags:
- 科学上网
categories:
- 科学上网
description: OpenClash是OpenWrt软路由系统下的科学上网代理软件客户端，功能强大且支持多种代理协议，如Shadowsocks(SS)、ShadowsocksR(SSR)、VMess(V2Ray)、Trojan、Socks、Snell等代理协议，根据灵活的规则配置实现策略代理。通过
---
OpenClash是OpenWrt软路由系统下的科学上网代理软件客户端，功能强大且支持多种代理协议，如Shadowsocks(SS)、ShadowsocksR(SSR)、VMess(V2Ray)、Trojan、Socks、Snell等代理协议，根据灵活的规则配置实现策略代理。通过本文2025最新OpenClash使用教程快速入门篇所掌握的技巧，能快速方便配置代理协议进行代理访问。  
  
![OpenClash 从入门到精通](https://openclash.org/wp-content/uploads/2023/04/1680628090-OpenClash-1024x538.jpg)OpenClash 从入门到精通

Table of Contents

[](https://openclash.org/#)

  * [简介](https://openclash.org/# "简介")
  * [界面预览](https://openclash.org/# "界面预览")
  * [OpenClash下载](https://openclash.org/# "OpenClash下载")
  * [节点服务器](https://openclash.org/# "节点服务器")
    * [免费节点](https://openclash.org/# "免费节点")
    * [收费节点](https://openclash.org/# "收费节点")
    * [自己搭建节点](https://openclash.org/# "自己搭建节点")
  * [添加节点](https://openclash.org/# "添加节点")
    * [步骤一：复制节点订阅地址](https://openclash.org/# "步骤一：复制节点订阅地址")
    * [步骤二：导入节点订阅地址](https://openclash.org/# "步骤二：导入节点订阅地址")
    * [步骤三：开启系统代理](https://openclash.org/# "步骤三：开启系统代理")
  * [使用教程](https://openclash.org/# "使用教程")
    * [代理模式](https://openclash.org/# "代理模式")
    * [如何切换节点](https://openclash.org/# "如何切换节点")
  * [常见问题](https://openclash.org/# "常见问题")
    * [支持哪些协议？](https://openclash.org/# "支持哪些协议？")
  * [最新更新](https://openclash.org/# "最新更新")

## 简介

OpenClash 是 OpenWrt 软路由系统下的科学上网代理软件客户端，OpenWrt软件包名为：`luci-app-openclash`。

## 界面预览

[![OpenClash 主界面](https://openclash.org/wp-content/uploads/2024/02/1708669117-OpenClash-Interface-1024x683.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708669117-OpenClash-Interface.jpg)OpenClash 主界面

## OpenClash下载

可进入本站的[最新版下载](https://openclash.org/openclash-download/)专区进行下载，也可以选择以下的方式进行下载安装。

## 节点服务器

节点服务器即软件中的配置订阅，在使用之前，首先需要添加一个 [OpenClash节点](https://openclash.org/openclash-node/) 即服务端才能使用代理上网功能，更多节点可参考本站[节点订阅地址](https://openclash.org/openclash-node/)。

### 免费节点

由于软件支持Shadowsocks(SS)、ShadowsocksR(SSR)、VMess(V2Ray)、Trojan、Socks、Snell等代理协议，如需免费节点可以使用搜索引擎搜索。

### 收费节点

免费节点资源少或者觉得免费节点不稳定的话可以考虑购买收费节点。推荐搬瓦工官方机场 [Just My Socks](https://jmsnode.com/)支持 Shadowsocks 及 V2Ray 协议，并且有多个数据中心及套餐可选，也可以访问本站[好用的OpenClash节点购买机场推荐](https://openclash.org/node/)。

技术小白建议购买机场，无需编写配置文件，直接导入节点订阅地址链接即可使用，机场推荐购买：[龙猫云机场 (不限制设备数量，特别适合路由器使用，国内高速中转加密隧道，性价比IPLC专线机场，价格低至15.00元！)](https://openclash.org/totorocloud/)

### 自己搭建节点

如果对稳定性要求高且有一定的技术基础，推荐自己搭建节点，速度有保证且安全性也最高，具体搭建教程可参考下面的链接。

  * [V2Ray 搭建](https://www.linuxv2ray.com/) (VMess)
  * [Shadowsocks 搭建](https://www.linuxsss.com/) (SS)
  * [ShadowsocksR 搭建](https://www.linuxssr.com/) (SSR)
  * [Trojan 搭建](https://www.linuxtrojan.com/)

## 添加节点

作为快速入门篇教程，本文主要讲述从节点订阅地址方式添加节点，一个有三个步骤，分别是复制节点订阅地址、导入节点订阅地址、开启系统代理。

### 步骤一：复制节点订阅地址

一般主流的服务商都会直接提供节点订阅地址链接，直接复制服务商提供的地址即可，如下图所示：

![1708674225 Subscription Interface Example 02](https://openclash.org/wp-content/uploads/2024/02/1708674225-Subscription-Interface-Example-02.jpg)![1708674227 Subscription Interface Example 01](https://openclash.org/wp-content/uploads/2024/02/1708674227-Subscription-Interface-Example-01.jpg)

### 步骤二：导入节点订阅地址

点击菜单栏的`配置订阅`，在编辑配置文件订阅处找到添加按钮，点击`添加`按钮，如下图所示：

[![OpenClash 添加节点订阅地址链接](https://openclash.org/wp-content/uploads/2024/02/1708686777-openclash-config-subscribe-1024x856.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708686777-openclash-config-subscribe.jpg)添加节点订阅地址链接

随后在配置订阅添加页面，在`配置文件名`处输入机场名称，在`订阅地址`处粘贴从步骤一复制的节点订阅地址，随后点击`保存配置`，如下图所示：

[![OpenClash 填写具体节点订阅信息](https://openclash.org/wp-content/uploads/2024/02/1708686811-openclash-config-subscribe-add-subscribe-1024x856.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708686811-openclash-config-subscribe-add-subscribe.jpg)填写具体节点订阅信息

### 步骤三：开启系统代理

点击主菜单的运行状态，可以看到刚才添加的配置文件信息状态为启用，点击页面最下方的启动 OpenClash 即可开启系统代理，如下图所示：

[![OpenClash 开启系统代理](https://openclash.org/wp-content/uploads/2024/02/1708687033-openclash-start-proxy-1024x856.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708687033-openclash-start-proxy.jpg)开启系统代理

## 使用教程

### 代理模式

插件的运行模式一共有三种模式，分别是 Rule 模式、Global 模式、Direct 模式。

  * Rule 模式：所有请求根据配置文件规则进行分流
  * Global 模式：所有请求直接发往代理服务器
  * Direct 模式：所有请求直接发往目的地，即不使用代理

直接点击插件主界面的代理模式即可切换代理模式，如下图所示：

[![OpenClash 切换代理模式](https://openclash.org/wp-content/uploads/2024/02/1708687556-openclash-proxy-mode-1024x856.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708687556-openclash-proxy-mode.jpg)切换代理模式

### 如何切换节点

在插件的`运行状态`主界面，点击 `Dashboard 控制面板` 选项，即可进入 Clash 控制界面，按钮如下图所示：

[![OpenClash 控制面板](https://openclash.org/wp-content/uploads/2024/02/1708687719-openclash-dashboard-1024x856.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708687719-openclash-dashboard.jpg)控制面板

随后出现 Clash 控制界面，这里和大部分 Clash 软件的界面一样，如 ClashX 等，点击左边菜单的`代理`，然后在右边`策略组`里按需求选择任意节点切换即可，如下图所示：

[![OpenClash 切换代理节点](https://openclash.org/wp-content/uploads/2024/02/1708687952-openclash-dashboard-dashboard-1024x856.jpg)](https://openclash.org/wp-content/uploads/2024/02/1708687952-openclash-dashboard-dashboard.jpg)切换代理节点
