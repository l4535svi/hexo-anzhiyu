---
title: 将Telegram channel变成博客/QQ空间说说/树洞/备忘录/情侣日常记录，cloudflare超好玩的新项目，超多好玩
date: '2024-12-29 12:00:00'
cover: /img/covers/telegram-channelqqcloudflare.jpg
tags:
- 建站
categories:
- 建站
description: '✨ 特性与应用场景 将 Telegram Channel 转为微博客 作为个人备忘录 个人树洞，让你悄悄做一个有趣的人 支持多人同时发表动态 类似 QQ 空间的说说功能 个人专属微博 更多应用场景，欢迎探索！ 🪧 演示 真实用户展示 面条实验室 : memo.miantiao.m'
---
## ✨ 特性与应用场景

  * 将 Telegram Channel 转为微博客
  * 作为个人备忘录
  * 个人树洞，让你悄悄做一个有趣的人
  * 支持多人同时发表动态
  * 类似 QQ 空间的说说功能
  * 个人专属微博
  * 更多应用场景，欢迎探索！

* * *

## [](https://www.limin.studio/2024/11/08/BroadcastChannel/#%F0%9F%AA%A7-%E6%BC%94%E7%A4%BA "🪧 演示")🪧 演示

### [](https://www.limin.studio/2024/11/08/BroadcastChannel/#%E7%9C%9F%E5%AE%9E%E7%94%A8%E6%88%B7%E5%B1%95%E7%A4%BA "真实用户展示")真实用户展示

  * 面条实验室: [memo.miantiao.me](https://memo.miantiao.me/)（作者的微博客）
  * 利民工作室 Limin Studio: [channel.limin.studio](https://channel.limin.studio/)（我的微博客）

* * *

## [](https://www.limin.studio/2024/11/08/BroadcastChannel/#%F0%9F%9B%A0%EF%B8%8F-%E5%89%8D%E6%9C%9F%E5%87%86%E5%A4%87 "🛠️ 前期准备")🛠️ 前期准备

  1. Cloudflare: [点击进入](https://broadcast-channel.pages.dev/)（必备）
  2. 域名（非必备，但推荐）: [Spaceship 超低价域名平台](https://spaceship.sjv.io/limin)
  3. Telegram（必备）：需创建频道
  4. GitHub（必备）：[GitHub 主页](https://github.com/)
  5. Myfin（可开通 50 张虚拟卡用于绑定 Cloudflare 以避免扣费）:  
[Myfin 视频介绍](https://youtu.be/gg3Ji4WDszs?si=IiIjpVLoodG_w7_H)
  6. Telegram 搜索机器人: 推荐使用 [SoSo 机器人](https://t.me/soso?start=a_7133970706)

* * *

## [](https://www.limin.studio/2024/11/08/BroadcastChannel/#%F0%9F%8F%97%EF%B8%8F-%E9%83%A8%E7%BD%B2%E6%AD%A5%E9%AA%A4 "🏗️ 部署步骤")🏗️ 部署步骤

  1. Fork 项目: [点击 Fork](https://github.com/ccbikai/BroadcastChannel/fork) 此项目到你的 GitHub
  2. 在 Cloudflare 中创建 Pages 并连接到 GitHub
  3. 选择 BroadcastChannel 项目并选择 Astro 框架
  4. 配置环境变量 `CHANNEL` 为你的频道名称（最低配置，更多可选项见下文）
  5. 保存并部署
  6. 可选：绑定域名
  7. 更新代码后重新部署，参考 [GitHub 官方文档](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork#syncing-a-fork-branch-from-the-web-ui)

* * *

## [](https://www.limin.studio/2024/11/08/BroadcastChannel/#%E2%9A%92%EF%B8%8F-%E9%85%8D%E7%BD%AE%E7%A4%BA%E4%BE%8B "⚒️ 配置示例")⚒️ 配置示例

plaintext

```

    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    11  
    12  
    13  
    14  
    15  
    16  
    17  
    18  
    19  
    20  
    21  
    22  
    23  
    24  
    25  
    26  
    27  
    28  
    29  
    30  
    31  
    32  
    33  
    34  
    35  
    36  
    37  
    38  
    39  
    40  
    41  
    42  
    43  
    44  
    45  
    46  
    47  
    

```

| 

```

    ## Telegram 频道用户名（必须配置），t.me/ 后的字符  
    CHANNEL=miantiao_me  
      
    ## 语言与时区设置  
    LOCALE=zh-cn  
    TIMEZONE=Asia/Shanghai  
      
    ## 社交媒体用户名  
    TELEGRAM=ccbikai  
    TWITTER=ccbikai  
    GITHUB=ccbikai  
      
    ## 社交媒体 URL 配置  
    DISCORD=https://discord.com  
    PODCAST=https://podcast.com  
      
    ## 头部与尾部代码注入（支持 HTML）  
    FOOTER_INJECT=FOOTER_INJECT  
    HEADER_INJECT=HEADER_INJECT  
      
    ## SEO 配置项  
    NO_FOLLOW=false  
    NO_INDEX=false  
      
    ## Sentry 配置项  
    SENTRY_AUTH_TOKEN=SENTRY_AUTH_TOKEN  
    SENTRY_DSN=SENTRY_DSN  
    SENTRY_PROJECT=SENTRY_PROJECT  
      
    ## Telegram 主机名称与静态资源代理  
    HOST=telegram.dog  
    STATIC_PROXY=  
      
    ## 启用谷歌站内搜索  
    GOOGLE_SEARCH_SITE=memo.miantiao.me  
      
    ## 标签页设置（英文逗号分割）  
    TAGS=标签A,标签B,标签C  
      
    ## 评论展示设置  
    COMMENTS=true  
      
    ## 链接配置（英文逗号和分号分割）  
    LINKS=Title1,URL1;Title2,URL2;Title3,URL3;  
      
    ## 侧边栏导航配置  
    NAVS=Title1,URL1;Title2,URL2;Title3,URL3;  
    

```

  
  
---|---
