---
title: WireGuard一键脚本
date: '2025-11-22 12:00:00'
cover: /img/covers/wireguard.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 温馨提示 免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！ 配置要求 最低配置：1H-512M 操作系统：Ubuntu 22.04 连接软件：Wireguard协议
---
## 温馨提示

免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！  

## [](https://geto.run/wireguard.html#header-attention)配置要求

最低配置：1H-512M  
操作系统：Ubuntu 22.04  
连接软件：Wireguard协议不支持使用常用的连接软件，需要用专用软件进行连接[点击进入官网下载](https://www.wireguard.com/install/)

## [](https://geto.run/wireguard.html#header-install)安装方式

#### 请复制以下指令到ssh连接软件粘贴执行

```

    bash <(curl -Ls https://raw.geto.run/proxy/node/main/wireguard.sh)
    

```

* * *

## [](https://geto.run/wireguard.html#header-point)功能介绍

> 高性能内核级 VPN：运行在 Linux 内核空间，开销极低，性能优于 OpenVPN、IPSec；  
> 跨平台支持：支持 Windows / Linux / macOS / iOS / Android，全平台原生客户端，无需额外插件；  
> 简洁安全：仅基于现代加密（Noise Protocol Framework），配置简单，不依赖复杂的证书体系；  
> 稳定性强：基于 UDP，性能高且延迟低，适用于长时间稳定运行的 VPN 场景；  
> 支持多用户：可通过简单的公钥/私钥管理实现多用户接入。  
> 缺点：  
> 协议特征明显，不适合强封锁地区（流量识别度较高）；  
> 依赖内核模块，部分虚拟机或低配 VPS 不支持；  
> 更适合作为传统 VPN 使用，而非代理协议。  
> 适用场景：  
> 个人私有 VPN / 内网穿透；  
> 团队/家庭安全访问内网资源；  
> 需要稳定长期连接的科学办公环境；  
> 

## [](https://geto.run/wireguard.html#header-install)如何选择？

协议组合| 抗封锁| 延迟| 稳定性| 部署复杂度| 适用建议  
---|---|---|---|---|---  
Hysteria2 + UDP + TLS + Obfs| ★★★☆☆| ★★★★★| ★★★☆☆| ★★☆☆☆| 流媒体 / 备用  
TUIC + UDP + QUIC + TLS| ★★★★☆| ★★★★★| ★★★★☆| ★★★★★| 游戏 / 多任务场景  
VLESS + Reality + uTLS + Vision| ★★★★★| ★★★☆☆| ★★★★☆| ★☆☆☆☆| 配置简单安全可靠  
WireGuard + UDP + Kernel-VPN| ★★☆☆☆| ★★★★☆| ★★★★★| ★★★☆☆| 游戏股票等低延迟场景
