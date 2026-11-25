---
title: 换帮一个github吧，命令发我一下
date: '2026-10-16 12:00:00'
cover: https://picsum.photos/seed/github/800/450
tags:
- 电脑优化
categories:
- 电脑优化
description: '如果你是想 换绑另一个 GitHub 账号 ，在 PowerShell 执行： # 登录新账号，按提示选择浏览器登录 gh auth login --hostname github.com --web # 让 Git 使用该账号凭据 gh auth setup-git # 查看当'
---
如果你是想**换绑另一个 GitHub 账号** ，在 PowerShell 执行：
[code]
    # 登录新账号，按提示选择浏览器登录
    gh auth login --hostname github.com --web
    
    # 让 Git 使用该账号凭据
    gh auth setup-git
    
    # 查看当前登录账号
    gh auth status
[/code]

如果新账号之前已经登录过，直接切换：
[code]
    gh auth switch --hostname github.com
[/code]

如果你指的是**更换项目绑定的仓库** ，用这个：
[code]
    git remote set-url origin https://github.com/新账号/仓库名.git
    git remote -v
[/code]

星期四21:11
