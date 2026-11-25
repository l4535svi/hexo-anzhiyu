---
title: ChatGPT2API
date: '2026-04-27 12:00:00'
cover: https://picsum.photos/seed/chatgpt2api/800/450
tags:
- GPT
categories:
- GPT
description: 支持文生图、图生图编辑、多图合成，模型包括非常强大的 gpt-image-2，并且还没有某包那样的水印 6.22号最新升级教程如果你是用 Docker Compose 部署的，项目作者给出的官方升级方式是： cd chatgpt2api docker pull ghcr.io/b
---
支持文生图、图生图编辑、多图合成，模型包括非常强大的 gpt-image-2，并且还没有某包那样的水印

6.22号最新升级教程如果你是用 Docker Compose 部署的，项目作者给出的官方升级方式是：
[code] 
    cd chatgpt2api  
      
    docker pull ghcr.io/basketikun/chatgpt2api:latest  
      
    docker compose down  
      
    docker compose up -d
[/code]
[/code]

更新谷歌ai最可行的

## 方法一：使用 Docker Compose (推荐，最常见的方法)

如果你最初是通过 `docker compose up -d` 或者 `docker-compose.yml` 文件部署的，请按照以下步骤操作：

**1\. 进入项目目录** 首先，通过终端进入你存放 `docker-compose.yml` 和 `config.json` 的目录：
[code]
    cd /你的/项目/路径/chatgpt2api
    
[/code]

**2\. 同步最新的项目代码 (可选但推荐)** 如果你最初是通过 `git clone` 下载的项目，建议先拉取最新的配置文件（如最新的 `docker-compose.yml` 可能会新增环境变量）：
[code]
    git pull
    
[/code]

_注意：这可能会提示你合并配置，如果你的`docker-compose.yml` 有魔改过，请注意检查差异。_

**3\. 拉取最新的 Docker 镜像** 使用以下命令拉取最新的 `ghcr.io/basketikun/chatgpt2api:latest` 镜像：
[code]
    docker compose pull
    # 或者旧版命令：docker-compose pull
    
[/code]

**4\. 重新启动容器并应用更新** 执行以下命令，Docker Compose 会自动检测到镜像的变更，停止旧容器并使用新镜像启动新容器：
[code]
    docker compose up -d
    # 或者旧版命令：docker-compose up -d
    
[/code]

**5\. 清理废弃的旧镜像 (可选)** 更新完成后，为了节省服务器磁盘空间，可以清理掉旧版本的悬空镜像：
[code]
    docker image prune -f
    
[/code]

  

## 修改管理员密码

方式一：Docker Compose 部署，推荐

  1. 进入项目目录：

`cd chatgpt2api `

  2. 编辑 docker-compose.yml：

`nano docker-compose.yml `

找到这一段：

`environment: - STORAGE_BACKEND=json # - CHATGPT2API_AUTH_KEY=your_secret_key `

改成这样，注意去掉前面的 #：

`environment: - STORAGE_BACKEND=json - CHATGPT2API_AUTH_KEY=你的新密码 `

例如：

`environment: - STORAGE_BACKEND=json - CHATGPT2API_AUTH_KEY=MyNewAdminKey_2026 `

  3. 保存退出。

如果你用的是 nano：

`Ctrl + O 回车 Ctrl + X `

  4. 重启容器：

`docker compose up -d`

##   

## 彻底删除（必须这样做）
[code]
    rm -rf ~/chatgpt2api
[/code]

然后再确认：
[code]
    ls
[/code]

👉 必须看不到：
[code] 
    chatgpt2api
[/code]

  

