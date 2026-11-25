---
title: OpenClaw流式输出配置指南
date: '2026-03-06 12:00:00'
cover: https://picsum.photos/seed/openclaw-2/800/450
tags:
- OpenClaw
categories:
- OpenClaw
description: 昨夜 Telegram 创始人宣布了一项重大更新： 流式输出功能（sendMessageDraft）现已向所有聊天机器人开放！ 以前这个功能只有经过认证的 AI 机器人（如 Copilot、Grok）才能用。现在，我们自己搭建的 [OpenClaw] AI 机器人终于也能实现类似
---
昨夜 Telegram 创始人宣布了一项重大更新：流式输出功能（sendMessageDraft）现已向所有聊天机器人开放！ 以前这个功能只有经过认证的 AI 机器人（如 Copilot、Grok）才能用。现在，我们自己搭建的 [OpenClaw] AI 机器人终于也能实现类似“打字机”一样的逐段吐字效果了，再也不用傻等模型把整段话全部生成完才一次性发出来了。

![:light_bulb:](https://emoji.discourse-cdn.com/twitter/light_bulb.png?v=15) 原理说明：

这次是 Telegram API 层面的变动，因为 OpenClaw 本身已经支持该特性，所以不需要升级 OpenClaw 本体，只需要简单修改一下参数就能激活。其核心原理是先发送一个草稿占位符，然后不断编辑修改内容来实现吐字效果。

![:hammer_and_wrench:](https://emoji.discourse-cdn.com/twitter/hammer_and_wrench.png?v=15) 配置指南（两种方法任选）：

方法一：直接向机器人发提示词（推荐）

直接把下面这段话发给你的 OpenClaw 机器人让它自己改：

> 访问此文档页面：`https://docs.openclaw.ai/channels/telegram#live-stream-preview-native-drafts-message-edits` 按文档说明启用流式预览和草稿/推理气泡

 _(注：如果你想看它的“思考过程”，可以直接对机器人发指令  `/reasoning stream` )_

方法二：手动修改配置文件

  1. 打开配置文件 `~/.openclaw/openclaw.json`
  2. 找到 `channels` → `telegram` 节点
  3. 增加或修改以下两个参数：

  * `"streamMode": "partial"`
  * `"blockStreaming": false`

  4. 保存配置并重启 gateway。

![:pushpin:](https://emoji.discourse-cdn.com/twitter/pushpin.png?v=15) 验证是否成功：

正常情况下，你会看到消息是一小块一小块刷新出来的（同一条消息不断被编辑）。注意：受限于 TG 的机制，目前还做不到像网页端那样真正的一个字一个字蹦，而是大约 10 个字左右的“分块更新”，但体验已经比以前好太多了！
