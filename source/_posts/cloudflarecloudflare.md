---
title: 【保姆教程】Cloudflare自家域名也能做节点？教你优选Cloudflare自家域名变成节点
date: '2024-10-20 12:00:00'
cover: https://picsum.photos/seed/cloudflarecloudflare/800/450
tags:
- 节点分享
categories:
- 节点分享
description: 如何将Cloudflare自家域名转变为高效节点。无论你是新手还是有经验的用户，这个教程将提供简单易懂的步骤，帮助你优化网络资源，提升访问速度,并有无限节点使用。 《部署教程说明》 VLESS免费节点部署项目地址： https://github.com/amclubs/am-cf
---
如何将Cloudflare自家域名转变为高效节点。无论你是新手还是有经验的用户，这个教程将提供简单易懂的步骤，帮助你优化网络资源，提升访问速度,并有无限节点使用。

《部署教程说明》VLESS免费节点部署项目地址：<https://github.com/amclubs/am-cf-tunnel>

Trojan免费节点部署项目地址：<https://github.com/amclubs/am-cf-trojan>

## [](https://am.809098.xyz/am-cf-domain/#%E4%B8%80%E3%80%81%E9%9C%80%E8%A6%81%E5%87%86%E5%A4%87%E7%9A%84%E5%89%8D%E6%8F%90%E8%B5%84%E6%96%99 "一、需要准备的前提资料")一、需要准备的前提资料

