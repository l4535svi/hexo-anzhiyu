---
title: EdgeChat 部署教程：在 Cloudflare 上免费搭建团队聊天室（2026实测）
date: '2026-10-11 12:00:00'
tags:
- cloudflare项目
categories:
- cloudflare项目
description: 验证：2026-10-04 一句话结论 EdgeChat 是一款跑在 Cloudflare 上的开源团队聊天系统，实测从 Fork 到上线约 1 分钟，20 人小团队用免费层完全够用。 核心结论 经过实际测试： 首次部署约 1 分钟（本次实测），GitHub Actions 全自
---
验证：2026-10-04

## 一句话结论

EdgeChat 是一款跑在 Cloudflare 上的开源团队聊天系统，实测从 Fork 到上线约 1 分钟，20 人小团队用免费层完全够用。

## 核心结论

经过实际测试：

  * 首次部署约 1 分钟（本次实测），GitHub Actions 全自动创建 D1/KV/R2 资源并跑完迁移
  * 免费层每天 10 万次 Workers 请求（Cloudflare 官网免费额度），20 人小团队实测够用
  * 150 人左右、日常 40-50 人在线的社群免费层不够用，需升级 5 美元/月的 Workers Paid（本次实测估算）

适合：

  * 20-30 人的小团队、项目组，想有个独立聊天室但不想维护服务器的人
  * 有 Cloudflare 账号、愿意花 10 分钟配一次的人

不适合：

  * 上百人、日活几十人的大社群（免费层会超限报错，得加钱）
  * 想要微信那样开箱即用的、不想碰任何配置的人

## 什么是 EdgeChat？

EdgeChat 是一个运行在 Cloudflare 上的开源团队聊天系统。

它主要解决：

  1. 小团队需要一个独立的实时聊天室，不想用公共 IM
  2. 不想买服务器、不想运维，用 Serverless 全家桶搞定
  3. 邀请制管理，成员进出可控

目前主要应用于小团队内部沟通、项目群、兴趣小圈子场景。

## 为什么选择 EdgeChat？

方案| 价格 / 成本| 特点| 稳定性  
---|---|---|---  
自己买 VPS 搭 Rocket.Chat| 约 5 美元/月起（VPS 费用）| 功能全，但要自己运维| 看你运维水平  
用 Slack / 飞书免费版| 免费（功能受限）| 开箱即用| 高，但数据在别人手里  
EdgeChat + Cloudflare| 0 元（免费层，Cloudflare 官网）/ 5 美元/月（超量后）| 邀请制、数据在自己账号下、不用管服务器| 高，超限直接报错停服  
  
## 准备工作

开始之前需要：

  * 一个 Cloudflare 账号（免费注册就行）
  * 一个 GitHub 账号（用来跑 Actions 自动部署）
  * 10 分钟时间

预计时间：10 分钟（含等部署） 难度：⭐⭐

## EdgeChat 部署教程

### 第一步：Fork 仓库

打开 EdgeChat 的 GitHub 仓库，点 Fork 到你自己的账号下。我这一步就点了两下，没什么好说的。

### 第二步：拿 Cloudflare API Token

进 Cloudflare Dashboard，右上角头像 → 我的配置文件 → API 令牌 → 创建令牌 → 创建自定义令牌。

名字随便取，比如 edgechat。权限要加 4 个，缺一个部署都会失败：

  * Account / Workers Scripts / Edit
  * Account / D1 / Edit
  * Account / Workers KV Storage / Edit
  * Account / Workers R2 Storage / Edit

账户资源选"包括你的账号"，拉到最下面继续，创建令牌。

这个 Token 只显示一次，窗口关了就找不回，只能重建。一定先复制存好。

### 第三步：记下 Account ID

在 Workers & Pages 页面右侧栏能看到一串 Account ID，复制下来备用。

### 第四步：配 GitHub Secrets

