---
title: 当前最强后端，XrayR部署Nginx+Trojan
date: '2022-04-18 12:00:00'
cover: /img/covers/xrayrnginxtrojan.jpg
tags:
- 建站
categories:
- 建站
description: 特点 永久开源且免费。 支持V2ray，Trojan， Shadowsocks多种协议。 支持Vless和XTLS等新特性。 支持单实例对接多面板、多节点，无需重复启动。 支持限制在线IP 支持节点端口级别、用户级别限速。 配置简单明了。 修改配置自动重启实例。 方便编译和升级，
---
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
  
## 

# 正文：

## centOS7为例

## 首先 CentOS 禁用 SELinux

```

    sed -i 's/enforcing/disabled/g' /etc/selinux/config /etc/selinux/config  
    #修改后要重启  
    reboot

```

安装加速

推荐使用BBR2或BBRPlus

```

    yum install wget  
    wget -N --no-check-certificate "https://github.000060000.xyz/tcp.sh" && chmod +x tcp.sh && ./tcp.sh

```

关闭防火墙

```

    systemctl stop firewalld.service  \\关闭  
      
    systemctl disable firewalld.service  \\开机禁自启

```

## 部署Nginx并安装stream模块

```

    yum update  
    yum -y install epel-release  
    yum install -y nginx  
    yum install nginx-mod-stream

```

检测Nginx状态，是否安装成功

```

    systemctl start nginx

```

```

    systemctl status nginx.service

```

添加nginx开机自启

```

    systemctl enable nginx.service

```

 

安装失败自行排查原因，或手动编译Nginx 1.21.0

cerbot部署证书

```

    yum install snapd  
    systemctl enable --now snapd.socket  
    ln -s /var/lib/snapd/snap /snap  
    snap install snap-store

```

```

    snap install core;  snap refresh core  
    snap install --classic certbot  
    ln -s /snap/bin/certbot /usr/bin/certbot  
    certbot --nginx

```

## PS：cerbot教程随官方文档更新，视频为老版本教程，两者同样适用，如果执行certbot –nginx 后 提示

## `Could not automatically find a matching server block for 域名. Set the `server_name` directive to use the Nginx installer`

## 在/etc/nginx/nginx.conf 配置文件中 `server_name` 添加你的域名

示例：

```

    server_name aaa.con

```

重载nginx；重新部署证书

```

    systemctl restart nginx.service  
    certbot --nginx

```

 

 

Nginx配置

修改/etc/nginx/nginx.conf配置文件

```

    stream {  
        server {  
            listen              443 ssl;                    # 设置监听端口为443  
      
            ssl_protocols       TLSv1.2 TLSv1.3;      # 设置使用的SSL协议版本  
      
            ssl_certificate /etc/nginx/ssl/xx.com.pem; # 证书地址  
            ssl_certificate_key /etc/nginx/ssl/xx.com.key; # 秘钥地址  
            ssl_session_cache   shared:SSL:10m;             # SSL TCP会话缓存设置共享内存区域名为  
                                                            # SSL，区域大小为10MB  
            ssl_session_timeout 10m;                        # SSL TCP会话缓存超时时间为10分钟  
            proxy_protocol    on; # 开启proxy_protocol获取真实ip  
            proxy_pass        127.0.0.1:1234; # 后端Trojan监听端口  
        }  
    }

```

 

请将上方代码添加到http与events中间一行

/etc/nginx/nginx.conf配置文件参考：

```

    events {  
        worker_connections 768;  
        # multi_accept on;  
    }  
      
    stream {  
        server {  
            listen              443 ssl;                    # 设置监听端口为443  
      
            ssl_protocols       TLSv1.2 TLSv1.3;      # 设置使用的SSL协议版本  
      
            ssl_certificate /etc/nginx/ssl/xx.com.pem; # 证书地址  
            ssl_certificate_key /etc/nginx/ssl/xx.com.key; # 秘钥地址  
            ssl_session_cache   shared:SSL:10m;             # SSL TCP会话缓存设置共享内存区域名为  
                                                            # SSL，区域大小为10MB  
            ssl_session_timeout 10m;                        # SSL TCP会话缓存超时时间为10分钟  
            proxy_protocol    on; # 开启proxy_protocol获取真实ip  
            proxy_pass        127.0.0.1:1234; # 后端Trojan监听端口  
        }  
    }  
      
    http {  
      
        ##  
        # Basic Settings  
        ##

```

