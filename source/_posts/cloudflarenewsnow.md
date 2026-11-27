---
title: 通过Cloudflare免费部署newsnow 优雅地阅读实时热门新闻
date: '2025-03-31 12:00:00'
cover: /img/covers/cloudflarenewsnow.jpg
tags:
- 建站
categories:
- 建站
description: 《部署教程说明》 解决 多个新闻来源 要打开多个网站或app等的 观看 的问题，能过通过结合 Cloudflare部署newsnow 项目,可以汇总所有 实时热门新闻 ,并可以一个页面观看. 【YouTube频道】 | 【Telegram频道】 | 【GitHub仓库】 项目地址
---
《部署教程说明》

解决多个新闻来源要打开多个网站或app等的观看的问题，能过通过结合Cloudflare部署newsnow项目,可以汇总所有实时热门新闻,并可以一个页面观看.

[【YouTube频道】 | ](https://youtube.com/@am_clubs?sub_confirmation=1)[【Telegram频道】 | ](https://t.me/am_clubs)[【GitHub仓库】](https://github.com/amclubs)

  * 项目地址：<https://github.com/amclubs/newsnow>

## 一、需要准备的前提资料

### 1、注册免费cloudflare帐号(邮箱就可以免费注册)

  * 注册地址：[https://cloudflare.com](https://cloudflare.com/) [[点击观看视频教程]](https://youtu.be/ITeuSbHVQ2E)

### 2、注册免费域名

  * [dynv6域名视频教程](https://youtu.be/Nl0BV2ocYb8) | [cloudns域名视频教程](https://youtu.be/oi8OgTOZLug) | [l53域名视频教程](https://youtu.be/-LpostXqKRo) | [所有免费域名视频教程](https://www.youtube.com/playlist?list=PLGVQi7TjHKXZGODTvB8DEervrmHANQ1AR)

### 3、GitHub帐号一个

  * 自己邮箱去注册

## 二、如何Cloudflare部署newsnow项目

  1. (无登录教程)如果部署到Cloudflare,详情请查看视频教程

  2. (需要登录教程)通过GitHub授权登录,详细请查看视频教程

### 1、GitHub OAuth 配置

  1. [创建 GitHub App](https://github.com/settings/applications/new)
  2. 无需特殊权限
  3. 回调 URL 设置为：`https://your-domain.com/api/oauth/github`（替换 your-domain 为实际域名）
  4. 获取 Client ID 和 Client Secret

### 2、环境变量配置

plaintext

```

    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    

```

| 

```

    # Github Clien ID  
    G_CLIENT_ID=  
    # Github Clien Secret  
    G_CLIENT_SECRET=  
    # JWT Secret, 通常就用 Clien Secret  
    JWT_SECRET=  
    # 初始化数据库, 首次运行必须设置为 true，之后可以将其关闭  
    INIT_TABLE=true  
    # 是否启用缓存  
    ENABLE_CACHE=true  
    

```
  
  
---|---  
  
### 3、创建并设置 Cloudflare D1 数据库

  1. 在Cloudflare的 存储和数据库 -> D1 SQL 数据库 创建一个数据库,名称自定义(如:newsnow)
  2. 在Cloudflare的page项目的 设置 -> 绑定 添加D1绑定 ,名称为: NEWSNOW_DB 值选择上面D1 SQL创建的名称自定义(如:newsnow)
  3. 重新部署page项目

[![tools-arc](https://raw.githubusercontent.com/amclubs/newsnow/main/screenshots/preview-1.png)](https://raw.githubusercontent.com/amclubs/newsnow/main/screenshots/preview-1.png)[![tools-arc](https://raw.githubusercontent.com/amclubs/newsnow/main/screenshots/preview-2.png)](https://raw.githubusercontent.com/amclubs/newsnow/main/screenshots/preview-2.png)[[点击观看视频教程]](https://youtu.be/-a6NJ6vPSu4)

▶️ 新人[YouTube](https://www.youtube.com/channel/UCaU8zmom0Vi1LvZZw5Y_8NQ?sub_confirmation=1) 需要您的支持，请务必订阅频道帮我点赞、关注、打开小铃铛， _十分感谢！！！_  
✅在Fork项目时,请 follow 我的[GitHub](https://github.com/amclubs)、给我所有项目一个 Star 星星支持下！你的支持是我不断前进的动力！ 💖  
✅解锁更多技能 [加入TG群【am_clubs】](https://t.me/am_clubs)、[YouTube频道【@am_clubs】](https://www.youtube.com/channel/UCaU8zmom0Vi1LvZZw5Y_8NQ?sub_confirmation=1)、[【博客(国内)】](https://amclubss.com/)、[【博客(国际)】](https://amclubs.blogspot.com/)  
✅点击观看教程[CLoudflare免费节点](https://www.youtube.com/playlist?list=PLGVQi7TjHKXbrY0Pk8gm3T7m8MZ-InquF) | [VPS搭建节点](https://www.youtube.com/playlist?list=PLGVQi7TjHKXaVlrHP9Du61CaEThYCQaiY) | [获取免费域名](https://www.youtube.com/playlist?list=PLGVQi7TjHKXZGODTvB8DEervrmHANQ1AR) | [免费VPN](https://www.youtube.com/playlist?list=PLGVQi7TjHKXY7V2JF-ShRSVwGANlZULdk) | [IPTV源](https://www.youtube.com/playlist?list=PLGVQi7TjHKXbkozDYVsDRJhbnNaEOC76w) | [Mac和Win工具](https://www.youtube.com/playlist?list=PLGVQi7TjHKXYBWu65yP8E08HxAu9LbCWm) | [AI分享](https://www.youtube.com/playlist?list=PLGVQi7TjHKXaodkM-mS-2Nwggwc5wRjqY)

# 

[点击展开] 赞赏支持 ~🧧

  * ``
  * ``

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://github.com/user-attachments/assets/e6cdc42a-6374-4722-b833-601738f72196)  

# 

> 免责声明:  
> 1、该项目设计和开发仅供学习、研究和安全测试目的。请于下载后 24 小时内删除, 不得用作任何商业用途, 文字、数据及图片均有所属版权, 如转载须注明来源。  
> 2、使用本程序必循遵守部署服务器所在地区的法律、所在国家和用户所在国家的法律法规。对任何人或团体使用该项目时产生的任何后果由使用者承担。  
> 3、作者不对使用该项目可能引起的任何直接或间接损害负责。作者保留随时更新免责声明的权利，且不另行通知。

# 

* * *

【银河录像局】 奈飞账号合租，Ai账号多模型国内直连，性价比拉满  
🌐点击官网：[【nf.video】](https://nf.video/xng6j)注册 🎁95折优惠码：amclubs

* * *

【红杏云】 中转高速机场,8元220G/每月✅玩游戏首选，解锁ChatGPT、全流媒体(送小火箭)[【送自动签到脚本】](https://github.com/amclubs/am-check-in)  
🌐点击官网[【https://hongxingdl.com】](https://hongxingdl.com/web/#/login?code=mn5Tuipf)注册 🎁8折优惠码：AM科技

* * *

【极速云】 全专线机场 低至8元100G/每月✅全IEPL专线，畅爽晚高峰 解锁ChatGPT、全流媒体(送小火箭)  
🌐点击官网[【https://极速666.com】](https://w1.lypyf.com/#/register?code=MCdAybnR)注册 🎁8折优惠码：AM888

* * *

【69云】 中转高速机场 9.9元400G/每月✅看片秒加载，解锁ChatGPT、全流媒体(送小火箭)[【送自动签到脚本】](https://github.com/amclubs/am-check-in)  
🌐点击官网[【https://69yun69.com】](https://proxy-69.69yun69.com/auth/register?code=UcWJkh)注册

* * *

【LocalCard虚拟卡】 免认证 | 免实名 | 免月费 | 全卡段支持chatgpt | 多种消费场景 | 超过60种货币  
🌐点击官网[【https://www.localcard.hk】](https://www.localcard.hk/#/pages/H5/login?code=bkBrXNCf)注册 🎁开卡时输入优惠券减5刀：amclubs

* * *

[![头像](https://809098.xyz/img/default.ico)![头像](https://809098.xyz/img/default.ico)](https://amclubss.com/ "头像")

AM科技

技术分享 满满干货

[原创](https://amclubss.com/newsnow/ "该文章为原创文章，注意版权协议")通过Cloudflare免费部署newsnow 优雅地阅读实时热门新闻

打赏作者

![Scan me!](data:image/png;base64,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)

使用手机访问这篇文章

[](https://service.weibo.com/share/share.php?title=%E9%80%9A%E8%BF%87Cloudflare%E5%85%8D%E8%B4%B9%E9%83%A8%E7%BD%B2newsnow%20%E4%BC%98%E9%9B%85%E5%9C%B0%E9%98%85%E8%AF%BB%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB&url=https://amclubss.com/newsnow/&pic=/img/newsnow.jpg)

本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。转载请注明来自 [AM科技](https://amclubss.com/)！

[cloudflare50](https://amclubss.com/tags/cloudflare/)[CF48](https://amclubss.com/tags/CF/)[CDN14](https://amclubss.com/tags/CDN/)[免费工具6](https://amclubss.com/tags/%E5%85%8D%E8%B4%B9%E5%B7%A5%E5%85%B7/)[新闻1](https://amclubss.com/tags/%E6%96%B0%E9%97%BB/)[newsnow1](https://amclubss.com/tags/newsnow/)

[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Famclubss.com%2Fnewsnow%2F)[](https://twitter.com/intent/tweet?text=%E9%80%9A%E8%BF%87Cloudflare%E5%85%8D%E8%B4%B9%E9%83%A8%E7%BD%B2newsnow%20%E4%BC%98%E9%9B%85%E5%9C%B0%E9%98%85%E8%AF%BB%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB%20%7C%20AM%E7%A7%91%E6%8A%80&url=https%3A%2F%2Famclubss.com%2Fnewsnow%2F&via=https%3A%2F%2Famclubss.com)[](https://service.weibo.com/share/share.php?url=https%3A%2F%2Famclubss.com%2Fnewsnow%2F&title=%E9%80%9A%E8%BF%87Cloudflare%E5%85%8D%E8%B4%B9%E9%83%A8%E7%BD%B2newsnow%20%E4%BC%98%E9%9B%85%E5%9C%B0%E9%98%85%E8%AF%BB%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB%20%7C%20AM%E7%A7%91%E6%8A%80&pic=%2Fimg%2Fnewsnow.jpg&appkey=)[](http://connect.qq.com/widget/shareqq/index.html?url=https%3A%2F%2Famclubss.com%2Fnewsnow%2F&title=%E9%80%9A%E8%BF%87Cloudflare%E5%85%8D%E8%B4%B9%E9%83%A8%E7%BD%B2newsnow%20%E4%BC%98%E9%9B%85%E5%9C%B0%E9%98%85%E8%AF%BB%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB%20%7C%20AM%E7%A7%91%E6%8A%80&source=%E9%80%9A%E8%BF%87Cloudflare%E5%85%8D%E8%B4%B9%E9%83%A8%E7%BD%B2newsnow%20%E4%BC%98%E9%9B%85%E5%9C%B0%E9%98%85%E8%AF%BB%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB%20%7C%20AM%E7%A7%91%E6%8A%80&desc=%E3%80%8A%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B%E8%AF%B4%E6%98%8E%E3%80%8B%20%E8%A7%A3%E5%86%B3%E5%A4%9A%E4%B8%AA%E6%96%B0%E9%97%BB%E6%9D%A5%E6%BA%90%E8%A6%81%E6%89%93%E5%BC%80%E5%A4%9A%E4%B8%AA%E7%BD%91%E7%AB%99%E6%88%96app%E7%AD%89%E7%9A%84%E8%A7%82%E7%9C%8B%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%8C%E8%83%BD%E8%BF%87%E9%80%9A%E8%BF%87%E7%BB%93%E5%90%88Cloudflare%E9%83%A8%E7%BD%B2newsnow%E9%A1%B9%E7%9B%AE%2C%E5%8F%AF%E4%BB%A5%E6%B1%87%E6%80%BB%E6%89%80%E6%9C%89%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB%2C%E5%B9%B6%E5%8F%AF%E4%BB%A5%E4%B8%80%E4%B8%AA%E9%A1%B5%E9%9D%A2%E8%A7%82%E7%9C%8B.%20%20%E3%80%90YouTube%E9%A2%91%E9%81%93%E3%80%91%20%7C%20%E3%80%90Telegram%E9%A2%91%E9%81%93%E3%80%91%20%7C%20%E3%80%90GitHub%E4%BB%93%E5%BA%93%E3%80%91%20%20%20%E9%A1%B9%E7%9B%AE%E5%9C%B0%E5%9D%80%EF%BC%9Ahttps%3A%26%23x2F%3B%26%23x2F%3Bgithu&pics=%2Fimg%2Fnewsnow.jpg&summary=%22%E3%80%8A%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B%E8%AF%B4%E6%98%8E%E3%80%8B%20%E8%A7%A3%E5%86%B3%E5%A4%9A%E4%B8%AA%E6%96%B0%E9%97%BB%E6%9D%A5%E6%BA%90%E8%A6%81%E6%89%93%E5%BC%80%E5%A4%9A%E4%B8%AA%E7%BD%91%E7%AB%99%E6%88%96app%E7%AD%89%E7%9A%84%E8%A7%82%E7%9C%8B%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%8C%E8%83%BD%E8%BF%87%E9%80%9A%E8%BF%87%E7%BB%93%E5%90%88Cloudflare%E9%83%A8%E7%BD%B2newsnow%E9%A1%B9%E7%9B%AE%2C%E5%8F%AF%E4%BB%A5%E6%B1%87%E6%80%BB%E6%89%80%E6%9C%89%E5%AE%9E%E6%97%B6%E7%83%AD%E9%97%A8%E6%96%B0%E9%97%BB%2C%E5%B9%B6%E5%8F%AF%E4%BB%A5%E4%B8%80%E4%B8%AA%E9%A1%B5%E9%9D%A2%E8%A7%82%E7%9C%8B.%20%20%E3%80%90YouTube%E9%A2%91%E9%81%93%E3%80%91%20%7C%20%E3%80%90Telegram%E9%A2%91%E9%81%93%E3%80%91%20%7C%20%E3%80%90GitHub%E4%BB%93%E5%BA%93%E3%80%91%20%20%20%E9%A1%B9%E7%9B%AE%E5%9C%B0%E5%9D%80%EF%BC%9Ahttps%3A%26%23x2F%3B%26%23x2F%3Bgithu%22)

[![cover of previous post](https://809098.xyz/img/liangxinyun.jpg)上一篇【良心云】直连机场 2元100G 6元1000G超低价格，注册免费送100G流量！三网网络质量优秀，流媒体解锁，GPT解锁，支持新疆河南地区使用](https://amclubss.com/liangxinyun/)

喜欢这篇文章的人也看了

[![cover](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 2025-03-24Android手机版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题](https://amclubss.com/amclubs-cfnat-android/ "Android手机版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题")

[![cover](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 2025-03-13Linux版(软路由) 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题 结合openclash使用](https://amclubss.com/amclubs-cfnat-linux/ "Linux版\(软路由\) 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题 结合openclash使用")

[![cover](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 2025-03-15Mac版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题](https://amclubss.com/amclubs-cfnat-mac/ "Mac版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题")

[![cover](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 2025-03-08amclubs-cfnat解决Cloudflare的泛播IP的问题，自动优先IP实现免费科学上网 windows桌面版](https://amclubss.com/amclubs-cfnat/ "amclubs-cfnat解决Cloudflare的泛播IP的问题，自动优先IP实现免费科学上网 windows桌面版")

[![cover](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 2024-08-17【免费双向绑定域名】小白教程ClouDNS免费申请,全可绑Cloudflare,解说双向绑定教你避免所有坑](https://amclubss.com/domain-cloudns/ "【免费双向绑定域名】小白教程ClouDNS免费申请,全可绑Cloudflare,解说双向绑定教你避免所有坑")

[![cover](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 2024-09-15【免费域名】如何0元购买ggff.net域名,可以绑定Cloudflare快去注册一个备用](https://amclubss.com/domain-l53/ "【免费域名】如何0元购买ggff.net域名,可以绑定Cloudflare快去注册一个备用")

* * *

 评论

匿名评论[隐私政策](https://amclubss.com/privacy)

昵称

邮箱

网址

0/500

发送

没有评论

查看更多

Powered by [Twikoo](https://twikoo.js.org/) v1.6.25

不要太劳累了，早睡更健康

![avatar](https://809098.xyz/img/default.ico)

![status](https://bu.dusays.com/2021/03/03/317b790a902ec.png)

AM科技 技术分享 满满干货，从0到1实现，从到落地应用，尽情期待~

# [AM科技技术分享 满满干货](https://amclubss.com/)

[](https://github.com/amclubs "Github")[](https://youtube.com/@am_clubs "YouTube")[](https://t.m/am_clubs "Telegram")[](https://facebook.com/profile.php?id=61563982690740 "Facebook")[](https://tiktok.com/@amclubss "TikTok")[](https://x.com/AMClubss "X\(Twitter\)")

文章目录

  1. [一、需要准备的前提资料](https://amclubss.com/newsnow/#%E4%B8%80%E3%80%81%E9%9C%80%E8%A6%81%E5%87%86%E5%A4%87%E7%9A%84%E5%89%8D%E6%8F%90%E8%B5%84%E6%96%99)
  2. [二、如何Cloudflare部署newsnow项目](https://amclubss.com/newsnow/#%E4%BA%8C%E3%80%81%E5%A6%82%E4%BD%95Cloudflare%E9%83%A8%E7%BD%B2newsnow%E9%A1%B9%E7%9B%AE)
     1. [1、GitHub OAuth 配置](https://amclubss.com/newsnow/#1%E3%80%81GitHub-OAuth-%E9%85%8D%E7%BD%AE)
     2. [2、环境变量配置](https://amclubss.com/newsnow/#2%E3%80%81%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AE)
     3. [3、创建并设置 Cloudflare D1 数据库](https://amclubss.com/newsnow/#3%E3%80%81%E5%88%9B%E5%BB%BA%E5%B9%B6%E8%AE%BE%E7%BD%AE-Cloudflare-D1-%E6%95%B0%E6%8D%AE%E5%BA%93)

* * * 最近发布

[![通过Cloudflare免费部署newsnow 优雅地阅读实时热门新闻](https://809098.xyz/img/newsnow.jpg)](https://amclubss.com/newsnow/ "通过Cloudflare免费部署newsnow 优雅地阅读实时热门新闻")

[通过Cloudflare免费部署newsnow 优雅地阅读实时热门新闻](https://amclubss.com/newsnow/ "通过Cloudflare免费部署newsnow 优雅地阅读实时热门新闻")

[![【良心云】直连机场 2元100G 6元1000G超低价格，注册免费送100G流量！三网网络质量优秀，流媒体解锁，GPT解锁，支持新疆河南地区使用](https://809098.xyz/img/liangxinyun.jpg)](https://amclubss.com/liangxinyun/ "【良心云】直连机场 2元100G 6元1000G超低价格，注册免费送100G流量！三网网络质量优秀，流媒体解锁，GPT解锁，支持新疆河南地区使用")

[【良心云】直连机场 2元100G 6元1000G超低价格，注册免费送100G流量！三网网络质量优秀，流媒体解锁，GPT解锁，支持新疆河南地区使用](https://amclubss.com/liangxinyun/ "【良心云】直连机场 2元100G 6元1000G超低价格，注册免费送100G流量！三网网络质量优秀，流媒体解锁，GPT解锁，支持新疆河南地区使用")

[![Android手机版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题](https://809098.xyz/img/amclubs-cfnat-android.jpg)](https://amclubss.com/amclubs-cfnat-android/ "Android手机版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题")

[Android手机版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题](https://amclubss.com/amclubs-cfnat-android/ "Android手机版 自动优先IP实现免费科学上网 amclubs-cfnat解决Cloudflare的泛播IP的问题")

[![【tapcloud】大陆最强机场，不限制设备数量，最低只需6元，🎁五折优惠码：AM科技](https://809098.xyz/img/tapcloud.jpg)](https://amclubss.com/tapcloud/ "【tapcloud】大陆最强机场，不限制设备数量，最低只需6元，🎁五折优惠码：AM科技")

[【tapcloud】大陆最强机场，不限制设备数量，最低只需6元，🎁五折优惠码：AM科技](https://amclubss.com/tapcloud/ "【tapcloud】大陆最强机场，不限制设备数量，最低只需6元，🎁五折优惠码：AM科技")

[![lycheeip 🚀高速静态住宅IP推荐！原生独享双ISP！| 大带宽TikTok运营 | 跨境电商运营 | 静态住宅代理 | AM科技](https://809098.xyz/img/lycheeip.jpg)](https://amclubss.com/lycheeip/ "lycheeip 🚀高速静态住宅IP推荐！原生独享双ISP！| 大带宽TikTok运营 | 跨境电商运营 | 静态住宅代理 | AM科技")

[lycheeip 🚀高速静态住宅IP推荐！原生独享双ISP！| 大带宽TikTok运营 | 跨境电商运营 | 静态住宅代理 | AM科技](https://amclubss.com/lycheeip/ "lycheeip 🚀高速静态住宅IP推荐！原生独享双ISP！| 大带宽TikTok运营 | 跨境电商运营 | 静态住宅代理 | AM科技")

[](https://github.com/amclubs "GitHub")[](https://youtube.com/@AM_CLUB "YouTube")[](https://t.me/am_clubs "电报\(Telegram\)交流群")![返回顶部](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)[](mailto:amclubss@gmail.com "Email")[](https://facebook.com/profile.php?id=61563982690740 "Facebook")[](https://tiktok.com/@amclubss "TikTok")[](https://x.com/AMClubss "X\(Twitter\)")

工具

[订阅工具](https://github.com/amclubs/am-cf-tunnel/blob/main/README.md "订阅工具")[服务监控](https://nezha.amclubs.us.kg/ "服务监控")[Dig](https://toolbox.googleapps.com/apps/dig/ "Dig")[加密/解密](https://toolbox.googleapps.com/apps/encode_decode/ "加密/解密")[IPCheck](https://ipcheck.ing/ "IPCheck")

CND | 公益

[Cloudflare](https://cloudflare.com/ "Cloudflare")[fastly](https://www.fastly.com/signup/?tier=free "fastly")[gcore](https://gcore.com/zh/cdn "gcore")[优选/反代域名IP](https://amclubss.com/cf/ "优选/反代域名IP")[应用监控](https://uptimeflare.amclubss.us.kg/ "应用监控")

热门项目

[免费vless节点](https://github.com/amclubs/am-cf-tunnel "免费vless节点")[免费trojan节点](https://github.com/amclubs/am-cf-trojan "免费trojan节点")[免费vmess节点](https://github.com/ansoncloud8/am-serv00-vmess "免费vmess节点")[serv00(alist)](https://github.com/amclubs/am-cf-alist-freebsd "serv00\(alist\)")[聚合汇聚订阅](https://github.com/amclubs/am-cf-sub-rss "聚合汇聚订阅")

推荐项目

[免费Vercel直播](https://github.com/amclubs/iptv-go "免费Vercel直播")[CF部署BPB节点](https://github.com/amclubs/BPB-Worker-Panel "CF部署BPB节点")[免费CF存储KV](https://github.com/amclubs/am-cf-text2kv "免费CF存储KV")[CF私密github](https://github.com/amclubs/am-cf-github2raw "CF私密github")[免费CF测速地址](https://github.com/amclubs/am-cf-speed-test-url "免费CF测速地址")

容器

[vercel](https://vercel.com/ "vercel")[iptv-go](https://github.com/amclubs/iptv-go "iptv-go")[huggingface](https://huggingface.co/ "huggingface")[koyeb](https://www.koyeb.com/ "koyeb")

机场推荐

[红杏云](https://hongxingdl.com/web/#/login?code=mn5Tuipf "红杏云")[69云](https://am.69yun69.com/ "69云")[极速云](https://w1.lypyf.com/#/register?code=MCdAybnR "极速云")

友链

[![AM科技-GitHub仓库](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://github.com/amclubs/ "AM科技-GitHub仓库")[![AM科技-YouTube频道](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://youtube.com/@AM_CLUB "AM科技-YouTube频道")[![AM科技-电报\(Telegram\)交流群](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://t.me/am_clubs "AM科技-电报\(Telegram\)交流群")[![AM科技-官网教程](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://amclubss.com/ "AM科技-官网教程")[![AM科技-Email](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](mailto:amclubss@gmail.com "AM科技-Email")[![AM科技-Facebook](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://facebook.com/profile.php?id=61563982690740 "AM科技-Facebook")[![AM科技-TikTok](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://tiktok.com/@amclubss "AM科技-TikTok")[![AM科技-X\(Twitter\)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://x.com/AMClubss "AM科技-X\(Twitter\)")

©2025 By [AM科技](https://amclubss.com/ "AM科技")

[技术分享-满满干货](https://youtube.com/@AM_CLUB "技术分享-满满干货")

[文章97](https://amclubss.com/archives/ "archive")[标签164](https://amclubss.com/tags/ "tag")[分类8](https://amclubss.com/categories/ "category")

功能

显示模式

网页

[![AM科技](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)AM科技](https://amclubss.com/ "AM科技")[![博客\(国际\)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)博客(国际)](https://amclubs.blogspot.com/ "博客\(国际\)")

项目

[![Github](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)Github](https://github.com/amclubs/ "Github")

教程Tutorial

  * [全部文章](https://amclubss.com/archives/)
  * [标签](https://amclubss.com/tags/)
  * [文章分类](https://amclubss.com/categories/)
  * [常见问题FAQ](https://amclubss.com/FAQ/)

推荐REC

  * [机场推荐](https://amclubss.com/categories/%E6%9C%BA%E5%9C%BA%E6%8E%A8%E8%8D%90/)
  * [VPS推荐](https://amclubss.com/categories/%E5%85%8D%E8%B4%B9%E6%9C%8D%E5%8A%A1%E5%99%A8/)

公益服务CSR

  * [CloudFlare优先](https://amclubss.com/cf/)
  * [短链生成器](https://amclubss.com/categories/%E5%85%8D%E8%B4%B9CF%E8%8A%82%E7%82%B9/)
  * [订阅转换](https://amclubss.com/categories/%E5%85%8D%E8%B4%B9CF%E8%8A%82%E7%82%B9/)

关于AM

  * [关于AM科技](https://amclubss.com/about)
  * [YouTube频道](https://youtube.com/@am_clubs)
  * [GitHub仓库](https://github.com/amclubs)
  * [Telegram交流群](https://t.me/am_clubs)
  * [Email](mailto:amclubss@gmail.com)
  * [Facebook](https://facebook.com/profile.php?id=61563982690740)
  * [TikTok](https://tiktok.com/@amclubss)
  * [X(Twitter)](https://x.com/AMClubss)

[常见问题FAQ](https://amclubss.com/FAQ/)

[博客(国际)](https://amclubs.blogspot.com/)

标签

[3D动画4](https://amclubss.com/tags/3D%E5%8A%A8%E7%94%BB/)[69yun1](https://amclubss.com/tags/69yun/)[69yun691](https://amclubss.com/tags/69yun69/)[AI11](https://amclubss.com/tags/AI/)[AM科技2](https://amclubss.com/tags/AM%E7%A7%91%E6%8A%80/)[CF48](https://amclubss.com/tags/CF/)[Canvas1](https://amclubss.com/tags/Canvas/)[ChatGPT8](https://amclubss.com/tags/ChatGPT/)[Copilot1](https://amclubss.com/tags/Copilot/)[LocalCard1](https://amclubss.com/tags/LocalCard/)[UI1](https://amclubss.com/tags/UI/)[VPN47](https://amclubss.com/tags/VPN/)[ai13](https://amclubss.com/tags/ai/)[chatgpt6](https://amclubss.com/tags/chatgpt/)[cloudflare50](https://amclubss.com/tags/cloudflare/)[deepseek4](https://amclubss.com/tags/deepseek/)[desktop1](https://amclubss.com/tags/desktop/)[gpt-4o-mini4](https://amclubss.com/tags/gpt-4o-mini/)[gpt4o5](https://amclubss.com/tags/gpt4o/)[tapcloud1](https://amclubss.com/tags/tapcloud/)[v2rayN21](https://amclubss.com/tags/v2rayN/)[vless9](https://amclubss.com/tags/vless/)[专线5](https://amclubss.com/tags/%E4%B8%93%E7%BA%BF/)[免费节点44](https://amclubss.com/tags/%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9/)[大模型11](https://amclubss.com/tags/%E5%A4%A7%E6%A8%A1%E5%9E%8B/)[实体卡1](https://amclubss.com/tags/%E5%AE%9E%E4%BD%93%E5%8D%A1/)[小白教程9](https://amclubss.com/tags/%E5%B0%8F%E7%99%BD%E6%95%99%E7%A8%8B/)[常见问题1](https://amclubss.com/tags/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98/)[技术分享2](https://amclubss.com/tags/%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB/)[机场9](https://amclubss.com/tags/%E6%9C%BA%E5%9C%BA/)[极速云2](https://amclubss.com/tags/%E6%9E%81%E9%80%9F%E4%BA%91/)[沉浸式翻译1](https://amclubss.com/tags/%E6%B2%89%E6%B5%B8%E5%BC%8F%E7%BF%BB%E8%AF%91/)[满满干货2](https://amclubss.com/tags/%E6%BB%A1%E6%BB%A1%E5%B9%B2%E8%B4%A7/)[科学上网48](https://amclubss.com/tags/%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91/)[红杏云1](https://amclubss.com/tags/%E7%BA%A2%E6%9D%8F%E4%BA%91/)[良心云1](https://amclubss.com/tags/%E8%89%AF%E5%BF%83%E4%BA%91/)[节点13](https://amclubss.com/tags/%E8%8A%82%E7%82%B9/)[虚拟卡1](https://amclubss.com/tags/%E8%99%9A%E6%8B%9F%E5%8D%A1/)[解锁GPT30](https://amclubss.com/tags/%E8%A7%A3%E9%94%81GPT/)[订阅30](https://amclubss.com/tags/%E8%AE%A2%E9%98%85/)

* * *

繁

[](https://amclubss.com/newsnow/#post-comment "直达评论")

播放音乐

Something Just Like This (Don Diablo Remix)

通知

你好呀

复制成功，复制和转载请标注本文地址
