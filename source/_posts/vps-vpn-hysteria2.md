---
title: 最便宜vps 最快协议 搭建vpn节点 Hysteria2 抢占宽带 拯救垃圾线路 提升上网速度
date: '2025-04-02 12:00:00'
tags:
- VPS
categories:
- VPS
description: 最便宜vps 最快协议 搭建vpn节点 Hysteria2 抢占宽带 拯救垃圾线路 提升上网速度 🕓2024年10月24日 本文介绍如何在vps上搭建Hysteria2协议的vpn. Hysteria2与vmess, vless相比, 传输速度大幅提升, 它是一款基于HTTP/1
---
# 最便宜vps 最快协议 搭建vpn节点 Hysteria2 抢占宽带 拯救垃圾线路 提升上网速度

🕓2024年10月24日

本文介绍如何在vps上搭建Hysteria2协议的vpn.  
Hysteria2与vmess, vless相比, 传输速度大幅提升, 它是一款基于HTTP/1.3 QUIC魔改的翻墙协议，底层是用UDP协议进行数据传输，能够在网络拥堵、丢包等恶劣环境中提升科学上网体验。  
Hysteria2与Hysteria1相比，大幅提升了稳定性，支持nginx反代伪装，预防GFW的主动探测，有效减少被封的概率。  
本文演示用的主机是RackNerd的vps, 笔者认为它是目前全宇宙最具性价比的vps, $10.99美元/年, 流量3000G/月. 当然, 你也可以使用其他品牌的vps进行操作.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvRwdoucpPhxkv6uEOZaNjXRkduQbrUww2bo1ThlgfYlcNm6E0VAq3nKW_iSFNbTBgJ86tuC8ys5EdXO1QRjbusIpoWfSDguInhg1S6VvsbnTneErnFBJbJg4D59DgZm3VnaMAuJEn4c05c45BdUzIa6l0OeTXrIIjy5RpL-g_H0Q9FyUeuUcR1aFdVlFF/w640-h360/%E6%9C%80%E4%BE%BF%E5%AE%9Cvps%20%E6%9C%80%E5%BF%AB%E5%8D%8F%E8%AE%AE%20%E6%90%AD%E5%BB%BAvpn%E8%8A%82%E7%82%B9%20Hysteria2%20%E6%8A%A2%E5%8D%A0%E5%AE%BD%E5%B8%A6%20%E6%8B%AF%E6%95%91%E5%9E%83%E5%9C%BE%E7%BA%BF%E8%B7%AF%20%E6%8F%90%E5%8D%87%E4%B8%8A%E7%BD%91%E9%80%9F%E5%BA%A6.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvRwdoucpPhxkv6uEOZaNjXRkduQbrUww2bo1ThlgfYlcNm6E0VAq3nKW_iSFNbTBgJ86tuC8ys5EdXO1QRjbusIpoWfSDguInhg1S6VvsbnTneErnFBJbJg4D59DgZm3VnaMAuJEn4c05c45BdUzIa6l0OeTXrIIjy5RpL-g_H0Q9FyUeuUcR1aFdVlFF/s1280/%E6%9C%80%E4%BE%BF%E5%AE%9Cvps%20%E6%9C%80%E5%BF%AB%E5%8D%8F%E8%AE%AE%20%E6%90%AD%E5%BB%BAvpn%E8%8A%82%E7%82%B9%20Hysteria2%20%E6%8A%A2%E5%8D%A0%E5%AE%BD%E5%B8%A6%20%E6%8B%AF%E6%95%91%E5%9E%83%E5%9C%BE%E7%BA%BF%E8%B7%AF%20%E6%8F%90%E5%8D%87%E4%B8%8A%E7%BD%91%E9%80%9F%E5%BA%A6.jpg)

  

  

**一、准备工作**

1、一台境外VPS  
我使用的vps是 RackNerd的, 操作系统 Ubuntu

