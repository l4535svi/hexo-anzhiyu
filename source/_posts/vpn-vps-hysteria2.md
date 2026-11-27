---
title: 搬瓦工翻墙 搭建高速vpn教程 搭建节点 无需域名 只要vps 从零开始 保姆级教程 hysteria2
date: '2025-04-02 12:00:00'
cover: /img/covers/vpn-vps-hysteria2.jpg
tags:
- 节点分享
categories:
- 节点分享
description: 本教程介绍如何在vps上搭建个人专属的高速vpn, 晚高峰也很快, 全过程实操演示, 不需要域名, 只要有1台vps就行. 本视频演示用的是搬瓦工的vps(限量款29刀/年, 特惠款46刀/年), 如果你用的是其他品牌或者免费的vps, 可以跳转到第2节, 直接观看搭建vpn的演
---
本教程介绍如何在vps上搭建个人专属的高速vpn, 晚高峰也很快, 全过程实操演示, 不需要域名, 只要有1台vps就行. 本视频演示用的是搬瓦工的vps(限量款29刀/年, 特惠款46刀/年), 如果你用的是其他品牌或者免费的vps, 可以跳转到第2节, 直接观看搭建vpn的演示教程.

  

  

[code]
    章节：
    00:00 开场白
    00:42 本视频使用的资源下载
    03:34 搬瓦工的注册及选择套餐
    06:09 搬瓦工VPS套餐及线路选择
    09:37 搬瓦工VPS常用操作
    17:51 VPS是否被墙及延迟速度检测
    21:11 用finalshell连接VPS
    23:16 搭建vpn节点(重点)
    28:37 在本机电脑上配置v2ray
    32:56 搭建的VPN效果展示
    33:48 下期预告
    
[/code]

## 1\. 资源下载

本视频中用到的 所有脚本/配置/软件 下载  
一次下载, 全部拥有, 拒绝多次下载烦恼

### 1.1 windows x64:

`1.1a 国内云盘`

#### 1.1.1 下载 "宝箱"：

电脑 下载链接:  
<https://pan.quark.cn/s/aa2f6614ee80>  
或者 手机扫码:  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRbAl8LXtmNMhzxXVmPn9d_C__M-Z7MHbTv5QIXbFRUpO8cZr1VZmHt8m1XUTVaQhhMu-DKciQyC38RWwKgysMqr11-fIe2W_AC70Bf1AQUssupSWPl_N-m1yCPKVKCJ3xtBYA0nToPvMydGe0s34Oorj7ArlIRtqL6bC3na9thPHC1gq-iWJDlcv2Xxsi/s1600/Pasted%20image%2020250323174927.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRbAl8LXtmNMhzxXVmPn9d_C__M-Z7MHbTv5QIXbFRUpO8cZr1VZmHt8m1XUTVaQhhMu-DKciQyC38RWwKgysMqr11-fIe2W_AC70Bf1AQUssupSWPl_N-m1yCPKVKCJ3xtBYA0nToPvMydGe0s34Oorj7ArlIRtqL6bC3na9thPHC1gq-iWJDlcv2Xxsi/s120/Pasted%20image%2020250323174927.png)

  

#### 1.1.2 下载 "钥匙"：

<https://pan.quark.cn/s/f84d5a2a7fa0>  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6J2mwGJz3c_HeaUSkIxEgCUmUrmLAuPhgCuYAjISN_UmF4JGB-JSUbsg4B-RU3xUKIC2ieVecIsBmUIKH_Fr95So012pmPv6Ue647BKAA7Du1i0G7GQFuzM0DPtvbAjf4Az-2ajAKZb_4yW-N40VwbUlUV_pv-tc5HuTbm1WIxsCquXlobxdg_5sVf6p9/s1600/Pasted%20image%2020250323180212.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6J2mwGJz3c_HeaUSkIxEgCUmUrmLAuPhgCuYAjISN_UmF4JGB-JSUbsg4B-RU3xUKIC2ieVecIsBmUIKH_Fr95So012pmPv6Ue647BKAA7Du1i0G7GQFuzM0DPtvbAjf4Az-2ajAKZb_4yW-N40VwbUlUV_pv-tc5HuTbm1WIxsCquXlobxdg_5sVf6p9/s120/Pasted%20image%2020250323180212.png)

  

#### 1.1.3 下载后 使用方法：

(1).把"**钥匙** "复制到"**宝箱** "的文件夹的内部, 使得所有文件放在同一个文件夹内;  
(2).双击"**afei** ", 获得宝物.

`1.1b 国外云盘`  
<https://drive.google.com/drive/folders/14eYZ8KLDsYUJro9-f2FFdM3mf8wQBeAS?usp=sharing>

### 1.2 macOS arm64 苹果CPU

2020年之后的新苹果电脑  
下载链接:  
<https://drive.google.com/drive/folders/1dDj1IqZFPXQbbrrIQ3qOYhbLFhp_hOhs?usp=sharing>

### 1.3 macOS x64 intelCPU

2019年之前的老苹果电脑  
下载链接:  
<https://drive.google.com/drive/folders/1SIbOKcT06iqx_81jX6YaajxvlUUMZ8O6?usp=sharing>

## 2\. 注册/登录 搬瓦工(vps提供商)

搬瓦工是一家提供vps的互联网公司, 它家的vps有和国内(电信、联通、移动)直连的线路, 网络延迟低, 速度快, 个人独享IP, 价格也不高. 适用于在国外视频平台的博主/直播、跨境电商、经常网上付款或收款的、考虑到安全上网的(VPN有隐私或数据被记录或泄露风险).

官网(注册)网址:  
<https://cutt.ly/7ro8ty8x>

搬瓦工 vps性价比套餐:  
<https://afeinet.blogspot.com/2024/12/21.html>

注册/购买 实操演示 视频教程:  
<https://www.youtube.com/watch?v=NhlMXe0YAZE>

## 3\. 检测是否被墙

关闭翻墙软件  
打开命令行(快捷键 `Win+R`), 输入`cmd`, 敲回车
[code]
    ping 你vps的ip地址
    
[/code]

## 4\. 检测响应速度
[code]
    htpps://itdog.cn
    
[/code]

## 5\. 安装系统

Ubuntu 22.04 或 Ubuntu 24.0

## 6\. 升级apt
[code]
    apt update
    
[/code]

## 7\. 安装防火墙
[code]
    apt install ufw -y
    
[/code]

开启所有端口
[code]
    ufw disable
    
[/code]

## 8\. 安装hy2
[code]
    #一键安装Hysteria2
    bash <(curl -fsSL https://get.hy2.sh/)
    
    #生成自签证书
    openssl req -x509 -nodes -newkey ec:<(openssl ecparam -name prime256v1) -keyout /etc/hysteria/server.key -out /etc/hysteria/server.crt -subj "/CN=bing.com" -days 36500 && sudo chown hysteria /etc/hysteria/server.key && sudo chown hysteria /etc/hysteria/server.crt
    
    #启用Hysteria2 设置开机自启
    systemctl enable hysteria-server.service
    
[/code]

## 9\. VPS配置
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

重启Hysteria2
[code]
    systemctl restart hysteria-server.service
    
[/code]

查看Hysteria2状态
[code]
    systemctl status hysteria-server.service
    
[/code]

查看后, 在英文输入法下 按字母 Q 退出

同时看到以下两个结果代表成功  
active (running)  
server up and running {"listen": ":443"}

## 10\. v2rayN 客户端配置
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

## 11\. sing-box配置文件(Android/IOS)

11.1 iPhone操作  
美区apple id登录后, 打开 app store, 搜 sing-box
