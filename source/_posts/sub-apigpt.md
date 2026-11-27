---
title: 安装sub-api，白嫖gpt的反带工具
date: '2026-04-15 12:00:00'
cover: /img/covers/sub-apigpt.jpg
tags:
- GPT
categories:
- GPT
description: 升级后出现cf跳出验证如何解决： cd sub2api-deploy进入文件 证据（你给的配置） 你当前有： SERVER_MODE=release 👉 在很多 Go 项目里： release = 生产模式 → 强制安全（验证码开启） debug/dev = 开发模式 → 关闭验
---
升级后出现cf跳出验证如何解决：
[code]
    cd sub2api-deploy进入文件  
    
    
    ## 证据（你给的配置）
    
    你当前有：
[code]
    SERVER_MODE=release
[/code]

👉 在很多 Go 项目里：
[code]
    release = 生产模式 → 强制安全（验证码开启）  
    debug/dev = 开发模式 → 关闭验证码
    
    二、正确改法（关键）
[/code]

### 1️⃣ 编辑 `.env`

### nano .env
[/code]
[code]
### 2️⃣ 修改这几行（必须改）

把：SERVER_MODE=release
[/code]
[code]
改成
[code]
    SERVER_MODE=debug  
    APP_ENV=dev
[/code]

### 3️⃣ 保存

### 3️⃣ 保存
[code] 
    Ctrl + X  
    Y  
    回车
[/code]

* * *

## 三、关键步骤（很多人错这里）升级都使用这个4.17

❌ 不要用：
[code]
    docker restart sub2api
[/code]

👉 必须：
[code]
    docker compose down  
    docker compose up -d
[/code]
[/code]

### docke更新

## 一、标准更新流程（docker-compose）

你现在用这个项目，大概率是 `docker-compose` 部署（README推荐）

### 1️⃣ 拉最新镜像
[code] 
    docker compose pull
[/code]

或者指定：
[code] 
    docker pull weishaw/sub2api:latest
[/code]

镜像就是这个：`weishaw/sub2api`

* * *

### 2️⃣ 重建容器（关键）
[code] 
    docker compose up -d
[/code]

如果想强制更新（推荐）：
[code] 
    docker compose up -d --force-recreate
[/code]

* * *

### 3️⃣ 查看是否更新成功
[code] 
    docker compose ps  
    docker compose logs -f sub2api
[/code]

###   

###   

###   

### ocker Compose（推荐）

[](https://github.com/Wei-Shaw/sub2api/blob/v0.1.106/README_CN.md#%E6%96%B9%E5%BC%8F%E4%BA%8Cdocker-compose%E6%8E%A8%E8%8D%90)

使用 Docker Compose 部署，包含 PostgreSQL 和 Redis 容器。

#### 前置条件

[](https://github.com/Wei-Shaw/sub2api/blob/v0.1.106/README_CN.md#%E5%89%8D%E7%BD%AE%E6%9D%A1%E4%BB%B6-1)

  * Docker 20.10+
  * Docker Compose v2+

#### 快速开始（一键部署）

[](https://github.com/Wei-Shaw/sub2api/blob/v0.1.106/README_CN.md#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2)

使用自动化部署脚本快速搭建：
[code]
    # 创建部署目录
    mkdir -p sub2api-deploy && cd sub2api-deploy
    
    # 下载并运行部署准备脚本
    curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
    
    # 启动服务
    docker compose up -d
    
    # 查看日志
    docker compose logs -f sub2api  
      
    
[/code]
