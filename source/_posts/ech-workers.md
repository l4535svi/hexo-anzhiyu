---
title: ECH Workers 客户端
date: '2025-12-18 12:00:00'
cover: /img/covers/ech-workers.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 跨平台的 ECH Workers 代理客户端，支持 Windows、macOS 和 Linux（ARM/x86），提供图形界面和命令行两种使用方式。 📋 目录 功能特性 版本更新 快速开始 命令行使用 图形界面使用 软路由部署 系统要求 故障排除 技术文档 ✨ 功能特性 核心功能
---
[![GitHub release](https://camo.githubusercontent.com/9dedc5373af413ff0c141e3d7daf6249af9f08d867d2c2e483715e79aa3438b1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f62794a6f65792f6563682d776b2e737667)](https://github.com/byJoey/ech-wk/releases) [![License](https://camo.githubusercontent.com/7013272bd27ece47364536a221edb554cd69683b68a46fc0ee96881174c4214c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)](https://github.com/byJoey/ech-wk/blob/main/LICENSE)

跨平台的 ECH Workers 代理客户端，支持 Windows、macOS 和 Linux（ARM/x86），提供图形界面和命令行两种使用方式。

## 📋 目录

[](https://github.com/byJoey/ech-wk#-%E7%9B%AE%E5%BD%95)

  * [功能特性](https://github.com/byJoey/ech-wk#%E5%8A%9F%E8%83%BD%E7%89%B9%E6%80%A7)
  * [版本更新](https://github.com/byJoey/ech-wk#%E7%89%88%E6%9C%AC%E6%9B%B4%E6%96%B0)
  * [快速开始](https://github.com/byJoey/ech-wk#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)
  * [命令行使用](https://github.com/byJoey/ech-wk#%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%BD%BF%E7%94%A8)
  * [图形界面使用](https://github.com/byJoey/ech-wk#%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E4%BD%BF%E7%94%A8)
  * [软路由部署](https://github.com/byJoey/ech-wk#%E8%BD%AF%E8%B7%AF%E7%94%B1%E9%83%A8%E7%BD%B2)
  * [系统要求](https://github.com/byJoey/ech-wk#%E7%B3%BB%E7%BB%9F%E8%A6%81%E6%B1%82)
  * [故障排除](https://github.com/byJoey/ech-wk#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)
  * [技术文档](https://github.com/byJoey/ech-wk#%E6%8A%80%E6%9C%AF%E6%96%87%E6%A1%A3)

## ✨ 功能特性

[](https://github.com/byJoey/ech-wk#-%E5%8A%9F%E8%83%BD%E7%89%B9%E6%80%A7)

### 核心功能

[](https://github.com/byJoey/ech-wk#%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD)

  * ✅ ECH 加密 \- 基于 TLS 1.3 ECH (Encrypted Client Hello) 技术，加密 SNI 信息
  * ✅ 多协议支持 \- 同时支持 SOCKS5 和 HTTP CONNECT 代理协议
  * ✅ 智能分流 \- 三种分流模式：全局代理、跳过中国大陆、直连模式
  * ✅ IPv4/IPv6 双栈 \- 完整支持 IPv4 和 IPv6 地址的分流判断

### 图形界面功能

[](https://github.com/byJoey/ech-wk#%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E5%8A%9F%E8%83%BD)

  * ✅ 多服务器管理 \- 支持多个服务器配置，快速切换
  * ✅ 一键系统代理 \- 自动设置系统代理，支持分流模式
  * ✅ 系统托盘 \- 最小化到系统托盘，不占用任务栏
  * ✅ 开机自启 \- 支持 Windows 和 macOS 开机自动启动
  * ✅ 高 DPI 支持 \- 完美支持高分辨率显示器
  * ✅ 实时日志 \- 查看代理运行状态和日志
  * ✅ 配置持久化 \- 自动保存配置，下次启动自动加载

### 高级功能

[](https://github.com/byJoey/ech-wk#%E9%AB%98%E7%BA%A7%E5%8A%9F%E8%83%BD)

  * ✅ 自动 IP 列表更新 \- 自动下载并应用完整的中国 IP 列表（IPv4/IPv6）
  * ✅ DNS 优选 \- 支持自定义 DoH 服务器进行 ECH 查询
  * ✅ IP 直连 \- 支持指定服务端 IP，绕过 DNS 解析
  * ✅ 跨平台支持 \- Windows、macOS、Linux（x86_64/ARM64）

## 🆕 版本更新

[](https://github.com/byJoey/ech-wk#-%E7%89%88%E6%9C%AC%E6%9B%B4%E6%96%B0)

### v1.3 最新优化

[](https://github.com/byJoey/ech-wk#v13-%E6%9C%80%E6%96%B0%E4%BC%98%E5%8C%96)

#### 核心功能增强

[](https://github.com/byJoey/ech-wk#%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD%E5%A2%9E%E5%BC%BA)

  * IPv6 完整支持

    * 新增 IPv6 地址分流判断功能
    * 自动下载并加载中国 IPv6 IP 列表（`chn_ip_v6.txt`）
    * 支持 IPv4/IPv6 双栈环境下的智能分流
  * 智能 IP 列表管理

    * 自动检测 IP 列表文件是否存在或为空
    * 文件缺失时自动从 GitHub 下载最新列表
    * 支持 IPv4 和 IPv6 列表的独立管理
    * 列表来源：[mayaxcn/china-ip-list](https://github.com/mayaxcn/china-ip-list)
  * 分流逻辑优化

    * 分流判断逻辑移至 Go 核心程序，性能更优
    * 支持域名解析后的多 IP 地址判断
    * 改进的二分查找算法，提升查询效率

#### 命令行体验改进

[](https://github.com/byJoey/ech-wk#%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%BD%93%E9%AA%8C%E6%94%B9%E8%BF%9B)

  * 默认行为优化

    * 命令行模式下，`-routing` 参数默认值改为 `global`（全局代理）
    * 更符合命令行用户的使用习惯
    * GUI 模式不受影响，仍使用配置的默认值
  * 参数说明完善

    * 更新帮助信息，明确各参数的作用和默认值
    * 添加分流模式的详细说明

#### 兼容性提升

[](https://github.com/byJoey/ech-wk#%E5%85%BC%E5%AE%B9%E6%80%A7%E6%8F%90%E5%8D%87)

  * 向后兼容
    * 保持与旧版本配置文件的兼容性
    * 自动迁移和升级配置格式
    * 平滑升级体验

### 历史版本

[](https://github.com/byJoey/ech-wk#%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC)

#### v1.0

[](https://github.com/byJoey/ech-wk#v10)

  * 初始版本发布
  * 基础代理功能
  * 图形界面支持
  * 系统代理设置

## 🚀 快速开始

[](https://github.com/byJoey/ech-wk#-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

### 方法 1: 使用预编译版本（推荐）

[](https://github.com/byJoey/ech-wk#%E6%96%B9%E6%B3%95-1-%E4%BD%BF%E7%94%A8%E9%A2%84%E7%BC%96%E8%AF%91%E7%89%88%E6%9C%AC%E6%8E%A8%E8%8D%90)

从 [GitHub Releases](https://github.com/byJoey/ech-wk/releases) 下载对应平台的压缩包：

#### 桌面版本（包含 GUI）

[](https://github.com/byJoey/ech-wk#%E6%A1%8C%E9%9D%A2%E7%89%88%E6%9C%AC%E5%8C%85%E5%90%AB-gui)

  * Windows x64: `ECHWorkers-windows-amd64.zip`
  * macOS Intel: `ECHWorkers-darwin-amd64.zip`
  * macOS Apple Silicon: `ECHWorkers-darwin-arm64.zip`
  * Linux x86_64: `ECHWorkers-linux-amd64.tar.gz`
  * Linux ARM64: `ECHWorkers-linux-arm64.tar.gz`

#### 软路由版本（仅命令行）

[](https://github.com/byJoey/ech-wk#%E8%BD%AF%E8%B7%AF%E7%94%B1%E7%89%88%E6%9C%AC%E4%BB%85%E5%91%BD%E4%BB%A4%E8%A1%8C)

  * Linux x86_64: `ECHWorkers-linux-amd64-softrouter.tar.gz`
  * Linux ARM64: `ECHWorkers-linux-arm64-softrouter.tar.gz`

#### Docker版本（仅测试x86）

[](https://github.com/byJoey/ech-wk#docker%E7%89%88%E6%9C%AC%E4%BB%85%E6%B5%8B%E8%AF%95x86)

  * DockerHub仓库：<https://hub.docker.com/r/cirnosalt/ech-workers-docker>

#### 安装步骤

[](https://github.com/byJoey/ech-wk#%E5%AE%89%E8%A3%85%E6%AD%A5%E9%AA%A4)

  1. 解压文件

```
# Windows: 解压到任意目录
         # macOS/Linux: 解压到 /usr/local/bin 或自定义目录
         tar -xzf ECHWorkers-linux-amd64.tar.gz

```

  2. 设置执行权限（Linux/macOS）

```
chmod +x ech-workers
         chmod +x ECHWorkersGUI  # 如果使用 GUI

```

  3. 运行程序

     * Windows: 双击 `ECHWorkersGUI.exe` 启动 GUI，或运行 `ech-workers.exe` 使用命令行
     * macOS/Linux: 运行 `./ECHWorkersGUI` 启动 GUI，或运行 `./ech-workers` 使用命令行

> 注意: 预编译版本已包含所有依赖，无需安装 Python 或任何其他软件。  
> 首次运行"跳过中国大陆"模式时，程序会自动下载 IP 列表文件。

## 💻 命令行使用

[](https://github.com/byJoey/ech-wk#-%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%BD%BF%E7%94%A8)

`ech-workers` 支持纯命令行运行，适合服务器环境、软路由或无图形界面场景。

### 命令语法

[](https://github.com/byJoey/ech-wk#%E5%91%BD%E4%BB%A4%E8%AF%AD%E6%B3%95)

```

    ech-workers [选项]

```

### 参数说明

[](https://github.com/byJoey/ech-wk#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)

#### 必需参数

[](https://github.com/byJoey/ech-wk#%E5%BF%85%E9%9C%80%E5%8F%82%E6%95%B0)

参数| 说明| 示例  
---|---|---  
`-f`| 服务端地址（必需）| `-f your-worker.workers.dev:443`  
  
#### 可选参数

[](https://github.com/byJoey/ech-wk#%E5%8F%AF%E9%80%89%E5%8F%82%E6%95%B0)

参数| 默认值| 说明| 示例  
---|---|---|---  
`-l`| `127.0.0.1:30000`| 本地监听地址| `-l 0.0.0.0:30001`  
`-token`| 空| 身份验证令牌| `-token your-token-here`  
`-ip`| 空| 指定服务端 IP（绕过 DNS）| `-ip 1.2.3.4`  
`-dns`| `dns.alidns.com/dns-query`| ECH 查询 DoH 服务器| `-dns dns.alidns.com/dns-query`  
`-ech`| `cloudflare-ech.com`| ECH 查询域名| `-ech cloudflare-ech.com`  
`-routing`| `global`| 分流模式| `-routing bypass_cn`  
  
#### 分流模式说明

[](https://github.com/byJoey/ech-wk#%E5%88%86%E6%B5%81%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E)

模式| 值| 说明  
---|---|---  
全局代理| `global`| 所有流量都走代理（默认模式）  
跳过中国大陆| `bypass_cn`| 中国 IP 直连，其他走代理  
直连模式| `none`| 所有流量直连，不设置代理  
  
> 注意:
> 
>   * 使用 `bypass_cn` 模式时，程序会自动下载中国 IP 列表（IPv4/IPv6）
>   * 如果 IP 列表文件不存在或为空，程序会自动从 GitHub 下载
>   * IP 列表文件保存在程序目录：`chn_ip.txt`（IPv4）和 `chn_ip_v6.txt`（IPv6）
> 

### 使用示例

[](https://github.com/byJoey/ech-wk#%E4%BD%BF%E7%94%A8%E7%A4%BA%E4%BE%8B)

#### 基本用法

[](https://github.com/byJoey/ech-wk#%E5%9F%BA%E6%9C%AC%E7%94%A8%E6%B3%95)

```

    # Windows
    ech-workers.exe -f your-worker.workers.dev:443
    
    # macOS / Linux
    ./ech-workers -f your-worker.workers.dev:443

```

#### 指定监听地址

[](https://github.com/byJoey/ech-wk#%E6%8C%87%E5%AE%9A%E7%9B%91%E5%90%AC%E5%9C%B0%E5%9D%80)

```

    # 监听所有网络接口（适合软路由）
    ./ech-workers -f your-worker.workers.dev:443 -l 0.0.0.0:30001
    
    # 仅监听本地（默认）
    ./ech-workers -f your-worker.workers.dev:443 -l 127.0.0.1:30001

```

#### 使用分流模式

[](https://github.com/byJoey/ech-wk#%E4%BD%BF%E7%94%A8%E5%88%86%E6%B5%81%E6%A8%A1%E5%BC%8F)

```

    # 全局代理模式（默认）
    ./ech-workers -f your-worker.workers.dev:443 -routing global
    
    # 跳过中国大陆模式（自动下载 IP 列表）
    ./ech-workers -f your-worker.workers.dev:443 -routing bypass_cn
    
    # 直连模式
    ./ech-workers -f your-worker.workers.dev:443 -routing none

```

#### 完整参数示例

[](https://github.com/byJoey/ech-wk#%E5%AE%8C%E6%95%B4%E5%8F%82%E6%95%B0%E7%A4%BA%E4%BE%8B)

```

    ./ech-workers \
      -f your-worker.workers.dev:443 \
      -l 0.0.0.0:30001 \
      -token your-token \
      -ip saas.sin.fan \
      -dns dns.alidns.com/dns-query \
      -ech cloudflare-ech.com \
      -routing bypass_cn

```

#### 查看帮助

[](https://github.com/byJoey/ech-wk#%E6%9F%A5%E7%9C%8B%E5%B8%AE%E5%8A%A9)

```

    ./ech-workers -h
    # 或
    ./ech-workers --help

```

### 后台运行

[](https://github.com/byJoey/ech-wk#%E5%90%8E%E5%8F%B0%E8%BF%90%E8%A1%8C)

#### Linux/macOS

[](https://github.com/byJoey/ech-wk#linuxmacos)

使用 nohup:

```

    nohup ./ech-workers -f your-worker.workers.dev:443 -l 127.0.0.1:30001 > ech-workers.log 2>&1 &

```

使用 screen:

```

    screen -S ech-workers
    ./ech-workers -f your-worker.workers.dev:443 -l 127.0.0.1:30001
    # 按 Ctrl+A 然后 D 分离会话

```

使用 systemd (推荐):

创建服务文件 `/etc/systemd/system/ech-workers.service`:

```

    [Unit]
    Description=ECH Workers Proxy Client
    After=network.target
    
    [Service]
    Type=simple
    User=your-username
    WorkingDirectory=/path/to/ech-workers
    ExecStart=/path/to/ech-workers -f your-worker.workers.dev:443 -l 127.0.0.1:30001 -routing bypass_cn
    Restart=always
    RestartSec=5
    StandardOutput=journal
    StandardError=journal
    
    [Install]
    WantedBy=multi-user.target

```

启用并启动服务:

```

    sudo systemctl daemon-reload
    sudo systemctl enable ech-workers
    sudo systemctl start ech-workers
    sudo systemctl status ech-workers

```

查看日志:

```

    sudo journalctl -u ech-workers -f

```

#### Windows

[](https://github.com/byJoey/ech-wk#windows)

使用 PowerShell:

```

    Start-Process -FilePath "ech-workers.exe" `
      -ArgumentList "-f", "your-worker.workers.dev:443", "-l", "127.0.0.1:30001" `
      -WindowStyle Hidden

```

使用任务计划程序:

  1. 打开"任务计划程序"
  2. 创建基本任务
  3. 设置触发器为"计算机启动时"
  4. 操作选择启动程序：`ech-workers.exe`
  5. 添加参数：`-f your-worker.workers.dev:443 -l 127.0.0.1:30001`

### 配置代理客户端

[](https://github.com/byJoey/ech-wk#%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86%E5%AE%A2%E6%88%B7%E7%AB%AF)

启动代理后，配置应用程序使用 SOCKS5 代理：

  * 代理地址: `127.0.0.1:30001`（或你指定的监听地址）
  * 代理类型: SOCKS5
  * 端口: 30001（或你指定的端口）

#### 浏览器配置

[](https://github.com/byJoey/ech-wk#%E6%B5%8F%E8%A7%88%E5%99%A8%E9%85%8D%E7%BD%AE)

Chrome/Edge:

```

    # Linux/macOS
    google-chrome --proxy-server="socks5://127.0.0.1:30001"
    
    # Windows
    chrome.exe --proxy-server="socks5://127.0.0.1:30001"

```

Firefox:

  * 设置 → 网络设置 → 手动代理配置
  * SOCKS 主机: `127.0.0.1`
  * 端口: `30001`
  * SOCKS v5

#### 环境变量配置

[](https://github.com/byJoey/ech-wk#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE)

Linux/macOS:

```

    export ALL_PROXY=socks5://127.0.0.1:30001
    export HTTP_PROXY=socks5://127.0.0.1:30001
    export HTTPS_PROXY=socks5://127.0.0.1:30001

```

Windows (PowerShell):

```

    $env:ALL_PROXY="socks5://127.0.0.1:30001"
    $env:HTTP_PROXY="socks5://127.0.0.1:30001"
    $env:HTTPS_PROXY="socks5://127.0.0.1:30001"

```

### 日志输出

[](https://github.com/byJoey/ech-wk#%E6%97%A5%E5%BF%97%E8%BE%93%E5%87%BA)

程序会在控制台输出运行日志，包括：

  * 启动信息和 ECH 配置状态
  * 分流模式加载状态
  * IP 列表下载和加载信息
  * 代理连接和错误信息

将输出重定向到文件：

```

    ./ech-workers -f your-worker.workers.dev:443 -l 127.0.0.1:30001 > ech-workers.log 2>&1

```

## 🖥️ 图形界面使用

[](https://github.com/byJoey/ech-wk#%EF%B8%8F-%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E4%BD%BF%E7%94%A8)

### 基本使用

[](https://github.com/byJoey/ech-wk#%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8)

  1. 配置服务器

     * 点击"新增"添加服务器配置
     * 填写服务地址（如：`your-worker.workers.dev:443`）和监听地址（如：`127.0.0.1:30001`）
     * 可选：填写身份令牌、优选IP、DOH服务器、ECH域名等高级选项
     * 点击"保存"保存当前配置
  2. 选择分流模式

     * 全局代理: 所有流量都走代理
     * 跳过中国大陆: 中国网站直连，其他网站走代理（自动下载 IP 列表）
     * 不改变代理: 不设置系统代理，手动配置
  3. 启动代理

     * 点击"启动代理"按钮启动代理服务
     * 查看日志区域了解运行状态
     * 点击"停止"按钮停止代理服务
  4. 设置系统代理

     * 启动代理后，点击"设置系统代理"按钮
     * 系统会自动配置代理设置
     * 停止代理或关闭程序时会自动清理系统代理

### 系统托盘

[](https://github.com/byJoey/ech-wk#%E7%B3%BB%E7%BB%9F%E6%89%98%E7%9B%98)

  * 最小化到托盘: 关闭窗口时程序会最小化到系统托盘，不会退出
  * 显示窗口: 双击托盘图标或右键菜单选择"显示窗口"
  * 退出程序: 右键托盘图标选择"退出"

### 开机自启

[](https://github.com/byJoey/ech-wk#%E5%BC%80%E6%9C%BA%E8%87%AA%E5%90%AF)

勾选"开机启动"复选框，程序会在系统启动时自动运行并启动代理。

## 🛣️ 软路由部署

[](https://github.com/byJoey/ech-wk#%EF%B8%8F-%E8%BD%AF%E8%B7%AF%E7%94%B1%E9%83%A8%E7%BD%B2)

### 图形化推荐

[](https://github.com/byJoey/ech-wk#%E5%9B%BE%E5%BD%A2%E5%8C%96%E6%8E%A8%E8%8D%90)

<https://github.com/SunshineList/luci-app-ech-workers>

### OpenWrt 部署

[](https://github.com/byJoey/ech-wk#openwrt-%E9%83%A8%E7%BD%B2)

### 一键脚本

[](https://github.com/byJoey/ech-wk#%E4%B8%80%E9%94%AE%E8%84%9A%E6%9C%AC)

```

    wget https://raw.githubusercontent.com/byJoey/ech-wk/refs/heads/main/softrouter.sh
    chmod +x softrouter.sh
    ./softrouter.sh

```

```

    #后续使用只需要这一行
    ./softrouter.sh

```

#### 1\. 上传文件

[](https://github.com/byJoey/ech-wk#1-%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)

```

    # 通过 SCP 上传
    scp ech-workers root@192.168.1.1:/usr/bin/
    
    # 或通过 WinSCP、FileZilla 等工具上传

```

#### 2\. 设置执行权限

[](https://github.com/byJoey/ech-wk#2-%E8%AE%BE%E7%BD%AE%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90)

```

    ssh root@192.168.1.1
    chmod +x /usr/bin/ech-workers

```

#### 3\. 创建启动脚本

[](https://github.com/byJoey/ech-wk#3-%E5%88%9B%E5%BB%BA%E5%90%AF%E5%8A%A8%E8%84%9A%E6%9C%AC)

创建 `/etc/init.d/ech-workers`：

```

    #!/bin/sh /etc/rc.common
    
    START=99
    STOP=10
    USE_PROCD=1
    
    start_service() {
        procd_open_instance
        procd_set_param command /usr/bin/ech-workers \
            -f your-worker.workers.dev:443 \
            -l 0.0.0.0:30001 \
            -token your-token \
            -routing bypass_cn
        procd_set_param respawn
        procd_set_param stdout 1
        procd_set_param stderr 1
        procd_close_instance
    }

```

设置权限：

```

    chmod +x /etc/init.d/ech-workers

```

#### 4\. 启用并启动服务

[](https://github.com/byJoey/ech-wk#4-%E5%90%AF%E7%94%A8%E5%B9%B6%E5%90%AF%E5%8A%A8%E6%9C%8D%E5%8A%A1)

```

    /etc/init.d/ech-workers enable
    /etc/init.d/ech-workers start

```

#### 5\. 查看服务状态

[](https://github.com/byJoey/ech-wk#5-%E6%9F%A5%E7%9C%8B%E6%9C%8D%E5%8A%A1%E7%8A%B6%E6%80%81)

```

    /etc/init.d/ech-workers status
    logread | grep ech-workers

```

#### 6\. 配置 OpenWrt 代理

[](https://github.com/byJoey/ech-wk#6-%E9%85%8D%E7%BD%AE-openwrt-%E4%BB%A3%E7%90%86)

在 PassWall、OpenClash 等插件中配置：

  * 代理类型: SOCKS5
  * 服务器: `软路由的IP`
  * 端口: `30001`

### iKuai 软路由部署

[](https://github.com/byJoey/ech-wk#ikuai-%E8%BD%AF%E8%B7%AF%E7%94%B1%E9%83%A8%E7%BD%B2)

#### 1\. 上传文件

[](https://github.com/byJoey/ech-wk#1-%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6-1)

通过 iKuai 的 Web 管理界面或 SSH 上传 `ech-workers` 到 `/bin/` 目录。

#### 2\. 创建启动脚本

[](https://github.com/byJoey/ech-wk#2-%E5%88%9B%E5%BB%BA%E5%90%AF%E5%8A%A8%E8%84%9A%E6%9C%AC)

创建 `/etc/init.d/ech-workers.sh`：

```

    #!/bin/sh
    /bin/ech-workers -f your-worker.workers.dev:443 -l 127.0.0.1:30001 -routing bypass_cn &

```

设置权限：

```

    chmod +x /etc/init.d/ech-workers.sh

```

#### 3\. 添加到开机启动

[](https://github.com/byJoey/ech-wk#3-%E6%B7%BB%E5%8A%A0%E5%88%B0%E5%BC%80%E6%9C%BA%E5%90%AF%E5%8A%A8)

编辑 `/etc/rc.local`，添加：

```

    /etc/init.d/ech-workers.sh

```

### Docker部署

[](https://github.com/byJoey/ech-wk#docker%E9%83%A8%E7%BD%B2)

参数说明：

```

    --network host #网络类型一般推荐直接host 
      -e ARG_F="" #填写你的workers域名和端口 
      -e ARG_ECH="cloudflare-ech.com" #ech查询域名，一般保持默认 
      -e ARG_TOKEN="" #你设置的token
      -e ARG_IP="visa.com" #优选IP或域名
      -e ARG_L="0.0.0.0:30000" #Socks5服务器的IP和端口，0.0.0.0为全局监听
      -e ARG_ROUTING="global" #分流模式，global=全局代理 bypass_cn=绕过大陆
    

```

docker运行命令模板，按照上面的说明填写，然后复制到终端运行：

```

    docker run -d \
      --name cfech \
      --restart always \
      --network host \
      -e ARG_F="" \
      -e ARG_ECH="cloudflare-ech.com" \
      -e ARG_TOKEN="" \
      -e ARG_IP="visa.com" \
      -e ARG_L="0.0.0.0:30000" \
      -e ARG_ROUTING="global" \
      cirnosalt/ech-workers-docker:latest
    

```

### 软路由配置建议

[](https://github.com/byJoey/ech-wk#%E8%BD%AF%E8%B7%AF%E7%94%B1%E9%85%8D%E7%BD%AE%E5%BB%BA%E8%AE%AE)

#### 网络配置

[](https://github.com/byJoey/ech-wk#%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE)

```

    # 监听所有网络接口（推荐）
    ./ech-workers -f your-worker.workers.dev:443 -l 0.0.0.0:30001 -routing bypass_cn
    
    # 或仅监听内网接口
    ./ech-workers -f your-worker.workers.dev:443 -l 192.168.1.1:30001 -routing bypass_cn

```

#### 防火墙规则

[](https://github.com/byJoey/ech-wk#%E9%98%B2%E7%81%AB%E5%A2%99%E8%A7%84%E5%88%99)

确保防火墙允许代理端口：

```

    # OpenWrt
    uci add firewall rule
    uci set firewall.@rule[-1].name='Allow-ECH-Workers'
    uci set firewall.@rule[-1].src='lan'
    uci set firewall.@rule[-1].dest_port='30001'
    uci set firewall.@rule[-1].proto='tcp'
    uci set firewall.@rule[-1].target='ACCEPT'
    uci commit firewall
    /etc/init.d/firewall reload

```

#### 性能优化

[](https://github.com/byJoey/ech-wk#%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96)

  * 使用 `-ip` 参数指定固定 IP，减少 DNS 查询
  * 调整系统资源限制（如文件描述符数量）
  * 考虑使用 `systemd` 或 `procd` 管理进程

#### 监控和日志

[](https://github.com/byJoey/ech-wk#%E7%9B%91%E6%8E%A7%E5%92%8C%E6%97%A5%E5%BF%97)

```

    # 查看进程状态
    ps | grep ech-workers
    
    # 查看日志
    logread | grep ech-workers
    
    # 测试连接
    curl --socks5 127.0.0.1:30001 http://www.google.com

```

## 📋 系统要求

[](https://github.com/byJoey/ech-wk#-%E7%B3%BB%E7%BB%9F%E8%A6%81%E6%B1%82)

### 操作系统

[](https://github.com/byJoey/ech-wk#%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F)

  * Windows: Windows 10+ (Windows 11 完全支持)
  * macOS: macOS 10.13+
  * Linux: Ubuntu 18.04+ / Debian 10+ / CentOS 7+ (支持 x86_64 和 ARM64)

### 运行时要求

[](https://github.com/byJoey/ech-wk#%E8%BF%90%E8%A1%8C%E6%97%B6%E8%A6%81%E6%B1%82)

  * 预编译版本: 无需额外依赖，可直接运行
  * 从源码编译:
    * Python 3.6+ (仅 GUI 需要)
    * Go 1.23+ (仅编译时需要，ECH 功能需要此版本)

### 网络要求

[](https://github.com/byJoey/ech-wk#%E7%BD%91%E7%BB%9C%E8%A6%81%E6%B1%82)

  * 能够访问 GitHub (用于自动下载 IP 列表)
  * 能够访问 Cloudflare Workers 服务

## 🔧 故障排除

[](https://github.com/byJoey/ech-wk#-%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)

### IP 列表下载失败

[](https://github.com/byJoey/ech-wk#ip-%E5%88%97%E8%A1%A8%E4%B8%8B%E8%BD%BD%E5%A4%B1%E8%B4%A5)

问题: 程序无法下载中国 IP 列表

解决方案:

  1. 检查网络连接，确保能够访问 GitHub
  2. 手动下载 IP 列表文件：

```
# IPv4 列表
         curl -L -o chn_ip.txt "https://raw.githubusercontent.com/mayaxcn/china-ip-list/refs/heads/master/chn_ip.txt"
         
         # IPv6 列表
         curl -L -o chn_ip_v6.txt "https://raw.githubusercontent.com/mayaxcn/china-ip-list/refs/heads/master/chn_ip_v6.txt"

```

  3. 将文件放在程序目录下，程序会自动使用

### 找不到 ech-workers

[](https://github.com/byJoey/ech-wk#%E6%89%BE%E4%B8%8D%E5%88%B0-ech-workers)

问题: GUI 提示找不到 `ech-workers` 可执行文件

解决方案:

  1. 确保已编译 Go 程序：

```
go build -o ech-workers ech-workers.go

```

  2. 确保 `ech-workers` 与 GUI 在同一目录
  3. 检查文件执行权限（Linux/macOS）：

```
chmod +x ech-workers

```

### Windows 11 系统代理问题

[](https://github.com/byJoey/ech-wk#windows-11-%E7%B3%BB%E7%BB%9F%E4%BB%A3%E7%90%86%E9%97%AE%E9%A2%98)

问题: Windows 11 系统代理设置失败

解决方案:

  1. 确保以管理员权限运行程序
  2. 检查防火墙设置
  3. 程序会自动使用正确的代理格式（`127.0.0.1:端口`）

### Linux 系统代理设置

[](https://github.com/byJoey/ech-wk#linux-%E7%B3%BB%E7%BB%9F%E4%BB%A3%E7%90%86%E8%AE%BE%E7%BD%AE)

问题: Linux 不支持自动设置系统代理

解决方案:

  * 在系统设置中配置 SOCKS5 代理为 `127.0.0.1:端口`
  * 或使用环境变量：

```
export ALL_PROXY=socks5://127.0.0.1:端口

```

### bad CPU type in executable (macOS)

[](https://github.com/byJoey/ech-wk#bad-cpu-type-in-executable-macos)

问题: 在 macOS 上运行时报错 "bad CPU type"

解决方案:

  * Intel Mac 请下载 `darwin-amd64` 版本
  * Apple Silicon Mac 请下载 `darwin-arm64` 版本

### PyQt5 安装问题

[](https://github.com/byJoey/ech-wk#pyqt5-%E5%AE%89%E8%A3%85%E9%97%AE%E9%A2%98)

问题: GUI 无法启动，提示 PyQt5 未安装

解决方案:

```

    # macOS
    pip3 install --user PyQt5
    
    # Windows
    pip install PyQt5
    
    # Linux (Debian/Ubuntu)
    sudo apt install python3-pyqt5

```

### 软路由重启后服务未启动

[](https://github.com/byJoey/ech-wk#%E8%BD%AF%E8%B7%AF%E7%94%B1%E9%87%8D%E5%90%AF%E5%90%8E%E6%9C%8D%E5%8A%A1%E6%9C%AA%E5%90%AF%E5%8A%A8)

问题: 软路由重启后代理服务未启动

解决方案:

  1. 检查启动脚本权限：

```
chmod +x /etc/init.d/ech-workers

```

  2. 确保服务已启用：

```
/etc/init.d/ech-workers enable

```

  3. 检查系统日志：

```
logread | grep ech-workers

```

## 📚 技术文档

[](https://github.com/byJoey/ech-wk#-%E6%8A%80%E6%9C%AF%E6%96%87%E6%A1%A3)

### ECH (Encrypted Client Hello)

[](https://github.com/byJoey/ech-wk#ech-encrypted-client-hello)

ECH 是 TLS 1.3 的扩展功能，用于加密 TLS 握手中的 SNI（服务器名称指示），提供更强的隐私保护。这是本程序的核心功能，需要 Go 1.23+ 支持。

### 中国 IP 列表

[](https://github.com/byJoey/ech-wk#%E4%B8%AD%E5%9B%BD-ip-%E5%88%97%E8%A1%A8)

程序会自动从 [mayaxcn/china-ip-list](https://github.com/mayaxcn/china-ip-list) 下载完整的中国 IP 列表，用于"跳过中国大陆"分流模式。

  * IPv4 列表: `chn_ip.txt` \- 包含约 8000+ 个 IPv4 地址段
  * IPv6 列表: `chn_ip_v6.txt` \- 包含完整的中国 IPv6 地址段

列表文件保存在程序目录，如果文件不存在或为空，程序会自动下载。

### 分流逻辑

[](https://github.com/byJoey/ech-wk#%E5%88%86%E6%B5%81%E9%80%BB%E8%BE%91)

分流判断在 Go 核心程序中实现，使用高效的二分查找算法：

  1. 域名解析: 如果目标是域名，先解析为 IP 地址
  2. IP 检查: 检查所有解析到的 IP（IPv4/IPv6）
  3. 范围匹配: 使用二分查找在 IP 列表中查找匹配
  4. 决策: 根据分流模式决定是否走代理

### 系统代理设置

[](https://github.com/byJoey/ech-wk#%E7%B3%BB%E7%BB%9F%E4%BB%A3%E7%90%86%E8%AE%BE%E7%BD%AE)

  * Windows: 通过注册表设置系统代理，支持 SOCKS5 代理
  * macOS: 使用 `networksetup` 命令设置所有网络服务的 SOCKS 代理
  * Linux: 暂不支持自动设置，需要手动配置

### 配置文件

[](https://github.com/byJoey/ech-wk#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)

配置文件保存在：

  * Windows: `%APPDATA%\ECHWorkersClient\config.json`
  * macOS: `~/Library/Application Support/ECHWorkersClient/config.json`
  * Linux: `~/.config/ECHWorkersClient/config.json`

## 🤝 致谢

[](https://github.com/byJoey/ech-wk#-%E8%87%B4%E8%B0%A2)

本项目的客户端和 Go 核心程序均基于 [CF_NAT](https://t.me/CF_NAT) 的原始代码开发。

  * 原始项目来源: [CF_NAT - 中转](https://t.me/CF_NAT)
  * Telegram 频道: [@CF_NAT](https://t.me/CF_NAT)
  * 中国 IP 列表: [mayaxcn/china-ip-list](https://github.com/mayaxcn/china-ip-list)

## 📄 许可证

[](https://github.com/byJoey/ech-wk#-%E8%AE%B8%E5%8F%AF%E8%AF%81)

本项目基于 [CF_NAT](https://t.me/CF_NAT) 的原始代码开发。

## 🌟 Star History