### [](https://am.809098.xyz/am-cf-domain/#1%E3%80%81%E6%B3%A8%E5%86%8C%E5%85%8D%E8%B4%B9cloudflare%E5%B8%90%E5%8F%B7-%E9%82%AE%E7%AE%B1%E5%B0%B1%E5%8F%AF%E4%BB%A5%E5%85%8D%E8%B4%B9%E6%B3%A8%E5%86%8C "1、注册免费cloudflare帐号\(邮箱就可以免费注册\)")1、注册免费cloudflare帐号(邮箱就可以免费注册)

  * 注册地址：[https://cloudflare.com](https://cloudflare.com/)  
[[点击观看视频教程]](https://youtu.be/ITeuSbHVQ2E)

### [](https://am.809098.xyz/am-cf-domain/#2%E3%80%81%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B "2、免费节点部署教程")2、免费节点部署教程

  * [【【VLESS免费节点】教程](https://youtu.be/dPH63nITA0M)
  * [【【Trojan免费节点】教程](https://youtu.be/uh27CVVi6HA)

### [](https://am.809098.xyz/am-cf-domain/#3%E3%80%81%E6%B3%A8%E5%86%8C%E5%85%8D%E8%B4%B9%E5%9F%9F%E5%90%8D%EF%BC%88%E5%8F%AF%E9%80%89%EF%BC%89 "3、注册免费域名（可选）")3、注册免费域名（可选）

  * [【us.kg域名免费申请】](https://youtu.be/cI36vtXuQrM)
  * [【YDNS域名免费申请】](https://youtu.be/Na92q5QE1Yo)
  * [【dynv6域名免费申请】](https://youtu.be/Nl0BV2ocYb8)
  * [【l53域名免费申请】](https://youtu.be/-LpostXqKRo)
  * [【cloudns域名免费申请】](https://youtu.be/oi8OgTOZLug)
  * [【nyc.mn域名免费申请】](https://youtu.be/Op5MjevsO3w)
  * [【obl.org域名免费申请】](https://youtu.be/IRx6UVRNA2E)
  * [【dnsexit域名免费申请】](https://youtu.be/mha-ec8GTxE)

### [](https://am.809098.xyz/am-cf-domain/#4%E3%80%81%E4%B8%8B%E8%BD%BD-pinginfoview%E5%B7%A5%E5%85%B7 "4、下载 pinginfoview工具")4、下载 [pinginfoview](https://www.nirsoft.net/utils/multiple_ping_tool.html)工具

  * 下载地址：[【点击进入下载】](https://www.nirsoft.net/utils/pinginfoview.zip)

### [](https://am.809098.xyz/am-cf-domain/#5%E3%80%81%E5%9C%A8%E7%BA%BF%E6%9F%A5%E7%9C%8BIP%E5%92%8C%E5%9F%9F%E5%90%8D%E5%B7%A5%E5%85%B7 "5、在线查看IP和域名工具")5、在线查看IP和域名工具

  * 查找域名IP：[【点击进入下载】](https://www.itdog.cn/ping)
  * 查找网段的IP：[【点击进入下载】](https://www.itdog.cn/find_ping)

## [](https://am.809098.xyz/am-cf-domain/#%E4%BA%8C%E3%80%81%E8%8E%B7%E5%8F%96Cloudflare%E8%87%AA%E5%AE%B6%E5%9F%9F%E5%90%8D%E5%8F%98%E6%88%90%E8%8A%82%E7%82%B9%EF%BC%8C%E5%AE%9E%E7%8E%B0%E6%97%A0%E9%99%90%E8%8A%82%E7%82%B9%E4%BD%BF%E7%94%A8 "二、获取Cloudflare自家域名变成节点，实现无限节点使用")二、获取Cloudflare自家域名变成节点，实现无限节点使用

### [](https://am.809098.xyz/am-cf-domain/#1%E3%80%81%E7%99%BB%E5%BD%95Cloudflare-%E7%82%B9%E5%87%BB%E5%B7%A6%E8%BE%B9-%E7%BD%91%E7%AB%99-%E5%9C%A8%E7%BB%91%E5%AE%9A%E7%9A%84%E5%9F%9F%E5%90%8D%E4%B8%AD-%E7%82%B9%E5%87%BB%E7%BB%91%E5%AE%9A%E7%9A%84%E5%9F%9F%E5%90%8D-%E8%BF%9B%E5%85%A5%E9%A1%B5%E9%9D%A2%E7%82%B9%E5%87%BB%E5%B7%A6%E8%BE%B9-DNS-%E7%82%B9%E5%87%BB-%E8%AE%B0%E5%BD%95-%E5%9C%A8-Cloudflare-%E5%90%8D%E7%A7%B0%E6%9C%8D%E5%8A%A1%E5%99%A8-%E7%9C%8B%E5%88%B0DNS%E8%AE%B0%E5%BD%95%EF%BC%8C%E5%A6%82%E4%B8%8B "1、登录Cloudflare ->点击左边 网站 ->在绑定的域名中 点击绑定的域名 -> 进入页面点击左边 DNS -> 点击 记录 -> 在 Cloudflare 名称服务器 看到DNS记录，如下")1、登录Cloudflare ->点击左边 网站 ->在绑定的域名中 点击绑定的域名 -> 进入页面点击左边 DNS -> 点击 记录 -> 在 Cloudflare 名称服务器 看到DNS记录，如下

plaintext
[code]
    1  
    2  
    3  
    
[/code]

| 
[code]
    类型	值  
    NS	piotr.ns.cloudflare.com  
    NS	violet.ns.cloudflare.com  
    
[/code]  
  
---|---  
  
### [](https://am.809098.xyz/am-cf-domain/#2%E3%80%81%E5%9C%A8%E7%BA%BF%E5%B7%A5%E5%85%B7-itdog-%E6%8A%8A%E4%B8%8A%E9%9D%A2%E5%9C%A8DNS%E8%AE%B0%E5%BD%95%E6%89%BE%E5%87%BA%E5%9F%9F%E5%90%8D%E7%9A%84%E7%BD%91%E6%AE%B5%E7%9A%84IP "2、在线工具 itdog 把上面在DNS记录找出域名的网段的IP")2、在线工具 itdog 把上面在DNS记录找出域名的网段的IP

  * 查找域名IP：[【点击进入进入】](https://www.itdog.cn/ping)
  * 查找网段的IP：[【点击进入进入】](https://www.itdog.cn/find_ping)

### [](https://am.809098.xyz/am-cf-domain/#3%E3%80%81%E9%80%9A%E8%BF%87pinginfoview%E5%B7%A5%E5%85%B7%E6%89%BE%E5%87%BA%E7%BD%91%E6%AE%B5%E7%9A%84IP%E7%9A%84%E5%9F%9F%E5%90%8D "3、通过pinginfoview工具找出网段的IP的域名")3、通过pinginfoview工具找出网段的IP的域名

  * 下载地址：[【点击进入下载】](https://www.nirsoft.net/utils/pinginfoview.zip)

### [](https://am.809098.xyz/am-cf-domain/#4%E3%80%81%E6%89%BE%E5%88%B0Cloudflare%E8%87%AA%E5%AE%B6%E5%9F%9F%E5%90%8D%E5%90%8E%EF%BC%8C%E5%B0%B1%E5%8F%AF%E4%BB%A5%E5%AE%8C%E6%88%90%E7%94%A8%E6%9D%A5%E5%81%9A%E8%8A%82%E7%82%B9%E4%BD%BF%E7%94%A8%E4%BA%86 "4、找到Cloudflare自家域名后，就可以完成用来做节点使用了")4、找到Cloudflare自家域名后，就可以完成用来做节点使用了

➖➖➖➖➖相关视频推荐➖➖➖➖➖➖➖➖

  * [【免费VLESS节点部署】教程](https://youtu.be/dPH63nITA0M)
  * [【Trojan免费节点】教程](https://youtu.be/uh27CVVi6HA)
  * [【优先IP或域名】教程](https://youtu.be/pKrlfRRB0gU)
  * [【serv00一键部署socks5】教程](https://youtu.be/Bw82BH_ecC4)
  * [【订阅工具使用教】教程](https://youtu.be/xGOL57cmvaw)
  * [【免费Karing订阅工具使用教】教程](https://youtu.be/M3vLLBWfuFg)
  * [【CF免费KV文件存储优选IP文件】教程](https://youtu.be/dzxezRV1v-o)
  * [【CF部署GitHub私有仓库存储优选IP文件】教程](https://youtu.be/vX3U3FuuTT8)
  * [【聚合订阅器部署】教程](https://youtu.be/YBO2hf96150)
  * [【解决常见订阅测试-1】教程](https://youtu.be/kYQxV1G-ePw)

[[点击观看视频教程]](https://youtu.be/novrPiMsK70)

▶️ 新人[YouTube](https://youtube.com/@AM_CLUB) 需要您的支持，请务必订阅频道帮我点赞、关注、打开小铃铛， _十分感谢！！！_  
✅在Fork项目时,请 follow 我的GitHub、给我所有项目一个 Star 星星支持下！你的支持是我不断前进的动力！ 💖

# [](https://am.809098.xyz/am-cf-domain/#)

[点击展开] 赞赏支持 ~🧧

  * ``

# [](https://am.809098.xyz/am-cf-domain/#-1)

免责声明:

  * 1、该项目设计和开发仅供学习、研究和安全测试目的。请于下载后 24 小时内删除, 不得用作任何商业用途, 文字、数据及图片均有所属版权, 如转载须注明来源。
  * 2、使用本程序必循遵守部署服务器所在地区的法律、所在国家和用户所在国家的法律法规。对任何人或团体使用该项目时产生的任何后果由使用者承担。
  * 3、作者不对使用该项目可能引起的任何直接或间接损害负责。作者保留随时更新免责声明的权利，且不另行通知。

# [](https://am.809098.xyz/am-cf-domain/#-2)

➖➖➖➖➖广告位➖➖➖➖  
【红杏加速器】机场,专属全场套餐5折,低至5元左右222G,数量有限,先到先得!!!  
🌐点击官网[【https://hongxingdl.com】](https://hongxingdl.com/web/#/login?code=mn5Tuipf)注册  
🎁5折优惠码：`AM科技`  
✅高速iepl专线，独家定制极速机场专线，玩游戏首选，解锁奈飞、ChatGPT、全流媒体。

➖➖➖➖➖➖➖➖➖➖➖➖➖  
【69云】中转高速机场  
🌐点击官网[【https://69yun69.com】](https://proxy-69.69yun69.com/auth/register?code=UcWJkh)注册  
🎁不限时套餐，永久有效，让您的流量永不过期。签到，每日免费流量  
✅看片秒加载，全流媒体解锁，Chatgpt解锁web+app！双千兆节点，一秒下载不卡顿

➖➖➖➖➖➖➖➖➖➖➖➖➖  
【云狐VPN】专线机场  
🌐点击官网[【https://yunhu.ink】](https://www.yh15.xyz/register?code=KPO6IFwh)注册  
✅无视晚高峰，高清流畅体验Netflix、Disney+等，可配置中转静态住宅IP，Chat GPT专线，海外社交流媒体全解锁。

➖➖➖➖➖➖➖➖➖➖➖➖➖
