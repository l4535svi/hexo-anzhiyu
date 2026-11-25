---
title: CLIProxyAPIPlus版本如何安装更新
date: '2026-04-07 12:00:00'
cover: https://picsum.photos/seed/cliproxyapiplus/800/450
tags:
- GPT
categories:
- GPT
description: 一、最简单安装（推荐） 方式1：直接 Docker（最快） 项目自带 docker-compose.yml ，直接跑： git clone https://github.com/router-for-me/CLIProxyAPIPlus.git cd CLIProxyAPIPlu
---
# 一、最简单安装（推荐）

## 方式1：直接 Docker（最快）

项目自带 `docker-compose.yml`，直接跑：
[code] 
    git clone https://github.com/router-for-me/CLIProxyAPIPlus.git  
    cd CLIProxyAPIPlus  
      
    cp config.example.yaml config.yaml  
      
    docker compose up -d
[/code]

👉 优点：

  * 一步启动 
  * 自动处理环境 

👉 官方也支持 docker 方式部署 

# 一、如果你是 Docker 部署（你大概率是这个）

## 直接升级（标准流程）
[code] 
    cd CLIProxyAPIPlus  
      
    docker compose pull  
    docker compose up -d
[/code]

* * *

## 强制重建（推荐）
[code] 
    docker compose down  
    docker compose pull  
    docker compose up -d --build
[/code]

* * *

👉 优点：

  * 不丢配置（config.yaml 保留） 
  * 自动替换新版本