RackNerd 购买地址：优惠码15OFFDEDI  
[点我购买>>](https://bit.ly/3YDpRSR)

(2024年最新的万圣节活动, 我购买的时候, 视频制作时, 还没有这个套餐)  
内存 1G, 固态硬盘 17G, 流量 3000G/月, 带宽1000Gbps  
价格 $10.98/年, 续费同价, [更多套餐>>](https://afeinet.blogspot.com/2024/10/22.html)

## vps精选

最新 2024 万圣节活动 特惠款 10月23日发售

内存| CPU| SSD| 流量| 价格| 购买网址| 备注  
---|---|---|---|---|---|---  
1.0 G| 1核| 17G| 3T/月| $10.98/年| [链接](https://bit.ly/3YDpRSR)| 最新特惠  
~~1.5 G~~| ~~1核~~| ~~25G~~| ~~**4T** /月~~| ~~$16.88/年~~| ~~[链接](https://cutt.ly/ueFXBseX)~~|  售罄  
~~10月31日 加推  
**洛杉矶 DC2** 机房  
重点推荐 速度快~~  
~~2.5 G~~| ~~2核~~| ~~38G~~| ~~**6T** /月~~| ~~$23.88/年~~| ~~[链接](https://cutt.ly/oeFVhKEI)~~|  售罄  
~~10月31日 加推  
**洛杉矶 DC2** 机房  
重点推荐 速度快~~  
  
2024 黑色星期五 促销

VPS套餐，美国圣何塞、西雅图、达拉斯、芝加哥、纽约、亚特兰大机房可选，1G内存以上套餐还另外可选洛杉矶DC-02机房，全部1个IPv4，1Gbps带宽，KVM虚拟化，优惠码`15OFFDEDI`.

阿飞建议: 移动,联通,广电宽带的用户一定要选洛杉矶DC-02机房.

CPU| 内存| 硬盘| 流量| 价格| 购买地址  
---|---|---|---|---|---  
1核| 1G| 20GB SSD| 1.5TB| 10.99美元/年| [点此购买](https://bit.ly/3ZucB3A)  
2核| 2.5G| 40GB SSD| 3TB| 18.93美元/年| [点此购买](https://bit.ly/4gfp7cv)  
2核| 3G| 60GB SSD| 5.5TB| 27.89美元/年| [点此购买](https://bit.ly/49exd32)  
3核| 4.5G| 100GB SSD| 8.5TB| 39.88美元/年| [点此购买](https://bit.ly/3OyqN5b)  
4核| 5G| 130GB SSD| 12TB| 55.93美元/年| [点此购买](https://bit.ly/49ivmtR)  
  
RackNerd官网 [点我前往>>](https://bit.ly/4fjgUnl)

当然, 你也可以使用其他品牌的vps进行操作.

2、下载并安装FinalShell SSH工具  
Windows X64版,下载地址:  
[点我下载](https://pan.quark.cn/s/17448b767b97)

macOS Arm版,支持m1,m2,m3 cpu,下载地址:  
[点我下载](https://pan.quark.cn/s/424b0411592b)

macOS X64版,支持旧款intel cpu,下载地址:  
[点我下载](https://pan.quark.cn/s/5eb21d7b25de)

当然, 你也可以使用其他SSH连接工具进行操作.

**二、搭建步骤**

1.系统组件升级至最新：
[code]
    apt update -y && apt install -y curl && apt install -y socat
    
[/code]

2.Hysteria 2 一键安装脚本
[code]
    wget -N --no-check-certificate https://raw.githubusercontent.com/flame1ce/hysteria2-install/main/hysteria2-install-main/hy2/hysteria.sh && bash hysteria.sh
    
[/code]

3.查看 hysteria 服务 状态
[code]
    systemctl status hysteria-server.service
    
[/code]

4.启动 hysteria 服务
[code]
    systemctl start hysteria-server.service
    
[/code]

5.设置 hysteria 服务 开机自启
[code]
    systemctl enable hysteria-server.service
    
[/code]

6.其他常用命令  
停止 hysteria 服务
[code]
    systemctl stop hysteria-server.service
    
[/code]

重启 hysteria 服务
[code]
    systemctl restart hysteria-server.service
    
[/code]

**三、开放端口**

节点如果不能正常使用，请先放行端口，  
将下面的命令复制, 粘贴后敲回车.  
注意: 80和443一定要开放, 另外, 再将 xxx 改为你自己的hysterial监听端口。
[code]
    iptables -I INPUT -p tcp --dport 80 -j ACCEPT
    iptables -I INPUT -p tcp --dport 443 -j ACCEPTiptables -I INPUT -p tcp --dport xxx -j ACCEPT
[/code]

开放所有端口
[code]
    ufw disable
    
[/code]

**四、客户端配置**

1、**Windows**  建议使用 V2rayN

**国内下载:**

V2ray 6.60版  
下载 "宝箱"：  
<https://pan.quark.cn/s/8641a1edfdb3>  
下载 "钥匙"：  
<https://pan.quark.cn/s/62d3e80719c4>

使用方法：  
1.把"钥匙"复制到"宝箱"的文件夹的内部, 使得所有文件放在同一个文件夹内;  
2.双击"afei", 获得宝物.  

**国外下载:  ** 若你在国外, 也可在其官网自行下载

2、**IOS/MAC**  建议使用 Shadowrocket($2.99) 或 Karing(免费)需要使用美区 AppleID 登录 App Store 下载，如果没有美区ID，可以点击免费申请一个  
Karing安装及使用教程: [点我观看>>](https://youtu.be/6aDXg0rM6bw)

3、**安卓手机**  建议使用 Hiddify或者 Karing  
Karing 国内下载: [点击下载>>](https://pan.quark.cn/s/60fa8d7253a7)  
Hiddify 国内下载: [点击下载>>](https://github.com/2dust/v2rayN/releases/latest)  
当然, 若你在国外, 也可以在 Google Play 商店或其官网自行下载  
Karing安装及使用教程: [点我观看>>](https://youtu.be/6aDXg0rM6bw)

**五、参考网站**

项目地址：<https://v2.hysteria.network/zh/>  
项目github地址：<https://github.com/apernet/hysteria>

**六、常见问题**

1、搭建的账号之前能用，突然不能用了，怎么解决？

A.如果ip不能ping通，FinalShell不能直接连接vps服务器，说明ip被墙了，需要换ip。进入后台, 点击 chang Ip, 填写表单即可. 建议在美国工作日时间提交, 很快就可以更换IP. 注意, 购买后,前3天免费更换, 过期后$3美元/次.  
B.如果ip正常，大概率是端口号被封了，换端口号，重新搭建。

2、需要安装bbr加速吗？

不需要。bbr加速是tcp加速，而hysteria是Quic(udp)协议。所以不用再部署bbr加速。
