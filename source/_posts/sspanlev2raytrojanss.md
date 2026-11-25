---
title: sspanle手动对接v2ray、trojan、ss
date: '2022-04-18 12:00:00'
tags:
- 建站
categories:
- 建站
description: 'XrayR为GIthub上开源项目，项目地址 XrayR-project/XrayR: A Xray backend framework that can easily support many panels. 一个基于Xray的后端框架，支持V2ay,Trojan,Shadow'
---
# XrayR为GIthub上开源项目，项目地址

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
  
# 正文：

## 

#### 默认为CentOS7

## 

安装lrzsz软件，root权限下。安装lrzsz 并上传 [XrayR](https://blog.lvuy.xyz/wp-content/uploads/2022/03/XrayR-linux-32.zip)
[code]
    yum -y install lrzsz  
    rz   // 选择文件上传即可
[/code]

安装unzip,CentOS ZIP解压工具 并解压   [XrayR](https://blog.lvuy.xyz/wp-content/uploads/2022/03/XrayR-linux-32.zip)
[code]
    yum install -y unzip zip  
    unzip XrayR-linux-32.zip
[/code]

root目录下，修改cogfig并运行xrayr
[code]
    ./XrayR -config config.yml
[/code]

### 使用systemctl管理守护进程

### vim /etc/systemd/system/XrayR.service

### 把以下内容复制进去
[code]
    [Unit]  
    Description=XrayR Service  
    After=network.target nss-lookup.target  
    Wants=network.target  
      
    [Service]  
    User=root  
    Group=root  
    Type=simple  
    LimitAS=infinity  
    LimitRSS=infinity  
    LimitCORE=infinity  
    LimitNOFILE=999999  
    WorkingDirectory=/root/  
    ExecStart=/root/XrayR -config /root/config.yml  
    Restart=on-failure  
    RestartSec=10  
      
    [Install]  
    WantedBy=multi-user.target  
    
[/code]
[code]
    systemctl enable --now  XrayR  #运行 并添加开机自启  
    systemctl status XrayR    #查看状态
[/code]

 

 

# config示例：
[code]
    PanelType: "V2board" # Panel type: SSpanel, V2board, PMpanel #面板类型  
    ApiConfig:  
        ApiHost: "http://127.0.0.1:667"    #机场域名  
        ApiKey: "123"                      #对接密钥  
        NodeID: 41                         #节点ID  
        NodeType: V2ray # Node type: V2ray, Trojan, Shadowsocks, Shadowsocks-Plugin  #协议类型  
        Timeout: 30 # Timeout for the api request, Default is 5 sec  
        EnableVless: false # Enable Vless for V2ray Type  
        EnableXTLS: false # Enable XTLS for V2ray and Trojan  
        SpeedLimit: 0 # Local settings will replace remote settings, 0 means disable  
        DeviceLimit: 0 # Local settings will replace remote settings, 0 means disable  
        RuleListPath: # /etc/XrayR/rulelist Path to local rulelist file  
        DisableCustomConfig: false # Disable custom config
[/code]

## 如果需要增加TLS 则修改
[code]
    CertConfig:  
        CertMode: dns # Option about how to get certificate: none, file, http, dns. Choose "none" will forcedly disable the tls config.  
        RejectUnknownSni: false # Reject unknown SNI, default false  
        CertDomain: "node2.test.com" # Domain to cert   #节点域名  
        CertFile: /etc/XrayR/cert/node2.test.com.cert # Provided if the CertMode is file  #域名证书  
        KeyFile: /etc/XrayR/cert/node2.test.com.key                   #证书密钥  
        Provider: alidns # DNS cert provider, Get the full support list here: https://go-acme.github.io/lego/dns/   #证书注册商  
        Email: test@me.com  
        DNSEnv: # DNS ENV option used by DNS provider  
            ALICLOUD_ACCESS_KEY: aaa   #证书注册商账号  
            ALICLOUD_SECRET_KEY: bbb   #证书注册商密钥
[/code]

PS:未作注释则不需要修改
