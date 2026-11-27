---
title: 最新 OpenClaw + Ollama + ChatGPT 本地部署！无需API、永久免费AI、断网也能用（Windows保姆级教程）
date: '2026-03-30 12:00:00'
cover: /img/covers/openclaw-ollama-chatgpt-apiaiwindows.jpg
tags:
- OpenClaw
categories:
- OpenClaw
description: 大家好，我是超哥。今天教你在Windows上，用 OpenClaw + Ollama + ChatGPT 搭建一个完全免费的本地AI，不用API、断网也能用，小白也能一步一步搞定。 一、安装Windows Terminal Windows 终端程序是一款新式、快速、高效、强大且高
---
大家好，我是超哥。今天教你在Windows上，用 OpenClaw + Ollama + ChatGPT 搭建一个完全免费的本地AI，不用API、断网也能用，小白也能一步一步搞定。

![](https://www.xchaoge.com/d/file/efpub/2026/03-25/3e35cb0394489038edc272e3c78b4a0c.png)

### 一、安装Windows Terminal

Windows 终端程序是一款新式、快速、高效、强大且高效的终端应用程序，适用于命令行工具和命令提示符，PowerShell和 WSL 等 Shell 用户。主要功能包括多个选项卡、窗格、Unicode、和 UTF-8 字符支持，GPU 加速文本渲染引擎以及自定义主题、样式和配置。

**下载地址：**[https://apps.microsoft.com/detail/9n0dx20hk701?hl=zh-CN&gl=CN](https://apps.microsoft.com/detail/9n0dx20hk701?hl=zh-CN&gl=CN)

### 二、安装 WSL

![](https://www.xchaoge.com/d/file/efpub/2026/03-26/501e799829015140f9c69fed22c5f348.png)

在 PowerShell(管理员)执行安装WSL命令：

1.

wsl --install

Copy

安装完成后重启电脑，然后安装Ubuntu命令：

1.

wsl --install -d Ubuntu

Copy

打开Windows Terminal，来到ubuntu

### 三、查看显卡驱动状态

查看显卡驱动状态命令：

1.

nvidia-smi

Copy

### 四、更新Ubuntu系统

更新Ubuntu系统命令：

1.

sudo apt update

2.

sudo apt upgrade -y

Copy

### 五、安装环境

#### **1\. 安装 Python**

安装 Python命令：

1.

sudo apt install python3-pip python3-venv -y

Copy

#### **2\. 安装解压缩软件**

安装解压缩软件命令：

1.

sudo apt install -y zstd

Copy

#### **3\. 安装nodejs**

安装 nodejs 命令：

1.

curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -

2.

sudo apt install -y nodejs

Copy

#### **4\. 安装 Git**

安装 Git 命令：

1.

sudo apt update

2.

sudo apt install -y git

Copy

**检查有没有成功：**

1.

node -v

2.

npm -v

3.

git --version

Copy

### 六、安装ollama

![](https://www.xchaoge.com/d/file/efpub/2026/03-26/37bfd39ec8c214436d3f847b8d03e722.png)

**ollama官网：**<https://ollama.com/>

安装 ollama 命令：

1.

curl -fsSL https://ollama.com/install.sh | sh

Copy

### 七、下载安装ollama AI模型

**ollama ChatGPT 模型列表：**<https://ollama.com/library/gpt-oss>

安装ollama AI模型命令：

1.

ollama run gpt-oss:20b

Copy

### 八、安装配置openclaw

![](https://www.xchaoge.com/d/file/efpub/2026/03-26/3368eeee05ec9c5aeb6911286afa4553.jpg)

**openclaw官网：**[https://openclaw.ai](https://openclaw.ai/)

安装配置 openclaw 命令：

1.

curl -fsSL https://openclaw.ai/install.sh | bash

Copy

报错执行命令：

1.

echo 'export PATH="/home/chaoge/.npm-global/bin:$PATH"' >> ~/.bashrc

2.

source ~/.bashrc

Copy

### 九、常用命令：

进入openclaw 命令行聊天：openclaw tui

退出命令行聊天：Ctrl+D

进入openclaw 网页界面聊天：openclaw gateway

重新配置openclaw命令：openclaw onboard

Windows 里 wsl 子系统 ubuntu的文件路径：\\\wsl$\Ubuntu\
