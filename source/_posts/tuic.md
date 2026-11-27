---
title: TUIC一键脚本
date: '2025-11-22 12:00:00'
cover: /img/covers/tuic.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 温馨提示 免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！ 配置要求 最低配置：1H-512M 操作系统：Ubuntu 22.04 安装方式 请复制以下指令到ssh
---
## 温馨提示

免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！  

## [](https://geto.run/tuic.html#header-attention)配置要求

最低配置：1H-512M  
操作系统：Ubuntu 22.04

## [](https://geto.run/tuic.html#header-install)安装方式

#### 请复制以下指令到ssh连接软件粘贴执行
[code]
    bash <(curl -Ls https://raw.geto.run/proxy/node/main/tuic.sh)
    
[/code]

* * *

## [](https://geto.run/tuic.html#header-point)功能介绍

> 0-RTT 握手：支持零延迟连接建立，显著提升首次连接速度  
> QUIC 传输层：基于 UDP 构建，避免 TCP 的队头阻塞问题，实现多路复用和快速恢复  
> 用户态拥塞控制：支持 BBR、CUBIC 等算法，灵活调节带宽与延迟  
> 原生 UDP 转发：支持 Full Cone NAT，兼容性强，适用于游戏、VoIP 等场景  
> 支持 UDP 分片与重组：可处理超过 MTU 的大包，提升稳定性  
> 适用场景：  
> 长期开通的公网节点；  
> 追求低延迟流媒体服务；  
> 单连接承载多任务，节省资源  
> 

## [](https://geto.run/tuic.html#header-install)如何选择？

协议组合| 抗封锁| 延迟| 稳定性| 部署复杂度| 适用建议  
---|---|---|---|---|---  
Hysteria2 + UDP + TLS + Obfs| ★★★☆☆| ★★★★★| ★★★☆☆| ★★☆☆☆| 流媒体 / 备用  
TUIC + UDP + QUIC + TLS| ★★★★☆| ★★★★★| ★★★★☆| ★★★★★| 游戏 / 多任务场景  
VLESS + Reality + uTLS + Vision| ★★★★★| ★★★☆☆| ★★★★☆| ★☆☆☆☆| 配置简单安全可靠  
WireGuard + UDP + Kernel-VPN| ★★☆☆☆| ★★★★☆| ★★★★★| ★★★☆☆| 游戏股票等低延迟场景  
  
All rights reserved [geto.run](https://geto.run/tuic.html#).
