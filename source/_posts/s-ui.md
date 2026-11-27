---
title: S-UI(改版)
date: '2026-08-11 12:00:00'
cover: /img/covers/s-ui.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: '基于 SagerNet/sing-box 的高级 Web 面板 本仓库是 alireza0/s-ui 的二次开发分支,在保留上游全部能力的基础上, 把已在 3x-ui 改版 验证过的体验改进搬了过来: 全自动一键安装、面板更新指向本仓库、协议模板、行内二维码、批量删除、中转与多节'
---
基于 [SagerNet/sing-box](https://github.com/SagerNet/sing-box) 的高级 Web 面板

> 本仓库是 [alireza0/s-ui](https://github.com/alireza0/s-ui) 的二次开发分支,在保留上游全部能力的基础上, 把已在 [3x-ui 改版](https://github.com/Teminuosi/3x-ui) 验证过的体验改进搬了过来: 全自动一键安装、面板更新指向本仓库、协议模板、行内二维码、批量删除、中转与多节点部署(逐步推进)。
> 
> 仅供个人学习与交流,请勿用于非法用途,请勿用于生产环境。上游版权归原作者所有。

[![License](https://camo.githubusercontent.com/81ebbb173edfc6a5992ce99e45ed23c9ca88b1ca7d4845ff425ca843a9ae89ae/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d47504c25323056332d626c75652e7376673f6c6f6e6743616368653d74727565)](https://www.gnu.org/licenses/gpl-3.0.en.html)

> 🌐 官网 / 导航站：[https://3yuedaohang.com](https://3yuedaohang.com/) — 免费节点、搭建教程、订阅工具，一站直达。
> 
> 📺 YouTube 频道：<https://www.youtube.com/@zhanzhang3yue>
> 
> 🖥️ 机器推荐：<https://3yuedaohang.com/cn2/banwagong>

* * *

## 快速开始

[](https://github.com/Teminuosi/s-ui#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

### 全自动安装(推荐)

[](https://github.com/Teminuosi/s-ui#%E5%85%A8%E8%87%AA%E5%8A%A8%E5%AE%89%E8%A3%85%E6%8E%A8%E8%8D%90)

一条命令装好,全程无需交互:全自动会自动生成随机管理员账号密码和随机面板路径,装完直接打印访问信息。

```

    SUI_AUTO=1 bash <(curl -Ls https://raw.githubusercontent.com/Teminuosi/s-ui/main/install.sh)

```

### 交互式安装

[](https://github.com/Teminuosi/s-ui#%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%AE%89%E8%A3%85)

想自己一步步设置端口、路径、账号密码,用普通模式:

```

    bash <(curl -Ls https://raw.githubusercontent.com/Teminuosi/s-ui/main/install.sh)

```

装好后,在服务器上随时输入 `s-ui` 打开管理菜单(启动/停止/重启、改设置、改账号、SSL 证书、BBR 等)。

### Windows

[](https://github.com/Teminuosi/s-ui#windows)

  1. 从 [Releases](https://github.com/Teminuosi/s-ui/releases/latest) 下载最新 Windows 包并解压
  2. 以管理员身份运行 `install-windows.bat`,按向导完成

* * *

## 默认安装信息

[](https://github.com/Teminuosi/s-ui#%E9%BB%98%E8%AE%A4%E5%AE%89%E8%A3%85%E4%BF%A1%E6%81%AF)

项目| 默认值  
---|---  
面板端口| `2095`  
面板路径| `/app/`  
订阅端口| `2096`  
订阅路径| `/sub/`  
账号 / 密码| `admin`  
  
> 全自动安装(`SUI_AUTO=1`)会把账号密码和面板路径换成随机值,请留意安装结束时打印的信息。 升级(已存在数据库)时全自动模式会保留原有设置,不会改动你的账号与路径。

* * *

## 与上游的差异(本分支在做的事)

[](https://github.com/Teminuosi/s-ui#%E4%B8%8E%E4%B8%8A%E6%B8%B8%E7%9A%84%E5%B7%AE%E5%BC%82%E6%9C%AC%E5%88%86%E6%94%AF%E5%9C%A8%E5%81%9A%E7%9A%84%E4%BA%8B)

  * 阶段 0 — Fork 基建:安装/更新脚本全部指向本仓库;CI 按 tag 出 Release 并把版本号写进面板;全自动安装体验。✅
  * 阶段 1 — 一键模板 + 二维码 + 批量删除:常用协议(VLESS+Reality、Hysteria2 等)一键建好;客户端列表行内出二维码;入站/客户端支持多选批量删除。🚧
  * 阶段 2 — 中转:粘贴落地分享链接→自动转 outbound→一步配好路由的"添加中转"向导。🚧
  * 阶段 3 — 多节点部署:以"另一台 S-UI = 一个节点"的方式,中央面板通过 APIv2 令牌远程下发配置、同步流量与心跳。🚧

> 持续跟进上游修复与 sing-box 内核升级,按需回合(不整体合并)。

* * *

## 支持的平台

[](https://github.com/Teminuosi/s-ui#%E6%94%AF%E6%8C%81%E7%9A%84%E5%B9%B3%E5%8F%B0)

平台| 架构| 状态  
---|---|---  
Linux| amd64 / arm64 / armv7 / armv6 / armv5 / 386 / s390x| ✅  
Windows| amd64 / 386 / arm64| ✅  
macOS| amd64 / arm64| 🚧 实验性  
  
## 功能概览

[](https://github.com/Teminuosi/s-ui#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%A7%88)

  * 多协议:Mixed、SOCKS、HTTP、Direct、Redirect、TProxy;VLESS、VMess、Trojan、Shadowsocks;ShadowTLS、Hysteria、Hysteria2、Naive、TUIC(支持 XTLS)
  * 入站 / 出站高级配置;流量路由界面(PROXY Protocol、外部/透明代理、SSL、端口)
  * 客户端流量上限与到期时间;在线客户端、流量统计与系统状态监控
  * 订阅服务(link / json / clash,可加外部订阅);面板与订阅 HTTPS
  * 多语言(英语、波斯语、越南语、简体中文、繁体中文、俄语);明暗主题;API 接口

* * *

## Docker 安装

[](https://github.com/Teminuosi/s-ui#docker-%E5%AE%89%E8%A3%85)

展开

```

    # 安装 Docker
    curl -fsSL https://get.docker.com | sh
    
    # 运行 S-UI(GHCR 镜像)
    mkdir s-ui && cd s-ui
    docker run -itd \
        -p 2095:2095 -p 2096:2096 -p 443:443 -p 80:80 \
        -v $PWD/db/:/app/db/ \
        -v $PWD/cert/:/root/cert/ \
        --name s-ui --restart=unless-stopped \
        ghcr.io/teminuosi/s-ui:latest

```

自行构建镜像:

```

    git clone --recurse-submodules https://github.com/Teminuosi/s-ui
    cd s-ui
    docker build -t s-ui .

```

## 卸载

[](https://github.com/Teminuosi/s-ui#%E5%8D%B8%E8%BD%BD)

```

    sudo -i
    systemctl disable s-ui --now
    rm -f /etc/systemd/system/sing-box.service
    systemctl daemon-reload
    rm -fr /usr/local/s-ui
    rm -f /usr/bin/s-ui

```

* * *

## 本地开发

[](https://github.com/Teminuosi/s-ui#%E6%9C%AC%E5%9C%B0%E5%BC%80%E5%8F%91)

展开

```

    # 克隆(含前端子模块)
    git clone --recurse-submodules https://github.com/Teminuosi/s-ui
    cd s-ui
    
    # 一键构建并运行(前端 + 后端)
    ./runSUI.sh

```

分步构建:

```

    # 前端
    cd frontend && npm install && npm run build && cd ..
    # 后端(需先构建前端)
    rm -fr web/html/* && cp -R frontend/dist/* web/html/
    go build -o sui main.go
    ./sui

```

前端代码在独立子模块仓库:[Teminuosi/s-ui-frontend](https://github.com/Teminuosi/s-ui-frontend)

## 环境变量

[](https://github.com/Teminuosi/s-ui#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)

变量| 取值| 默认  
---|---|---  
SUI_LOG_LEVEL| `debug` / `info` / `warn` / `error`| `info`  
SUI_DEBUG| `true` / `false`| `false`  
SUI_BIN_FOLDER| 字符串| `bin`  
SUI_DB_FOLDER| 字符串| `db`  
SINGBOX_API| 字符串| -
