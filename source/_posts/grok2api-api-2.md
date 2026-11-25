---
title: Grok2API 保姆级教程，免费搭建大模型 API
date: '2026-04-01 12:00:00'
cover: https://picsum.photos/seed/grok2api-api-2/800/450
tags:
- OpenClaw
categories:
- OpenClaw
description: Grok2Api 把 Grok 包装成 OpenAI 风格的 API 服务，还能一键 NSFW 如果你要接入现有程序、做 API 服务、跑多账号池，或者统一管理调用入口，它就会顺手很多 项目地址： https://github.com/chenyme/grok2api 推荐服务器
---
Grok2Api 把 Grok 包装成 OpenAI 风格的 API 服务，还能一键 NSFW

[![51168ab0059e58356b094641158f3725.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/51168ab0059e58356b094641158f3725.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/51168ab0059e58356b094641158f3725.png)

如果你要接入现有程序、做 API 服务、跑多账号池，或者统一管理调用入口，它就会顺手很多

[![9f754d91ec32d7bc3ff9080190800a9f.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/9f754d91ec32d7bc3ff9080190800a9f.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/9f754d91ec32d7bc3ff9080190800a9f.png)

项目地址：<https://github.com/chenyme/grok2api>

推荐服务器部署，不要选择国内地区，选择linux版本，有Docker Compose上手快 腾讯云新加坡，硅谷，东京地区价格是199元一年，2核4G30M带宽，60GBSSD盘 1.5T月流量↓↓↓

购买地址：<https://curl.qcloud.com/oyWDLkRJ>

[![901e6a6b9d578895522b0f72d15243ec.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/901e6a6b9d578895522b0f72d15243ec.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/901e6a6b9d578895522b0f72d15243ec.png)

教程

一、系统ubuntu24，安装 Docker + Compose
[code]
    sudo apt update && sudo apt install -y ca-certificates curl gnupg && \
    sudo install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    sudo chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    sudo apt update && \
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    
[/code]

[![3c91a84e433cd5f5230b26bbca01ad65.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/3c91a84e433cd5f5230b26bbca01ad65.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/3c91a84e433cd5f5230b26bbca01ad65.png) 二、启动 Docker
[code]
    sudo systemctl enable docker
    sudo systemctl start docker
    
[/code]

[![67f276b1aef734debf6517b88995ea9f.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/67f276b1aef734debf6517b88995ea9f.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/67f276b1aef734debf6517b88995ea9f.png)

三、安装grok2Api
[code]
    git clone https://github.com/chenyme/grok2api
    
    cd grok2api
    
    docker compose up -d
    
[/code]

[![c4efbe6ee4356861422c02ff542a97a7.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/c4efbe6ee4356861422c02ff542a97a7.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/c4efbe6ee4356861422c02ff542a97a7.png)

四、访问面板，打开浏览器：

[http://你的IP:8000/admin](http://xn--ip-0p3cm89l:8000/admin)

账号：不用填 密码：grok2api

⚠️ 一定要改密码！

[![40cf822ee8adf09a54e0bc90bf8074af.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/40cf822ee8adf09a54e0bc90bf8074af.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/40cf822ee8adf09a54e0bc90bf8074af.png)

五.获取 Token（SSO Cookie）

在浏览器中打开并登录 grok.com

按 F12 打开浏览器开发者工具

依次点击 Application（应用） → Cookies → 选择 grok.com

在 Cookie 列表中找到名为 sso、sso-rw 或 ssoBasic 的条目

复制该条目的 值（通常是以 eyJ 开头的长字符串）

[![03370f9d0c944352b96cfe6870889b60.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/03370f9d0c944352b96cfe6870889b60.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/03370f9d0c944352b96cfe6870889b60.png)

六、将此值粘贴到 grok2api 管理后台的 Token 添加对话框中

[![58d0639c4228d919a901c6801be5f976.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/58d0639c4228d919a901c6801be5f976.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/58d0639c4228d919a901c6801be5f976.png)

七、成功

[![2532b6fa44f164f9887dbf6008fa0c68.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/2532b6fa44f164f9887dbf6008fa0c68.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/2532b6fa44f164f9887dbf6008fa0c68.png)

八、配置管理生成Api密钥

[![0962c691c9e3f63bda196c1688d666fc.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/0962c691c9e3f63bda196c1688d666fc.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/0962c691c9e3f63bda196c1688d666fc.png)

九、对话
[code]
    curl -X POST "http://154.9.227.209:8000/v1/chat/completions" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer 你的API_KEY" \
      -d '{
        "model": "grok-4",
        "messages": [
          {
            "role": "user",
            "content": "你好"
          }
        ]
      }'
    
[/code]

[![9c16384c5ce591edbfa2e103b22cc642.png](https://github.com/helloyangy/Grok2API-Tutorial/raw/main/_resources/9c16384c5ce591edbfa2e103b22cc642.png)](https://github.com/helloyangy/Grok2API-Tutorial/blob/main/_resources/9c16384c5ce591edbfa2e103b22cc642.png)

调用：<http://localhost:8000/v1>

模型：grok-4
