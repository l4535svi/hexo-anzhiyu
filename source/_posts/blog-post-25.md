---
title: 创建生图机器人
date: '2026-04-15 12:00:00'
cover: /img/covers/blog-post-25.jpg
tags:
- Hermes Agent
categories:
- Hermes Agent
description: Hermes Agent 新手使用十大技巧 1、安装 Hermes curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash 注意：w
---
Hermes Agent 新手使用十大技巧

# 1、安装 Hermes

```

    curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

```

注意：windows 用户需要在 WSL2 环境中使用

```

    wsl --install

```

更新 hermes

```

    hermes update

```

# 2、配置主模型

```

    hermes  model
    或者直接配置
    hermes config set model.default anthropic/claude-sonnet-4
    

```

  

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=YmQ2ZmVlYTQ1NDY4OTBjYmJiOTU3NGQ0NDJmMjBhMTRfQ2dHNEgxbG9oV0VyZkFOUG9vd3VrNVRMSk5FR1JOdTVfVG9rZW46VzlGZGJ5T3RFb2U5dzV4N2VtZWNIcEpNbjNmXzE3NzYyMTkyMTQ6MTc3NjIyMjgxNF9WNA)

这里建议可以装一个 openrouter, 很多免费模型

https://openrouter.ai/models?q=free

  

注意，因为输入 APIKEY 看不到，容易重复输入两次，可以查看配置文件

```

    ～/.hermes/.env

```

# 3、配置辅助模型

```

    model:
      default: anthropic/claude-sonnet-4
      provider: anthropic

```

```

    auxiliary:
      vision:
        provider: auto
        model: ""
      web_extract:
        provider: auto
        model: ""
      compression:
        provider: auto
        model: ""
      session_search:
        provider: auto
        model: ""
      approval:
        provider: auto
        model: ""
      skills_hub:
        provider: auto
        model: ""
      mcp:
        provider: auto
        model: ""
      flush_memories:
        provider: auto
        model: ""
    

```

## 任务模块

任务| 任务属性| 是否影响“聪明搭档感”| 模型选择| 说明  
---|---|---|---|---  
`vision`  
| 中频脏活  
| 中  
| 有视觉理解能力的模型，如果用的多要求高就用 Genimi -3.1系列， 否则直接使用 OpenRouter免费的 Gemini-2.5 或者 GLM-5.1-turbo| 平时不一定天天用，但一旦要看截图、看页面、看图片，就很关键。影响“看图是否靠谱”，但不是长期搭档感的核心。  
`web_extract`| 高频脏活| 低| 便宜的模型  
| 很典型的脏活累活，主要是网页抓取、提炼、清洗。对成本影响大，但对“它像不像懂你的搭档”影响没那么直接。  
`compression`| 高频脏活| 中  
| 便宜的模型| 非常高频，而且很适合用便宜模型做。它主要影响长对话是否稳定、是否不爆上下文，会影响流畅度，但不是最直观的“聪明感”来源。  
`session_search`| 中高频| 高| 好的模型| 这是最影响“它记不记得我们之前聊过什么”的环节之一。它做得好，用户会明显觉得这个 Agent 有连续性、有长期记忆感。  
`approval`| 高频脏活| 低| 便宜的模型| 本质是低成本安全判断。重要，但更偏系统安全，不太影响用户感受到的“聪明搭档感”。  
`skills_hub`| 低频脏活| 低| 便宜的模型| 偶尔用来搜技能、装技能。不是高频，也不是用户日常最能感知的智能维度。  
`mcp`| 中频关键链路| 高| 便宜的模型| 这个很重要。MCP 调用如果理解得好，Agent 会显得更会用工具、更像熟练搭档。它不完全是脏活，而是“工具理解能力”的关键入口。  
`flush_memories`| 低频关键链路| 中高| 便宜的模型| 不是高频，但它直接影响“值得记住的东西有没有被写下来”。用户未必每次都感知到，但长期看很重要。  
  
## 配置方式

  * 首先得在模型配置里面配好你要用的所有模型
  * 然后通过对话的方式让 hermes 直接修改

```

    请将我的 vision 模型更换 openrouter 的google/gemini-2.5-flash

```

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2VlODAwNjhlYTMyMzhkZDUwZTdiNzcwNzg1YjVhMTZfaW4ySThIQUtqdkl6MUZxUmZpM0hGamRKQ21uR3BMWVJfVG9rZW46U2tKZmJUNFNtb2hmdkR4UjY0VmNxTTM5bnViXzE3NzYyMTkyMTQ6MTc3NjIyMjgxNF9WNA)

# 4、写好 SOUL.md：先定义 Hermes 是谁

## SOUL.md 是什么？

  * Hermes 的性格底色
  * 说话方式
  * 做事风格
  * 价值观和边界

