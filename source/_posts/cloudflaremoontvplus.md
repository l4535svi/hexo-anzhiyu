---
title: Cloudflare搭建Moontvplus^
date: '2026-05-26 12:00:00'
tags:
- 影视大全
categories:
- 影视大全
description: 简介 MoonTVPlus是基于MoonTV v100二次开发的增强版影视聚合播放器。它在原版基础上新增了外部播放器支持、视频超分、弹幕系统、评论抓取等实用功能，提供更强大的观影体验。 项目地址： 链接直达 前期准备： 一个 Cloudflare 账号 一个GitHub 账号 一
---
# [](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E7%AE%80%E4%BB%8B)[](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E7%AE%80%E4%BB%8B "简介")简介

MoonTVPlus是基于MoonTV v100二次开发的增强版影视聚合播放器。它在原版基础上新增了外部播放器支持、视频超分、弹幕系统、评论抓取等实用功能，提供更强大的观影体验。

项目地址：[链接直达](https://github.com/mtvpls/MoonTVPlus)

前期准备：

  1. 一个 Cloudflare 账号
  2.  一个GitHub 账号
  3. 一个Upstash账号[点击注册](https://console.upstash.com/auth/sign-in)

# [](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#Cloudflare-Workers-%E9%83%A8%E7%BD%B2)[](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#Cloudflare-Workers-%E9%83%A8%E7%BD%B2 "Cloudflare Workers 部署")Cloudflare Workers 部署

## [](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E8%8E%B7%E5%8F%96Cloudflare-API-Token%E5%92%8C%E8%B4%A6%E6%88%B7ID)[](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E8%8E%B7%E5%8F%96Cloudflare-API-Token%E5%92%8C%E8%B4%A6%E6%88%B7ID "获取Cloudflare API Token和账户ID")**获取Cloudflare API Token和账户ID**

  * 访问[Cloudflare 仪表板](https://dash.cloudflare.com/)

  * 点击右上角头像 > 我的个人资料 > API Tokens >点击“Create Token”  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus.png)](https://img.skilladd.org/MoonTVPlus/moontvplus.png)

选择“Edit Cloudflare Workers”模板  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus1.png)](https://img.skilladd.org/MoonTVPlus/moontvplus1.png)

权限设置：

  * 帐户 - Cloudflare Workers 脚本 - 编辑

  * 账户-D1-编辑（仅在使用D1数据库时需要）  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus2.png)](https://img.skilladd.org/MoonTVPlus/moontvplus2.png)  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus3.png)](https://img.skilladd.org/MoonTVPlus/moontvplus3.png)

  * 创建后复制生成的API Token

  * 在[Dashboard首页](https://dash.cloudflare.com/)右侧可以看到你的账户ID  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus4.png)](https://img.skilladd.org/MoonTVPlus/moontvplus4.png)

## [](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E8%8E%B7%E5%8F%96Upstash-Redis)[](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E8%8E%B7%E5%8F%96Upstash-Redis "获取Upstash Redis")获取Upstash Redis

注册登录，创建redis数据库（免费256MB）  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus7.png)](https://img.skilladd.org/MoonTVPlus/moontvplus7.png)  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus8.png)](https://img.skilladd.org/MoonTVPlus/moontvplus8.png)

复制访问的**URL地址** 和**Token**

[![](https://img.skilladd.org/MoonTVPlus/moontvplus5.png)](https://img.skilladd.org/MoonTVPlus/moontvplus5.png)

## [](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E9%85%8D%E7%BD%AEGitHub-Secrets)[](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E9%85%8D%E7%BD%AEGitHub-Secrets "配置GitHub Secrets")**配置GitHub Secrets**

Secret 名称| 说明| 示例值  
---|---|---  
CLOUDFLARE_API_TOKEN| Cloudflare API Token| your_api_token_here  
CLOUDFLARE_ACCOUNT_ID| Cloudflare Account ID| abc123def456  
USERNAME| 站长账号| admin  
PASSWORD| 站长密码| your_secure_password  
NEXT_PUBLIC_STORAGE_TYPE| 存储类型| upstash  
UPSTASH_URL| Upstash Redis URL| [https://xxx.upstash.io](https://xxx.upstash.io/)  
UPSTASH_TOKEN| Upstash Redis Token| your_upstash_token  
  
进入你 Fork 的仓库，点击 **Settings** > **Secrets and variables** > **Actions** > **New repository secret** ，添加以下必需的 Secrets：  
[![](https://img.skilladd.org/MoonTVPlus/moontvplus6.png)](https://img.skilladd.org/MoonTVPlus/moontvplus6.png)

# [](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E9%A3%9F%E7%94%A8)[](https://skilladd.org/2026/04/11/49.Cloudflare%E6%90%AD%E5%BB%BAMoontvplus/#%E9%A3%9F%E7%94%A8 "食用")食用

视频源：[test.json](https://raw.githubusercontent.com/rapier15sapper/ew/refs/heads/main/test.json)
