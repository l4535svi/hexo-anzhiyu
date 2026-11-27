---
title: Hermes Agent
date: '2026-04-12 12:00:00'
cover: /img/covers/hermes-agent.jpg
tags:
- Hermes Agent
categories:
- Hermes Agent
description: '电脑win升级命令 pip install --upgrade hermes 卸载命令 ： hermes uninstall 配置对话命令: 2. Hermes接入Telegram 执行： hermes gateway setup 选择： Telegram 填入： BOT TOK'
---
电脑win升级命令

pip install --upgrade hermes

卸载命令  ：hermes uninstall

```

配置对话命令:

### 2\. Hermes接入Telegram

执行：
    hermes gateway setup

```

选择：

  * Telegram 

填入：

```
 
    BOT TOKEN

```

* * *

### 3\. 启动机器人

```
 
    hermes gateway start
    
      
    
    
    后台运行
    
    nohup hermes gateway run > ~/.hermes/logs/gateway.log 2>&1 &

```

### 克隆本仓库

[](https://github.com/byJoey/hermesctl#%E5%85%8B%E9%9A%86%E6%9C%AC%E4%BB%93%E5%BA%93)

```

    git clone https://github.com/byJoey/hermesctl.git
    cd hermesctl
    chmod +x hermesctl.sh
    ./hermesctl.sh

```

### 一行下载运行（与克隆等价，便于随手试）

[](https://github.com/byJoey/hermesctl#%E4%B8%80%E8%A1%8C%E4%B8%8B%E8%BD%BD%E8%BF%90%E8%A1%8C%E4%B8%8E%E5%85%8B%E9%9A%86%E7%AD%89%E4%BB%B7%E4%BE%BF%E4%BA%8E%E9%9A%8F%E6%89%8B%E8%AF%95)

```

    curl -fsSL https://raw.githubusercontent.com/byJoey/hermesctl/main/hermesctl.sh -o hermesctl.sh && chmod +x hermesctl.sh && ./hermesctl.sh

```

### 直接运行（本地已有脚本时）

[](https://github.com/byJoey/hermesctl#%E7%9B%B4%E6%8E%A5%E8%BF%90%E8%A1%8C%E6%9C%AC%E5%9C%B0%E5%B7%B2%E6%9C%89%E8%84%9A%E6%9C%AC%E6%97%B6)

```

    chmod +x hermesctl.sh
    ./hermesctl.sh

```

### 快捷命令 `hc`

[](https://github.com/byJoey/hermesctl#%E5%BF%AB%E6%8D%B7%E5%91%BD%E4%BB%A4-hc)

首次启动脚本会把自身复制到 `~/.local/bin/hermesctl.sh` 并生成 `~/.local/bin/hc`，并在 `~/.zshrc` / `~/.bashrc` 中追加 `PATH`（若尚未包含）。之后：

```

    source ~/.zshrc   # 或 ~/.bashrc
    hc

```

### 帮助

[](https://github.com/byJoey/hermesctl#%E5%B8%AE%E5%8A%A9)

```

    ./hermesctl.sh --help

```

## 1\. 安装 Hermes Agent

运行一行安装程序：

```

    # Linux / macOS / WSL2 / Android (Termux)  
    curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash  
    

```

Android / Termux

如果您要在手机上安装，请参阅专门的[Termux 指南](https://hermes-agent.nousresearch.com/docs/getting-started/termux)，了解经过测试的手动路径、支持的附加功能以及当前 Android 特有的限制。

Windows 用户

请先安装[WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)，然后在 WSL2 终端中运行上述命令。

完成后，重新装填弹药：

```

    source ~/.bashrc   # or source ~/.zshrc  
    

```

## 2\. 设置服务提供商

安装程序会自动配置您的 LLM 提供程序。如需稍后更改，请使用以下命令之一：

```

    hermes model       # Choose your LLM provider and model  
    hermes tools       # Configure which tools are enabled  
    hermes setup       # Or configure everything at once  
    

```

`hermes model`引导您选择推理提供程序：

提供者| 它是什么| 如何设置  
---|---|---  
我们门户| 基于订阅的零配置| 通过 OAuth 登录`hermes model`  
OpenAI Codex| ChatGPT OAuth 使用 Codex 模型| 通过设备代码进行身份验证`hermes model`  
人类学| Claude 直接建模（Pro/Max 或 API 密钥）| `hermes model`使用 Claude Code 身份验证或 Anthropic API 密钥  
OpenRouter| 跨多种模型的多提供商路由| 请输入您的 API 密钥  
Z.AI| GLM / Zhipu 托管模型| 放`GLM_API_KEY`/`ZAI_API_KEY`  
Kimi / Moonshot| Moonshot 托管的编码和聊天模型| 放`KIMI_API_KEY`  
迷你麦克斯| 国际 MiniMax 端点| 放`MINIMAX_API_KEY`  
MiniMax 中国| 中国区 MiniMax 端点| 放`MINIMAX_CN_API_KEY`  
阿里云| Qwen模型通过DashScope| 放`DASHSCOPE_API_KEY`  
拥抱脸| 通过统一路由器支持 20 多种开放式模型（Qwen、DeepSeek、Kimi 等）| 放`HF_TOKEN`  
千克代码| KiloCode托管模型| 放`KILOCODE_API_KEY`  
OpenCode Zen| 按需付费访问精选模型| 放`OPENCODE_ZEN_API_KEY`  
OpenCode Go| 开放模型订阅费每月 10 美元| 放`OPENCODE_GO_API_KEY`  
深潜| 直接访问 DeepSeek API| 放`DEEPSEEK_API_KEY`  
GitHub Copilot| GitHub Copilot 订阅（GPT-5.x、Claude、Gemini 等）| 通过 OAuth`hermes model`或`COPILOT_GITHUB_TOKEN`/`GH_TOKEN`  
GitHub Copilot ACP| Copilot ACP 代理后端（启动本地`copilot`CLI）| `hermes model`（需要`copilot`CLI + `copilot login`）  
Vercel AI 网关| Vercel AI 网关路由| 放`AI_GATEWAY_API_KEY`  
自定义端点| VLLM、SGLang、Ollama 或任何与 OpenAI 兼容的 API| 设置基本 URL + API 密钥  
  
提示

您可以随时切换服务提供商`hermes model`，无需更改代码，也无需担心被锁定。配置自定义端点时，Hermes 会提示您输入上下文窗口大小，并在条件允许的情况下自动检测。详情请参阅[“上下文长度检测” 。](https://hermes-agent.nousresearch.com/docs/integrations/providers#context-length-detection)

## 3\. 开始聊天

```

    hermes  
    

```

搞定！你会看到一个欢迎横幅，上面显示你的模型、可用工具和技能。输入消息并按回车键。

```

    ❯ What can you help me with?  
    

```

该代理程序拥有网络搜索、文件操作、终端命令等工具——所有功能开箱即用。

## 4\. 试用主要功能

### 让它使用终端

```

    ❯ What's my disk usage? Show the top 5 largest directories.  
    

```

代理将代表您运行终端命令并向您显示结果。

### 使用斜杠命令

输入`/`以查看所有命令的自动完成下拉菜单：

命令| 它的作用  
---|---  
`/help`| 显示所有可用命令  
`/tools`| 列出可用工具  
`/model`| 交互式切换模型  
`/personality pirate`| 尝试培养一种有趣的个性  
`/save`| 保存对话  
  
### 多行输入

按`Alt+Enter`或`Ctrl+J`添加新行。非常适合粘贴代码或编写详细提示。

### 打断代理人

如果客服人员处理时间过长，只需输入一条新消息并按回车键——这会中断当前任务并切换到您的新指令。`Ctrl+C`这种方法也有效。

### 恢复会话

退出时，Hermes 会打印一个恢复命令：

```

    hermes --continue    # Resume the most recent session  
    hermes -c            # Short form  
    

```

## 5\. 进一步探索

接下来可以尝试以下几点：

### 设置沙盒终端

为了安全起见，请在 Docker 容器或远程服务器上运行代理：

```

    hermes config set terminal.backend docker    # Docker isolation  
    hermes config set terminal.backend ssh       # Remote server  
    

```

### 连接消息平台

通过 Telegram、Discord、Slack、WhatsApp、Signal、电子邮件或 Home Assistant，从您的手机或其他设备与 Hermes 聊天：

```

    hermes gateway setup    # Interactive platform configuration  
    

```

### 添加语音模式

想在命令行界面 (CLI) 中使用麦克风输入或在消息传递中使用语音回复吗？

```

    pip install "hermes-agent[voice]"  
      
    # Optional but recommended for free local speech-to-text  
    pip install faster-whisper  
    

```

然后启动 Hermes 并在命令行界面中启用它：

```

    /voice on  
    

```

按下此键`Ctrl+B`即可录音，或`/voice tts`让 Hermes 朗读回复。有关在 CLI、Telegram、Discord 和 Discord 语音频道中的完整设置，请参阅[“语音模式” 。](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)

### 安排自动化任务

```

    ❯ Every morning at 9am, check Hacker News for AI news and send me a summary on Telegram.  
    

```

代理将设置一个定时任务，通过网关自动运行。

### 浏览并安装技能

```

    hermes skills search kubernetes  
    hermes skills search react --source skills-sh  
    hermes skills search https://mintlify.com/docs --source well-known  
    hermes skills install openai/skills/k8s  
    hermes skills install official/security/1password  
    hermes skills install skills-sh/vercel-labs/json-render/json-render-react --force  
    

```

尖端：

  * 用于`--source skills-sh`搜索公共`skills.sh`目录。
  * `--source well-known`与文档/网站 URL 一起使用，可发现其中的技能`/.well-known/skills/index.json`。
  * `--force`仅在审核第三方技能后方可使用。它可以覆盖非危险策略限制，但不能覆盖`dangerous`扫描结果。

`/skills`或者在聊天中使用斜杠命令。

### 通过 ACP 在编辑器中使用 Hermes

Hermes 还可以作为 ACP 服务器运行，供 VS Code、Zed 和 JetBrains 等兼容 ACP 的编辑器使用：

```

    pip install -e '.[acp]'  
    hermes acp  
    

```

有关设置详情，请参阅[ACP 编辑器集成。](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)

### 尝试使用 MCP 服务器

通过模型上下文协议连接到外部工具：

```

    # Add to ~/.hermes/config.yaml  
    mcp_servers:  
      github:  
        command: npx  
        args: ["-y", "@modelcontextprotocol/server-github"]  
        env:  
          GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxx"  
    

```

* * *

## 快速参考

命令| 描述  
---|---  
`hermes`| 开始聊天  
`hermes model`| 选择您的法学硕士（LLM）提供商和模式  
`hermes tools`| 配置每个平台启用哪些工具  
`hermes setup`| 完整设置向导（一次性配置所有内容）  
`hermes doctor`| 诊断问题  
`hermes update`| 更新至最新版本  
`hermes gateway`| 启动消息网关  
`hermes --continue`| 继续上个会话
