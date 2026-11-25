---
title: Clawdbot完全本地化部署教程
date: '2026-02-06 12:00:00'
cover: https://picsum.photos/seed/clawdbot/800/450
tags:
- Clawdbot
categories:
- Clawdbot
description: 电脑安装 修复命令:openclaw doctor 修复高级命令:openclaw doctor --fix 启动后报错，然后需要用这个命令运行 命令:openclaw dashboard --no-open 打开管理员 PowerShell。 执行以下命令以允许本地脚本运行：
---
电脑安装

 修复命令:openclaw doctor

修复高级命令:openclaw doctor --fix

启动后报错，然后需要用这个命令运行

命令:openclaw dashboard --no-open

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgPDUlZKIMpzh0v3mb2oVCHTRI3ewTIo2q2a_6z2pspUvZjCAqV4zK6xFufJ4VaqlyHy7cGHua3XEe1xWjs9gH4aGcVbUKZNQTzI0Z3-SE-94uV7MFU6Po4mNrvbJMbxaCukKK4apQHMuk5OJ5tS-OihpVDV5aWlWQtpVnNsWGq_wq50QNsqMGx7mRlpqCf)](https://blogger.googleusercontent.com/img/a/AVvXsEgPDUlZKIMpzh0v3mb2oVCHTRI3ewTIo2q2a_6z2pspUvZjCAqV4zK6xFufJ4VaqlyHy7cGHua3XEe1xWjs9gH4aGcVbUKZNQTzI0Z3-SE-94uV7MFU6Po4mNrvbJMbxaCukKK4apQHMuk5OJ5tS-OihpVDV5aWlWQtpVnNsWGq_wq50QNsqMGx7mRlpqCf)

  

  1. 打开管理员 PowerShell。 
  2. 执行以下命令以允许本地脚本运行： 

[code]
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
[/code]
[/code]

  * `RemoteSigned`：允许本地脚本运行，但从互联网下载的脚本必须有签名。 
  * `-Scope CurrentUser`：只修改当前用户，不影响系统全局策略。 

  3. 确认提示时输入 `Y`。 
  4. 然后再运行： 

[code] 
    openclaw doctor --fix
[/code]
[/code]

# OpenClaw审核弹窗拦截自动化？关闭命令

openclaw config set tools.exec.security full

openclaw config set tools.exec.ask off

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhnkRl2aG_jFPIivRhtTtyL3TKupwSzEvCT4dC4s9cWPNWeZ1UcXesh2eXFyRmAsmFg1ct4-t555eTJwp28VsStuggpTkfA74U5EhnAFnJRXbRjY87taBLgmivNcPA5O_K4po4YND-DHKD1sKq7vJQqcfa5rMZ6_aM9L_XGHQGgc_1-P-aeBIBazUKJfHMQ=w443-h241)](https://blogger.googleusercontent.com/img/a/AVvXsEhnkRl2aG_jFPIivRhtTtyL3TKupwSzEvCT4dC4s9cWPNWeZ1UcXesh2eXFyRmAsmFg1ct4-t555eTJwp28VsStuggpTkfA74U5EhnAFnJRXbRjY87taBLgmivNcPA5O_K4po4YND-DHKD1sKq7vJQqcfa5rMZ6_aM9L_XGHQGgc_1-P-aeBIBazUKJfHMQ)

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjST7vTzQGyj31E8kmHTTSmprrSX4IWBT5Fpzl5zBR1ZYiXxUVUKYHLiJo2402gC6R-WPdgbC-Gnidn4cgZeSkAeL89VcG020LEF8X8hyfUddoyVkJeR4d-JaUc83yXdA8KxSM-54dwynRyUw6_p6k7CfZhEgt39ye-mxbKltwkvBfiQt5o_ebaQV9iyXup=w491-h265)](https://blogger.googleusercontent.com/img/a/AVvXsEjST7vTzQGyj31E8kmHTTSmprrSX4IWBT5Fpzl5zBR1ZYiXxUVUKYHLiJo2402gC6R-WPdgbC-Gnidn4cgZeSkAeL89VcG020LEF8X8hyfUddoyVkJeR4d-JaUc83yXdA8KxSM-54dwynRyUw6_p6k7CfZhEgt39ye-mxbKltwkvBfiQt5o_ebaQV9iyXup)

  
  

  

  

创建agent

理解了多Agent的意义之后，我们来看具体怎么操作。添加一个新的Agent，只需要一条命令:

            openclaw agents add cut

这里的cut 就是你给这个Agent起的ID，可以换成任何你想要的名字，但记住，同一个系统里不能有重复的ID。

运行完之后，OpenClaw会引导你完成几步配置:第一步，添加工作区。它会问你这个Agent的工作目录放在哪，比如我这里填的是:

第一步，添加工作区。它会问你这个Agent的工作目录放在哪，比如我这里填的是:

Add OpenClaw agent

Workspace directory/Users/superhuang/.openclaw/workspace-pod

第二步，复制认证信息。如果你的主账号已经登录过了，这里可以直接复制主账号的认证配置过来修改就好，不需要重新走一遍完整的登录流程。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgAeqDeV55XXR8Eq5rdc_LJhOFEes5KUT0ys_G8M3Wiw8_KrQ5YpePysYhvRQFqpxUo4ui3AmjxHwmd3hHZhU7NBIKLptO4NuDELIZcLkvXOukB2iRS02ffYGa1lu-ne53o-UYzgwW8WtQTEqapRcLIEMTJ5pgomfdCXupP3K0EJ_Cpch1e7Lzg1jYzaCyZ=w579-h260)](https://blogger.googleusercontent.com/img/a/AVvXsEgAeqDeV55XXR8Eq5rdc_LJhOFEes5KUT0ys_G8M3Wiw8_KrQ5YpePysYhvRQFqpxUo4ui3AmjxHwmd3hHZhU7NBIKLptO4NuDELIZcLkvXOukB2iRS02ffYGa1lu-ne53o-UYzgwW8WtQTEqapRcLIEMTJ5pgomfdCXupP3K0EJ_Cpch1e7Lzg1jYzaCyZ)

  

  

  

电脑运行报错是有任务没有处理

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgFB_QUDnq1wXztzPsKHoXUEeFpB-BP9HAUVcl6Le3i3JMAVucnQ5Dzgf0n6v1G6ogBR6_CxelBMeBrxlJUV8yboEKGO6dZdV9GmzIRz7mNVC3xeMuoRCsckvDpp7Cl0HdPAipsnycirLUE8x3rHcv3rL01RMisxkPqVZH8Bc5nYCSqUhpbJjd_ig8rxv9c=w505-h281)](https://blogger.googleusercontent.com/img/a/AVvXsEgFB_QUDnq1wXztzPsKHoXUEeFpB-BP9HAUVcl6Le3i3JMAVucnQ5Dzgf0n6v1G6ogBR6_CxelBMeBrxlJUV8yboEKGO6dZdV9GmzIRz7mNVC3xeMuoRCsckvDpp7Cl0HdPAipsnycirLUE8x3rHcv3rL01RMisxkPqVZH8Bc5nYCSqUhpbJjd_ig8rxv9c)

## 第一步：删除残留任务（最关键）

# 

用管理员 CMD 执行：
[code] 
    schtasks /query | findstr OpenClaw
[/code]

如果能看到类似：
[code] 
    OpenClaw Gateway
[/code]

直接删除：
[code] 
    schtasks /delete /tn "OpenClaw Gateway" /f
[/code]

# 第二步需要根据上面的报错任务发给ai执行直接执行

### 1️⃣ 强制删除任务

在管理员 PowerShell 执行：
[code] 
    schtasks /delete /tn "OpenClaw Gateway" /f
[/code]

如果提示拒绝访问，执行：
[code] 
    whoami /groups
[/code]

确认是否包含：
[code] 
    BUILTIN\Administrators
[/code]

  

  

**安装命令vps**

curl -fsSL https://openclaw.ai/install.sh | bash

  

OpenClaw 配置

。进入TUI:

openclaw tui

。进入配置:

openclaw configure

  

2.电脑安装命令

▼本期视频相关链接▼ 1\. 安装 Git https://git-scm.com/ 2\. 安装 Nodejs https://nodejs.org/ 3\. PowerShell Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 4\. 安装 OpenClaw iwr -useb https://openclaw.ai/install.ps1 | iex 5\. Telegram 配对码 openclaw pairing approve telegram [配对码] 6\. Chrome 游览器插件 openclaw browser extension install C:\Users\geekreal\\.openclaw\browser 7\. OpenClaw启动停止重启 openclaw status # 命令查看状态 openclaw gateway start # 启动 openclaw gateway stop # 停车 openclaw gateway restart # 重启

如何启动命令报错运行这个都可以了

:Start with: openclaw gateway install

管理面板

openclaw configure

  

1.免费使用ollom

安装命令

ollama run qwen3.5:cloud

******启动命令ollama launch openclaw****  
****  
****5.中国版本安装**  
**一件安装命令:**
[code]
     # 自动安装 Node.js 和所有依赖
    curl -fsSL https://clawd.org.cn/install.sh | bash
[/code]

**  
**

# 引导向导(CLI)

引导向导是在macOS、Linux 或Windows（通过WSL2；强烈推荐）上设置OpenClaw 的推荐方式。 它在一个引导流程中配置本地网关或远程网关连接，以及频道、技能和工作区默认设置。

主要入口点：
[code]
    openclaw-cn onboard
[/code]

最快首次聊天：打开控制UI（无需频道设置）。运行`openclaw-cn dashboard`并在浏览器中聊天。文档：[仪表板](https://clawd.org.cn/web/dashboard.html)。

后续重新配置：
[code]
    openclaw-cn configure
[/code]

推荐：设置Brave Search API 密钥，这样代理就可以使用`web_search`（`web_fetch`无需密钥即可工作）。最简单的方法：`openclaw-cn configure --section web`这会存储

  

**  
****  
****  
****  
****  
**
