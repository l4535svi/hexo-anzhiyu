---
title: 飞书多个机器人配置多个\workspaces教程
date: '2026-03-16 12:00:00'
cover: /img/covers/workspaces.jpg
tags:
- OpenClaw
categories:
- OpenClaw
description: 1.问题， 我现在都是这样配置的啊，a机器人对接C:\Users\Administrator.openclaw\workspace-yj，b机器人对接C:\Users\Administrator.openclaw\workspace-sosove，但是我让配置的时候，a配置好，b
---
[![](https://blogger.googleusercontent.com/img/a/AVvXsEiWbLiWPbosBeaSxmdkqRyqTSM6X_KPPWUgyNKm0vaUMAzYucB7pCKvYvw5gHl87ziPncmT_j3XGxHilWpSzSHN2iJwfIBJ1wi-gnGlN4gr0S3aj5_LQA0CobImi1N29eqCqJMF5QPTzWNKaZVsYA7WAwdufOuA00AGTrUTN5E6o72yI1RsTIRje40RtBmU=w652-h384)](https://blogger.googleusercontent.com/img/a/AVvXsEiWbLiWPbosBeaSxmdkqRyqTSM6X_KPPWUgyNKm0vaUMAzYucB7pCKvYvw5gHl87ziPncmT_j3XGxHilWpSzSHN2iJwfIBJ1wi-gnGlN4gr0S3aj5_LQA0CobImi1N29eqCqJMF5QPTzWNKaZVsYA7WAwdufOuA00AGTrUTN5E6o72yI1RsTIRje40RtBmU)

  
1.问题，我现在都是这样配置的啊，a机器人对接C:\Users\Administrator.openclaw\workspace-yj，b机器人对接C:\Users\Administrator.openclaw\workspace-sosove，但是我让配置的时候，a配置好，b都无法工作了，b配置好啊，都无法工作了

解决方案：System: [2026-03-16 14:55:50 GMT+8] Exec completed (vivid-ne, code 1) :: 00): Config warnings:\n- plugins.entries.feishu: plugin feishu: duplicate plugin id detected; later plugin may be overridden (C:\Users\Administrator.openclaw\extensions\feishu\in…

[Mon 2026-03-16 15:02 GMT+8] App ID：cli_a93dc41d20f85cd4  
App Secret:GxTPpI9Sv25uKjeqVK4hFbWp6l7pjp8L这个配置到C:\Users\Administrator.openclaw\workspace-yj这个当中  
App ID:cli_a93dccb534351bdb  
App Secret:erozxkMTRSwEj5PhzPSlSd7eVEFsW1vG这个配置到C:\Users\Administrator.openclaw\workspace-sosove飞书二个机器人，然后测试跑通，让二个机器人能够同时运行

直接发问题让他自己配置，然后都可以实现这个效果了

  

｛App ID：cli_a93dc41d20f85cd4

App Secret:GxTPpI9Sv25uKjeqVK4hFbWp6l7pjp8L这个配置到C:\Users\Administrator\\.openclaw\workspace-yj这个当中

App ID:cli_a93dccb534351bdb

App Secret:erozxkMTRSwEj5PhzPSlSd7eVEFsW1vG这个配置到C:\Users\Administrator\\.openclaw\workspace-sosove飞书二个机器人，然后测试跑通，让二个机器人能够同时运行｝
