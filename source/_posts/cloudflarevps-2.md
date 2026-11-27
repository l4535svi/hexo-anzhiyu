---
title: cloudflare搭建的vps探针和网站检测面板^
date: '2026-01-17 12:00:00'
cover: /img/covers/cloudflarevps-2.jpg
tags:
- 哪吒探针
categories:
- 哪吒探针
description: 简介 这是一个在部署 Cloudflare Workers 上的简单 VPS 监控面板，使用 Cloudflare D1 数据库存储数据。本指南将引导您通过 Cloudflare 网页控制面板 完成配置，并使用命令行工具。 项目地址： 链接直达 项目部署 创建Worker 登录
---
# 简介

这是一个在部署 Cloudflare Workers 上的简单 VPS 监控面板，使用 Cloudflare D1 数据库存储数据。本指南将引导您通过 Cloudflare**网页控制面板** 完成配置，并使用命令行工具。

项目地址：[链接直达](https://github.com/kadidalax/cf-vps-monitor)

# [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E9%A1%B9%E7%9B%AE%E9%83%A8%E7%BD%B2 "项目部署")项目部署

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E5%88%9B%E5%BB%BAWorker)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E5%88%9B%E5%BB%BAWorker "创建Worker")创建Worker

  1. 登录 Cloudflare
  2. 在左侧菜单中，点击 `计算和AI`，选择 `Workers & Pages`
  3. 在右上角，点击 `创建应用程序`
  4. 选择 `从 Hello World! 开始`
  5. 在`Worker name`，自定义输入项目名称。点击`部署`
  6. 修改worker代码，为：[cf-vps-monitor/worker.js at main · kadidalax/cf-vps-monitor · GitHub](https://github.com/kadidalax/cf-vps-monitor/blob/main/worker.js)代码

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E6%B7%BB%E5%8A%A0%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E6%B7%BB%E5%8A%A0%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F "添加环境变量")添加环境变量

在部署的workers项目的 `设置` → `变量和机密` 中添加以下环境变量(增加安全性)：

