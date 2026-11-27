---
title: Windows端WSL安装和CPA-Manager-Plus 反代理安装
date: '2026-07-14 12:00:00'
cover: /img/covers/windowswslcpa-manager-plus.jpg
tags:
- GPT
categories:
- GPT
description: 1. 安装标准的Linux 系统 wsl --install -d Ubuntu-26.04 2. 配置代理 export http_proxy = "http://127.0.0.1:10809" export https_proxy = "http://127.0.0.1:1
---
1\. 安装标准的Linux 系统

 wsl --install -d Ubuntu-26.04 

  

2\. 配置代理

export http_proxy="http://127.0.0.1:10809"

export https_proxy="http://127.0.0.1:10809"

  

3\. 安装docker 

3\. 1 下载一键脚本：curl -fsSL https://get.docker.com -o get-docker.sh

3.2 ：执行一键安装 sudo http_proxy="http://127.0.0.1:10809" https_proxy="http://127.0.0.1:10809" sh get-docker.sh

  

4\. docker 代理配置

sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<'EOF'

{

  "proxies": {

    "http-proxy": "http://127.0.0.1:10809",

    "https-proxy": "http://127.0.0.1:10809",

    "no-proxy": "localhost,127.0.0.1"

  }

}

EOF

sudo service docker restart

docker compose up -d

================================================================

docker-compose.yml 文件地址

https://telegram.me/QingLongAndroid/724?comment=103490

  

  

  

**CPA URL** :`http://cli-proxy-api:8317`

  

CPA 安装 ：https://github.com/seakee/CPA-Manager-Plus

  WSL 官方安装指南：https://learn.microsoft.com/zh-cn/windows/wsl/install

WSL 基本命令：https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands

操作场景/阶段| 涉及组件/工具| 核心命令与操作步骤| 配置详情与技巧| 注意事项与常见问题| 功能优势 (推断)| 来源  
---|---|---|---|---|---|---  
系统环境准备| BIOS / 任务管理器 / PowerShell| "dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart"; "dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart"| 确认 BIOS 中已启用虚拟化（Intel VMX 或 AMD SVM）。Windows 10 版本需 1903/2004 (内部版本 19401) 以上或 Windows 11。| 若未开启硬件虚拟化，WSL 2 将无法启动。旧版系统需手动启用虚拟机平台组件。| 确保底层硬件与系统支持 Hyper-V 架构，为 WSL 2 的轻量级虚拟机提供运行基础。| [1][2][3][4][5][6]  
WSL 安装与更新| Windows Terminal / PowerShell| "wsl --install"; "wsl --update"; "wsl --status"| 国内环境建议使用 "wsl --install --web-download" 加速。安装后执行 "--update" 以保持核心功能最新。| 初次安装通常需要重启电脑。WSL 现已通过 Microsoft Store 独立分发，实现解耦更新。| 一行命令完成部署，极大地降低了 Linux 环境搭建门槛，并能快速获得安全补丁和新特性（如 systemd）。| [1][3][4][7][8]  
Linux 发行版部署与管理| Ubuntu, Kali, Debian, Arch| "wsl -l -o" (查看在线列表); "wsl --install -d <Name>"; "wsl -s <Name>" (设置默认)| 首次启动需创建 Linux 用户名和密码。支持多发行版并行且环境彻底隔离。| 卸载实例需使用 "wsl --unregister <Name>"，该操作会抹掉所有数据且不可恢复。| 允许开发者根据项目需求（如安全测试或机器学习）快速切换和共存多个 Linux 环境。| [1][3][5][8]  
自定义路径部署与迁移| wsl --import / --export| "wsl --export <Name> <Path\filename.tar>"; "wsl --import <NewName> <InstallPath> <Source.tar>"| 可通过导出后再导入的方式将实例安装到非系统盘（如 D 盘），以节省 C 盘空间。| 导入后默认用户可能变为 root，需手动配置默认用户。确保操作前实例已关闭。| 避免虚拟磁盘文件 (ext4.vhdx) 撑爆系统盘，同时实现开发环境的“快照级”备份与克隆。| [1][2][5][9]  
AI| | | | | |   
  
| | | | | |   
容器化开发集成| Docker Desktop / Docker Engine| "sudo docker run -p 6379:6379 redis"; 在 Docker Desktop 勾选 "Use the WSL 2 based engine"。| WSL 2 默认支持 systemd。Windows 客户端可直接连接 localhost 访问 WSL 里的容器服务。| 在 WSL 内部执行 Docker 命令通常需要 "sudo"。Docker 在关闭前不会自动完全释放缓存内存。| 具备完整 Linux 内核，使 Docker 性能接近原生 Linux，极大提升了容器化应用和 Agent 部署的兼容性。| [1][2][4][10][8]  
高级 IDE 联动 (VS Code)| VS Code / Remote-WSL 扩展| 在 WSL 目录执行 "code ."; 在资源管理器输入 "\wsl$" 访问文件。| 需在 Windows 端安装 VS Code 及其 WSL 扩展。UI 在 Windows 运行，逻辑和调试在 WSL 服务端运行。| **强烈建议** 将项目文件放在 Linux 原生目录（如 /home/user）而非 /mnt/c，以避免跨系统 IO 开销导致性能下降。| 消除跨平台开发摩擦，在保持 Windows 办公便利的同时，利用 Linux 的工具链进行高性能开发与调试。| [1][2][3][4][10][5][6]  
网络模式调优与代理| .wslconfig| 在 "%USERPROFILE%.wslconfig" 添加 "[wsl2] \n networkingMode=mirrored \n dnsTunneling=true"| 将网络改为“镜像模式”，使 WSL 与宿主机共享 IP，解决局域网访问和代理自动同步问题。| 修改配置后需执行 "wsl --shutdown" 并等待 8 秒重启生效。不再推荐 NAT 模式下的手动查 IP 方案。| 简化网络结构，解决 GitHub/HuggingFace 访问困难，提供更稳定的跨设备访问体验。| [1][2]  
资源限制与管理| .wslconfig| 在 .wslconfig 写入 "memory=8GB \n processors=4"| 根据物理内存合理分配资源，如 16G 内存建议分配 8-12G 给 WSL。使用 "wsl --shutdown" 释放内存。| 默认最高占用 80% 内存，大模型训练任务可能导致整机卡顿。需通过 .wslconfig 进行精细化限制。| 防止 WSL 进程过度消耗宿主机资源导致系统死机，提升多任务并行效率。| [2][11]  
系统维护与故障排除| WSLg / Windows Terminal| "wsl --list --verbose"; "wsl --shutdown"; "wsl hostname -I"| 使用 Windows Terminal 管理多标签页。对于 GUI 错误，参考 WSLg 诊断指南或 GitHub Issue。| WSL 2 仅支持独立 GUI 应用（如 GIMP、浏览器），不支持完整的桌面环境体验。| 拥有成熟的社区支持，支持跨系统剪切粘贴及原生窗口级交互体验。| [10][7][8]  
外部设备与硬件直通| USBIPD-WIN| 使用 "usbipd" 命令连接 USB 设备| WSL 2 不直接支持物理串行端口，需通过 USBIPD-WIN 项目连接外部硬件。| 原生 WSL 2 暂不支持直接访问物理串口，需依赖第三方