继续重载nginx检查是否报错

```

    systemctl restart nginx.service

```

 

注意事项：

1\. 请配置SSL证书

2\. proxy_pass 127.0.0.1:1234 后端Trojan监听端口与您网站前端节点监听端口一致

3\. listen端口可以1-65535随意修改，此处为客户端连接端口

## 部署XrayR

XrayR一键部署

```

    bash <(curl -Ls https://raw.githubusercontent.com/XrayR-project/XrayR-release/master/install.sh)

```

配置文件路径：`/etc/XrayR/config.yml`

XrayR Trojan配置

## 关键配置：

### ListenIP: 127.0.0.1

### EnableProxyProtocol: true

### EnableFallback: true

### CertMode: none

注意1：请务必确保CertMode为none，交由Nginx处理tls

注意2：在回落时请确保回落站点是http1.1，nginx如果有一个站点是h2会导致全部站点都变成h2（巨坑）

完整样例

```

     -  
    PanelType: "SSpanel" # Panel type: SSpanel, V2board, PMpanel  
    ApiConfig:  
    ApiHost: "https://xxx.com"  
    ApiKey: "123"  
    NodeID: 1  
    NodeType: Trojan # Node type: V2ray, Shadowsocks, Trojan  
    Timeout: 10 # Timeout for the api request  
    EnableVless: false # Enable Vless for V2ray Type  
    EnableXTLS: false # Enable XTLS for V2ray and Trojan  
    SpeedLimit: 0 # Mbps, Local settings will replace remote settings, 0 means disable  
    DeviceLimit: 0 # Local settings will replace remote settings, 0 means disable  
    RuleListPath: # /etc/XrayR/rulelist Path to local rulelist file  
    ControllerConfig:  
    ListenIP: 127.0.0.1 # IP address you want to listen  
    SendIP: 0.0.0.0 # IP address you want to send pacakage  
    UpdatePeriodic: 60 # Time to update the nodeinfo, how many sec.  
    EnableDNS: false # Use custom DNS config, Please ensure that you set the dns.json well  
    DNSType: AsIs # AsIs, UseIP, UseIPv4, UseIPv6, DNS strategy  
    EnableProxyProtocol: true # Only works for WebSocket and TCP  
    EnableFallback: true # Only support for Trojan and Vless  
    FallBackConfigs: # Support multiple fallbacks  
    -  
    SNI: # TLS SNI(Server Name Indication), Empty for any  
    Path: # HTTP PATH, Empty for any  
    Dest: fake.website.com:80 # Required, Destination of fallback, check https://xtls.github.io/config/fallback/ for details.  
    ProxyProtocolVer: 0 # Send PROXY protocol version, 0 for dsable  
    CertConfig:  
    CertMode: none # Option about how to get certificate: none, file, http, dns. Choose "none" will forcedly disable the tls config.  
    CertDomain: "node1.test.com" # Domain to cert  
    CertFile: /etc/XrayR/cert/node1.test.com.cert # Provided if the CertMode is file  
    KeyFile: /etc/XrayR/cert/node1.test.com.key  
    Provider: alidns # DNS cert provider, Get the full support list here: https://go-acme.github.io/lego/dns/  
    Email: test@me.com  
    DNSEnv: # DNS ENV option used by DNS provider  
    ALICLOUD_ACCESS_KEY: aaa  
    ALICLOUD_SECRET_KEY: bbb

```

重启并检查 Nginx 和 XrayR

```

    systemctl restart nginx  
    XrayR restart

```

```

    systemctl status nginx  
    XrayR status

```

