---
title: vps机器人没有反应执行命令
date: '2026-03-15 12:00:00'
tags:
- OpenClaw
categories:
- OpenClaw
description: 第一步：只保留一个 gateway 执行这组： openclaw gateway stop pkill -f openclaw-gateway ps -ef | grep openclaw-gateway | grep -v grep ss -lntp | grep 18789
---
## 第一步：只保留一个 gateway

执行这组：
[code] 
    openclaw gateway stop  
    pkill -f openclaw-gateway  
    ps -ef | grep openclaw-gateway | grep -v grep  
    ss -lntp | grep 18789
[/code]

正常结果应该是：

  * 查不到 `openclaw-gateway`

  * 18789 没监听

如果还在，就再执行一次：
[code] 
    pkill -9 -f openclaw-gateway  
    ss -lntp | grep 18789
[/code]

* * *

## 第二步：只启动一次，并盯日志

然后只执行一次：
[code] 
    openclaw gateway
[/code]