变量名| 类型| 值  
---|---|---  
JWT_SECRET| 密钥| [JWT_SECRET密钥生成](https://jwtsecrets.com/#generator)随机生成  
  
## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E8%AE%BE%E7%BD%AE%E8%A7%A6%E5%8F%91%E9%A2%91%E7%8E%87)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E8%AE%BE%E7%BD%AE%E8%A7%A6%E5%8F%91%E9%A2%91%E7%8E%87 "设置触发频率")设置触发频率

**设置触发频率主要检测网站用**

在部署的workers项目的 `设置` → `触发事件`，选择`Cron触发器`，设置每小时检查一次。  
[![](https://66852688.xyz/vps-monitor/vps-monitor.jpg)](https://66852688.xyz/vps-monitor/vps-monitor.jpg)

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E7%BB%91%E5%AE%9A-D1-%E6%95%B0%E6%8D%AE%E5%BA%93)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E7%BB%91%E5%AE%9A-D1-%E6%95%B0%E6%8D%AE%E5%BA%93 "绑定 D1 数据库")绑定 D1 数据库

  1. 在左侧菜单中，找到并点击 `存储和数据库`
  2. 在下拉菜单中，选择 `D1 SQL 数据库`
  3. 点击 `创建数据库`
  4. 为数据库命名自定义，然后点击 `创建`
  5. 在部署的workers项目的 `绑定` → `添加绑定`，选择`D1数据库`
  6. 在 `变量名称` 处输入 `DB` (必须大写)
  7. 在 `D1 数据库` 下拉菜单中，选择你之前创建的数据库
  8. 点击 `部署`

**初始化数据库** ，Worker URL加上`/api/init-db`  
[![](https://66852688.xyz/vps-monitor/vps-monitor1.jpg)](https://66852688.xyz/vps-monitor/vps-monitor1.jpg)

# [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E9%A3%9F%E7%94%A8)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E9%A3%9F%E7%94%A8 "食用")食用

使用凭据登录，用户名: `admin`密码: `monitor2025!`，**记得修改密码** 。  
[![](https://66852688.xyz/vps-monitor/vps-monitor3.jpg)](https://66852688.xyz/vps-monitor/vps-monitor3.jpg)

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E6%B7%BB%E5%8A%A0%E6%9C%8D%E5%8A%A1%E5%99%A8)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E6%B7%BB%E5%8A%A0%E6%9C%8D%E5%8A%A1%E5%99%A8 "添加服务器")添加服务器

自定义输入服务器名称，点击**保存**  
[![](https://66852688.xyz/vps-monitor/vps-monitor4.jpg)](https://66852688.xyz/vps-monitor/vps-monitor4.jpg)

在点击**保存**  
[![](https://66852688.xyz/vps-monitor/vps-monitor5.jpg)](https://66852688.xyz/vps-monitor/vps-monitor5.jpg)

复制**sh脚步** 在vps上执行，就可以添加了。

[![](https://66852688.xyz/vps-monitor/vps-monitor6.jpg)](https://66852688.xyz/vps-monitor/vps-monitor6.jpg)

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E6%B7%BB%E5%8A%A0%E7%BD%91%E7%AB%99)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E6%B7%BB%E5%8A%A0%E7%BD%91%E7%AB%99 "添加网站")添加网站

如下输入就可以添加监控  
[![](https://66852688.xyz/vps-monitor/vps-monitor7.jpg)](https://66852688.xyz/vps-monitor/vps-monitor7.jpg)

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#Telegram-%E9%80%9A%E7%9F%A5%E8%AE%BE%E7%BD%AE)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#Telegram-%E9%80%9A%E7%9F%A5%E8%AE%BE%E7%BD%AE "Telegram 通知设置")Telegram 通知设置

  1. 在电报上添加`@BotFather`好友
  2. 输入`/start`，会弹出一些选项
  3. 然后在输入`/newbot`，弹出提示（Alright, a new bot. How are we going to call it? Please choose a name for your bot.）要你给你的机器人命名一个名称
  4. 在聊天输入框中输入你机器人的名称（比如名称**skilladd_bot**)
  5. 这时候成功创建机器人，**使用此令牌访问HTTP API** 的提示，将API值在bot Token输入框粘贴一些
  6. 在电报上添加`@User Info • Get ID • IDbot`好友
  7. 在菜单选择中，选择`group`创建一个群
  8. 点击选择创建一个新群，输入群名称，添加刚才创建的机器入群，权限设置为私密
  9. 创建完成之后，在`@User Info • Get ID • IDbot`的聊天中会出现群组ID值，将ID值复制chatID的输入框
  10. 保存telegram设置后，群组会出现验证的消息。

[![](https://66852688.xyz/vps-monitor/vps-monitor8.jpg)](https://66852688.xyz/vps-monitor/vps-monitor8.jpg)

# [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E9%97%AE%E9%A2%98)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#%E9%97%AE%E9%A2%98 "问题")问题

## [](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#Worker%E8%AF%B7%E6%B1%82%E6%95%B0)[](https://skilladd.org/2026/01/15/44.cloudflare%E6%90%AD%E5%BB%BA%E7%9A%84vps%E6%8E%A2%E9%92%88%E5%92%8C%E7%BD%91%E7%AB%99%E6%A3%80%E6%B5%8B%E9%9D%A2%E6%9D%BF/#Worker%E8%AF%B7%E6%B1%82%E6%95%B0 "Worker请求数")Worker请求数

  * **Worker 和 D1 每日配额:**  本项目当前最大的限制是Worker请求数，主要是vps上报数据的消耗，每日请求数可以用这个公式计算：`vps数量 *（86400/上报频率）`，得到的数字再除以100000就是已消耗百分比。

> 比如你有十台vps服务器，更新频率为每分钟更新一次（60s)，(10*（86400/60))/100000=0.144=14.4%
