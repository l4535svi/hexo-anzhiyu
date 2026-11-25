---
title: 🚀 零成本部署使用 GitHub 榜首 AI Agent：OpenClaw (ClawdBot) 保姆级指南
date: '2026-02-04 12:00:00'
cover: https://picsum.photos/seed/github-ai-agentopenclaw-clawdbot/800/450
tags:
- OpenClaw
categories:
- OpenClaw
description: 最近 GitHub Trending 榜首的 OpenClaw (原名 ClawdBot / Mlotbot) 非常火，这里整理了一套目前性价比最高（几近白嫖）的部署方案——利用 GitHub Codespaces 进行云端部署，然后使用QWE免费模型。 💡 为什么要用 GitH
---
最近 GitHub Trending 榜首的 **OpenClaw**  (原名 ClawdBot / Mlotbot) 非常火，这里整理了一套目前性价比最高（几近白嫖）的部署方案——利用 **GitHub Codespaces**  进行云端部署，然后使用QWE免费模型。

#### 💡 为什么要用 GitHub Codespaces？

  * **配置良心** ：直接赠送 2核 8G 内存 + 32G 硬盘的云环境。

  * **完全免费** ：相比购买 VPS，这是零成本体验的最佳选择。

  * **省心** ：环境预设好，无需复杂的运维配置。

* * *

#### 🛠️ 部署核心步骤

**1\. 创建云端环境**

  * https://github.com/codespaces 

  * 等待片刻，你会进入一个类似 VS Code 的网页版编辑器。

**2\. 一键安装 OpenClaw**

在 Codespaces 的下方终端（Terminal）中运行官方安装命令：

Bash
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
    
[/code]

安装速度很快，约两三分钟即可完成。

**3\. 配置模型 (以  ** Qwen Code**  为例)**

  * 推荐使用国产 Qwen Code (每天2000次请求)。

  * 在安装向导中：

    * 模式选择：`Quick Start`

    * 模型选择：`Moonshot AI` ->  Qwen Code

    * 直接谷歌账号一键授权

**4\. 配置交互端 (TG)**

* * *

#### ⚡ 启动与配对 (关键避坑)

**1\. 首次启动**

codespaces 限制无法自启动在终端运行：

Bash
[code]
    openclaw gateway --verbose
    
[/code]

// 后台运行 

nohup openclaw gateway --verbose > /tmp/openclaw-gateway.log 2>&1 &

**2\. 配对认证**

  * 在 私聊 Bot，它会发给你一个 **配对码 (Pairing code)** 。

  * 回到终端，**先停止服务**  (Ctrl+C)，然后运行：

Bash
[code]openclaw pairing approve XXXX
        
[/code]

(按提示输入配对码)

  * 完成后再次启动服务。

**3\. 访问 Web 控制台 & 解决 "1008" 报错**

  * **端口映射** ：Codespaces 会自动转发 `18789` 端口，点击“端口(Ports)”标签页的小地球图标即可访问 Web UI。

  * **解决缺 Token** ：Web 界面提示认证时，输入之前保存的 Gateway Token。

  * **解决 "Pairing required"** ：

    * **方法一 (命令行)** ：新开一个终端，运行 `openclaw devices list` 拿到 Request ID，再运行 `openclaw devices approve <你的ID>`。

    * **方法二 (改配置)** ：修改 `~/.openclaw/devices/pending.json` 文件，将 `"silent": false` 改为 `true`。

* * *

#### ✨ OpenClaw 能做什么？

部署完成后，你拥有了一个 7x24 小时在线的 AI 员工：

  * **全自动编程** ：在 TG 下达需求，它能写代码甚至通过 GitHub Pages 自动部署上线。

  * **文档撰写** ：自动生成并推送 Readme 文档，还能自己优化图片。

  * **信息整理** ：搜集 GitHub 热门项目、整理日报等。

**总结** ：这是目前体验 OpenClaw 最经济、最极客的方式，既然是 Agent 时代，不妨给自己配一个免费的 AI 管家试试！
