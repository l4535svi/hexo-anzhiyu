---
title: 自建汇聚订阅 CF-Workers-SUB
date: '2025-01-18 12:00:00'
cover: https://picsum.photos/seed/cf-workers-sub/800/450
tags:
- 节点分享
categories:
- 节点分享
description: 这是一个将多个节点和订阅合并为单一链接的工具，支持自动适配与自定义分流，简化了订阅管理。 🛠 功能特点 节点链接自动转换成base64订阅链接： 这是最基础的功能，可以将您的节点自动转换为base64格式的订阅链接； 将多个base64订阅汇聚成一个订阅链接： 可以将多个订阅（例
---
[![自建汇聚订阅 CF-Workers-SUB](https://github.com/cmliu/CF-Workers-SUB/raw/main/sub.png)](https://github.com/cmliu/CF-Workers-SUB/blob/main/sub.png)

> 这是一个将多个节点和订阅合并为单一链接的工具，支持自动适配与自定义分流，简化了订阅管理。

## 🛠 功能特点

[](https://github.com/cmliu/CF-Workers-SUB#-%E5%8A%9F%E8%83%BD%E7%89%B9%E7%82%B9)

  1. 节点链接自动转换成base64订阅链接： 这是最基础的功能，可以将您的节点自动转换为base64格式的订阅链接；
  2. 将多个base64订阅汇聚成一个订阅链接： 可以将多个订阅（例如不同的机场）合并成一个订阅，只需使用一个订阅地址即可获取所有节点；
  3. 自动适配不同梯子的格式订阅链接： 依托[订阅转换](https://sub.fxxk.dedyn.io/)服务，自动将订阅转换为不同梯子所需的格式，实现一条订阅适配多种梯子；
  4. 专属代理分流规则： 自定义分流规则，实现个性化的分流模式；
  5. 更多功能等待发掘...

## 🎬 视频教程

[](https://github.com/cmliu/CF-Workers-SUB#-%E8%A7%86%E9%A2%91%E6%95%99%E7%A8%8B)

  * CF-Workers-SUB 视频教程: <https://www.youtube.com/watch?v=w6rRY4FDd58>

## 🤝 社区支持

[](https://github.com/cmliu/CF-Workers-SUB#-%E7%A4%BE%E5%8C%BA%E6%94%AF%E6%8C%81)

  * Telegram 交流群: [@CMLiussss](https://t.me/CMLiussss)
  * 感谢 [Alice Networks](https://alicenetworks.net/) 提供的云服务器维持 [CM订阅转换服务](https://sub.fxxk.dedyn.io/)

## 📦 Pages 部署方法

[](https://github.com/cmliu/CF-Workers-SUB#-pages-%E9%83%A8%E7%BD%B2%E6%96%B9%E6%B3%95)

`「 Pages GitHub 部署文字教程 」`

### 

[](https://github.com/cmliu/CF-Workers-SUB#1-%E9%83%A8%E7%BD%B2-cloudflare-pages)

  *   * ``````

### 

[](https://github.com/cmliu/CF-Workers-SUB#2-%E7%BB%99-pages%E7%BB%91%E5%AE%9A-%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9F%9F)

  * ````
  * ````
  * ``````

### 

[](https://github.com/cmliu/CF-Workers-SUB#3-%E4%BF%AE%E6%94%B9-%E5%BF%AB%E9%80%9F%E8%AE%A2%E9%98%85%E5%85%A5%E5%8F%A3-)

``

  * ````````

### 

[](https://github.com/cmliu/CF-Workers-SUB#4-%E6%B7%BB%E5%8A%A0%E4%BD%A0%E7%9A%84%E8%8A%82%E7%82%B9%E5%92%8C%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5)

  1. ``
  2. ``
[/code]
[code]

## 🛠️ Workers 部署方法

[](https://github.com/cmliu/CF-Workers-SUB#%EF%B8%8F-workers-%E9%83%A8%E7%BD%B2%E6%96%B9%E6%B3%95)

`「 Workers 部署文字教程 」`

### 

[](https://github.com/cmliu/CF-Workers-SUB#1-%E9%83%A8%E7%BD%B2-cloudflare-worker)

  *   * [](https://github.com/cmliu/CF-Workers-SUB/blob/main/_worker.js)

### 

[](https://github.com/cmliu/CF-Workers-SUB#2-%E4%BF%AE%E6%94%B9-%E8%AE%A2%E9%98%85%E5%85%A5%E5%8F%A3-)

``

  * ``
[/code]
[/code]
[code]

### 

[](https://github.com/cmliu/CF-Workers-SUB#3-%E6%B7%BB%E5%8A%A0%E4%BD%A0%E7%9A%84%E8%8A%82%E7%82%B9%E6%88%96%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5)

  1. ``
  2. ``
[/code]
[code]

## 📋 变量说明

[](https://github.com/cmliu/CF-Workers-SUB#-%E5%8F%98%E9%87%8F%E8%AF%B4%E6%98%8E)

变量名| 示例| 备注  
---|---|---  
TOKEN| `auto`| 快速订阅内置节点的订阅路径地址 /auto  
TGTOKEN| `6894123456:XXXXXXXXXX0qExVsBPUhHDAbXXXXXqWXgBA`| 发送TG通知的机器人token  
TGID| `6946912345`| 接收TG通知的账户数字ID  
SUBNAME| `CF-Workers-SUB`| 订阅名称  
SUBAPI| `subapi.fxxk.dedyn.io`| clash、singbox等 订阅转换后端  
SUBCONFIG| [https://raw.github.../ACL4SSR_Online_MultiCountry.ini](https://raw.githubusercontent.com/cmliu/ACL4SSR/main/Clash/config/ACL4SSR_Online_MultiCountry.ini)| clash、singbox等 订阅转换配置文件  
  
## ⚠️ 注意事项

[](https://github.com/cmliu/CF-Workers-SUB#%EF%B8%8F-%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

项目中，TGTOKEN和TGID在使用时需要先到Telegram注册并获取。其中，TGTOKEN是telegram bot的凭证，TGID是用来接收通知的telegram用户或者组的id。
