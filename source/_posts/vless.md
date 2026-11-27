---
title: Vless一键脚本
date: '2025-11-22 12:00:00'
cover: /img/covers/vless.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 温馨提示 免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！ 配置要求 最低配置：1H-512M 操作系统：Ubuntu 22.04 安装方式 请复制以下指令到ssh
---
## 温馨提示

免责声明：该项目仅供个人学习、交流，请遵守各个国家（当地）的法律法规，勿用于非法用途，请勿用于生产环境，用户的一切操作，与本站点不承担任何一切法律关系，请文明上网！  

## [](https://geto.run/vless.html#header-attention)配置要求

最低配置：1H-512M  
操作系统：Ubuntu 22.04

## [](https://geto.run/vless.html#header-install)安装方式

#### 请复制以下指令到ssh连接软件粘贴执行

#### 单IP安装命令

```

    bash <(curl -Ls https://raw.geto.run/proxy/node/main/vless.sh)
    

```

#### 多IP安装命令

```

    bash <(curl -Ls https://raw.geto.run/proxy/node/main/vless-plus.sh)
    

```

* * *

## [](https://geto.run/vless.html#header-point)功能介绍

> 抗识别性极强：Reality 模拟浏览器握手，借助 uTLS 和 Vision，将流量伪装为正常 TLS；  
> 无需证书：相比传统 TLS，Reality 不依赖于域名/签发证书，部署更灵活；  
> 低识别风险：支持伪装为真实站点（如 Cloudflare、NVIDIA），对防火墙极度友好；  
> 基于 TCP：流量更稳定，尤其适合城市宽带 / 教育网；  
> 无需中间代理：直接入口部署即可使用。  
> 适用场景：  
> 长期开通的公网节点；  
> 高干扰 / 高频封锁区域；  
> 注重隐蔽性和可信度  
> 

## [](https://geto.run/vless.html#header-install)如何选择？

协议组合| 抗封锁| 延迟| 稳定性| 部署复杂度| 适用建议  
---|---|---|---|---|---  
Hysteria2 + UDP + TLS + Obfs| ★★★☆☆| ★★★★★| ★★★☆☆| ★★☆☆☆| 流媒体 / 备用  
TUIC + UDP + QUIC + TLS| ★★★★☆| ★★★★★| ★★★★☆| ★★★★★| 游戏 / 多任务场景  
VLESS + Reality + uTLS + Vision| ★★★★★| ★★★☆☆| ★★★★☆| ★☆☆☆☆| 配置简单安全可靠  
WireGuard + UDP + Kernel-VPN| ★★☆☆☆| ★★★★☆| ★★★★★| ★★★☆☆| 游戏股票等低延迟场景