[![全球高质量代理IP，助力业务无界增长](https://www.cunzhangblog.com/geonix_ads.webp)全球高质量代理IP，助力业务无界增长了解更多 →覆盖200+国家，提供机房IP、住宅IP、手机IP，满足多场景业务需求](https://go.czlab.dev/geonix)

回你 Fork 的仓库，Settings → Secrets and variables → Actions，新建：

  * `CLOUDFLARE_API_TOKEN`：第二步的 Token
  * `CLOUDFLARE_ACCOUNT_ID`：第三步的 ID
  * `EDGECHAT_ADMIN_USERNAME`：管理员用户名，比如 admin
  * `EDGECHAT_ADMIN_PASSWORD`：管理员密码，用强密码
  * `EDGECHAT_ADMIN_DISPLAY_NAME`：显示名，比如 Web3村长

注意：工作流只在首次部署时创建管理员，后面再部署不会覆盖密码。改密码去网页里改。

### 第五步：跑 Deploy Worker

点仓库上方的 Actions，同意启用。工作流列表里有 5 个，选 Deploy Worker，别选错（Deploy Demo 是演示站，点了会失败）。

点 Run workflow，直接运行，两个勾选框都别勾。首次部署我这边约 1 分钟跑完。

### 第六步：打开聊天室

回 Cloudflare → 计算 → Workers，刷新一下就能看到 cfchat 这个 Worker，点进去有分配的域名，打开就是登录页。

用第四步设的管理员账号登录，进管理后台把站点名称、图标改成你自己的。我改完名发现 logo 没刷新过来，可能是个小 bug，不影响用。

### 拉人进来怎么操作？

EdgeChat 是邀请制，没有公开注册。两种方式：

  * 注册链接：建个链接，设好可用次数（比如团队 20 人就设 20），发给大家自己注册
  * 创建用户：你直接指定用户名和初始密码，对方拿来登录就行，适合帮不懂操作的人建号

我实测两种都试了：链接注册和直接建号，消息都是实时互通的。

## 我的测试体验

测试环境：

  * 设备：Win
  * 版本：EdgeChat 2.10.1（部署文档更新日期 2026-10-03）
  * 使用时长：部署 + 功能走查约 1 小时

✅ 好的方面：

  * 部署是真省心，Actions 全自动，D1/KV/R2 不用手动建
  * 消息实时性 ok，我开两个窗口对发，秒到
  * 邀请制这点我喜欢，小圈子用不怕陌生人混进来

❌ 不足的地方：

  * 改完站点名称 logo 没刷新，疑似 bug
  * 免费层是硬限制，超了直接报错停服，不会提前预警

## 常见问题 FAQ

### EdgeChat 部署要多少钱？

0 元起步。Cloudflare 免费层 cover 20 人小团队；150 人左右的社群要上 5 美元/月的 Workers Paid（本次实测估算）。

### 新手从哪开始？

先 Fork 仓库，再按本文第二步到第五步走，10 分钟能跑通。API Token 的 4 个权限别漏，这是最常见的翻车点。

### 在中国大陆能用吗？

Worker 的 workers.dev 域名在大陆访问不稳定，建议绑自己备案过的自定义域名。具体网络问题以实际测试为准。

### 部署失败了怎么办？

先看 Actions 的日志报错。最常见的是 API Token 少了 R2 权限（权限名叫 Workers R2 Storage，容易漏），回去补上重跑就行。

### 有什么风险？数据会丢吗？

有两点要注意：第一，首次部署生成的加密密钥丢了，历史消息永久读不回来，一定要备份到密码管理器；第二，免费层超限直接停服，次日 08:00（北京时间）恢复，重要群聊别全押在免费层上。

### 一定要用 GitHub Actions 部署吗？

不是。也可以本地 wrangler 手动部署。但 Actions 省心，推荐新手走 Actions。

## 总结

通过实际测试：

  1. 从 Fork 到聊天室上线约 1 分钟（本次实测），全程不用碰服务器
  2. 免费层每天 10 万次请求（Cloudflare 官网），20 人小团队实测够用
  3. 加密密钥必须备份，丢了历史消息找不回来

如果你的需求是给小团队搭个独立聊天室，EdgeChat 是一个值得尝试的方案；如果是上百人的大社群，先算好 5 美元/月的预算再动手。

## 相关资源

  * GitHub：<https://github.com/aozorae/Edgechat>
  * Cloudflare 注册：<https://dash.cloudflare.com/sign-up>
  * 完整部署文档:<https://pan.quark.cn/s/6386bcb7096d>
