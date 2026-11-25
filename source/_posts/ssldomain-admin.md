---
title: 不错的域名和SSL证书监控项目：Domain Admin
date: '2025-02-26 12:00:00'
cover: https://picsum.photos/seed/ssldomain-admin/800/450
tags:
- 建站
categories:
- 建站
description: https://domain-admin.readthedocs.io/zh-cn/latest/index.html https://blog.ydxian.xyz/archives/domain https://www.mfssl.com/detection/www.alip
---
#   

# https://domain-admin.readthedocs.io/zh-cn/latest/index.html

# https://blog.ydxian.xyz/archives/domain

# https://www.mfssl.com/detection/www.alipan.com

  

https://bugxia.com/723.html

  

  

https://uutool.cn/ssl-time/

  

  

  

# Domain Admin[](https://domain-admin.readthedocs.io/zh-cn/latest/index.html#domain-admin "此标题的永久链接")

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/domain-admin)](https://pypi.org/project/domain-admin) [![PyPI](https://img.shields.io/pypi/v/domain-admin.svg)](https://pypi.org/project/domain-admin) [![PyPI - Downloads](https://img.shields.io/pypi/dm/domain-admin?label=pypi%20downloads)](https://pypi.org/project/domain-admin) [![Docker Image Version \(latest semver\)](https://img.shields.io/docker/v/mouday/domain-admin?label=docker%20version&sort=semver)](https://hub.docker.com/r/mouday/domain-admin) [![Docker Pulls](https://img.shields.io/docker/pulls/mouday/domain-admin)](https://hub.docker.com/r/mouday/domain-admin) [![Build Status](https://app.travis-ci.com/mouday/domain-admin.svg?branch=master)](https://app.travis-ci.com/mouday/domain-admin) [![PyPI - License](https://img.shields.io/pypi/l/domain-admin)](https://github.com/mouday/domain-admin/blob/master/LICENSE) [![Documentation Status](https://readthedocs.org/projects/domain-admin/badge/?version=latest)](https://domain-admin.readthedocs.io/zh_CN/latest/?badge=latest) [![GitHub release](https://img.shields.io/github/v/release/dromara/domain-admin)](https://github.com/dromara/domain-admin/releases) [![GitHub Stars](https://img.shields.io/github/stars/dromara/domain-admin?color=%231890FF&style=flat-square)](https://github.com/dromara/domain-admin) [![宝塔服务器面板，一键全能部署及管理](https://img.shields.io/badge/BT_Deploy-Install-20a53a)](https://www.bt.cn/u/MaBJJC) [![](https://raw.githubusercontent.com/mouday/domain-admin/master/image/domain.svg)](https://raw.githubusercontent.com/mouday/domain-admin/master/image/domain.svg)

> 该项目已加入 [Dromara开源社区](https://github.com/dromara/domain-admin)

基于Python + Vue3.js 技术栈实现的域名和SSL证书监测平台

用于解决，不同业务域名SSL证书，申请自不同的平台，到期后不能及时收到通知，导致线上访问异常，被老板责骂的问题

Domain Admin是一个轻量级监控方案，占用系统资源较少。同时，Domain Admin也可以作为一个Flask 和 Vue.js前后端分离的项目模板

  * 项目优势

    * 集中管理: 提供一个统一的平台来管理多个域名，极大地提高了管理效率。

    * 自动提醒: 支持域名到期提醒，帮助用户避免因域名过期导致的服务中断。

    * 开源灵活: 作为开源项目，用户可以根据自身需求进行定制和扩展。

    * 社区支持: 拥有活跃的社区，可以获得持续的更新和问题支持。

    * 用户友好: 界面简洁直观，容易上手。

  * 功能描述

    * 核心功能：`域名`、`SSL证书` 和 `托管证书文件` 的过期监控，到期提醒

    * 支持证书：单域名证书、多域名证书、泛域名（通配符）证书、IP证书、自签名证书

    * 证书部署：单一主机部署、多主机部署、动态主机部署

    * 通知渠道：支持邮件、Webhook、企业微信、钉钉、飞书等通知方式

    * 支持平台：macOS、Linux、Windows

    * 辅助功能：`Let’s Encrypt` SSL证书免费申请和SSL证书自动续期

    * 多语言：支持中文、英文

  * 项目地址：[后端代码（github）](https://github.com/dromara/domain-admin)、[后端代码（国内镜像）](https://gitee.com/dromara/domain-admin)

  * 发布渠道：[PyPI](https://pypi.org/project/domain-admin)、[Docker](https://hub.docker.com/r/mouday/domain-admin)、[Releases](https://github.com/mouday/domain-admin/releases)、[1Panel](https://apps.fit2cloud.com/1panel/domain-admin)、[宝塔](https://www.bt.cn/u/MaBJJC)

  * 使用文档：[readthedocs](https://domain-admin.readthedocs.io/zh_CN/latest/?badge=latest)

  * 接口文档：[github](https://mouday.github.io/domain-admin/)、[gitee](https://mouday.gitee.io/domain-admin/)

## 安装[](https://domain-admin.readthedocs.io/zh-cn/latest/index.html#id4 "此标题的永久链接")

请参考安装文档：<https://domain-admin.readthedocs.io/zh_CN/latest/manual/install.html>

如果不想安装，可以直接使用我们部署好的线上应用，需要体验的用户可以加入`QQ群` 或 `微信群`，提供邮箱即可

  * 预览版（纯静态、无实际功能，账号密码随意）：<https://mouday.github.io/domain-admin-web/>

  * 体验版（由大家伙捐献的服务器，邮箱注册即可体验）：<https://demo.domain-admin.cn/>

建议自行部署，这样比较安全

> 服务器和域名由群友赞助提供

本项目支持的安装方式

安装方式| 链接  
---|---  
宝塔| [链接](https://www.bt.cn/u/MaBJJC)  
Docker| [链接](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#docker)  
源码| [链接](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id4)  
1Panel| [链接](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#panel)  
k8s| [链接](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#k8s)  
pip| [链接](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#pip)  
  
## 项目截图[](https://domain-admin.readthedocs.io/zh-cn/latest/index.html#id11 "此标题的永久链接")

账号密码随意（例如：admin/123456），预览模式仅提供模拟数据，无法操作修改

1、网页版：

[![](https://gitee.com/mouday/domain-admin/raw/master/image/dashboard.png)](https://gitee.com/mouday/domain-admin/raw/master/image/dashboard.png) [![](https://gitee.com/mouday/domain-admin/raw/master/image/screencapture.png)](https://gitee.com/mouday/domain-admin/raw/master/image/screencapture.png)

  * 预览地址：<https://mouday.github.io/domain-admin-web/>

本项目采用的是前后端分离模式，前端代码在另外一个仓库。

前端项目地址（请自行解码）：aHR0cHM6Ly9naXRodWIuY29tL21vdWRheS9kb21haW4tYWRtaW4td2Vi

或者关注微信公众号：

![](https://gitee.com/mouday/domain-admin/raw/master/image/coding-big-tree.jpg)

回复：`domain-admin-web`，获取完整的前端代码

2、移动端版：

![](https://gitee.com/mouday/domain-admin/raw/master/image/screencapture-mini.png)

  * 移动端预览地址(请使用移动端窗口体验)：<https://mouday.github.io/domain-admin-mini/>

移动端项目地址（请自行解码）：aHR0cHM6Ly9naXRodWIuY29tL21vdWRheS9kb21haW4tYWRtaW4tbWluaQ==

为了更多地人参与到项目中来，现已开放前端代码，加入QQ群即可获取前端项目地址

## 问题反馈交流[](https://domain-admin.readthedocs.io/zh-cn/latest/index.html#id12 "此标题的永久链接")

由于访问github的网络不稳定，如果需要及时获得反馈，请通过以下方式联系

QQ群号: 731742868

邀请码：domain-admin

![](https://gitee.com/mouday/domain-admin/raw/master/image/qq-group.jpeg)

微信交流群

![](https://gitee.com/mouday/domain-admin/raw/master/image/coding-big-tree.jpg)

回复：`domain-admin`，和众多使用者一起交流学习使用经验，反馈使用问题，获得更及时的解答和修复

提交PR的小伙伴，可以进去`核心开发者交流群`，和更多志同道合的朋友交流

## 更新日志[](https://domain-admin.readthedocs.io/zh-cn/latest/index.html#id13 "此标题的永久链接")

[CHANGELOG.md](https://domain-admin.readthedocs.io/zh_CN/latest/manual/changelog.html)

## 使用者[](https://domain-admin.readthedocs.io/zh-cn/latest/index.html#id14 "此标题的永久链接")

虚位以待，可以将使用者公司或个人的名字放到这里

赞助者可以进入`赞助商群`，优先处理你的问题

时间| 赞助者| 金额  
---|---|---  
2023-11-21| [@1275788667](https://github.com/1275788667)| ￥50  
  
  * 
| [@hhdebb](https://github.com/hhdebb)| 若干  
2024-04-23| [@1275788667](https://github.com/1275788667)| ￥50  
  
  * 
| `星河 ๑.`| 若干  
2024-07-10| [@1275788667](https://github.com/1275788667)| ￥50  
2024-10-31| ldytech| ￥200  
2024-11-01| [@xiaobiaozhao](https://github.com/xiaobiaozhao)| ￥50  
  
![](https://gitee.com/mouday/domain-admin/raw/master/image/alipay.jpg)

[![Stargazers over time](https://starchart.cc/dromara/domain-admin.svg)](https://starchart.cc/mouday/domain-admin)

[![Featured｜HelloGitHub](https://api.hellogithub.com/v1/widgets/recommend.svg?rid=2b44fb56aca14df7a6279b0997f7325c&claim_uid=Hb7yUF2AEhnmSwJ)](https://hellogithub.com/repository/2b44fb56aca14df7a6279b0997f7325c)

目录

  * [用户手册](https://domain-admin.readthedocs.io/zh-cn/latest/manual/index.html)
    * [项目简介](https://domain-admin.readthedocs.io/zh-cn/latest/manual/index.html#id2)
    * [使用说明](https://domain-admin.readthedocs.io/zh-cn/latest/manual/index.html#id3)
  * [安装方式](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html)
    * [方式一：宝塔面板安装](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id3)
    * [方式二：docker启动](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#docker)
    * [方式三：下载源码安装](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id5)
    * [方式四：1Panel面板安装](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#panel)
    * [方式五：k8s部署](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#k8s)
    * [方式六：pip安装](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#pip)
    * [其他部署方式](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id6)
    * [平滑升级](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id7)
    * [可选配置](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id8)
    * [配置参数](https://domain-admin.readthedocs.io/zh-cn/latest/manual/install.html#id9)
  * [通知配置](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html)
    * [1、邮件](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html#id2)
    * [2、WebHook](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html#webhook)
    * [3、企业微信](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html#id9)
    * [4、钉钉](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html#id10)
    * [5、飞书](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html#id11)
    * [6、模板和参数](https://domain-admin.readthedocs.io/zh-cn/latest/manual/notify.html#id12)
  * [SSL证书申请](https://domain-admin.readthedocs.io/zh-cn/latest/manual/ssl-cert.html)
    * [1、填写域名](https://domain-admin.readthedocs.io/zh-cn/latest/manual/ssl-cert.html#id1)
    * [2、验证域名](https://domain-admin.readthedocs.io/zh-cn/latest/manual/ssl-cert.html#id2)
    * [3、下载证书](https://domain-admin.readthedocs.io/zh-cn/latest/manual/ssl-cert.html#id3)
    * [4、远程部署](https://domain-admin.readthedocs.io/zh-cn/latest/manual/ssl-cert.html#id4)
    * [说明](https://domain-admin.readthedocs.io/zh-cn/latest/manual/ssl-cert.html#id5)
  * [常见问题](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html)
    * [1、暂不支持多进程方式启动](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id2)
    * [2、为什么外网访问不到？](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id3)
    * [3、Windows平台启动报错,找不到模块 `fcntl`](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#windows-fcntl)
    * [4、添加域名数据后系统异常](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id4)
    * [5、邮件发送失败](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id5)
    * [7、监控域名非443的端口](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id6)
    * [8、修改数据库链接](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id7)
    * [10、支持`prometheus` 的`/metrics`接口](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#prometheus-metrics)
    * [11、部分域名无法查询到信息](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id10)
    * [12、获取ingress的域名](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#ingress)
    * [13、证书监控原理](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id11)
    * [14、域名监控原理](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id12)
    * [15、提示缺少依赖](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id13)
    * [16、主机地址显示错误](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#id14)
    * [17、忘记admin密码怎么办](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#admin)
    * [18、database is locked](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#database-is-locked)
    * [19、Python2.7 依赖问题](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#python2-7)
    * [20、grafana 的展示模版](https://domain-admin.readthedocs.io/zh-cn/latest/manual/question.html#grafana)
  * [扩展插件](https://domain-admin.readthedocs.io/zh-cn/latest/manual/plugins.html)
    * [domain-admin-cronjob](https://domain-admin.readthedocs.io/zh-cn/latest/manual/plugins.html#domain-admin-cronjob)
  * [开发计划](https://domain-admin.readthedocs.io/zh-cn/latest/manual/plan.html)
  * [二次开发](https://domain-admin.readthedocs.io/zh-cn/latest/manual/development.html)
    * [技术选型](https://domain-admin.readthedocs.io/zh-cn/latest/manual/development.html#id2)
    * [接口文档](https://domain-admin.readthedocs.io/zh-cn/latest/manual/development.html#id3)
    * [测试证书](https://domain-admin.readthedocs.io/zh-cn/latest/manual/development.html#id4)
  * [升级日志](https://domain-admin.readthedocs.io/zh-cn/latest/manual/changelog.html)
  * [相关文章](https://domain-admin.readthedocs.io/zh-cn/latest/manual/article.html)
    * [媒体报道](https://domain-admin.readthedocs.io/zh-cn/latest/manual/article.html#id2)
    * [参考文章](https://domain-admin.readthedocs.io/zh-cn/latest/manual/article.html#id23)

[下一页 ](https://domain-admin.readthedocs.io/zh-cn/latest/manual/index.html "用户手册")
[code]
    在数据管理中可以看到具体的证书以及证书的剩余有效天数。  
      
      
      
    这里显示的我个人博客站证书到期时间，与网页这边完全一致。
[/code]