[![功能展示](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/b4d7752629dac4e31eb7a09761905f69.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/b4d7752629dac4e31eb7a09761905f69.png)

提供账号池管理，Docker 一键部署

[![账号池管理](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/171fce8cff8b899985c4fd77a940b3fe.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/171fce8cff8b899985c4fd77a940b3fe.png)

项目地址： <https://github.com/basketikun/chatgpt2api>

* * *

## 服务器推荐

[](https://github.com/helloyangy/chatgpt2api-Tutorial#%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%8E%A8%E8%8D%90)

推荐服务器部署，不要选择国内地区，选择 Linux 版本 Docker 上手快。

腾讯云新加坡 / 硅谷 / 东京地区价格是 199 元一年，2 核 4G 30M 带宽，60GB SSD 盘 1.5T 月流量，推荐硅谷地区 CN2 线路，系统选 Ubuntu 24。

购买地址： <https://curl.qcloud.com/oyWDLkRJ>

[![服务器选购](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/72d493eab65af6588b3ed9cb7585b177.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/72d493eab65af6588b3ed9cb7585b177.png)

* * *

## 部署教程

[](https://github.com/helloyangy/chatgpt2api-Tutorial#%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B)

### 1\. 安装 Docker

[](https://github.com/helloyangy/chatgpt2api-Tutorial#1-%E5%AE%89%E8%A3%85-docker)
[code]
    sudo apt update
    sudo apt install -y ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo docker run hello-world
[/code]

[![安装 Docker](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/1b55ecb41568de331b7837106a34f478.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/1b55ecb41568de331b7837106a34f478.png)

### 2\. 下载项目

[](https://github.com/helloyangy/chatgpt2api-Tutorial#2-%E4%B8%8B%E8%BD%BD%E9%A1%B9%E7%9B%AE)
[code]
    git clone https://github.com/basketikun/chatgpt2api.git
[/code]

[![下载项目](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/6c30c3ba3b8489f503b9fd6ecc8a55ee.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/6c30c3ba3b8489f503b9fd6ecc8a55ee.png)

### 3\. 打开项目

[](https://github.com/helloyangy/chatgpt2api-Tutorial#3-%E6%89%93%E5%BC%80%E9%A1%B9%E7%9B%AE)
[code]
    cd chatgpt2api
[/code]

[![打开项目](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/2a931cd1cbb42d623e73c8d6591ea95c.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/2a931cd1cbb42d623e73c8d6591ea95c.png)

### 4\. 运行

[](https://github.com/helloyangy/chatgpt2api-Tutorial#4-%E8%BF%90%E8%A1%8C)
[code]
    sudo docker compose up -d
[/code]

[![运行](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/be9bb8cbf61b90a40033e0833d94c500.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/be9bb8cbf61b90a40033e0833d94c500.png)

### 5\. 打开浏览器访问

[](https://github.com/helloyangy/chatgpt2api-Tutorial#5-%E6%89%93%E5%BC%80%E6%B5%8F%E8%A7%88%E5%99%A8%E8%AE%BF%E9%97%AE)
[code]
    http://你的服务器公网IP:3000
    
[/code]

> 注意： 记得防火墙放通 3000 端口

密钥是：`chatgpt2api`

[![浏览器访问](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/77ebddebd919b8c4827d1ef153911885.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/77ebddebd919b8c4827d1ef153911885.png)

### 6\. 导入账号

[](https://github.com/helloyangy/chatgpt2api-Tutorial#6-%E5%AF%BC%E5%85%A5%E8%B4%A6%E5%8F%B7)

选择：导入 Session JSON

[![导入账号](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/bbf7e2ed2e956358bc8cdf46cebd624e.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/bbf7e2ed2e956358bc8cdf46cebd624e.png)

### 7\. 获取 accessToken

[](https://github.com/helloyangy/chatgpt2api-Tutorial#7-%E8%8E%B7%E5%8F%96-accesstoken)

打开以下地址，复制页面返回的完整 JSON，系统会自动提取其中的 `accessToken`：
[code]
    https://chatgpt.com/api/auth/session
    
[/code]

[![获取 Token](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/60402961b5c49b5dfa11d63c05663efe.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/60402961b5c49b5dfa11d63c05663efe.png)

### 8\. 导入成功

[](https://github.com/helloyangy/chatgpt2api-Tutorial#8-%E5%AF%BC%E5%85%A5%E6%88%90%E5%8A%9F)

[![导入成功](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/379270ac146b2a9e040291a88ff65821.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/379270ac146b2a9e040291a88ff65821.png)

### 9\. 点击顶部的画图

[](https://github.com/helloyangy/chatgpt2api-Tutorial#9-%E7%82%B9%E5%87%BB%E9%A1%B6%E9%83%A8%E7%9A%84%E7%94%BB%E5%9B%BE)

[![画图功能](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/be37cf15f64404da2e63d8d8a94a6f2d.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/be37cf15f64404da2e63d8d8a94a6f2d.png)

### 10\. 切换模型

[](https://github.com/helloyangy/chatgpt2api-Tutorial#10-%E5%88%87%E6%8D%A2%E6%A8%A1%E5%9E%8B)

模型可以切换为 `gpt-image-2`，额度剩余 7

[![切换模型](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/0e5ef3be8bba1adc9911ee10b7c06ffc.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/0e5ef3be8bba1adc9911ee10b7c06ffc.png)

### 11\. 效果展示

[](https://github.com/helloyangy/chatgpt2api-Tutorial#11-%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA)

提示词：生成一个女生在抖音直播

效果非常强大

[![效果展示 1](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/7b57d7ec22aa431bc1d199c629afd23f.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/7b57d7ec22aa431bc1d199c629afd23f.png)

[![效果展示 2](https://github.com/helloyangy/chatgpt2api-Tutorial/raw/main/_resources/461a5b44163a0b064e94150e696fee5b.png)](https://github.com/helloyangy/chatgpt2api-Tutorial/blob/main/_resources/461a5b44163a0b064e94150e696fee5b.png)

* * *

## API 调用

[](https://github.com/helloyangy/chatgpt2api-Tutorial#api-%E8%B0%83%E7%94%A8)

OpenAI 兼容图片生成接口，用于文生图：
[code]
    curl http://localhost:8000/v1/images/generations \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <auth-key>" \
      -d '{
        "model": "gpt-image-2",
        "prompt": "一只漂浮在太空里的猫",
        "n": 1,
        "response_format": "b64_json"
      }'
[/code]

参数| 值  
---|---  
模型| `gpt-image-2`  
密钥| `chatgpt2api`  
  
> 按需编辑 `config.json` 的密钥，编辑后需要重启 Docker
