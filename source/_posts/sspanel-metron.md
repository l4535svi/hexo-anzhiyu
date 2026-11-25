---
title: 易支付对接sspanel Metron 教程以及支付源码
date: '2022-04-18 12:00:00'
tags:
- 建站
categories:
- 建站
description: V免签能够免签约收款，但是很多都不支持V免签，对接上易支付就很方便了，很多源码都支持易支付的协议。 准备好一台VPS。搭建好宝塔面板。 上传好源码后 设置伪静态 location / { if (!-e $request_filename ) { rewrite ^/(.[a-z
---
V免签能够免签约收款，但是很多都不支持V免签，对接上易支付就很方便了，很多源码都支持易支付的协议。

准备好一台VPS。搭建好宝塔面板。

上传好源码后

设置伪静态
[code]
    location / {  
     if (!-e $request_filename) {  
       rewrite ^/(.[a-zA-Z0-9\-\_]+).html$ /index.php?mod=$1 last;  
     }  
     rewrite ^/pay/(.*)$ /pay.php?s=$1 last;  
    }  
    location ^~ /plugins {  
      deny all;  
    }  
    location ^~ /includes {  
      deny all;  
    }
[/code]

[![image.png](https://heaid.top/usr/uploads/2021/08/756057888.png)](https://heaid.top/usr/uploads/2021/08/756057888.png)

[![image.png](https://heaid.top/usr/uploads/2021/08/3027198238.png)](https://heaid.top/usr/uploads/2021/08/3027198238.png)

成功安装，如需重新安装，请手动删除install目录下install.lock文件！

上传V免签插件。

[![image.png](https://heaid.top/usr/uploads/2021/08/2325241839.png)](https://heaid.top/usr/uploads/2021/08/2325241839.png)

[![image.png](https://heaid.top/usr/uploads/2021/08/3800498719.png)](https://heaid.top/usr/uploads/2021/08/3800498719.png)

配置好V免签密钥~！

 

创建好商户直接对接即可。

 

# 源码下载~！

[限时免费~！易支付源码，内涵最新监控端](https://blog.lvuy.xyz/wp-content/uploads/2022/04/%E5%B7%B2%E5%AE%89%E8%A3%85v%E5%85%8D%E7%AD%BE%E5%BD%A9%E8%99%B9%E6%98%93%E6%94%AF%E4%BB%98.zip)

## sspanel-metron对接易支付插件 自行去TG群下载
