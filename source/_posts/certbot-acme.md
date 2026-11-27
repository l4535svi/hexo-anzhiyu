---
title: 用certbot申请免费的域名证书 比acme还好用！
date: '2025-03-06 12:00:00'
cover: /img/covers/certbot-acme.jpg
tags:
- 免费域名
categories:
- 免费域名
description: Certbot是一个由Electronic Frontier Foundation（EFF）赞助的开源工具，用于自动化管理和部署SSL/TLS证书。SSL/TLS证书是用于加密网站与用户之间传输的数据的一种安全协议。Certbot的主要目的是使网站管理员能够轻松获取、部署和更新这
---
[![](https://blog.kejilion.pro/wp-content/uploads/2024/04/image.png)](https://blog.kejilion.pro/wp-content/uploads/2024/04/image.png)

  
  

Certbot是一个由Electronic Frontier Foundation（EFF）赞助的开源工具，用于自动化管理和部署SSL/TLS证书。SSL/TLS证书是用于加密网站与用户之间传输的数据的一种安全协议。Certbot的主要目的是使网站管理员能够轻松获取、部署和更新这些证书，以确保网站的安全性。

Certbot支持许多常见的Web服务器，包括但不限于Apache、Nginx、Certbot还提供了一个通用的插件系统，使其能够与其他Web服务器和环境集成。

Certbot的工作原理是通过与Let's Encrypt通信来获取免费的SSL/TLS证书。Let's Encrypt是一个非营利性的证书颁发机构，致力于提供免费、自动化和开放的SSL/TLS证书服务，以推动互联网上更广泛的加密使用。Certbot与Let's Encrypt的结合使得网站管理员能够方便地为他们的网站启用HTTPS，提高网站的安全性和用户隐私。

SSL证书可以让数据加密进行通信，常用于网站客户端和服务端之间通信使用，免费证书**Let's Encrypt** 机构利于推进所有网站创建SSL证书安全通信。

安全通信443端口，目前TLS 1.3是最新版本。

  

**Debian/Ubuntu安装certbot**

apt update -y && apt install -y certbot

**CentOS安装certbot**

yum -y update && yum -y install certbot

**Alpine Linux安装certbot**

apk update && apk add certbot

  

**申请证书**

确认80和443未被占用

curl -s ipv4.ip.sb

certbot certonly --standalone -d **$yuming**  \--email your@email.com --agree-tos --no-eff-email --force-renewal

**证书存放目录**

ls /etc/letsencrypt/live/

  

**自动续签脚本**

curl -O https://raw.githubusercontent.com/kejilion/sh/main/auto_cert_renewal-1.sh

chmod +x auto_cert_renewal-1.sh

./auto_cert_renewal-1.sh

**定时执行**

echo "0 0 * * * cd ~ && ./auto_cert_renewal-1.sh" | crontab -

crontab -e

  

**DNS方式申请（国内申请可用）**

certbot certonly --manual --preferred-challenges dns -d yuming.com

[![](https://blog.kejilion.pro/wp-content/uploads/2024/04/image-2.png)](https://blog.kejilion.pro/wp-content/uploads/2024/04/image-2.png)

到域名后台解析一个TXT记录

填写名称和值

解析后5分钟

回到SSH终端回车继续申请
