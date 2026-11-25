---
title: CPA-Manager-Plus最新版本搭建教程
date: '2026-07-16 12:00:00'
cover: https://picsum.photos/seed/cpa-manager-plus/800/450
tags:
- GPT
categories:
- GPT
description: 一键安装脚本 bash <(curl -sL kejilion.sh) app CLIProxyAPI 安装脚本适合第一次部署，或已经有 CPA、只想把 CPAMP 跑起来的环境。它不会直接覆盖已有配置文件；执行前会先展示安装摘要，确认后才写入文件和启动服务。 cd ~/cpa-
---
# 一键安装脚本

# bash <(curl -sL kejilion.sh) app CLIProxyAPI 

安装脚本适合第一次部署，或已经有 CPA、只想把 CPAMP 跑起来的环境。它不会直接覆盖已有配置文件；执行前会先展示安装摘要，确认后才写入文件和启动服务。

## 
[code]
    cd ~/cpa-manager-plus
    cat secrets/cpamp-admin-key
[/code]
[/code]

如果输出类似：
[code] 
    cpamp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[/code]
[/code]

这就是登录密钥。打开：
[code] 
    http://你的服务器IP:18317/management.html  
      
    
    清理废弃的旧镜像 (可选) 更新完成后，为了节省服务器磁盘空间，可以清理掉旧版本的悬空镜像：
    
    
    
    
    
    
    
    docker image prune -f
[/code]
[/code]

## 更新

进入目录：
[code] 
    cd /root/cpa-manager-plus  
    
    
    ### 3. 拉取最新版镜像
    
    
    
[code]
    docker pull seakee/cpa-manager-plus:latest
[/code]
[/code]

官方 Docker 镜像持续发布新版，例如近期版本包含 v1.10、v1.11 等更新。

### 5\. 重新启动

如果你原来用 docker-compose：

直接：
[code] 
    docker compose up -d
[/code]
[/code]

如果提示旧镜像：
[code] 
    docker compose pull
    docker compose up -d
[/code]
[/code]

这是最推荐方式。

`
[/code]
[/code]

## 清理docker不用的；docker image prune -f

## 运行方式

  

下载脚本后运行：
[code]
    curl -fsSLO https://raw.githubusercontent.com/seakee/CPA-Manager-Plus/main/bin/install-cpamp.sh
    bash install-cpamp.sh
[/code]

如果需要先查看内容：
[code]
    less install-cpamp.sh
    bash install-cpamp.sh
[/code]

脚本会按顺序处理：

  1. 检查系统、架构、WSL、端口和必要命令。
  2. 选择后续操作语言。
  3. 选择安装范围：CPA + CPAMP，或仅安装 CPAMP。
  4. 选择部署方式：Docker，或 CPAMP 原生包。
  5. 生成最小配置文件和本机 secret 文件。
  6. 展示摘要，可确认、返回修改或退出。
  7. 确认后执行部署。