定义好它之后，才有人味

## 怎么定义

  * 直接编辑 SOUL.md, 在 ～/.hermes/SOUL.md

```

    你是谁
    你怎么说话
    你做事偏什么风格
    你遇到问题时优先怎么处理
    所以 SOUL.md 不是“多记一点东西”，而是“先定人格底色”。

```

```

    你是一个偏研究型的 AI 助手。
    
    你的默认工作方式：
    - 先给结论，再展开理由
    - 少说空话，少重复用户的话
    - 优先提炼变量、风险、下一步动作
    - 如果信息不足，先查证，不急着下判断
    - 输出风格简洁，像内部研究备忘录
    

```

  * 让 AI 帮你总结

```

    根据我们的对话记录，重新设置我的“灵魂”

```

# 5、搞懂Hermes记忆机制

文件 / 机制| 作用| 谁来维护| 会不会自动修改| 什么时候被用到  
---|---|---|---|---  
`SOUL.md`| 定义 Hermes 的人格、风格、身份感| 主要是用户手动维护| 一般不会；只有文件不存在时会自动生成默认模板| 每次构建系统提示时读取，作为 agent identity 的一部分  
`USER.md`| 存对用户的长期画像，比如沟通方式、习惯、偏好| 用户 + Hermes| 会，Hermes 会通过 memory tool 写入/更新| 每轮都会注入，帮助 Hermes 更懂用户  
`MEMORY.md`| 存长期稳定事实，比如用户偏好、环境信息、长期约定| 用户 + Hermes  
| 会，Hermes 会通过 memory tool 写入/更新| 每轮都会注入，用来减少重复提醒  
`Skill`| 存可复用的方法、流程、经验总结| 用户 + Hermes| 会，Hermes 会创建、更新、patch skill| 遇到类似任务时可直接复用，不必从零开始  
`state.db` 会话库| 存完整历史对话、工具调用、试错过程| Hermes 自动维护| 会，运行过程中持续写入| 用于 `session_search`、恢复上下文、回忆经历  
  
  

# 6、配置聊天通道

```

    执行 hermes  gateway setup

```

Platform| Voice| Images| Files| Threads| Reactions| Typing| Streaming  
---|---|---|---|---|---|---|---  
Telegram| ✅| ✅| ✅| ✅| —| ✅| ✅  
Discord| ✅| ✅| ✅| ✅| ✅| ✅| ✅  
Slack| ✅| ✅| ✅| ✅| ✅| ✅| ✅  
WhatsApp| —| ✅| ✅| —| —| ✅| ✅  
Signal| —| ✅| ✅| —| —| ✅| ✅  
SMS| —| —| —| —| —| —| —  
Email| —| ✅| ✅| ✅| —| —| —  
Home Assistant| —| —| —| —| —| —| —  
Mattermost| ✅| ✅| ✅| ✅| —| ✅| ✅  
Matrix| ✅| ✅| ✅| ✅| —| ✅| ✅  
DingTalk| —| —| —| —| —| ✅| ✅  
Feishu/Lark| ✅| ✅| ✅| ✅| ✅| ✅| ✅  
WeCom| ✅| ✅| ✅| —| —| ✅| ✅  
Weixin| ✅| ✅| ✅| —| —| ✅| ✅  
BlueBubbles| —| ✅| ✅| —| ✅| ✅| —  
  
  

  

  

  

# 7、执行 hermes doctor 做一个全面检查

```

    hermes doctor

```

输出全绿就说明 Hermes 运行正常，依赖和配置都没问题。如果有报错，它会提示具体是哪里出了问题。

# 8、接入 UI

https://github.com/nesquena/hermes-webui

```

    git clone https://github.com/nesquena/hermes-webui.git hermes-webui
    cd hermes-webui
    ./start.sh

```

# 9、一键迁移OpenClaw

可以，Hermes 内置了迁移命令：

```

    hermes claw migrate

```

# 10、安装技能

跟 OpenClaw 的技能是通用的，都是遵循了技能的标准协议

  * 自己聊天创建
  * # 10、安装技能

跟 OpenClaw 的技能是通用的，都是遵循了技能的标准协议

    * 自己聊天创建
    * 社区搜索

https://hermes-agent.nousresearch.com/docs/skills

https://clawhub.ai/

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=YjcwOTY0YzMxMGE4OTRmODc1ZDQ4M2ExYjU0ZjdlMWFfRG14eUF6Y0t2eTNTU3gxNHgyQW1GTG1nYzRac3NXTEZfVG9rZW46T2NPU2JuWFhLb1dIdFZ4ejA1emM1TlFVblFoXzE3NzYyMTkyMzY6MTc3NjIyMjgzNl9WNA)

社区搜索

https://hermes-agent.nousresearch.com/docs/skills

https://clawhub.ai/
