---
title: 科学上网：VPS 搭建 X-UI 面板
date: '2022-03-22 12:00:00'
cover: /img/covers/vps-x-ui.jpg
tags:
- 建站
categories:
- 建站
description: 使用X-UI搭建代理服务，具有以下优点： 支持系统状态监控：如CPU、内存、硬盘等状态 支持多用户多协议，网页可视化操作 支持流量统计 支持自定义Xray配置模板 支持HTTPS访问面板 支持面板自定义端口，账号与密码 快速生成分享连接或二维码 支持CDN套用 支持Fallbac
---
## 使用X-UI搭建代理服务，具有以下优点：

  * 支持系统状态监控：如CPU、内存、硬盘等状态
  * 支持多用户多协议，网页可视化操作
  * 支持流量统计
  * 支持自定义Xray配置模板
  * 支持HTTPS访问面板
  * 支持面板自定义端口，账号与密码
  * 快速生成分享连接或二维码
  * 支持CDN套用
  * 支持Fallback分流设置

### [](https://github.com/KEJIXIAOLU/dajian#%E8%AF%A6%E6%83%85%E8%AF%B7%E5%8F%82%E7%85%A7vps%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8Bhttpsyoutubei5idhrjij7c)详情请参照VPS搭建教程：<https://youtu.be/i5iDHRJiJ7c>

## [](https://github.com/KEJIXIAOLU/dajian#%E4%B8%80-%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)一、 准备工作

  * 1、已经解析的域名，Win+R输入CMD 回车：键入ping 空格输入你的域名，检查一下是否可以ping通
  * 2、一台境外VPS主流系统，例如：Debian/Ubuntu/CentOS
  * 3、下载并安装FinalShell SSH工具

Windows版下载地址: <http://www.hostbuf.com/downloads/finalshell_install.exe>

macOS版下载地址: <http://www.hostbuf.com/downloads/finalshell_install.pkg>

## [](https://github.com/KEJIXIAOLU/dajian#%E4%BA%8C%E5%AE%89%E8%A3%85%E6%9B%B4%E6%96%B0%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83)二、安装更新运行环境

### [](https://github.com/KEJIXIAOLU/dajian#1debianubuntu%E7%B3%BB%E7%BB%9F%E6%89%A7%E8%A1%8C%E4%BB%A5%E4%B8%8B%E5%91%BD%E4%BB%A4)1、Debian/Ubuntu系统执行以下命令：

```

    apt update -y && apt install -y curl && apt install -y socat

```

### [](https://github.com/KEJIXIAOLU/dajian#2centos%E7%B3%BB%E7%BB%9F%E6%89%A7%E8%A1%8C%E4%BB%A5%E4%B8%8B%E5%91%BD%E4%BB%A4)2、CentOS系统执行以下命令：

```

    yum update -y && yum update -y && yum install -y socat

```

### [](https://github.com/KEJIXIAOLU/dajian#%E8%BF%90%E8%A1%8Cacme%E8%84%9A%E6%9C%AC)运行Acme脚本

```

    curl https://get.acme.sh | sh

```

### [](https://github.com/KEJIXIAOLU/dajian#%E7%94%B3%E8%AF%B7%E8%AF%81%E4%B9%A6%E5%8F%8A%E5%AF%86%E9%92%A5)申请证书及密钥

【将代码中注释的邮箱和域名，改为你自己的】

```

    ~/.acme.sh/acme.sh --register-account -m xxxx@gmail.com

```

* * *

```

    ~/.acme.sh/acme.sh  --issue -d 输入你的域名  --standalone

```

### [](https://github.com/KEJIXIAOLU/dajian#%E4%B8%8B%E8%BD%BD%E8%AF%81%E4%B9%A6%E5%8F%8A%E5%AF%86%E9%92%A5)下载证书及密钥

```

    ~/.acme.sh/acme.sh --installcert -d 输入你的域名 --key-file /root/private.key --fullchain-file /root/cert.crt

```

### [](https://github.com/KEJIXIAOLU/dajian#%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7x-ui%E9%9D%A2%E6%9D%BF%E4%B8%80%E9%94%AE%E8%84%9A%E6%9C%AC)安装&升级x-ui面板一键脚本

```

    bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)

```

### [](https://github.com/KEJIXIAOLU/dajian#bbr2%E5%8A%A0%E9%80%9F)##BBR2加速##

```

    wget --no-check-certificate -q -O bbr2.sh "https://github.com/yeyingorg/bbr2.sh/raw/master/bbr2.sh" && chmod +x bbr2.sh && bash bbr2.sh auto

```

## [](https://github.com/KEJIXIAOLU/dajian#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)注意事项

  * 1、如何在申请证书及密钥这一步搭建失败，检查并放行端口，口令如下：

查看已开放的端口

```

        firewall-cmd --list-ports

```

开放端口（开放后需要要重启防火墙才生效）

```

    firewall-cmd --zone=public --add-port=3338/tcp --permanent

```

重启防火墙

```

    firewall-cmd --reload

```

停止防火墙

```

    systemctl stop firewalld

```

  * 2、如果是全新安装，默认网页端口为 54321，用户名和密码默认都是 admin ， 如何遇到打不开的情况，可能是端口没有放行，用【方法1】键入停止防火墙代码，或键入开放端口代码。
  * 3、V2ray软件：设置——参数设置——V2rayN设置——Core类型改为Xray_Core
