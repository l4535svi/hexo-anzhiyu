---
title: XrayR为GIthub上开源项目，项目地址
date: '2022-04-18 12:00:00'
cover: /img/covers/xrayrgithub.jpg
tags:
- 建站
categories:
- 建站
description: 'XrayR-project/XrayR: A Xray backend framework that can easily support many panels. 一个基于Xray的后端框架，支持V2ay,Trojan,Shadowsocks协议，极易扩展，支持多面板对接 (g'
---
[XrayR-project/XrayR: A Xray backend framework that can easily support many panels. 一个基于Xray的后端框架，支持V2ay,Trojan,Shadowsocks协议，极易扩展，支持多面板对接 (github.com)](https://github.com/XrayR-project/XrayR)

## 特点

  * 永久开源且免费。
  * 支持V2ray，Trojan， Shadowsocks多种协议。
  * 支持Vless和XTLS等新特性。
  * 支持单实例对接多面板、多节点，无需重复启动。
  * 支持限制在线IP
  * 支持节点端口级别、用户级别限速。
  * 配置简单明了。
  * 修改配置自动重启实例。
  * 方便编译和升级，可以快速更新核心版本， 支持Xray-core新特性。

## [](https://github.com/XrayR-project/XrayR#%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D)功能介绍

功能| v2ray| trojan| shadowsocks  
---|---|---|---  
获取节点信息| √| √| √  
获取用户信息| √| √| √  
用户流量统计| √| √| √  
服务器信息上报| √| √| √  
自动申请tls证书| √| √| √  
自动续签tls证书| √| √| √  
在线人数统计| √| √| √  
在线用户限制| √| √| √  
审计规则| √| √| √  
节点端口限速| √| √| √  
按照用户限速| √| √| √  
自定义DNS| √| √| √  
  
## [](https://github.com/XrayR-project/XrayR#%E6%94%AF%E6%8C%81%E5%89%8D%E7%AB%AF)支持前端

前端| v2ray| trojan| shadowsocks  
---|---|---|---  
sspanel-uim| √| √| √ (单端口多用户和V2ray-Plugin)  
v2board| √| √| √  
[PMPanel](https://github.com/ByteInternetHK/PMPanel)| √| √| √  
[ProxyPanel](https://github.com/ProxyPanel/ProxyPanel)| √| √| √  
  
## 正文开始

## 

## 关闭防火墙

```

    systemctl stop firewalld.service #关闭  
    systemctl disable firewalld.service#开机禁止自启

```

## 同步时间（对接v2ray需要执行，Trojan不需要执行）

```

    yum -y install ntpdate  
    timedatectl set-timezone Asia/Shanghai  
    ntpdate ntp2.aliyun.com

```

## 安装XrayR

一键脚本

```

    bash <(curl -Ls https://raw.githubusercontent.com/XrayR-project/XrayR-release/master/install.sh)

```

## 默认对接sspanel前端

## 对接V2ray

前端写法

SSpanel 节点地址格式

IP;监听端口;alterId;(tcp或ws);(tls或不填);path=/xxx|host=xxxx.com|server=xxx.com|outside_port=xxx

alterId设为0，则自动启用VMessAEAD。

注意：VMESS AEAD 将在 2022 年 1 月 1 日强制启用 请注意更新服务端配置，设置alterId = 0

tcp示例

ip;12345;0;tcp;;server=域名

示例：1.3.5.7;12345;0;tcp;;server=hk.domain.com

tcp+http示例

注意sspanel并不支持此类订阅下发，此选项只供开启后端http混淆。

ip;12345;0;tcp;;server=域名;headertype=http

示例：1.3.5.7;12345;0;tcp;;server=hk.domain.com;headertype=http

tcp + tls 示例

ip;12345;0;tcp;tls;server=域名|host=域名

示例：1.3.5.7;12345;0;tcp;tls;server=hk.domain.com|host=hk.domain.com

ws示例

ip;80;0;ws;;path=/xxx|server=域名|host=CDN域名

示例：1.3.5.7;80;0;ws;;path=/v2ray|server=hk.domain.com|host=hk.domain.com

ws + tls 示例

ip;443;0;ws;tls;path=/xxx|server=域名|host=CDN域名

示例：1.3.5.7;443;0;ws;tls;path=/v2ray|server=hk.domain.com|host=hk.domain.com

ws + tls (Caddy/Nginx) 示例

交由Caddy或者Nginx处理TLS 节点配置和 ws+tls一致，在后端配置`CertMode: none`

同时设置outside_port为Caddy/Nginx监听端口，转发到12345为XrayR监听端口。可以在后端配置`ListenIP: 127.0.0.1`监听本地端口。

ip;12345;0;tls;ws;path=/xxx|server=域名|host=CDN域名|outside_port=443

示例：1.3.5.7;12345;0;ws;tls;path=/v2ray|server=hk.domain.com|host=hk.domain.com示例：1.3.5.7;12345;2;ws;tls;path=/v2ray|server=hk.domain.com|host=hk.domain.com

grpc+tls示例

使用grpc建议升级sspanel至[Anankke/SSPanel-Uim@8f68b63](https://github.com/Anankke/SSPanel-Uim/commit/8f68b6360baf9f6624e1158e3cae81d93d1db107)

ip;12345;0;grpc;tls;host=域名|server=域名|servicename=任意字符串

示例：1.3.5.7;12345;0;grpc;tls;host=hk.domain.com|server=hk.domain.com|servicename=mygrpc

中转端口

在任一配置组|合后增加`|outside_port=xxx`,此项为用户连接端口。

XrayR没有`inside_port=xx`配置选项，如需监听本地端口，请在配置文件中设置监听ip为`127.0.0.1`。

示例：1.3.5.7;80;0;ws;;path=/v2ray|server=hk.domain.com|host=hk.domain.com|outside_port=12345

启用Vless

此项为实验性功能，请确保您使用的面板已经支持下发vless订阅，否则请手动配置客户端。

sspanel升级到此版本[Anankke/SSPanel-Uim@8f68b63](https://github.com/Anankke/SSPanel-Uim/commit/8f68b6360baf9f6624e1158e3cae81d93d1db107)后支持vless订阅下发

在任意协议配置后增加`enable_vless=true`

示例：hk.domain.com;12345;0;tcp;(tls或xtls);server=hk.domain.com|enable_vless=true

同时在本地设置文件将`EnableVless`设为true。

请开启vless同时务必使用tls或者xtls。

启用xtls

此项为实验性功能，请确保您使用的面板已经支持下发带有xtls的订阅，否则请手动配置客户端。

sspanel升级到此版本[Anankke/SSPanel-Uim@8f68b63](https://github.com/Anankke/SSPanel-Uim/commit/8f68b6360baf9f6624e1158e3cae81d93d1db107)后支持xtls订阅下发

将任意协议配置中的`tls`替换成`xtls`，如果xtls有流控flow，则在最后增加: `|flow=flow-vlaue`

示例：hk.domain.com;443;0;tcp;xtls;server=hk.domain.com|host=hk.domain.com|enable_vless=true|flo

## 

配置文件路径：`/etc/XrayR/config.yml`

```

    PanelType: "sspanel"            # 面板类型是V2board就写V2board，是sspanel就写sspanel  
    ApiConfig:  
    ApiHost: "http://127.0.0.1:667" #更改为前端域名  
    ApiKey: "123"                   #与前端config中mukye一致  
    NodeID: 41                      #更改为节点ID  
    NodeType: V2ray                 #默认V2ray不做更改    
    Timeout: 30 # Timeout for the api request, Default is 5 sec  
    EnableVless: false # Enable Vless for V2ray Type  
    EnableXTLS: false # Enable XTLS for V2ray and Trojan  
    SpeedLimit: 0 # Local settings will replace remote settings, 0 means disable  
    DeviceLimit: 0 # Local settings will replace remote settings, 0 means disable  
    RuleListPath: # /etc/XrayR/rulelist Path to local rulelist file  
    DisableCustomConfig: false # Disable custom config

```

如果只对接单纯的vmess 只需要修改以上配置

如果需要配置tls则需要更改以下配置

```

    CertConfig:  
    CertMode: dns # 默认  
    CertDomain: "node2.test.com" # 更改为节点域名  
    CertFile: /etc/XrayR/cert/node2.test.com.cert #对应证书路径  
    KeyFile: /etc/XrayR/cert/node2.test.com.key    #对应密钥路径  
    Provider: alidns # 更改为节点域名的注册商 完整的支持列表：https://go-acme.github.io/lego/dns/  
    Email: test@me.com  
    DNSEnv: # DNS ENV option used by DNS provider  
    ALICLOUD_ACCESS_KEY: aaa   #不同的DNS供应商对应不同的配置值 可在这里获得支持https://go-acme.github.io/lego/dns/  
    ALICLOUD_SECRET_KEY: bbb   #不同的DNS供应商对应不同的配置值 可在这里获得支持https://go-acme.github.io/lego/dns/

```

重启XrayR，如果重启失败自行分析日志

```

    xrayr resart #重启  
    xrayr log  #日志

```

## 对接Trojan

前端写法

SSpanel-uim 节点地址格式

域名或IP;port=用户连接端口#监听端口|host=xx

tcp示例

示例：gz.aaa.com;port=443|host=gz.aaa.com

grpc示例

使用trojan+grpc请升级sspanel至[Anankke/SSPanel-Uim@8f68b63](https://github.com/Anankke/SSPanel-Uim/commit/8f68b6360baf9f6624e1158e3cae81d93d1db107)

示例：gz.aaa.com;port=443|host=gz.aaa.com|grpc=1|servicename=mygrpc

中转示例

用户连接443，XrayR监听12345

示例：gz.aaa.com;port=443#12345|host=hk.aaa.com

启用xtls (此项为实验性功能)

sspanel升级到此版本[Anankke/SSPanel-Uim@8f68b63](https://github.com/Anankke/SSPanel-Uim/commit/8f68b6360baf9f6624e1158e3cae81d93d1db107)后支持xtls订阅下发

将任意协议配置中添加`enable_xtls=true`，如果xtls有流控flow，则在最后增加: `flow=flow-vlaue`

示例：gz.aaa.com;port=443|host=gz.aaa.com|enable_xtls=true|flow=xtls-rprx-direct

配置文件路径：`/etc/XrayR/config.yml`

```

    PanelType: "sspanel" # 面板类型是V2board就写V2board，是sspanel就写sspanel  
    ApiConfig:  
    ApiHost: "http://127.0.0.1:667" #更改为前端域名  
    ApiKey: "123" #与前端config中mukye一致  
    NodeID: 41 #更改为节点ID  
    NodeType: Trojan #更改为Trojan   
    Timeout: 30 # Timeout for the api request, Default is 5 sec  
    EnableVless: false # Enable Vless for V2ray Type  
    EnableXTLS: false # Enable XTLS for V2ray and Trojan  
    SpeedLimit: 0 # Local settings will replace remote settings, 0 means disable  
    DeviceLimit: 0 # Local settings will replace remote settings, 0 means disable  
    RuleListPath: # /etc/XrayR/rulelist Path to local rulelist file  
    DisableCustomConfig: false # Disable custom config

```

```

    CertConfig:  
    CertMode: dns # 默认  
    CertDomain: "node2.test.com" # 更改为节点域名  
    CertFile: /etc/XrayR/cert/node2.test.com.cert #对应证书路径  
    KeyFile: /etc/XrayR/cert/node2.test.com.key #对应密钥路径  
    Provider: alidns # 更改为节点域名的注册商 完整的支持列表：https://go-acme.github.io/lego/dns/  
    Email: test@me.com  
    DNSEnv: # DNS ENV option used by DNS provider  
    ALICLOUD_ACCESS_KEY: aaa #不同的DNS供应商对应不同的配置值 可在这里获得支持https://go-acme.github.io/lego/dns/  
    ALICLOUD_SECRET_KEY: bbb #不同的DNS供应商对应不同的配置值 可在这里获得支持https://go-acme.github.io/lego/dns/

```

重启XrayR，如果重启失败自行分析日志

```

    xrayr resart #重启  
    xrayr log  #日志

```

