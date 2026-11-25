---
title: CunMail临时邮箱部署教程（2026）：如何使用Cloudflare Workers搭建免费域名邮箱系统
date: '2026-07-31 12:00:00'
tags:
- 临时邮箱
categories:
- 临时邮箱
description: 本文介绍 CunMail 临时邮箱系统的完整部署流程。基于 Cloudflare Workers + D1 + Email Routing 构建，完全免费托管。支持自定义域名、自定义有效期、收邮件、桌面通知、密码找回。部署采用 GitHub Actions 自动部署，不需要本地环
---
本文介绍 CunMail 临时邮箱系统的完整部署流程。基于 Cloudflare Workers + D1 + Email Routing 构建，完全免费托管。支持自定义域名、自定义有效期、收邮件、桌面通知、密码找回。部署采用 GitHub Actions 自动部署，不需要本地环境。  
  
![自建临时邮箱](https://www.cunzhangblog.com/api/blob/images/af751c2a26e95888035086adb6f4307f1c1bd845.jpg)

## 核心结论

经过实际部署测试：

  * CunMail 完全跑在 Cloudflare 免费套餐上，不需要服务器，不需要月费
  * GitHub Actions 一键部署模式对新手友好，不需要本地环境
  * 部署完成后需要配置 Email Routing 的 Catch-all 规则，否则收不到邮件
  * 二级域名部署时，需要先在 Email Routing 设置中启用子域名，再配置路由规则

如果你有域名且托管在 Cloudflare 上，CunMail 是一个零成本可长期使用的临时邮箱方案。

适合：

  * 经常注册网站、需要保护真实邮箱的用户
  * 使用二级域名部署临时邮箱的用户
  * 想跑在 Cloudflare 免费套餐上的项目

* * *

## 什么是 CunMail？

CunMail 是一款基于 Cloudflare 全家桶（Workers + D1 + Email Routing）的开源临时邮箱系统。由 Web3村长在 vmail 基础上修改定制。

核心能力：

  1. 生成临时邮箱地址，用完即焚，保护真实邮箱隐私
  2. 支持自定义有效期：1 小时 / 6 小时 / 24 小时 / 7 天
  3. 支持收邮件，新邮件桌面通知
  4. 支持多域名，一个系统多个邮箱后缀
  5. 支持密码找回功能

## 为什么选择自建临时邮箱？

公用临时邮箱最大的问题是：很多网站已经屏蔽了那些公用域名。

方案| 费用| 域名掌控| 隐私保护| 可定制  
---|---|---|---|---  
CunMail（自建）| 免费| 自己的域名| 完全掌控| 开源可改  
公用临时邮箱| 免费| ❌ 被屏蔽概率高| 低，任何人都能用| ❌  
邮箱别名服务| 付费/有限免费| 依赖平台| 中| 有限  
  
自己搭建用自己域名，不存在被屏蔽的问题。

## 技术架构

CunMail 的技术栈：

层级| 技术  
---|---  
运行时| Cloudflare Workers  
数据库| Cloudflare D1（SQLite）  
邮件路由| Cloudflare Email Routing  
构建部署| GitHub Actions + Wrangler  
  
工作流程：用户通过前端生成邮箱 → Email Routing 将邮件投递到 Worker → Worker 解析存储到 D1 → 前端展示新邮件。

## 准备工作

开始部署之前，需要：

  * GitHub 账号
  * Cloudflare 账号（免费版即可）
  * 一个已托管在 Cloudflare 上的域名（主域名或二级域名均可）

预计时间：10-15 分钟

难度：⭐⭐

* * *

## CunMail 部署教程

### 第一步：Fork 仓库

CunMail：[点击跳转](https://github.com/cunzhangcrypto/cunmail)

打开 CunMail 的 GitHub 页面，点击右上角的 Fork，把项目复制到你自己的 GitHub 账号下。

### 第二步：准备 Cloudflare 信息

需要从 Cloudflare 获取以下四项信息：

① Cloudflare API Token

Cloudflare 头像 → 我的个人资料 → API 令牌 → 创建令牌。选择 使用 Cloudflare Workers 模板。需要额外添加 D1 数据库的编辑权限（在更多权限里搜索 D1，勾选编辑）。区域资源根据你的域名数量选择（单个选特定区域，多个选所有区域）。创建后复制 Token（只显示一次）。

② Account ID

任意域名概览页面，右侧最下方 API 区域即可看到。

③ D1 数据库

存储和数据库 → D1 → 创建数据库，名称随意（比如 `cunmail`）。创建后复制 Database ID。

④ 域名

确保你的域名已托管在 Cloudflare 上。

### 第三步：配置 GitHub Secrets

在 Fork 后的项目仓库中进入 Settings → Secrets and variables → Actions → New repository secret。

需要添加以下 6 个 Secret：

Secret 名称| 说明  
---|---  
`CF_API_TOKEN`| Cloudflare API Token  
`CF_ACCOUNT_ID`| Cloudflare Account ID  
`D1_DATABASE_NAME`| D1 数据库名称，如 cunmail  
`D1_DATABASE_ID`| D1 数据库 ID  
`EMAIL_DOMAIN`| 邮箱域名（多个用逗号分隔）  
`COOKIES_SECRET`| Cookie 加密密钥，随机字符串  
  
### 第四步：触发 GitHub Actions 部署

Actions → 选择 Deploy to Cloudflare → Run workflow → 选 main 分支 → Run workflow。等待部署完成。

部署成功后，Cloudflare 会自动创建一个 Worker，并分配一个 workers.dev 域名。

### 第五步：配置 Email Routing（关键步骤）

这一步很容易卡住，分两种情况：

#### 情况 A：使用二级域名（如 mail.example.com）

二级域名不能直接配置路由规则，需要先启用子域名：

  1. 进入 Cloudflare → 域名 → 电子邮件 → 电子邮件的路由
  2. 点击右上角 设置 → 在子域名区域添加你的二级域名（如 cunmail）
  3. 等待状态变为"已启用"

#### 情况 B：使用主域名（如 example.com）

可以直接配置路由规则。

启用后，回到路由规则，点击 创建规则：

  * 打开下方的 全收（Catch-all）开关
  * Action 选择：发送到 Worker
  * Worker 选择：你刚部署的 `cunmail`

回到设置，点击 添加缺失记录，等待 DNS 记录同步完成（状态显示"已启用"）。

关于全收规则：全收代表无论主域名还是子域名的邮件都发送到该 Worker。如果以后需要为主域名单独配置其他 Worker，单独创建的规则优先级高于全收规则。

### 第六步：测试收件

打开 Worker 分配的域名，进入临时邮箱页面。选择有效期（1小时/6小时/24小时/7天），点击一键生成邮箱。

向生成的邮箱地址发送一封测试邮件，十几秒后页面应自动接收到邮件。

密码找回功能：创建邮箱后点击"查看密码"保存。后续可以通过密码登录找回该邮箱。

### 多个域名的配置

如果需要在多个域名下使用临时邮箱，需要在 `EMAIL_DOMAIN` 中用逗号分隔多个域名。同时，每个域名都需要在 Email Routing 中配置对应的路由规则。

* * *

## 我的部署体验

测试环境：

  * 平台：Cloudflare Workers + D1 + Email Routing（免费套餐）
  * 域名：二级域名托管在 Cloudflare 上
  * 部署方式：GitHub Actions 自动部署

部署结果：

✅ 顺利的地方：

  * GitHub Actions 自动部署很省心，配置好 Secrets 后一键完成
  * 邮箱界面清爽，有效期设置直观
  * 收邮件速度很快，发送后十几秒就能收到
  * 密码找回功能实测可用

❌ 卡住的地方：

  * API Token 权限容易漏选 D1 编辑权限，如果部署失败先检查 Token
  * 二级域名需要先启用子域名才能配置路由规则，很多人不知道这一步
  * 域名多的时候每个都要单独配路由规则

## 优点和不足

### 优点

  * 零成本部署，跑在 Cloudflare 免费套餐上
  * 自定义域名，不会被网站屏蔽
  * GitHub Actions 一键部署，新手友好
  * 支持密码找回，不会丢了找不到

### 不足

  * 目前只支持收件，发件功能需要额外配置（下期视频介绍）
  * 二级域名配置路由规则比主域名多一步
  * 多个域名需要分别配置路由规则

## 常见问题 FAQ

### CunMail 部署需要花钱吗？

不需要。全部跑在 Cloudflare 免费套餐上。唯一需要的是自己的域名，域名年费正常就几十块。

### 部署完了收不到邮件怎么办？

检查三点：① Email Routing 是否已开通 ② 子域名是否已启用（二级域名部署时）③ Catch-all 路由规则是否已指向 Worker。

### 二级域名怎么配置？

在 Email Routing 设置中添加子域名，启用后再回到路由规则创建 Catch-all 规则。主域名可以直接配置路由规则，二级域名需要先启用。

### 临时邮箱的有效期多长？

支持 1 小时、6 小时、24 小时、7 天四个选项。到期后邮箱自动销毁。

### 支持多个域名吗？

支持。`EMAIL_DOMAIN` 中用逗号分隔多个域名。每个域名需要在 Email Routing 中配置对应的路由规则。

### 忘了邮箱密码怎么办？

创建邮箱时点击"查看密码"保存。后续可以通过密码登录找回该邮箱。超过有效期后邮箱销毁，找不回来。

### 能发邮件吗？

当前教程只支持收件。发件功能需要额外配置发信渠道，下期视频会详细介绍。

## 总结

本文介绍了 CunMail 临时邮箱系统的完整部署流程。

通过实际部署测试：

  1. 基于 Cloudflare Workers + D1 + Email Routing，零成本自建临时邮箱
  2. 二级域名部署需要先启用子域名再配置路由规则
  3. 收邮件功能完整，支持自定义有效期和密码找回

如果你有自己的域名且托管在 Cloudflare 上，CunMail 是一个值得搭建的临时邮箱系统。

## 相关资源

GitHub 仓库：<https://github.com/cunzhangcrypto/cunmail>

官网博客：<https://www.cunzhangblog.com/>

Cloudflare：<https://cloudflare.com/>

原项目 vmail：<https://github.com/oiov/vmail>

❤️ 请村长喝杯咖
