---
title: 利用Cloudflare R2 +Pages搭建在线图床系统，不限空间，不被墙，超级简单，完全免费
date: '2024-11-17 12:00:00'
cover: https://picsum.photos/seed/cloudflare-r2-pages/800/450
tags:
- 免费图库
categories:
- 免费图库
description: 项目仓库 https://github.com/MarSeventh/CloudFlare-ImgBed 简介 免费图片托管解决方案，基于 Cloudflare Pages 和 Telegram （文件大小不建议超过20MB，过大图片会自动压缩）。 部署流程 一、 前期准备 gi
---
### [](https://yixiu.icu/2024/11/17/tuchuang/#%E9%A1%B9%E7%9B%AE%E4%BB%93%E5%BA%93 "项目仓库")项目仓库

<https://github.com/MarSeventh/CloudFlare-ImgBed>

### [](https://yixiu.icu/2024/11/17/tuchuang/#%E7%AE%80%E4%BB%8B "简介")简介

免费图片托管解决方案，基于 Cloudflare Pages 和 Telegram （文件大小不建议超过20MB，过大图片会自动压缩）。

### [](https://yixiu.icu/2024/11/17/tuchuang/#%E9%83%A8%E7%BD%B2%E6%B5%81%E7%A8%8B "部署流程")部署流程

#### [](https://yixiu.icu/2024/11/17/tuchuang/#%E4%B8%80%E3%80%81-%E5%89%8D%E6%9C%9F%E5%87%86%E5%A4%87 "一、 前期准备")一、 前期准备

  1. github账号：<https://github.com/>
  2. cloudflare账号：<https://www.cloudflare.com/>
  3. 首先需要拥有一个Telegram账户，然后获取Telegram的`TG_BOT_TOKEN`和`TG_CHAT_ID`
  4. 自己的一个域名（可选）

#### [](https://yixiu.icu/2024/11/17/tuchuang/#%E4%BA%8C%E3%80%81%E6%89%80%E6%9C%89%E4%B8%9C%E8%A5%BF%E5%87%86%E5%A4%87%E5%A5%BD%E4%B9%8B%E5%90%8E%E6%88%91%E4%BB%AC%E6%AD%A3%E5%BC%8F%E5%BC%80%E5%A7%8B "二、所有东西准备好之后我们正式开始")二、所有东西准备好之后我们正式开始

  1. 获取Telegram的`TG_BOT_TOKEN`和`TG_CHAT_ID`  
向[@BotFather](https://t.me/BotFather)发送`/newbot`，按照提示输入bot的备注、用户名等信息。成功创建后获得`TG_BOT_TOKEN`
  2. 创建一个新的频道（Channel），进入新建的频道，选择频道管理，将刚才创建的机器人设为频道管理员。
  3. 在刚才创建的频道随便发一条消息，然后转发给[@VersaToolsBot](https://t.me/VersaToolsBot)，获取`TG_CHAT_ID`（频道ID）

#### [](https://yixiu.icu/2024/11/17/tuchuang/#%E4%B8%89%E3%80%81%E5%9C%A8github%E4%B8%8Afork%E9%A1%B9%E7%9B%AE "三、在github上fork项目")三、在github上fork项目

首先打开该[项目仓库](https://github.com/MarSeventh/CloudFlare-ImgBed)点击 “Fork”（如果你认可此项目 可以点击旁边的 starts 以支持作者）

#### [](https://yixiu.icu/2024/11/17/tuchuang/#%E5%9B%9B%E3%80%81%E7%99%BB%E5%BD%95cloudflare%E5%88%9B%E5%BB%BApages "四、登录cloudflare创建pages")四、登录cloudflare创建pages

  1. 成功创建 fork 后来到 [cloudflare](https://www.cloudflare.com/) 登录你的账号并打开仪表盘 点击侧边栏中的 `Workers 和 Pages`
  2. 然后选到 “Pages” 一栏，点击 “连接到 Git”
  3. 授权git之后选择该项目，什么都不用配置，直接点击部署

#### [](https://yixiu.icu/2024/11/17/tuchuang/#%E4%BA%94%E3%80%81%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E4%BB%A5%E5%8F%8A%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9F%9F%E5%90%8D "五、配置环境变量以及自定义域名")五、配置环境变量以及自定义域名

  1. 点击`KV`（在 Workers 和 Pages 菜单下），配置一个KV数据库，名称随意
  2. 点击`R2 对象存储`，配置一个R2存储桶，名称随意（需要信用卡，没有的自己去申请一个，实在不行虚拟卡也可以）
  3. 绑定`KV`和`R2 对象存储`
     1. 依次点击`Workers 和 Pages`->`概述`->`设置`->`绑定`
     2. 依次点击`添加`->`KV命名空间`，选择自己创建的`KV`，名称设置为`img_url`
     3. 依次点击`添加`->`R2存储桶`，选择自己创建的`R2 对象存储`，名称设置为`img_r2`
  4. 依次点击`Workers 和 Pages`->`概述`->`自定义域`，输入自己托管在cloudflare的域名(如果没有可忽略这个步骤)
  5. 依次点击`Workers 和 Pages`->`概述`->`设置`->`变量与机密`  
添加以下变量，其中`TG_BOT_TOKEN`和`TG_CHAT_ID`是必须添加的

变量名称| 作用| 是否必须  
---|---|---  
BASIC_USER| 后台管理的账户名| 必须  
BASIC_PASS| 后台管理的密码| 推荐  
AUTH_CODE| 前台的认证码| 强烈推荐 防止他人滥用  
TG_BOT_TOKEN| 刚才获得的机器人Token| *必须  
TG_CHAT_ID| 刚才获得的频道ID| *必须  
  
完成后点击保存 然后重新部署（所有关于环境变量的修改都要重新部署一遍）

选到 `部署` 一栏 在 `所有部署` 下面找到你最新的部署（就是最上面的那一个），鼠标点击在右侧三个点 在弹出的菜单中选择 `重新部署`

部署完成后即可使用！！！
