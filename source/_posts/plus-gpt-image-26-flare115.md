---
title: plus-gpt-image-2.6-flare搭建教程(个人项目二次改写11.5)
date: '2026-11-05 12:00:00'
cover: https://picsum.photos/seed/plus-gpt-image-26-flare115/800/450
tags:
- GPT
categories:
- GPT
description: '一、全新部署 cd ~ git clone https://github.com/wangai14/chatgpt2api-portable.git cd chatgpt2api-portable # 生成配置和随机登录密码 sh deploy.sh init # 拉取镜像 do'
---
### 一、全新部署
[code]
    cd ~
    
    git clone https://github.com/wangai14/chatgpt2api-portable.git
    
    cd chatgpt2api-portable
    
    # 生成配置和随机登录密码
    sh deploy.sh init
    
    # 拉取镜像
    docker compose pull app
    
    # 启动并等待健康检查
    docker compose up -d --no-build --pull never --wait --wait-timeout 120
    
    # 查看状态和端口
    docker compose ps
    docker compose port app 80
[/code]

浏览器访问：
[code]
    http://你的VPS公网IP:3000
[/code]

查看登录密码，复制 `=` 后面的完整内容：
[code]
    grep '^CHATGPT2API_AUTH_KEY=' .env
[/code]

### 二、之前已经部署过

先备份 `.env` 和 `data/`，然后：
[code]
    cd ~/chatgpt2api-portable
    git pull --ff-only
    sh deploy.sh
[/code]

### 三、访问异常时检查
[code]
    curl -I --max-time 5 http://127.0.0.1:3000/
    docker compose logs --tail=100 app
[/code]

本机正常、公网打不开时，再检查云安全组与防火墙是否放行 **TCP 3000** 。不要删除 `data/`，也不要执行 `docker compose down -v`。
