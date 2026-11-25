---
title: claw容器搭建哪吒监控
date: '2025-07-16 12:00:00'
tags:
- 哪吒探针
categories:
- 哪吒探针
description: claw免费容器 首月送5$，不需要验证信用卡，如果是已经有180天的github用户注册，可解锁每月5$ 点击这个链接进行注册： https://console.run.claw.cloud/signin?link=UDKJPZLNV4SK 项目地址：https://githu
---
claw免费容器 首月送5$，不需要验证信用卡，如果是已经有180天的github用户注册，可解锁每月5$

点击这个链接进行注册：<https://console.run.claw.cloud/signin?link=UDKJPZLNV4SK>

项目地址：https://github.com/nezhahq/nezha/pkgs/container/nezha

Image Name(镜像名称)：ghcr.io/nezhahq/nezha:v1.12.0

设置自定义域名 nezha.apepine.top

Local Storage，添加一个持久化存储 路径填/dashboard/data

配置grpc反代

Image Name(镜像名称)： nginx

添加自定义域名 agent.apepine.top

添加配置文件 Configmaps

file name ： /etc/nginx/conf.d/default.conf

粘贴以下内容：  
文件内容中 nezha.ns-imc7mqm6.svc.cluster.local 替换为你自己的哪吒面板容器的内网地址，就是刚刚创建的第一个容器  
内网地址可以去第一个容器看看 Network那里

[![](https://apepine.com/wp-content/uploads/2025/04/image-8-1024x303.png)](https://apepine.com/wp-content/uploads/2025/04/image-8-1024x303.png)

http://nezha.ns-imc7mqm6.svc.cluster.local:8008

内容：
[code]
    upstream dashboard {
        server nezha.ns-imc7mqm6.svc.cluster.local:8008;
        keepalive 512;
    }
    
    server {
        listen 80 http2;
        server_name nezha.ns-imc7mqm6.svc.cluster.local;
    
        underscores_in_headers on;
    
        location ^~ /proto.NezhaService/ {
            grpc_set_header Host $host;
            grpc_set_header nz-realip $remote_addr;
            grpc_read_timeout 600s;
            grpc_send_timeout 600s;
            grpc_socket_keepalive on;
            client_max_body_size 10m;
            grpc_buffer_size 4m;
            grpc_pass grpc://dashboard;
        }
    }
[/code]

现在可以访问域名啦

Agent对接地址： agent.apepine.top:80 #（第二个容器自定义的域名）
