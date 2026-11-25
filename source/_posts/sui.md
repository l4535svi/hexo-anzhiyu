---
title: 零基础新手节点搭建教程、S‐UI面板自建上网节点、包含多协议应有尽有、一次学会
date: '2025-11-19 12:00:00'
cover: https://picsum.photos/seed/sui/800/450
tags:
- 节点搭建
categories:
- 节点搭建
description: 'SSH连接工具 任选其中一个即可 FinalShell(推荐): FinalShell下载 MobaXterm: MobaXterm官网 S-UI面板+节点部署 1、必要更新操作(Debian/Ubuntu) apt update -y && apt install -y cur'
---
# SSH连接工具

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#ssh%E8%BF%9E%E6%8E%A5%E5%B7%A5%E5%85%B7)

任选其中一个即可  
FinalShell(推荐):[FinalShell下载](http://www.hostbuf.com/t/988.html)  
MobaXterm:[MobaXterm官网](https://mobaxterm.mobatek.net/)

# S-UI面板+节点部署

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#s-ui%E9%9D%A2%E6%9D%BF%E8%8A%82%E7%82%B9%E9%83%A8%E7%BD%B2)

### 1、必要更新操作(Debian/Ubuntu)

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#1%E5%BF%85%E8%A6%81%E6%9B%B4%E6%96%B0%E6%93%8D%E4%BD%9Cdebianubuntu)
[code]
    apt update -y && apt install -y curl socat wget
[/code]

**注意：**如果是centos系统，则运行yum update -y && yum install -y curl socat wget

### 2、安装S-UI

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#2%E5%AE%89%E8%A3%85s-ui)

感谢alireza0大佬开发如此好用的安装脚本
[code]
    VERSION=1.3.6 && bash <(curl -Ls https://raw.githubusercontent.com/alireza0/s-ui/$VERSION/install.sh) $VERSION
[/code]

### 3、挑选SNI伪装域名（任选一个）

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#3%E6%8C%91%E9%80%89sni%E4%BC%AA%E8%A3%85%E5%9F%9F%E5%90%8D%E4%BB%BB%E9%80%89%E4%B8%80%E4%B8%AA)
[code]
    如发现节点不能使用，或延迟显示-1，以下域名请随机挑选用于SNI，直到正常使用即可，或者直接照抄视频中一模一样的域名填写，确保可用
    aws.com
    bing.com
    snap.licdn.com
    devblogs.microsoft.com
    cdn.bizibly.com
    www.apple.com
    ts1.tc.mm.bing.net
    fpinit.itunes.apple.com
    go.microsoft.com
    catalog.gamepass.com
    gray-config-prod.api.arc-cdn.net
    apps.mzstatic.com
    tag.demandbase.com
    r.bing.com
    tag-logger.demandbase.com
    cdn-dynmedia-1.microsoft.com
    services.digitaleast.mobi
    gray.video-player.arcpublishing.com
    azure.microsoft.com
    beacon.gtv-pub.com
    amd.com
    
[/code]

# 面板管理、BBR加速

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#%E9%9D%A2%E6%9D%BF%E7%AE%A1%E7%90%86bbr%E5%8A%A0%E9%80%9F)

安装完成后，输入 s-ui 就能看到管理面板，如下图片所示，可以重新查看面板信息  
![image](https://private-user-images.githubusercontent.com/134616948/494049676-a45cc734-a388-4690-99e3-e2eef30fad91.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjM1MjMzNDAsIm5iZiI6MTc2MzUyMzA0MCwicGF0aCI6Ii8xMzQ2MTY5NDgvNDk0MDQ5Njc2LWE0NWNjNzM0LWEzODgtNDY5MC05OWUzLWUyZWVmMzBmYWQ5MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTExOVQwMzMwNDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wM2NhOTZiYjlhNTU3NmVhMDE2ZDM3YTkyNmY4NTdkODgwN2FlMTZkODZlZDI4ODUzNTkyNzNlYzk2NWI0Y2I0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.mOp58MJi5w5qhWBrRj1THh9mGZdhfP3JO4eu7IJT-88)  

重新获取SUI后台访问地址，可输入s-ui运行，再次输入10运行，查看面板参数来确定面板后台地址、管理员登录信息：  
![image](https://private-user-images.githubusercontent.com/134616948/494050360-90637ad1-d958-4253-97e8-76247919b744.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjM1MjMzNDAsIm5iZiI6MTc2MzUyMzA0MCwicGF0aCI6Ii8xMzQ2MTY5NDgvNDk0MDUwMzYwLTkwNjM3YWQxLWQ5NTgtNDI1My05N2U4LTc2MjQ3OTE5Yjc0NC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTExOVQwMzMwNDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMzZlODM1YTAzMDVjNGE4ZDlkMmM4ZDQ0Njc4OGMwNDRmNjYxNmY2OGEwYmQ5ZTE2ZmVhMzlmNWI3ODcyMDIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.8RgHo0f7CEQBQ-CLPpdmsQWMuVbpUnamaxoxCWFFKxA)

### BBR加速

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#bbr%E5%8A%A0%E9%80%9F)

输入s-ui运行，输入18运行，输入1运行，开启BBR加速，显著提升速度 ![image](https://private-user-images.githubusercontent.com/134616948/494051535-bf384751-b586-4688-bae8-9731aa4c48bb.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjM1MjMzNDAsIm5iZiI6MTc2MzUyMzA0MCwicGF0aCI6Ii8xMzQ2MTY5NDgvNDk0MDUxNTM1LWJmMzg0NzUxLWI1ODYtNDY4OC1iYWU4LTk3MzFhYTRjNDhiYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTExOVQwMzMwNDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNWM1ZmY0Yzk3NDI5NWQxOTlmZjcxMDBhODlhMDY4ZTk2ZWRiNWRmMmU1OWFmNDYzZTE3ZTk0ZjA2MmI4NGUzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.tmfx9VstsrZosH09GEF-7fhKY1ho4OuQUmXJqVrZ320)

# 各平台客户端下载

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#%E5%90%84%E5%B9%B3%E5%8F%B0%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%B8%8B%E8%BD%BD)

[V2Ray官网对于全平台客户端的总结和一览](https://www.v2ray.com/awesome/tools.html)  

Windows、MacBook：[v2rayN下载](https://github.com/2dust/v2rayN/releases/tag/7.14.12)  
**[解压软件winrar](https://www.winrar.com.cn/)  

MacBook打开软件提示损坏解决方法：[MacBook打开软件提示损坏解决方法](https://zhuanlan.zhihu.com/p/135948430)  
MacBook打开软件提示无法验证软件安全性：[MacBook打开软件提示无法验证安全性解决方法](https://zhuanlan.zhihu.com/p/489710134)  

苹果IOS、iPad、M芯片MacBook：App Store中，登录非国区账号，安装Shadowrocket小火箭（推荐，协议支持全面、便宜）  
不管是iPad平板还是iPhone手机，比较推荐的科学上网软件必定是：Shadowrocket，但是需要注册一个非国区或美区账号才能进行购买，目前是2.99美刀约20块人民币，注册美区账号和充值购买也非常简单，请参考以下两篇文章。  
如何注册美区Apple ID:<https://zhuanlan.zhihu.com/p/30761252365>  
美区账号如何充值：<https://zhuanlan.zhihu.com/p/636121931>  
注册美区ID并按以上方法充值后，在App Store中搜索Shadowrocket购买并下载安装  

安卓/Android：[NekoBox下载](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.0)  

# 结尾

[](https://github.com/xiaochaib/chaiwiki/wiki/%E9%9B%B6%E5%9F%BA%E7%A1%80%E6%96%B0%E6%89%8B%E8%8A%82%E7%82%B9%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B%E3%80%81S%E2%80%90UI%E9%9D%A2%E6%9D%BF%E8%87%AA%E5%BB%BA%E4%B8%8A%E7%BD%91%E8%8A%82%E7%82%B9%E3%80%81%E5%8C%85%E5%90%AB%E5%A4%9A%E5%8D%8F%E8%AE%AE%E5%BA%94%E6%9C%89%E5%B0%BD%E6%9C%89%E3%80%81%E4%B8%80%E6%AC%A1%E5%AD%A6%E4%BC%9A#%E7%BB%93%E5%B0%BE)

一郑重声明：请合理使用科学上网于学习知识、外贸或科研工作方面，遵守当地相关规定  
搬瓦工30天内新账户支持退款，请按以下操作，refunds，按提示交工单，不懂英文的请打开浏览器翻译  
![image](https://private-user-images.githubusercontent.com/134616948/242801612-3f77af08-23ed-4a7d-809e-651bfa5537d9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjM1MjMzNDAsIm5iZiI6MTc2MzUyMzA0MCwicGF0aCI6Ii8xMzQ2MTY5NDgvMjQyODAxNjEyLTNmNzdhZjA4LTIzZWQtNGE3ZC04MDllLTY1MWJmYTU1MzdkOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTExOVQwMzMwNDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NmE0ZThjNWQ3ZDgyZTJhYjc3ZjFmNjQ0ZjliNmM4Y2IzNjA2YTYwMjM4NTM1OTUwMWFhNDNmN2M3Y2FlNjVlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.vIxodPCkqn_FLgRrxI8_4u9pKm0G4SU8ghJdPo9IJBY)
