---
title: Hysteria2一键脚本
date: '2025-11-22 12:00:00'
cover: /img/covers/hysteria2.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 温馨提示 免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！ 配置要求 最低配置：1H-512M 操作系统：Ubuntu 22.04 安装方式 请复制以下指令到ssh
---
## 温馨提示

免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！  

## [](https://geto.run/hysteria2.html#header-attention)配置要求

最低配置：1H-512M  
操作系统：Ubuntu 22.04

## [](https://geto.run/hysteria2.html#header-install)安装方式

#### 请复制以下指令到ssh连接软件粘贴执行

```

    bash <(curl -Ls https://raw.geto.run/proxy/node/main/hysteria2.sh)
    

```

* * *

## [](https://geto.run/hysteria2.html#header-point)功能介绍

> 极速连接与低延迟：基于 QUIC over UDP，初次连接快（支持 0-RTT）；  
> 天然抗丢包：自动适应丢包重传，非常适合波动大的移动网络；  
> Obfs 模式内置：内建 Salty / Salamander 混淆插件，绕过 DPI 检测；  
> 密码认证 + TLS 模拟：能有效避免端口扫描和握手特征识别。  
> 缺点：  
> 纯 UDP 架构受部分运营商影响（如 NAT 设备封锁）；  
> 部分地区存在对 UDP 流量限速策略（如校园网）；  
> v2rayN 等传统客户端支持较弱（需 plugin）；  
> 适用场景：  
> 海外 VPS 接入移动端；  
> 追求低延迟流媒体服务；  
> 与服务器之间稳定性可控时非常高效；  
> 

## [](https://geto.run/hysteria2.html#header-install)如何选择？

协议组合| 抗封锁| 延迟| 稳定性| 部署复杂度| 适用建议  
---|---|---|---|---|---  
Hysteria2 + UDP + TLS + Obfs| ★★★☆☆| ★★★★★| ★★★☆☆| ★★☆☆☆| 流媒体 / 备用  
TUIC + UDP + QUIC + TLS| ★★★★☆| ★★★★★| ★★★★☆| ★★★★★| 游戏 / 多任务场景  
VLESS + Reality + uTLS + Vision| ★★★★★| ★★★☆☆| ★★★★☆| ★☆☆☆☆| 配置简单安全可靠  
WireGuard + UDP + Kernel-VPN| ★★☆☆☆| ★★★★☆| ★★★★★| ★★★☆☆| 游戏股票等低延迟场景
