---
title: 斐讯 n1 如何安装或刷入 iStoreOS openwrt 固件｜N1 iStoreOS 科学上网
date: '2025-09-19 12:00:00'
cover: https://picsum.photos/seed/n1-istoreos-openwrt-n1-istoreos/800/450
tags:
- 软路由
categories:
- 软路由
description: 前言 下载并安装 iStoreOS 网络配置 配置防火墙 iStoreOS 安装 openclash ssr plus passwall 科学上网插件 OpenClash、PassWall 插件简单实用教程 博主推荐的旁路由设置 前言 说句实话，之前有尝试过 斐讯n1 iStor
---
*    前言
  *    下载并安装 iStoreOS
  *    网络配置
  *    配置防火墙
  *    iStoreOS 安装 openclash ssr plus passwall 科学上网插件 
  *    OpenClash、PassWall 插件简单实用教程
  *    博主推荐的旁路由设置

## 前言

说句实话，之前有尝试过 斐讯n1 iStoreos openwrt 固件，但放弃了，当时的痛点就是

  * 刷入斐讯n1 iStoreos 固件后，无科学上网环境，无法安装科学上网插件 如openclash，passwall ssr plus
  * 前段时间，找到任何网络下 100% 能安装成功方法：[见博客](https://jameslifeblog.com/istoreos)
  * 文字太多？点击观看–>>>[视频教程](https://youtu.be/V-21RQFRFkE)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-13A-1024x499.png)

简单介绍下，iStoreOS 来源于 OpenWRT，相较于原版 OpenWRT，iStoreOS 具有以下优势：

  1. iStoreOS 提供了**软件中心** ：[**iStore**](https://github.com/linkease/istore) ，尽可能解决插件之间的依赖关系，可让大家自由自在安装插件，并且支持插件备份以及恢复。
  2. iStoreOS 固件升级时会保留用户安装的插件，避免升级以后还要再安装一遍插件。
  3. iStoreOS 官方支持的硬件都可以**在线升级** ，无需手动下载固件升级。
  4. iStoreOS 拥有**沙箱模式** 。通过 U 盘进入沙箱模式，后续的软件安装更新以及系统配置都在沙箱进行。不管安装插件搞坏了系统还是配置错误导致系统故障，拔掉 U 盘就回到进沙箱前的状态。如果对当前状态满意还可以回写到非沙箱环境。沙箱模式本身也是系统扩容的最简单的方法。
  5. iStoreOS 本身就是精简版本，所有的额外功能都是触发到了，依赖软件中心去额外安装插件实现。iStoreOS并不是臃肿的把所有用到的插件内置到固件中。

### ![易有云](https://site.istoreos.com/_nuxt/img/pic3@3x.ebb1ab9.png)

iStoreOS 还做了很多很多的交互简化，但是即使再简化，对于不同的用户级别，我们还是得提供了三套完全不一样的交互 UI。

  * 官方 [WIKI](https://github.com/istoreos/istoreos/wiki) 
  * iStoreOS [官网](https://site.istoreos.com/)
  * 斐讯 n1 如何安装 iStore 固件，官方教程：[点击跳转](https://fw20.koolcenter.com/iStoreOS/alpha/n1/)

### 

![iStoreOS扩展插件包+科学穿墙解锁备份-杨公子的博客](https://www.hiir.cn:12580/wp-content/uploads/2023/03/ceafe0321e2c-1024x573.png)

## 下载并安装 iStoreOS

注意，博主的斐讯 n1 刷入iStoreOS 固件前，斐讯n1已开启 U盘自启动；

  *  如何开启U盘自启动教程：[点击跳转](https://youtu.be/5e5S7ryJnU4?si=waVhZgejpSnm4rlB&t=415)
  * 准备1个 USB 2.0 协议的U盘，容量不低于 8GB
  * 如遇排除常见原因，依旧无法正常启动openwrt，更换全新的电源适配器（ 12V+1A 或者 12V+2A ）

1.下载 iStoreOS 固件，并写入提前准备好的 U 盘；

  * [点击直接下载（博主正在使用的版本 ](https://fw0.koolcenter.com/iStoreOS/alpha/n1/istoreos-22.03.6-2024043010-phicomm_n1-squashfs.img.gz) 
  * 下载地址：[官方 n1固件](https://fw20.koolcenter.com/iStoreOS/alpha/n1/)
  * 写盘 Rufus 软件：[`rufus-4.9p.exe (windows 便携版）`](https://github.com/pbatard/rufus/releases/download/v4.9/rufus-4.9p.exe)
  * 写盘 balenaEtcher 软件：[Download 1](https://github.com/balena-io/etcher/releases/download/v2.1.4/balenaEtcher-2.1.4-x64.dmg)    [Download 2 ( ARM )](https://github.com/balena-io/etcher/releases/download/v2.1.4/balenaEtcher-2.1.4-arm64.dmg)
  * 切记，无需解压固件压缩包，直接将固件写入到U盘即可！！
  * 更多：[其他软路由固件，点击跳转](https://fw20.koolcenter.com/iStoreOS/alpha/)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-3-1024x166.png)

### ![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-1-1024x590.png)

### ![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-2-1024x613.png)

2.将刷入 iStoreOS 固件的U盘插到，靠HDMI的 USB 口后，为斐讯N1 接入电源；

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-4-1024x598.png)

3.将可用的网线，插入斐讯 N1 网口，此时，iStoreOS 固件会自动获取 局域网IP地址，可通过如下即可访问iStoreOS管理后台。

  * 浏览器输入网址 ：[http://iStoreOS.local](http://istoreos.local/)
  * 默认登陆密码：password
  * 或者登陆主路由（同一个局域网的路由器后台）， 找到名称 “iStoreOS” 设备的IP地址，浏览器输入该IP地址

### ![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-4-1024x695.png)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-3-1024x543.png)

## 网络配置

1.成功登陆到后台后，点击左边“网络配置“，将斐讯n1 “配置为旁路由”；

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-6-1024x529.png)

2.按照下图，对斐讯 n1 进行网络设置

  * 点击“配置为旁路由”
  * 点击  “自动配置 ”[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image-1.png)[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image-1.png)
  * 点击“ 点此刷新 ”[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image.png)
  * 点击“自动填写”
  * 关闭DHCP，保存配置 （ 博主是开启DHCPV4 服务，配合静态路由使用）[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image-2.png)

![](https://doc.istoreos.com/assets/img/network1.608d83e3.png)

## 配置防火墙

  * istoreos的后台点击网络-防火墙
  * 在常规设置里，**入站数据，出站数据，转发** 这三个选项都选择**接受（ 如下图**
  * 在自定义规则里，添加一行`iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE`

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-1-1024x756.png)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-2-1024x440.png)

 

## iStoreOS 安装 openclash ssr plus passwall 科学上网插件 

### >下载 iStoreOS OpenClash、PassWall、SSR Plus 插件安装包

找到并下载 iStore passwall 插件  .run 安装包

  * 项目地址：<https://github.com/AUK9527/Are-u-ok>
  * 博客演示用是斐讯N1，所有插件下载地址：<https://github.com/AUK9527/Are-u-ok/tree/main/apps>
  * 斐讯 N1 Passwall：  [PassWall_25.8.26](https://github.com/AUK9527/Are-u-ok/raw/main/apps/all/PassWall_25.8.26_aarch64_a53_all_sdk_22.03.7.run)
  * 斐讯 N1 openclash： [OpenClash_0.46.137](https://github.com/AUK9527/Are-u-ok/raw/main/apps/all/OpenClash_0.46.137+aarch64_core.run)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-3-1024x609.png)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-4-1024x505.png)

特别注意

  * 不推荐passwall系列和ssr-plus一同安装，因为部分软件包可能存在冲突影响使用
  * 如果你在安装此包前尝试通过第三方软件源安装，可能导致意外的错误。推荐你删除所有自行添加的第三方软件源。
  * 注意，上述软件包安装，部分依赖依然要通过opkg软件源在线安装。如果安装失败，检查路由器自身的网络情况，特别是旁路由模式下最容易出现网络问题。
  * 再三注意需要路由器自身联网正常

 

### >安装前必做的准备工作
[code]
    此步骤是 100%安装成功的关键，一定要注意！！！
[/code]

**1.在默认的“首页”，找到并点击 “软件源配置”；**

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-1-1024x481.png)

**2.在弹出的窗口，将 “切换软件源” 更改为“ 阿里云”，点击“确认”，保存设置！**

  * 此步骤是切换到普通网络用的下载**源地址（ 插件，部分依赖依然要通过opkg软件源在线安装**

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-2-1024x566.png)

### >安装 OpenClash、PassWall、SSR Plus 插件安装包

点击“iStore”–>手动安装–>点击“选择上传或者直接拖放文件”（如下图

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-8-1024x312.png)

选择下载成功的 passwall .run包，就会自动跳出命令行界面进行安装（如下图

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-9A-1024x486.png)

 ![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-10-1024x328.png) ![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-11-1024x450.png) ![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-12-1024x418.png) 

待插件安装成功，弹出“任务执行成功”，点击右上角 “x”，退出安装界面。

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-13A-1024x499.png)

### >查看插件安装情况

点击“服务“，passwall 已经成功安装，其他插件，比如说openclash， ssrplus 等插件的基本一致。

但，不推荐passwall系列和ssr-plus一同安装，因为部分软件包可能存在冲突影响使用。

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istore-15-1024x571.png)

## OpenClash、PassWall 插件简单实用教程

Openclash彻底解决DNS污染，实现smartDNS：[点击跳转](https://jameslifeblog.com/openwrt-openclash2025)

PassWall 快速上手：[点击跳转 ](https://jameslifeblog.com/openwrt-passwall)

 

## 博主推荐的旁路由设置

此个性化设置的提前，斐讯n1已经能成功为局域网的设备提供科学上网网络；

如您只有几个需要特殊上网的设备，可以尝试，配合静态IP并使用标签管理。

#### 1.按照下图，设置 “网络向导”；

  * 点击“配置为旁路由”
  * 点击  “自动配置 ”[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image-1.png)[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image-1.png)
  * 点击“ 点此刷新 ”[](https://github.com/tohsaka888/n1_openwrt_config/blob/master/assets/image.png)
  * 点击“自动填写”
  * 开启DHCP，保存配置 

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-8-1024x593.png)

#### 2.设置网络—>接口

网络—>接口—>常规设置—>设备，只勾选“ eth0”(lan)—>保存；

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-7-1024x347.png)

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-9-1024x954.png)

#### 再点击“DHCP 服务器”

  * 在弹出的对话框，点击“高级设置”
  * 勾选“强制” 
  * DHCP选项，分别添加 “3,192.168.1.1”和“6,192.168.1.1”

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-5-1024x478.png)

  * “3,192.168.1.1”表示指派192.168.1.1作为**网关** （注意3和英文逗号）
  * “6,192.168.1.1”表示指派 192.168.1.1作为 **DNS 服务器** （注意6和英文逗号）
  * 设置成功后，默认所有设备，都由主路由 （192.168.1.1）处理网络需求

#### 3\. 最后，返回到上一级菜单，点击“保存并应用”！

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoreos202509-6-1024x289.png)

#### 4.通过“标签”管理，设置**科学上网的设备，** 使用旁路由的网关和DNS

  * 网络—>DHCP/DNS—>标签
  * 输入标签名“ t_proxy” 
  * 点击“添加”
  * 弹出菜单，分别输入“3,192.168.1.128“ 和“6,192.168.1.128“ 
  * 点击“保存”
  * 最后，点击“保存并应用”

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-10-1024x444.png)

  * “3,192.168.1.128”表示指派192.168.1.128 作为**网关** （注意3和英文逗号）
  * “6,192.168.1.128”表示指派 192.168.1.128作为 **DNS 服务器** （注意6和英文逗号）

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-11-1024x351.png)

#### 5\. 最后，对需要科学上网的设备，使用“t_proxy”标签。

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-13-1024x396.png)

依次输入主机名

  * 选择 设备的mac地址和IP地址
  * 租期，设置为 “ infinite ” （无时间限制）
  * 选择“t_proxy”标签
  * 点击“保存”
  * 最后，点击“保存并应用”

![](https://jameslifeblog.com/wp-content/uploads/2025/08/istoren1-12-1024x455.png) 

恭喜你，又解锁一个新技能！
