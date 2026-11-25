---
title: Hermes Agent 本地部署实战：从安装到 Telegram 控制（含完整踩坑记录
date: '2026-04-12 12:00:00'
tags:
- Hermes Agent
categories:
- Hermes Agent
description: 如果你最近在折腾 AI Agent，大概率已经听说过 OpenClaw。但这几天我实际体验下来，发现一个更有意思的方向—— Hermes Agent 。它不仅是一个 Agent，更像一个 可以持续进化的 AI 个体 。 这篇文章，我不讲概念，直接带你完整走一遍：从安装，到接入 T
---
如果你最近在折腾 AI Agent，大概率已经听说过 OpenClaw。但这几天我实际体验下来，发现一个更有意思的方向——Hermes Agent。它不仅是一个 Agent，更像一个可以持续进化的 AI 个体。

这篇文章，我不讲概念，直接带你完整走一遍：从安装，到接入 Telegram，再到解决一个“几乎所有人都会踩”的坑！

#  一、Hermes Agent 是什么？

Hermes Agent 是由 Nous Research 打造的一个自学习 AI Agent，它的核心特点是：

  * 内置学习循环（会成长）
  * 支持长期记忆
  * 支持多模型切换
  * 可以在云端运行
  * 支持 Telegram / 自动化控制

![](https://www.freedidi.com/wp-content/uploads/2026/04/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE-2026-04-11-211204.webp)

简单说一句：它不是一个工具，而是一个“会成长的 AI”。

# 部署教程：

 

# ![🛠](https://s.w.org/images/core/emoji/17.0.2/svg/1f6e0.svg) 二、安装 Hermes（快速流程）

安装过程本身不复杂，核心步骤如下，但需要区分不同的系统

#### 1、Windows一键安装命令：

Powershell （管理员）

irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex

 

![](https://www.freedidi.com/wp-content/uploads/2026/04/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE-2026-04-11-211528.webp)

#### 2、Mac/Linux/WSL2 一键安装命令：

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

 
[code]
    ![](https://www.freedidi.com/wp-content/uploads/2026/04/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE-2026-04-11-211743.webp)
    
    过程中你会遇到：
[/code]

  * 是否导入 OpenClaw 数据 → 建议 YES
  * 是否 migration → 必须 YES
  * setup 选择 → Quick setup

## 

##  Telegram 接入（关键步骤）

在 setup 过程中，你可以选择：Telegram（强烈推荐）

然后：

  1. 打开 Telegram 搜索 @BotFather
  2. 创建 Bot
  3. 获取 Token
  4. 填入 Hermes

## 

## 安全配置

建议填写：

  * Allowed user ID（只允许自己使用）在TG上搜索： @userinfobot 来获取你Telegram账户的ID

避免别人调用你的 AI。

 

# 三、最大坑：Telegram 没反应？

很多人（包括我）会卡在这里：

Telegram 发消息  
完全没有任何回复

##  常见错误表

> `Telegram: python-telegram-bot not installed  
> No adapter available for telegram`

##  本质原因

不是没安装依赖  
是装错环境

Hermes 使用的是：

自己的虚拟环境（venv）

而不是：

你系统的 Python / conda 四、正确解决方案（关键）

## 第一步：找到 Hermes 环境

cd $env:LOCALAPPDATA\hermes\hermes-agent
[code]
    你会看到：
    
    venv
[/code]

## 第二步：给 Hermes 的 Python 安装依赖

.\venv\Scripts\python.exe -m ensurepip .\venv\Scripts\python.exe -m pip install python-telegram-bot

## 第三步：验证

hermes doctor

看到：
[code]
    ✓ python-telegram-bot
[/code]

## 第四步：启动 gateway
[code]
    hermes gateway
[/code]

### Telegram 无法连接的解决的完整步骤如下：

1、进入安装目录下执行命令：

cd $env:LOCALAPPDATA\hermes\hermes-agent

.\venv\Scripts\python.exe -m pip install python-telegram-bot

2、进入后通过 Python 安装 pip和telegram依赖环境：

.\venv\Scripts\python.exe -m ensurepip

.\venv\Scripts\python.exe -m pip install --upgrade pip

.\venv\Scripts\python.exe -m pip install python-telegram-bot

安装成功后在新的窗口执行命令：

hermes gateway

就可以看到对接成功

 

![](https://www.freedidi.com/wp-content/uploads/2026/04/2026-04-11-15-00-32.00_07_01_15.Still005-scaled.webp)

###  五、测试 Telegram 控制

打开 Telegram，给你的 Bot 发送：
[code]
    hello
    
[/code]

如果正常：

AI 会直接回复  
终端也会有日志

# 

###  六、Hermes vs OpenClaw（关键区别）

对比项| OpenClaw| Hermes  
---|---|---  
UI| Web面板| ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) 无UI  
使用方式| 点网页| 聊天 / 自动运行  
记忆| 弱| 强  
学习能力| 无| 有  
模型切换| 一般| 非常灵活  
  
* * *

一句话总结：OpenClaw 是工具，Hermes 是“会成长的AI”。

# 

###  七、Hermes 的真正优势

很多人会问：“为什么它没有UI？”其实这是设计理念：AI 不应该被困在网页里

Hermes 的核心是：

  * 常驻运行
  * 随时调用
  * 像人一样交互

###  Hermes Agent 给我的感觉是：

不是“更强的工具”  
而是“下一代形态”

它最大的不同是：

  * 会学习
  * 会记忆
  * 可以长期运行
  * 可以远程控制

 

### 你可以继续探索：

  * 多模型切换（OpenRouter）
  * 自动任务（cron）
  * 多Agent协作

如果你正在做 AI 内容创作，这套工具非常值得深入。
