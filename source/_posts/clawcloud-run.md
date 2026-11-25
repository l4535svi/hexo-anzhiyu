---
title: Clawcloud-run自动登录助手，无忧保号，应对爪云新政策！
date: '2026-01-04 12:00:00'
cover: https://picsum.photos/seed/clawcloud-run/800/450
tags:
- ClawCloud项目
categories:
- ClawCloud项目
description: ClawCloud Run 免费计划新政策及自动登录助手部署教程 大家好，欢迎来到我的博客！最近， ClawCloud Run 推出了一个针对免费计划用户的闲置资源回收新政策。今天就来聊聊这个政策的要点，以及一个超级实用的工具—— ClawCloud Run 自动登录助手 ，帮助
---
# [](https://fkjun.com/p/clawcloud-run/#ClawCloud-Run-%E5%85%8D%E8%B4%B9%E8%AE%A1%E5%88%92%E6%96%B0%E6%94%BF%E7%AD%96%E5%8F%8A%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95%E5%8A%A9%E6%89%8B%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B "ClawCloud Run 免费计划新政策及自动登录助手部署教程")ClawCloud Run 免费计划新政策及自动登录助手部署教程

大家好，欢迎来到我的博客！最近，ClawCloud Run 推出了一个针对免费计划用户的闲置资源回收新政策。今天就来聊聊这个政策的要点，以及一个超级实用的工具——ClawCloud Run 自动登录助手，帮助大家避免服务被暂停或清零。

## [](https://fkjun.com/p/clawcloud-run/#%E6%B3%A8%E5%86%8CClawCloud-Run "注册ClawCloud Run")注册ClawCloud Run

