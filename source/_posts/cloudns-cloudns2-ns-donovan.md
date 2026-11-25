---
title: cloudns-cloudns2-ns-donovan
date: '2025-03-05 12:00:00'
tags:
- 免费域名
categories:
- 免费域名
description: 三步玩转cloudns双向域名托管，泛域名解析，双向解析 第一步：申请域名并托管 cloudns侧，2条记录： 空 NS donovan.ns.cloudflare.com 空 NS nucum.ns.cloudflare.com 第二步:解析证书 cloudns侧，2条记录：
---
# 三步玩转cloudns双向域名托管，泛域名解析，双向解析

[](https://www.youtube.com/@Univzeros)

 

  

  

第一步：申请域名并托管

cloudns侧，2条记录： 空 NS donovan.ns.cloudflare.com 空 NS nucum.ns.cloudflare.com 第二步:解析证书 cloudns侧，2条记录： _acme-challenge NS donovan.ns.cloudflare.com _acme-challenge NS nucum.ns.cloudflare.com 第三步：泛域名解析 cloudflare 侧，1条记录： dns(可随便写，与cloudns侧响应保持一致即可) A 任意地址（比如114.114.114.114） cloudns侧，3条记录： dns NS donovan.ns.cloudflare.com dns NS nucum.ns.cloudflare.com 

  * CNAME dns.xxxx.ddns-ip.net

https://www.youtube.com/watch?v=8yQ_8z1RNSk&t=376s[](https://www.youtube.com/@Univzeros)
