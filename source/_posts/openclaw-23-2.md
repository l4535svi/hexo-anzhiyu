---
title: 本地openclaw虚拟机一键打包安装，开启免费极速养虾模式
date: '2026-03-24 12:00:00'
cover: https://picsum.photos/seed/openclaw-23-2/800/450
tags:
- OpenClaw
categories:
- OpenClaw
description: 视频教程： 哔哩哔哩： https://www.bilibili.com/video/BV1GEwdzvEvY/ youtube： https://youtu.be/HsX5wGrh-2E 昨天给大家详细讲解了如何在vm虚拟机里，通过Ubuntu系统来安装openclaw，很多朋
---
视频教程：

哔哩哔哩：<https://www.bilibili.com/video/BV1GEwdzvEvY/>

youtube：<https://youtu.be/HsX5wGrh-2E>

* * *

昨天给大家详细讲解了如何在vm虚拟机里，通过Ubuntu系统来安装openclaw，很多朋友还是表示不好装，装不成功，那今天咱们来个极速模式，大海直接把昨天安装好的虚拟机打包，需要的朋友直接解压就可以使用。

## 1、安装vmware虚拟机

我这里用的版本是17.6.4，所以你要想使用这个打包，至少版本要大于等于我，低版本的朋友建议升级，vm是向下兼容的，升级了也可以打开低版本的虚拟机。

官方下载：<https://support.broadcom.com/group/ecx/free-downloads>

大海分流网盘：<https://www.dhzyw.com/archives/6993.html>

## 2、下载大海的虚拟机压缩包并解压

夸克网盘：<https://pan.quark.cn/s/712491c5023e> 提取码：S1gq

百度网盘：<https://pan.baidu.com/s/1zSF3-Zs0eyifOuajjxFlIQ?pwd=7xyw> 提取码: 7xyw

迅雷云盘：<https://pan.xunlei.com/s/VOnv97v8URxDPxHH7O_jZPwtA1?pwd=c7u5#>

这里建议解压到自己的固态硬盘里，速度会快一点

登录名ubuntu，登录密码是dhzyw

这里建议首次登录后修改登录密码，因为大海的教程暴露在公开环境，大家还是安全为主

ubuntu修改登录密码的命令：sudo passwd ubuntu（这个是修改ubuntu这个用户的密码）sudo passwd（这个是修改root密码）

## 3、ssh登录并获取虚拟机环境ip

虚拟机->ssh(h)->连接到ssh(h)

登录名ubuntu，密码是你刚刚修改好的

登录后关闭虚拟机，选择在后台运行

登录后输入 `ip addr`，找到 `ens33` 下的 `inet` 后的地址（如 `192.168.160.128`），记下它

## 4、ssh转发，登录小龙虾

真机powershell输入命令，页面不要关闭

ssh -L 18789:127.0.0.1:18789 ubuntu@192.168.160.128  （ip是你上边获取的这个）

## 5、浏览器访问

在 Windows 的 Chrome/Edge 浏览器地址栏输入：

`http://localhost:18789`

这个时候你就能看到自己的龙虾登录界面了

登录token：65ae1b16eba01af14b4ca83d7cd238f576e4354155878ef6

登录密码：dhzyw

假如没看到界面，那就是ollama模型和端口问题，关于模型安装和选择还有配置，参照上期视频和教程:<https://www.dhzyw.com/archives/7891.html>

openclaw网关和模型配置命令：
[code]
    openclaw onboard --install-daemon
[/code]