[点这里注册一个ClawCloudRun账号](https://console.run.claw.cloud/signin?link=WRJQ4YKZNLI5)

## [](https://fkjun.com/p/clawcloud-run/#%E6%96%B0%E6%94%BF%E7%AD%96%E8%A6%81%E7%82%B9 "新政策要点")新政策要点

ClawCloud Run 的这项政策主要针对免费计划用户，核心内容如下：

  1. 针对免费套餐：仅适用于免费用户。
  2. 不活跃判断标准：如果你的账号30天内没有登录控制台，就会被标记为不活跃。
  3. 后果：
     * 不会删除账号本身。
     * 但会把你部署的应用和服务全部清零/暂停（可能需要重新部署）。
     * 相当于服务被停掉，资源被回收。

对于使用免费容器的朋友来说，定期登录控制台“保活”就变得很重要了。

我个人没怎么用 ClawCloud Run，因为之前试过部署小应用，发现运行起来很卡，几乎用不下去。但很多粉丝和群友都在用，一个群友推荐了这个自动登录脚本，我试了下觉得不错，就调试优化了一下，开了个项目分享给大家。

项目名称：ClawCloud Run 自动登录助手（原脚本写得非常好，我只是修复了些小问题并优化了体验）。

## [](https://fkjun.com/p/clawcloud-run/#%E4%BD%BF%E7%94%A8%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6 "使用前提条件")使用前提条件

在使用脚本前，请确保：

  * 你的 ClawCloud Run 账号是通过 GitLab 注册的（脚本依赖此登录方式）。
  * 如果开启了两步验证（2FA），必须启用验证码（TOTP）方式（如 Google Authenticator 或类似验证器）。
    * 支持 Passkey + 验证码组合，但必须有验证码方式。
    * 如果没开启 2FA，直接用密码登录也没问题。

## [](https://fkjun.com/p/clawcloud-run/#%E9%83%A8%E7%BD%B2%E6%AD%A5%E9%AA%A4 "部署步骤")部署步骤

### [](https://fkjun.com/p/clawcloud-run/#1-Fork-%E9%A1%B9%E7%9B%AE%E5%88%B0%E8%87%AA%E5%B7%B1%E7%9A%84%E4%BB%93%E5%BA%93 "1. Fork 项目到自己的仓库")1\. Fork 项目到自己的仓库

打开原项目页面，点击 Fork，将项目 Fork 到你的 GitHub 账号下（名字保持默认即可）。

### [](https://fkjun.com/p/clawcloud-run/#2-%E9%85%8D%E7%BD%AE-Secrets-%E5%8F%98%E9%87%8F "2. 配置 Secrets 变量")2\. 配置 Secrets 变量

进入 Fork 后的项目 → Settings → Secrets and variables → Actions → 添加以下变量：

Secret 名称| 是否必须| 描述  
---|---|---  
`GH_USERNAME`| 是| 你的 GitHub 用户名。  
`GH_PASSWORD`| 是| 你的 GitHub 密码。  
`GH_SESSION`| 是| GitHub 的 `user_session` Cookie 值。首次运行时可不填，脚本会自动获取并提示你更新。如果配置了 `REPO_TOKEN`，脚本可自动更新此值。  
`TG_BOT_TOKEN`| 是| 用于发送通知的 Telegram Bot Token。如果你需要接收登录状态或进行两步验证，则必须配置。  
`TG_CHAT_ID`| 是| 你的 Telegram User ID 或 Channel ID，用于接收机器人消息。  
`REPO_TOKEN`| 是| GitHub Personal Access Token。如果希望脚本自动更新 `GH_SESSION`，需要提供此 Token。请授予 `repo` 权限。  
`TWO_FACTOR_WAIT`| 否| 两步验证的等待时间（秒），默认为 `120`。  
  
#### [](https://fkjun.com/p/clawcloud-run/#%E5%88%9B%E5%BB%BA-Telegram-%E6%9C%BA%E5%99%A8%E4%BA%BA "创建 Telegram 机器人")创建 Telegram 机器人

  1. 在 Telegram 搜索 @BotFather，发送 `/newbot` 创建机器人。
  2. 设置名字和用户名（用户名需以 `bot` 结尾）。
  3. 获取 Token，填入 `TG_BOT_TOKEN`。
  4. 获取 Chat ID：私聊我的应用机器人，[@fkjapps_bot](https://t.me/ffkjapps_bot), 使用/myid 命令。

#### [](https://fkjun.com/p/clawcloud-run/#%E7%94%9F%E6%88%90-GitHub-Token "生成 GitHub Token")生成 GitHub Token

  1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)。
  2. 生成新 Token，名称随意（如 “ClawCloud Run 登录”）。
  3. 过期时间选 No expiration。
  4. 权限勾选 repo。
  5. 复制 Token 填入 `REPO_TOKEN`。

### [](https://fkjun.com/p/clawcloud-run/#3-%E5%90%AF%E7%94%A8%E5%B9%B6%E8%BF%90%E8%A1%8C-Workflow "3. 启用并运行 Workflow")3\. 启用并运行 Workflow

  1. 项目 → Actions → 找到自动登录 workflow → Enable workflow。
  2. 手动 Run workflow 运行一次（首次验证）。
  3. Telegram 机器人会提示输入验证码 → 打开验证器 App 输入 6 位码并回复。
  4. 首次成功后，脚本保存 Cookie，后续自动登录无需验证码。

### [](https://fkjun.com/p/clawcloud-run/#4-%E8%BF%90%E8%A1%8C%E9%A2%91%E7%8E%87 "4. 运行频率")4\. 运行频率

默认每 5 天运行一次，足够保活。你可以在 workflow 文件中修改 cron 表达式调整频率。

## [](https://fkjun.com/p/clawcloud-run/#%E9%A1%B9%E7%9B%AE%E5%9C%B0%E5%9D%80 "项目地址")项目地址

[ClawCloud-Run](https://github.com/frankiejun/ClawCloud-Run)

## [](https://fkjun.com/p/clawcloud-run/#%E7%BB%93%E8%AF%AD "结语")结语

配置好后，这个助手就会定期自动登录 ClawCloud Run 控制台，保持账号活跃，避免应用被清零。原脚本作者写得真心不错，我只是小修小补。

有任何问题，欢迎在评论区留言，或加入我们的交流群一起讨论！

谢谢阅读，我们下次见！

[![头像](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)![头像](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://fkjun.com/ "头像")
