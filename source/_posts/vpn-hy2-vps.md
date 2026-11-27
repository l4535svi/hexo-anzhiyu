---
title: 搭建vpn节点 高速hy2 无需域名 用搬瓦工vps实操演示
date: '2025-04-02 12:00:00'
cover: /img/covers/vpn-hy2-vps.jpg
tags:
- VPS
categories:
- VPS
description: '本教程用到的所有软件和工具 手机 扫码 电脑 链接 https://pan.quark.cn/s/df9d5063d07b 解压密码 afeinet 因为太忙 百度盘 周日再传 登录搬瓦工 网址: https://bit.ly/4hg0eii 搬瓦工vps性价比套餐及购买 htt'
---
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEWC0b_w6NGC1oZn8HRDh_pBWoYxVKSZQjz2gX4-TNrN5l0FWsa8wobo5C-JAmz1GUnI6R7vmBNv_rJZM4fwWFseMuwMfHEndq_VpsNND_s1BWHBy2KUztd_taP0cxRLR5Rc0PjVzjJnYkLun6ettiWezQY9xqECnp6SYlrw80F3lF0Y4GAc7EW77TbKT9/s320/bar.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEWC0b_w6NGC1oZn8HRDh_pBWoYxVKSZQjz2gX4-TNrN5l0FWsa8wobo5C-JAmz1GUnI6R7vmBNv_rJZM4fwWFseMuwMfHEndq_VpsNND_s1BWHBy2KUztd_taP0cxRLR5Rc0PjVzjJnYkLun6ettiWezQY9xqECnp6SYlrw80F3lF0Y4GAc7EW77TbKT9/s1904/bar.jpg)

  

   本教程用到的所有软件和工具  
   手机 扫码

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1y_dFAiS6DGIui6yZf19vZjjQ4wjpCKmowtsYMxbV0mPuH9ioZjvFdV8RtbG75lnDVjE2c6xazMVyH3x4ZYhzAg4W_oWxkvRb9EuBkBw4iH6ySNxoCQRnPepiNlYdXc7nhvZJ3MhHVOgJNAKT9rTSufbAuBphP2hkX7nSQPq_LIM-kAve2URZ11zjjhhyphenhyphen/s1600/Pasted%20image%2020241224223221.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1y_dFAiS6DGIui6yZf19vZjjQ4wjpCKmowtsYMxbV0mPuH9ioZjvFdV8RtbG75lnDVjE2c6xazMVyH3x4ZYhzAg4W_oWxkvRb9EuBkBw4iH6ySNxoCQRnPepiNlYdXc7nhvZJ3MhHVOgJNAKT9rTSufbAuBphP2hkX7nSQPq_LIM-kAve2URZ11zjjhhyphenhyphen/s120/Pasted%20image%2020241224223221.png)

   电脑 链接  
   <https://pan.quark.cn/s/df9d5063d07b>  
   解压密码 afeinet  
   因为太忙 百度盘 周日再传

  

## 登录搬瓦工

网址: <https://bit.ly/4hg0eii>

搬瓦工vps性价比套餐及购买  
<https://afeinet.blogspot.com/2024/12/21.html>

## 检测是否被墙

打开命令行 快捷键 Win+R, 输入 cmd 敲回车
[code]
    ping 你vps的ip地址
    
[/code]

## 检测响应速度

htpps://itdog.cn

## 安装系统

Ubuntu 22.04 或 Ubuntu 24.0

## 升级apt
[code]
    apt update
    
[/code]

## 安装防火墙
[code]
    apt install ufw -y
    
[/code]

## 开启端口

开启 80 443 22 端口(追求安全)
[code]
    sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
[/code]

或者 开启所有端口(省事 推荐)
[code]
    ufw disable
    
[/code]

## 核心脚本
[code]
    #一键安装Hysteria2
    bash <(curl -fsSL https://get.hy2.sh/)
    
    #生成自签证书
    openssl req -x509 -nodes -newkey ec:<(openssl ecparam -name prime256v1) -keyout /etc/hysteria/server.key -out /etc/hysteria/server.crt -subj "/CN=bing.com" -days 36500 && sudo chown hysteria /etc/hysteria/server.key && sudo chown hysteria /etc/hysteria/server.crt
    
    #启用Hysteria2 设置开机自启
    systemctl enable hysteria-server.service
    
[/code]

## VPS配置文件
[code]
    cat << EOF > /etc/hysteria/config.yaml
    listen: :443 #监听端口
    
    #使用自签证书
    tls:
      cert: /etc/hysteria/server.crt
      key: /etc/hysteria/server.key
    
    auth:
      type: password
      password: 123456 #设置认证密码
      
    masquerade:
      type: proxy
      proxy:
        url: https://bing.com #伪装网址
        rewriteHost: true
    EOF
    
[/code]

## 重启Hysteria2
[code]
    systemctl restart hysteria-server.service
    
[/code]

## 查看Hysteria2状态
[code]
    systemctl status hysteria-server.service
    
[/code]

查看后, 在英文输入法下 按字母 Q 退出  
同时看到以下两个结果代表成功  
active (running)  
server up and running {"listen": ":443"}

## 准备v2rayN (Windows)

v2rayN 下载：<https://github.com/2dust/v2rayN/releases>  
Hysteria 2下载：<https://github.com/apernet/hysteria/releases>  
v2rayN阿飞版：<https://pan.quark.cn/s/df9d5063d07b>

## 客户端配置文件
[code]
    server: 104.160.22.22:443
    auth: 123456
    
    bandwidth:
      up: 40 mbps
      down: 100 mbps
      
    tls:
      sni: bing.com
      insecure: true 
    
    socks5:
      listen: 127.0.0.1:1080
    http:
      listen: 127.0.0.1:8080
    
[/code]

## sing-box配置文件(Android/IOS)

美区apple id登录后, app store, 搜 sing-box
[code]
    {
      "dns": {
        "servers": [
          {
            "tag": "cf",
            "address": "https://1.1.1.1/dns-query"
          },
          {
            "tag": "local",
            "address": "223.5.5.5",
            "detour": "direct"
          },
          {
            "tag": "block",
            "address": "rcode://success"
          }
        ],
        "rules": [
          {
            "geosite": "category-ads-all",
            "server": "block",
            "disable_cache": true
          },
          {
            "outbound": "any",
            "server": "local"
          },
          {
            "geosite": "cn",
            "server": "local"
          }
        ],
        "strategy": "ipv4_only"
      },
      "inbounds": [
        {
          "type": "tun",
          "inet4_address": "172.19.0.1/30",
          "auto_route": true,
          "strict_route": false,
          "sniff": true
        }
      ],
      "outbounds": [
        {
          "type": "hysteria2",
          "tag": "proxy",
          "server": "你的IP",
          "server_port": 443,
          "up_mbps": 20,
          "down_mbps": 100,
          "password": "123456",
          "tls": {
            "enabled": true,
            "server_name": "bing.com",
            "insecure": true
          }
        },
        {
          "type": "direct",
          "tag": "direct"
        },
        {
          "type": "block",
          "tag": "block"
        },
        {
          "type": "dns",
          "tag": "dns-out"
        }
      ],
      "route": {
        "rules": [
          {
            "protocol": "dns",
            "outbound": "dns-out"
          },
          {
            "geosite": "cn",
            "geoip": [
              "private",
              "cn"
            ],
            "outbound": "direct"
          },
          {
            "geosite": "category-ads-all",
            "outbound": "block"
          }
        ],
        "auto_detect_interface": true
      }
    }
[/code]
