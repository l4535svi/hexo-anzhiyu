---
title: LuCI App for Tuple ECH Worker
date: '2025-12-18 12:00:00'
cover: https://picsum.photos/seed/luci-app-for-tuple-ech-worker/800/450
tags:
- 节点搭建
categories:
- 节点搭建
description: 'OpenWrt LuCI 图形界面配置应用，用于管理 ECH Workers 代理服务。 🙏 致谢 : 本项目基于 byJoey/ech-wk 开发，感谢原作者的出色工作！ ✨ 功能特性 🔒 ECH 加密 : 支持 Encrypted Client Hello (TLS 1.3)'
---
[![GitHub](https://camo.githubusercontent.com/1cdd7c0336d33d7a36ee806ffa4d282bdd3a6ddd45259dda3626ada33d3ce58e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d4543482d2d576f726b6572732d626c75653f6c6f676f3d676974687562)](https://github.com/byJoey/ech-wk) [![License](https://camo.githubusercontent.com/d602072184585c4cf269ebe4c31c5d2cd20bb28e66669e274374e2cbe0ce1c45/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c2d2d332e302d677265656e2e737667)](https://github.com/SunshineList/luci-app-ech-workers/blob/main/LICENSE) [![OpenWrt](https://camo.githubusercontent.com/baf67b18992e7211410797da6bef4b4481632b1e3f6913ea63f980f805693a96/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f70656e5772742d4c7543492d626c75652e737667)](https://openwrt.org/)

OpenWrt LuCI 图形界面配置应用，用于管理 [ECH Workers](https://github.com/byJoey/ech-wk) 代理服务。

> 🙏 致谢: 本项目基于 [byJoey/ech-wk](https://github.com/byJoey/ech-wk) 开发，感谢原作者的出色工作！

* * *

## ✨ 功能特性

[](https://github.com/SunshineList/luci-app-ech-workers#-%E5%8A%9F%E8%83%BD%E7%89%B9%E6%80%A7)

  * 🔒 ECH 加密: 支持 Encrypted Client Hello (TLS 1.3)，隐藏真实 SNI
  * 🌐 多协议代理: 同时支持 SOCKS5 和 HTTP/HTTPS 代理协议
  * 🇨🇳 智能分流: 全局代理 / 跳过中国大陆 / 直连三种模式
  * 📊 Web 管理: LuCI 图形界面，配置简单直观
  * 🔄 服务管理: 支持启动/停止/重启，实时查看运行状态和日志
  * 🚀 自动重启: 基于 procd 的进程管理，服务崩溃自动恢复

* * *

## 📸 界面截图

[](https://github.com/SunshineList/luci-app-ech-workers#-%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE)

### 配置界面

[](https://github.com/SunshineList/luci-app-ech-workers#%E9%85%8D%E7%BD%AE%E7%95%8C%E9%9D%A2)

[![配置界面](https://github.com/SunshineList/luci-app-ech-workers/raw/main/doc/index.png)](https://github.com/SunshineList/luci-app-ech-workers/blob/main/doc/index.png)

### 日志查看

[](https://github.com/SunshineList/luci-app-ech-workers#%E6%97%A5%E5%BF%97%E6%9F%A5%E7%9C%8B)

[![日志查看](https://github.com/SunshineList/luci-app-ech-workers/raw/main/doc/log.png)](https://github.com/SunshineList/luci-app-ech-workers/blob/main/doc/log.png)

* * *

## 📦 安装方法

[](https://github.com/SunshineList/luci-app-ech-workers#-%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95)

### 下载

[](https://github.com/SunshineList/luci-app-ech-workers#%E4%B8%8B%E8%BD%BD)

从 [Releases](https://github.com/SunshineList/luci-app-ech-workers/releases) 页面下载 `luci-app-ech-workers_x.x.x_all.ipk`

> 💡 提示: 安装 ipk 后会自动检测路由器架构并下载对应的 `ech-workers` 二进制文件，无需手动安装！

### 安装步骤

[](https://github.com/SunshineList/luci-app-ech-workers#%E5%AE%89%E8%A3%85%E6%AD%A5%E9%AA%A4)

  1. 上传到路由器
[code]scp luci-app-ech-workers_*.ipk root@192.168.1.1:/tmp/
[/code]

  2. SSH 登录安装
[code]ssh root@192.168.1.1
         opkg install /tmp/luci-app-ech-workers_*.ipk
[/code]

  3. 访问界面

打开浏览器访问路由器管理页面，导航到 服务 → Tuple ECH Worker

> ⚠️ 注意: 自动下载需要路由器能访问 GitHub。如果下载失败，可手动下载对应架构的二进制文件到 `/usr/bin/ech-workers`

* * *

## ⚙️ 配置说明

[](https://github.com/SunshineList/luci-app-ech-workers#%EF%B8%8F-%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E)

### 基本设置

[](https://github.com/SunshineList/luci-app-ech-workers#%E5%9F%BA%E6%9C%AC%E8%AE%BE%E7%BD%AE)

配置项| 说明| 示例值  
---|---|---  
启用| 开启/关闭服务| ✓  
服务器地址| Workers 服务端地址| `your-worker.workers.dev:443`  
监听地址| 本地代理监听端口| `0.0.0.0:30001`  
身份令牌| 服务端验证密钥| 可选  
  
### 高级设置

[](https://github.com/SunshineList/luci-app-ech-workers#%E9%AB%98%E7%BA%A7%E8%AE%BE%E7%BD%AE)

配置项| 说明| 默认值  
---|---|---  
优选 IP/域名| Cloudflare CDN 优选地址| `cf.090227.xyz`  
DoH 服务器| DNS over HTTPS 服务器| `dns.alidns.com/dns-query`  
ECH 域名| 用于获取 ECH 配置| `cloudflare-ech.com`  
  
### 分流模式

[](https://github.com/SunshineList/luci-app-ech-workers#%E5%88%86%E6%B5%81%E6%A8%A1%E5%BC%8F)

模式| 说明  
---|---  
全局代理| 所有流量通过代理  
跳过中国大陆| 国内 IP 直连，其他走代理（推荐）  
直连模式| 所有流量直连，不使用代理  
  
* * *

## 🔧 客户端配置

[](https://github.com/SunshineList/luci-app-ech-workers#-%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%85%8D%E7%BD%AE)

服务启动后，在需要代理的设备上配置：

协议| 地址| 端口  
---|---|---  
SOCKS5| 路由器 IP| 30001（默认）  
HTTP| 路由器 IP| 30001（默认）  
  
### 示例

[](https://github.com/SunshineList/luci-app-ech-workers#%E7%A4%BA%E4%BE%8B)

  * Windows: 系统设置 → 网络和 Internet → 代理 → 手动设置代理
  * macOS: 系统偏好设置 → 网络 → 高级 → 代理
  * iOS/Android: WiFi 设置 → 配置代理 → 手动
  * 浏览器插件: SwitchyOmega、FoxyProxy 等

* * *

## 🐛 故障排除

[](https://github.com/SunshineList/luci-app-ech-workers#-%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)

### 查看服务状态

[](https://github.com/SunshineList/luci-app-ech-workers#%E6%9F%A5%E7%9C%8B%E6%9C%8D%E5%8A%A1%E7%8A%B6%E6%80%81)
[code]
    /etc/init.d/ech-workers status
[/code]

### 查看运行日志

[](https://github.com/SunshineList/luci-app-ech-workers#%E6%9F%A5%E7%9C%8B%E8%BF%90%E8%A1%8C%E6%97%A5%E5%BF%97)
[code]
    logread -e ech-workers | tail -n 50
[/code]

### 手动测试运行

[](https://github.com/SunshineList/luci-app-ech-workers#%E6%89%8B%E5%8A%A8%E6%B5%8B%E8%AF%95%E8%BF%90%E8%A1%8C)
[code]
    /usr/bin/ech-workers -f your-worker.workers.dev:443 -l 0.0.0.0:30001
[/code]

### 常见问题

[](https://github.com/SunshineList/luci-app-ech-workers#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)

问题| 解决方案  
---|---  
服务无法启动| 检查服务器地址是否正确，确保二进制文件有执行权限  
无法连接代理| 检查防火墙设置，确保监听端口未被占用  
速度慢| 尝试更换优选 IP 或 DoH 服务器  
  
* * *

## 📁 目录结构

[](https://github.com/SunshineList/luci-app-ech-workers#-%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)
[code]
    luci-app-ech-workers/
    ├── Makefile                 # OpenWrt SDK 构建配置
    ├── README.md                # 说明文档
    ├── luasrc/
    │   ├── controller/          # LuCI 控制器
    │   ├── model/cbi/           # CBI 配置模型
    │   └── view/ech-workers/    # 视图模板
    ├── po/                      # 国际化翻译
    └── root/                    # 系统配置文件
        └── etc/
            ├── config/          # UCI 默认配置
            ├── init.d/          # procd 服务脚本
            └── uci-defaults/    # 首次安装脚本
    
[/code]

* * *

## 📄 许可证

[](https://github.com/SunshineList/luci-app-ech-workers#-%E8%AE%B8%E5%8F%AF%E8%AF%81)

本项目采用 [GPL-3.0](https://github.com/SunshineList/luci-app-ech-workers/blob/main/LICENSE) 许可证。

* * *

## 🔗 相关链接

[](https://github.com/SunshineList/luci-app-ech-workers#-%E7%9B%B8%E5%85%B3%E9%93%BE%E6%8E%A5)

  * ECH Workers 核心项目: [byJoey/ech-wk](https://github.com/byJoey/ech-wk)
  * OpenWrt 官网: [openwrt.org](https://openwrt.org/)
  * LuCI 文档: [LuCI Wiki](https://openwrt.org/docs/guide-developer/luci)

* * *

## 🤝 贡献

[](https://github.com/SunshineList/luci-app-ech-workers#-%E8%B4%A1%E7%8C%AE)

欢迎提交 Issue 和 Pull Request！
