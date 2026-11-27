---
title: S5一键搭建脚本 附无限换IP教程
date: '2025-07-17 12:00:00'
cover: /img/covers/s5-ip.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 这是一键搭建S5教程 将此脚本命名为 s5.sh ，放到服务器上 bash <(curl -sSL http://你的服务器的IP/s5.sh ) S5格式为 IP:5555 无账密 如果说机器更换IP了，此脚本可自动进行更换 配合AWS，用面板进行更换IP，即可获取无限制的S5
---
这是一键搭建S5教程 将此脚本命名为 [s5.sh](https://www.nodeseek.com/jump?to=http%3A%2F%2Fs5.sh)，放到服务器上

bash <(curl -sSL [http://你的服务器的IP/s5.sh](https://www.nodeseek.com/jump?to=http%3A%2F%2Fxn--IP-0p3cl7jf7fo83a16xda%2Fs5.sh))

S5格式为  
IP:5555  
无账密

如果说机器更换IP了，此脚本可自动进行更换

![image](https://kycloud3.koyoo.cn/20250717dea53202507171511026075.png)

配合AWS，用面板进行更换IP，即可获取无限制的S5代理

```

    # 定义SOCKS代理端口
    SOCKS_PORT=5555
    
    # 定义配置文件路径
    CONFIG_FILE="/etc/danted.conf"
    
    # --- 函数定义 ---
    
    # 安装dante-server
    install_dante_server() {
        echo "正在安装 dante-server..."
        if command -v apt-get &> /dev/null; then
            sudo apt-get update
            sudo apt-get install -y dante-server
        elif command -v yum &> /dev/null; then
            sudo yum install -y dante-server
        else
            echo "无法识别您的包管理器，请手动安装 dante-server。"
            exit 1
        fi
        echo "dante-server 安装完成。"
    }
    
    # 配置dante-server
    configure_dante_server() {
        echo "正在配置 dante-server..."
        # 写入danted.conf文件，明确指定外部接口为 ens5
        cat << EOF | sudo tee ${CONFIG_FILE}
    logoutput: stderr
    internal: 0.0.0.0 port=${SOCKS_PORT} # 内部监听地址，监听所有接口的指定端口
    external: ens5 # <-- 已替换为你的实际外部网络接口名称
    socksmethod: none
    clientmethod: none
    
    client pass {
        from: 0.0.0.0/0 to: 0.0.0.0/0
        log: error connect disconnect
    }
    
    socks pass {
        from: 0.0.0.0/0 to: 0.0.0.0/0
        log: error connect disconnect
    }
    EOF
        echo "dante-server 配置完成，配置文件路径：${CONFIG_FILE}"
    }
    
    # 启动或重启dante服务
    start_dante_service() {
        echo "正在启动或重启 dante 服务..."
        # 停止所有旧的danted进程，确保干净启动
        sudo killall danted &> /dev/null
        # 尝试禁用systemd管理的服务，以防冲突
        sudo systemctl stop danted.service &> /dev/null
        sudo systemctl disable danted.service &> /dev/null
    
        # 启动danted服务，使用非daemon模式并在后台运行
        sudo danted -f ${CONFIG_FILE} &
    
        if [ $? -eq 0 ]; then
            echo "SOCKS5 代理已在 ${SOCKS_PORT} 端口启动，无认证。"
        else
            echo "SOCKS5 代理启动失败，请检查日志。"
        fi
    }
    
    # 获取当前公网IP
    get_current_ip() {
        # 尝试多种方式获取公网IP，确保兼容性
        # 使用 timeout 避免卡死
        IP=$(curl -s --max-time 10 ip.sb || curl -s --max-time 10 checkip.amazonaws.com || curl -s --max-time 10 ifconfig.me)
        if [ -z "$IP" ]; then
            echo "无法获取公网IP，请检查网络连接。" >&2
            return 1
        fi
        echo "$IP"
    }
    
    # --- 主逻辑 ---
    
    echo "--- S5 代理自动部署脚本启动 ---"
    
    # 检查dante-server是否已安装，如果没有则安装
    if ! command -v danted &> /dev/null; then
        install_dante_server
    fi
    
    # 配置dante-server
    configure_dante_server
    
    # 首次启动SOCKS代理
    start_dante_service
    
    # 获取初始IP
    OLD_IP=$(get_current_ip)
    if [ $? -ne 0 ]; then
        echo "脚本无法继续，因为无法获取初始IP。"
        exit 1
    fi
    echo "初始公网IP: ${OLD_IP}"
    
    # 进入循环检测IP
    while true; do
        sleep 60 # 每分钟检测一次
        NEW_IP=$(get_current_ip)
    
        if [ $? -ne 0 ]; then
            echo "获取新IP失败，将使用旧IP继续检测。"
            # 即使获取IP失败，也继续下一次循环，不中断服务
        elif [ "$NEW_IP" != "$OLD_IP" ]; then
            echo "IP地址已变化！旧IP: ${OLD_IP}, 新IP: ${NEW_IP}"
            start_dante_service # 重新启动SOCKS代理
            OLD_IP="$NEW_IP"
        else
            echo "IP地址未变化：${OLD_IP}"
        fi
    done
    

```

`  
`
