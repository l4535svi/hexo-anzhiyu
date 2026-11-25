---
title: 自建门户导航网站，CloudFlare搭建轻量化导航页面，无需服务器，无需vps，免费且开源！！！
date: '2024-09-14 12:00:00'
tags:
- 建站
categories:
- 建站
description: 大家好，这里是小白科技。 本期分享给大家，如何搭建自己的导航网站，无需服务器，操作简单， 本期视频演示： 登录到cloudflare官网： https://dash.cloudflare.com/login workers代码地址： https://github.com/hmhm
---
大家好，这里是小白科技。

本期分享给大家，如何搭建自己的导航网站，无需服务器，操作简单，

本期视频演示：

  

登录到cloudflare官网：<https://dash.cloudflare.com/login>

  

#### workers代码地址：<https://github.com/hmhm2022/Card-Tab/blob/main/update-workers>

  

创建KV空间名称：CARD_ORDER

  

创建变量

环境变量 名称：ADMIN_PASSWORD 

#### 用于设置后台管理密码

  

KV空间绑定名称：CARD_ORDER

#### 与新建的KV存储绑定，用于存储书签

  

最后绑定自定义域名就可以使用了。
