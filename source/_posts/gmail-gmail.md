---
title: Gmail 邮箱前缀 修改已经全部放开，但是请谨慎修改 Gmail 邮箱前缀：避免“谷歌授权登录”引发账号丢失
date: '2026-06-25 12:00:00'
cover: https://picsum.photos/seed/gmail-gmail/800/450
tags:
- GPT
categories:
- GPT
description: '- 六月 22, 2026 在使用 ChatGPT Team 账号搭配 Codex 时，频繁的 OAuth 登录往往会打断开发心流。其实，我们可以通过配置个人访问令牌（Personal Access Token）来实现免 OAuth 登录，极大提升使用体验。 本文将为您详细拆解具'
---
- [六月 22, 2026](https://gaojilingjuli.blogspot.com/2026/06/chatgpt-team-oauth-codex.html "permanent link")

  

在使用 ChatGPT Team 账号搭配 Codex 时，频繁的 OAuth 登录往往会打断开发心流。其实，我们可以通过配置个人访问令牌（Personal Access Token）来实现免 OAuth 登录，极大提升使用体验。

本文将为您详细拆解具体的操作步骤，并提供快速生成配置文件的自动化脚本。

* * *

## 🛠️ 操作步骤

### 第一步：开启允许创建个人访问令牌

首先，您需要登录拥有管理员权限的账号（或联系管理员），在工作空间（Workspace）设置中放开权限：

  1. 进入**权限与角色 (Permissions & Roles)** 设置。

  2. 找到**访问令牌 (Access Tokens)** 选项。

  3. 勾选并开启 **“允许用户创建个人访问令牌”** 。

  4. [![](https://blogger.googleusercontent.com/img/a/AVvXsEgPxGTguxAmP5QNkHfL8FzOtN16-L6dWN4TiG30G4dZVs5-dUuhSxlKrXGDwYcOSPwXMchx4KqaBYPYjGJkIusQAIAwhzdNaR2w5zwSzHAL2z5Lbpns2e6QsPfg5dVEFIBX0e9k482U0WPbjz5fbChoxPEp9YfXFTvgBH1F567-6lxKcice-07m0GKnWpQ=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgPxGTguxAmP5QNkHfL8FzOtN16-L6dWN4TiG30G4dZVs5-dUuhSxlKrXGDwYcOSPwXMchx4KqaBYPYjGJkIusQAIAwhzdNaR2w5zwSzHAL2z5Lbpns2e6QsPfg5dVEFIBX0e9k482U0WPbjz5fbChoxPEp9YfXFTvgBH1F567-6lxKcice-07m0GKnWpQ)

  
  

### 第二步：创建个人访问令牌

权限开启后，您可以为自己生成一个专属的 Token：

  1. 在设置中找到访问令牌的生成入口。

  2. 点击新建令牌，为其命名（例如 `default`），并分配合适的有效期（如 30 天）。

  3. 生成后，**请务必复制并妥善保存这串 Token** （它只会出现一次）。

### 第三步：配置 Codex App 或 CLI

获取到 Token 后，您可以通过以下两种方式之一将其配置到 Codex 客户端中：

**方式 A：通过命令行环境变量配置（推荐）**

在终端中执行以下命令：

PowerShell
[code]
    $env:CODEX_ACCESS_TOKEN = "你的_token"
    $env:CODEX_ACCESS_TOKEN | codex login --with-access-token
    
[/code]

**方式 B：通过修改`auth.json` 配置文件**

找到 Codex 的配置文件 `auth.json`，将其修改为如下格式：

JSON
[code]
    {
      "OPENAI_API_KEY": null,
      "personal_access_token": "你的token"
    }
    
[/code]

配置完成后，您就可以顺畅地使用 Codex，无需再进行繁琐的网页授权了。

* * *

## 💡 进阶技巧：在 CPA 中使用及自动导出脚本 

CPA 安装使用教程：https://www.youtube.com/watch?v=sLjTilvm2RQ

  

如果您使用 CPA（如各类 ChatGPT 代理/客户端 API），同样可以通过自定义请求头来使用该 Token。

  1. **配置自定义请求头：**

在 CPA 的相关配置中，添加如下 Headers 即可：

JSON
[code]{
           "authorization": "Bearer 你的token"
         }
         
[/code]

  2. **自动化生成 CPA 格式 JSON 文件：**

为了方便导入配置，您可以登录 ChatGPT 网页版，打开开发者工具（F12），在 Console (控制台) 中粘贴并运行以下 JavaScript 脚本。它会自动获取当前的 Session，并结合您输入的 Codex Token 生成一份适配 CPA 的配置文件并自动下载：

JavaScript
[code]
    (async () => {
        try {
            const inputToken = prompt("请输入你创建的 Codex 令牌（Access Token）：");
            const codexToken = inputToken?.trim().replace(/^Bearer\s+/i, "");
    
            if (!codexToken) {
                console.warn("未输入 Codex 令牌，已取消导出。");
                return;
            }
    
            const response = await fetch("https://chatgpt.com/api/auth/session");
    
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
    
            const data = await response.json();
    
            const now = new Date();
            const tzOffset = -now.getTimezoneOffset();
            const pad = (n) => String(n).padStart(2, "0");
            const sign = tzOffset >= 0 ? "+" : "-";
            const offsetHours = pad(Math.floor(Math.abs(tzOffset) / 60));
            const offsetMinutes = pad(Math.abs(tzOffset) % 60);
            const lastRefresh = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}T${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}${sign}${offsetHours}:${offsetMinutes}`;
    
            const output = {
                access_token: data.accessToken,
                account_id: data.account.id,
                disabled: false,
                email: data.user.email,
                expired: "2030-12-31T10:00:00+08:00",
                headers: {
                    authorization: "Bearer " + codexToken,
                },
                id_token: null,
                last_refresh: lastRefresh,
                refresh_token: null,
                type: "codex",
                websockets: true,
            };
    
            const blob = new Blob([JSON.stringify(output, null, 4)], { type: "application/json" });
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            link.download = data.user.email + ".json";
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        } catch (error) {
            console.error("导出 token 失败:", error);
        }
    })();
    
[/code]

> **📌 温馨提示** ：导出的 Token 和配置文件属于高度敏感的隐私数据，请勿在公开场合泄露，以免造成账号损失或 API 额度被盗刷。

codex 国外手机卡，让你的国内手机无缝支持esim :https://gaojilingjuli.blogspot.com/2026/06/root-hookgiffgaff-esim-apk.html 

* * *

参考：https://linux.do/t/topic/2436679
