---
title: 终级教程 零成本部署VLESS、Trojan免费节点 | 二合一 | 一键部署生成两协议订阅节点
date: '2025-06-01 12:00:00'
cover: https://picsum.photos/seed/vlesstrojan/800/450
tags:
- 科学上网
categories:
- 科学上网
description: 《部署教程说明》 通过Cloudflare零成本部署 VLESS/Trojan 免费节点！一键部署永久免部署( 解决修改或设置变量自动部署出现1101错误问题 ),最新版本可以实现 VLESS/Trojan合成一套部署生成两类型节点 、 0变量设置 、 解决IP跳动 、并可以 优
---
《部署教程说明》

通过Cloudflare零成本部署VLESS/Trojan免费节点！一键部署永久免部署(解决修改或设置变量自动部署出现1101错误问题),最新版本可以实现VLESS/Trojan合成一套部署生成两类型节点、0变量设置、解决IP跳动、并可以优选IP区域指定优选反代IP区域实现固定优选IP的落地IP,实现解锁ChatGPT、Netflix、TikTok等网站，还能轻松观看4K视频，永久免费。教程简单易懂，适合所有人，赶紧上手试试吧！

[【YouTube频道】 | ](https://youtube.com/@am_clubs?sub_confirmation=1)[【Telegram频道】 | ](https://t.me/am_clubs)[【GitHub仓库】](https://github.com/amclubs)

> 💡优势：无限流量,再也不用担心流量不够用,全免费不用VPS就可以部署。

  * VLESS/Trojan二合一节点项目地址：<https://github.com/amclubs/am-cf-tunnel>

## 一、需要准备的前提资料

### 1、注册免费cloudflare帐号(邮箱就可以免费注册)

  * 注册地址：[https://cloudflare.com](https://cloudflare.com/) [[点击观看视频教程]](https://youtu.be/ITeuSbHVQ2E)

### 2、注册免费域名 [点击观看所有免费域名视频教程](https://www.youtube.com/playlist?list=PLGVQi7TjHKXZGODTvB8DEervrmHANQ1AR)

### 3、订阅工具 [点击观看使用视频教程](https://youtu.be/xGOL57cmvaw)

👉 [点击加入TG群 AM科技｜分享交流群](https://t.me/AM_CLUBS)发送关键字 工具 获取下载

### 4、Cloudflare标准 端口 知识 [点击观看优选IP视频教程](https://youtu.be/pKrlfRRB0gU)

  * 80系端口(HTTP)：80，8080，8880，2052，2082，2086，2095
  * 443系端口(HTTPS)：443，2053，2083，2087，2096，8443
  * [IP落地测试工具地址](https://ip.sb/)

## 二、开始部署Cloudflare免费节点

### 一、Workers 部署方法 [视频教程](https://www.youtube.com/watch?v=dPH63nITA0M&t=151s)

点击展开/收起

  1.      *      * [](https://github.com/amclubs/am-cf-tunnel/blob/main/_worker.js)
  2. [](https://www.youtube.com/playlist?list=PLGVQi7TjHKXZGODTvB8DEervrmHANQ1AR)
     * ````````
     * [](https://amclubss.com/)````
  3.      * ``````````
     * ``````````````
  4.      * ``
     * ``
     * ``
     * ``
     * ``
     * ``
  5.      * ``
     * ``[](https://1024tools.com/uuid)``
     * ``

### 二、Pages 上传 部署方法 最佳推荐!!! [视频教程](https://www.youtube.com/watch?v=dPH63nITA0M&t=476s)

点击展开/收起

  1.      * [](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/_worker.js.zip)
     * ````[](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/_worker.js.zip)``
  2. [](https://youtu.be/wHJ6TJiCF0s)[](https://youtu.be/yEF1YoLVmig)[](https://www.youtube.com/watch?v=XS0EgqckUKo&t=320s)
     * ````
     *   
``````
  3.      * ``````````
     * ``````````````
     * ````[](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/_worker.js.zip)``
  4.      * ``
     * ``
     * ``
     * ``
     * ``
     * ``
  5.      * ``
     * ``[](https://1024tools.com/uuid)``
     * ``

### 三、Pages GitHub 部署方法 [视频教程](https://www.youtube.com/watch?v=dPH63nITA0M&t=654s)

点击展开/收起

  1.      *      * ``````
     * ````
  2. [](https://youtu.be/wHJ6TJiCF0s)[](https://youtu.be/yEF1YoLVmig)[](https://www.youtube.com/watch?v=XS0EgqckUKo&t=320s)
     * ````
     *   
``````
  3.      * ``````````
     * ``````````````
     * ``````
  4.      * ``
     * ``
     * ``
     * ``
     * ``
     * ``
  5.      * ``
     * ``[](https://1024tools.com/uuid)``
     * ``

## 四、变量说明 [视频教程](https://www.youtube.com/watch?v=ag12Rpc9KP4&t=739s)

变量名| 示例| 必填| 备注| YT  
---|---|---|---|---  
UUID| d0298536-d670-4045-bbb1-ddd5ea68683e（默认）| ✅| 支持Cloudflare的KV存储桶设置 [在线获取UUID](https://1024tools.com/uuid) 如果是Trojan节点的变量是：PASSWORD|   
PROT_TYPE| 输认空| ❌| 默认空,就是生成vless和trojan节点，vless(只生成vless节点)，trojan(只生成trojan节点)|   
IP_URL| [https://raw.github…/ipUrl.txt](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/ipUrl.txt)| ❌| （推荐）优选(ipv4、ipv6、域名、API)地址(支持多个之间`,`或 换行 作间隔)，支持文件连接后里带PROXYIP参数，可以实现不同区域优先IP使用不同的PROXYIP固定区域，解决IP乱跳问题| [教程](https://www.youtube.com/watch?v=4fcyJjstFdg&t=349s)  
IP_URL_TXT| [https://raw.github…/ipv4.txt](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/ipv4.txt)| ❌| （不推荐）优选ipv4、ipv6、域名、API地址(支持多个之间`,`或 换行 作间隔)| [教程](https://youtu.be/dzxezRV1v-o) [教程](https://youtu.be/vX3U3FuuTT8)  
IP_URL_CSV| [https://raw.github…/ipv4.csv](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/ipv4.csv)| ❌| （不推荐）优选ipv4/6的IP测速结果(支持多元素, 元素之间使用`,`作间隔)| [教程](https://youtu.be/vX3U3FuuTT8)  
IP_LOCAL| `icook.hk:2053#官方优选域名`| ❌| （不推荐）本地优选域名/优选IP(支持多元素之间`,`或 换行 作间隔)|   
PROXYIP| [proxyip.amclubs.kozow.com](http://proxyip.amclubs.kozow.com/)  
或  
[https://raw.github…/proxyip.txt](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/proxyip.txt)| ❌| 访问CloudFlare的CDN代理节点(支持多PROXYIP, PROXYIP之间使用`,`或 换行 作间隔),支持端口设置默认443 如: [proxyip.amclubs.kozow.com:2053](http://proxyip.amclubs.kozow.com:2053/) ，支持远程txt或csv文件| [教程](https://youtu.be/pKrlfRRB0gU)  
SOCKS5| user:password@127.0.0.1:1080| ❌| 优先作为访问CFCDN站点的SOCKS5代理| [教程](https://youtu.be/Bw82BH_ecC4)  
DNS_RESOLVER_URL| <https://cloudflare-dns.com/dns-query>| ❌| DNS解析获取作用，小白勿用|   
NO_TLS| true/false| ❌| 默认false,是否开启TLS系列端口，只有workers部署才可以使非用TLS系列端口|   
SL| 5| ❌| `CSV`文件里的测速结果满足速度下限|   
SUB_CONFIG| [https://raw.github…/ACL4SSR_Online_Mini.ini](https://raw.githubusercontent.com/amclubs/ACL4SSR/main/Clash/config/ACL4SSR_Online_Full_MultiMode.ini)| ❌| clash、singbox等 订阅转换配置文件|   
SUB_CONVERTER| [url.v1.mk](http://url.v1.mk/)| ❌| clash、singbox等 订阅转换后端的api地址|   
SUB_NAME| AM科技| ❌| 订阅名称|   
CF_EMAIL| [test@gmail.com](mailto:test@gmail.com)| ❌| CF账户邮箱(要和`CF_KEY`同时填才生效, 订阅信息将显示请求使用量, 小白别用)|   
CF_KEY| c6a944b5c9c18c235288bced8b85e| ❌| CF账户Global API Key(要和`CF_EMAIL`同时填才生效, 订阅信息将显示请求使用量, 小白别用)|   
TG_TOKEN| 6823456:XXXXXXX0qExVUhHDAbXXXqWXgBA| ❌| 发送TG通知的机器人token|   
TG_ID| 6946912345| ❌| 接收TG通知的账户数字ID|   
  
## 五、已适配订阅工具 [点击进入视频教程](https://youtu.be/xGOL57cmvaw) [点进进入karing视频教程](https://youtu.be/M3vLLBWfuFg)

  * Mac（苹果电脑）

    * [v2rayU](https://github.com/yanue/V2rayU/releases) | [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev/releases) | [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620) | [小火箭](https://apps.apple.com/us/app/shadowrocket/id932747118) | [surge](https://apps.apple.com/us/app/surge-5/id1442620678) | [karing](https://karing.app/download) | [sing-box](https://github.com/SagerNet/sing-box/releases) | [Clash Nyanpasu](https://github.com/keiko233/clash-nyanpasu/releases) | [openclash](https://github.com/vernesong/OpenClash/releases) | [Hiddify](https://github.com/hiddify/hiddify-next/releases)
  * Win（win系统电脑）

    * [v2rayN](https://github.com/2dust/v2rayN/releases) | [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev/releases) | [sing-box](https://github.com/SagerNet/sing-box/releases) | [Clash Nyanpasu](https://github.com/keiko233/clash-nyanpasu/releases) | [openclash](https://github.com/vernesong/OpenClash/releases) | [karing](https://karing.app/download) | [Hiddify](https://github.com/hiddify/hiddify-next/releases)
  * IOS（苹果手机）

    * [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev/releases) | [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620) | [小火箭](https://apps.apple.com/us/app/shadowrocket/id932747118) | [surge](https://apps.apple.com/us/app/surge-5/id1442620678) | [sing-box](https://github.com/SagerNet/sing-box/releases) | [Clash Nyanpasu](https://github.com/keiko233/clash-nyanpasu/releases) | [karing](https://karing.app/download) | [Hiddify](https://github.com/hiddify/hiddify-next/releases)
  * Android（安卓手机）

    * [v2rayNG](https://github.com/2dust/v2rayNG/releases) | [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev/releases) | [sing-box](https://github.com/SagerNet/sing-box/releases) | [Clash Nyanpasu](https://github.com/keiko233/clash-nyanpasu/releases) | [karing](https://karing.app/download) | [Hiddify](https://github.com/hiddify/hiddify-next/releases)
