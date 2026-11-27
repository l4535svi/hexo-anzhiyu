---
title: Cloudflare免费申请使用15年有效期的SSL自签证书，支持泛域名，实现全站https访问
date: '2025-03-06 12:00:00'
cover: /img/covers/cloudflare15sslhttps.jpg
tags:
- 免费域名
categories:
- 免费域名
description: 目前最常用的免费证书是 Let’s Encrypt，但是它的有效期只有 90 天，到期需要手动更新。 不过也有很多工具可以自动更新续期，例如： 宝塔面板 certbot Nginx Proxy Manager nginxWebUI 等… 现在我部分域名使用 Cloudflare（
---
[code]
    目前最常用的免费证书是 Let’s Encrypt，但是它的有效期只有 90 天，到期需要手动更新。  
      
    不过也有很多工具可以自动更新续期，例如：  
      
    宝塔面板  
    certbot  
    Nginx Proxy Manager  
    nginxWebUI  
    等…  
    现在我部分域名使用 Cloudflare（以下简称 CF） 进行托管，而 CF 可以免费申请长达 15年 有效期的 SSL 证书，所以今天给大家分享一下申请方式。  
      
    即使申请的证书是 15年，也是内部有效时间。就是指 CF 的自签证书（理论上可以自签50年、100年都可以）。对外，即客户层面看到的证书，还是 CF 帮我们自动申请的 Let’s Encrypt 的 E1证书；  
      
    所以必须搭配 Cloudflare 的 CDN 使用；（也就是需要开启“小云朵”）；  
      
    开启 CDN 后，国内访问速度可能会变慢；  
      
    申请步骤  
    登录 CF，域名需要托管到 CF 上面  
      
    点击要申请的 SSL 的网站  
      
      
      
    点击左侧菜单”SSL/TLS“下面的”概述“，将 SSL/TLS 加密模式设置为”完全“或者”完全（严格）“  
      
      
      
    点击左侧菜单”SSL/TLS“下面的”源服务器“，选择”创建证书“  
      
      
      
    选择”私钥类型“，填写”主机名“，选择证书有效期，然后”创建“  
      
      
      
    然后会生成”源证书“（pem）和”私钥“（key），这里的 ”私钥“（key） 只出现一次，切记复制保存，切记复制保存，切记复制保存，然后点击”确认“即可  
      
      
      
    如果 ”源证书“（pem）忘记了，可以点击”下载“查看，之后就可以在你服务器/VPS上配置这个证书了。  
      
      
      
    配置 DNS 解析时一定要开启”小云朵“，否则网站会提示”不能验证该证书“  
      
      
      
    其他  
    可以设置”始终使用 HTTPS“和"HTTP 严格传输安全 (HSTS)"策略  
      
      
      
    如果想换证书，直接“吊销”，重新申请即可！！！  
      
    个人使用 Let’s Encrypt 申请的证书是 R3 级别的，CF 帮我们申请的证书是 E1 级别的，它们都是免费的 SSL 证书，具有相同的加密强度。  
      
    主要区别在于颁发机构、支持的域名数量、有效期和自动续订。Let’s Encrypt R3证书需要手动续订，而Cloudflare E1证书会自动续订。Let’s Encrypt R3证书适用于个人网站、博客和小型企业网站，而Cloudflare E1证书适用于中小型企业网站和电子商务网站。  
    
[/code]
