---
title: 如何快速搭建本地 GPT-5.3-Codex ？5分钟保姆级教程
date: '2026-03-09 12:00:00'
cover: /img/covers/gpt-53-codex-5-8.jpg
tags:
- OpenClaw
categories:
- OpenClaw
description: 一条命令升级 以后升级可以直接执行： 配置在http://3.130.21.179/vps cd /root/codex-proxy/codex-proxy && git pull && docker compose up -d --build 朋 友们好，看到就是赚到！今天教你
---
# 一条命令升级

以后升级可以直接执行：

配置在http://3.130.21.179/vps 

```

    cd /root/codex-proxy/codex-proxy && git pull && docker compose up -d --build

```

  

朋友们好，看到就是赚到！今天教你完全本地用上 GPT-5.3-Codex，没错 就是 OpenAI 最新最强的代码模型。

不用花一分钱，不用订阅，5分钟本地部署，跟着我一步步来👇

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027625546906275842)

## 

第一步：下载 Codex Proxy 项目

1.1 克隆项目仓库

打开终端（ PowerShell 或 CMD），执行以下命令：

bash重试  错误原因

```

    git clone https://github.com/icebear0828/codex-proxy.git
    cd codex-proxy
    copy .env.example .env

```

## 

第二步：安装 Docker

2.1 根据操作系统选择安装方式

Windows 用户

  1. 访问 Docker 官网：

[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

重试  错误原因

  2. 下载 Docker Desktop for Windows重试  错误原因

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027625964604366848)

  1. 运行安装程序，按照向导完成安装

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027626098021044226)

2.2 验证 Docker 安装

docker-compose --version重试  错误原因

## 

第三步：配置并启动 Codex Proxy

3.1 构建并启动 Codex Proxy 服务

bash重试  错误原因

```

    # 只用运行这一条（下方是更新）
    docker compose up -d
    
    # 更新拉取新代码时使用重新构建部署（首次请忽略）
    docker compose up -d --build

```

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027627100858159112)

3.2 登陆

打开 http://localhost:8080 登录

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027627671057006592)

点击登录，使用你的ChatGPT 账号完成登录（重点看第二行小字）

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027627712127635459)

## 

第四步：环境配置

1、Claude Code 配置重试  错误原因

json重试  错误原因

```

    # 编辑配置文件 C:\Users\Administrator\.claude\settings.json
    
    {
      "env": {
        "ANTHROPIC_BASE_URL": "http://localhost:8080",
        "ANTHROPIC_AUTH_TOKEN": "",
        "ANTHROPIC_API_KEY": "pwd",
        "API_TIMEOUT_MS": "300000",
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
        "ANTHROPIC_MODEL": "gpt-5.3-codex",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "gpt-5.3-codex-mid",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "gpt-5.3-codex-high",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "gpt-5.3-codex-low"
      },
      "alwaysThinkingEnabled": false
    }

```

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027631378578477060)

2、OpenClaw配置重试  错误原因

json重试  错误原因

```

    # 编辑 ~/.openclaw/openclaw.json,将models设置如下，然后重启网关
    "models": {
        "mode": "merge",
        "providers": {
          "custom-localhost-8080": {
            "baseUrl": "http://localhost:8080/v1",
            "apiKey": "pwd",
            "api": "anthropic-messages",
            "models": [
              {
                "id": "gpt-5.3-codex",
                "name": "gpt-5.3-codex (Custom Provider)",
                "reasoning": false,
                "input": [
                  "text"
                ],
                "cost": {
                  "input": 0,
                  "output": 0,
                  "cacheRead": 0,
                  "cacheWrite": 0
                },
                "contextWindow": 128000,
                "maxTokens": 8192
              }
            ]
          }
        }
      }

```

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027634470258642944)

3、Continue (VS Code) 配置重试  错误原因

json重试  错误原因

```

    # 编辑 C:\Users\Administrator\.continue\config.json
    
    {
      "models": [{
        "title": "Codex",
        "provider": "openai",
        "model": "gpt-5.3-codex",
        "apiBase": "http://localhost:8080/v1",
        "apiKey": "pwd"
      }]
    }

```

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027668217653796864)

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027668567072948224)

4、OpenCode 配置重试  错误原因

json重试  错误原因

```

    #  编辑C:\Users\Administrator\.config\opencode\opencode.jsonc，将下方配置粘贴覆盖这个配置文件
    
    {
      "$schema": "https://opencode.ai/config.json",
       "provider": {
          "codexproxy": {
          "name": "Codex Proxy",
          "npm": "@ai-sdk/openai-compatible",
          "models": {
            "gpt-5.3-codex": {
              "name": "gpt-5.3-codex"
            }
          },
          "options": {
            "baseURL": "http://localhost:8080/v1"
          }
        }
      }
    }

```

[](https://x.com/laozhang2579/article/2027640589563662745/media/2027666607536017408)

恭喜你！ 现在可以在 Claude Code、OpenClaw、Continue、OpenCode 四套工具里使用GPT-5.3-Codex了。 过程中遇到什么问题，请在评论区留言，我都会回复~

仓库链接：

[https://github.com/icebear0828/codex-proxy](https://github.com/icebear0828/codex-proxy)

（记得点小星星） 项目作者：小八 

[@IceBearMiner](https://x.com/@IceBearMiner)

教程就到这里，如果这个教程帮到你了，请点赞 + 关注 + 转发 ！
