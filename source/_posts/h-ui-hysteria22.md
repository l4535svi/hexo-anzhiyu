---
title: 最新 H-ui 面板一键安装 hysteria2|歇斯底里2 节点，新手小白轻松搭建翻墙节点，支持多用户管理、链式代理出站
date: '2025-05-13 12:00:00'
cover: /img/covers/h-ui-hysteria22.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 一、准备工作 1、 服务器一台 （下面是我常用的，你可以参考） Racknerd ( $10.98美金一年，性价比)： https://n28.it/b8a6e8 搬瓦工（CN2 GIA 线路，体验好）： https://n28.it/ke226z HostVds（按小时计费，适
---
## 一、准备工作

#### 1、服务器一台（下面是我常用的，你可以参考）

  * Racknerd ( $10.98美金一年，性价比)： <https://n28.it/b8a6e8>
  * 搬瓦工（CN2 GIA 线路，体验好）： <https://n28.it/ke226z>
  * HostVds（按小时计费，适合测试） ： <https://n28.it/e2zhyt>

#### 2、域名一个

  * <https://n27.top/regery> （性价比较高，最便宜的.pp.ua后缀 $0.99美元/年，支持支付宝、加密货币、PayPal、虚拟卡支付）
  * 其他国外域名注册商：name、GoDaddy、Spaceship、Porkbun等;
  * 为方便也可以直接在 CloudFlare 购买

#### 3、服务器连接工具

  * FinallShell（windows、mac、linux） ：<https://www.hostbuf.com/t/988.html>
  * MobaXterm（Windows）：<https://github.com/RipplePiam/MobaXterm-Chinese-Simplified/releases>

### 4、 订阅工具

  * 安卓、ios、windows、MacOs 订阅客户端：<https://n28.it/k85wgs>

## 二、 一键安装 H-UI 面板

#### 安装运行环境：

1、Debian、Ubuntu系统

```

    apt update -y && apt install curl wget -y

```

2、CentOS、Alma、Rocky 系列系统

```

    yum update -y && yum install curl wget -y

```

#### 安装 H-ui 面板

```

    bash <(curl -fsSL https://raw.githubusercontent.com/jonssonyan/h-ui/main/install.sh)

```

说明：根据提示一步步安装即可,根据不同的 VPS 可能需要放行防火墙端口

## 一键脚本

```

     bash -c "$(curl -sS https://raw.githubusercontent.com/passeway/ufw/main/ufw.sh)"
    

```

这段脚本的作用是关闭和禁用防火墙服务（firewalld），关闭 SELinux，禁用 UFW 防火墙，设置 iptables 规则允许所有传入、转发和输出的流量，并且清除所有的 iptables 规则，最后保存 iptables 规则以防止重启后丢失。  
1：停止并禁用 firewalld 服务：停止并禁用当前运行的 firewalld 服务，如果存在的话。  
2：关闭 SELinux：将 SELinux 设置为“permissive”模式，这意味着 SELinux 仍然会记录违例，但不会阻止任何操作。  
3：禁用 UFW 防火墙：停止并禁用 UFW 防火墙服务。  
4：设置 iptables 规则允许所有传入、转发和输出的流量：将 iptables 的默认策略设置为允许所有传入、转发和输出的流量。  
5：清除 iptables 的 mangle 表和所有链的规则：清除所有 iptables 的规则和链。  

## 6：保存 iptables 规则以防止重启后丢失：使用 netfilter-persistent 工具保存当前的 iptables 规则。三、h-ui 配置 Hysteria2 节点

#### 1、默认访问地址(根据安装成功显示的用户密码登录)：

```

    http://IP:端口

```

#### 2、解析域名

  * 登录 Cloudflare (或者直接在购买域名的服务商平台)，在要绑定的域名的 DNS 添加一条A记录 , IP 解析到你服务器的 IP

#### 3、 申请证书TLS （点击 Hysteria 管理 -> TLS）

  * tls.type: 选择 acme 申请
  * acme.domains: 填入准备好的域名，例如：hui.domain.com（自己的域名）
  * acme.ca: 选择 letsencrypt
  * 保存一下配置
  * 点击 “开启” ，这时候会提示 http connection error，没有关系，使用 acmme 申请证书的时候需要等待一段时间证书才能申请下来
  * 可以进入 日志 -> Hysteria 日志 菜单查看日志,多刷新几次大概一分钟左右就可以
  * 刷新完之后，回到 Hysteria 管理 显示 Hysteria2 状态: 运行

#### 4、 域名代替IP去访问面板

  * 点击 系统设置，面板开启 https 选项，选择 是，然后点击 使用 Hysteria2 的证书 ，它会自动识别到证书的路径，点击 保存
  * 点击重启面板
  * 通过 域名访问节点面板，重新登录即可

#### 5、 使用、管理

  * 在账户管理模块，可以添加多用户，可以设置用户限额和套餐
  * 在 Hysteria 管理 菜单还可以设置出站规则实现链式代理等其他功能

#### 6、 订阅使用

  * 通过 账户信息 那里的 订阅/节点链接/二维码 可以导入到客户端使用
  * 各种设备对应的订阅客户端：<https://n27.top/k85wgs>
