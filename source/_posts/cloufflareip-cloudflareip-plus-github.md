---
title: cloufflareip-cloudflareip-plus-github
date: '2022-05-10 12:00:00'
cover: /img/covers/cloufflareip-cloudflareip-plus-github.jpg
description: 一、目前CloufFlare自选IP存在问题 二、使用CloudFlare自选IP PLUS解决上述问题？ 三、使用方法 必要条件： 用前必读： 方法一：GitHub Actions 运行（推荐） 方法二：在自己的VPS或电脑中运行 四、总结 WPJAM TOC 一、目前Clou
---
* [一、目前CloufFlare自选IP存在问题](https://hostmonit.com/cloudflare-select-ip-plus/#toc-1)
  * [二、使用CloudFlare自选IP PLUS解决上述问题？](https://hostmonit.com/cloudflare-select-ip-plus/#toc-2)
  * [三、使用方法](https://hostmonit.com/cloudflare-select-ip-plus/#toc-3)
    * [必要条件：](https://hostmonit.com/cloudflare-select-ip-plus/#toc-4)
    * [用前必读：](https://hostmonit.com/cloudflare-select-ip-plus/#toc-5)
  * [方法一：GitHub Actions 运行（推荐）](https://hostmonit.com/cloudflare-select-ip-plus/#toc-2)
  * [方法二：在自己的VPS或电脑中运行](https://hostmonit.com/cloudflare-select-ip-plus/#toc-7)
  * [四、总结](https://hostmonit.com/cloudflare-select-ip-plus/#toc-8)

[WPJAM TOC](http://blog.wpjam.com/project/wpjam-basic/)

## 一、目前CloufFlare自选IP存在问题

上一篇[文章](https://hostmonit.com/manually-select-ip/)提到了使用CloudFlare自选IP加速自己的网站，细心的小伙伴也发现了问题。简单总结有以下几点缺陷。

  1. 自己A记录填写的CloudFlare IP并不是永久可用，保不齐哪天你填写的CloudFlare IP被GFW给屏蔽了，那你的网站就歇菜了。
  2. 自己A记录填写的CloudFlare IP并不是能持续稳定，即使是CloufFlare，服务器也有被攻击的时候，这时你的网站打开速度就会很慢，有时可能会出现打不开的情况。
  3. 自己A记录填写的CloudFlare IP并不是对所有人访问速度都快，这一点建站的小伙伴要尤为注意，也许你ping这个Cloudflare IP延迟很低，但是你的站点并不是你一个人访问，你需要的是让国内外每个访问者都能高速访问你的网站。
  4. 普通站长很难去找到CloudFLare对不同运营商（移动、联通、电信）访问速度快的IP。

## 二、使用CloudFlare自选IP PLUS解决上述问题？

遇到问题那么就要解决掉，为了解决这些问题，站长不惜重金买了几台国内不同运营商的高带宽高流量VDS，并花了两天时间写了一套程序，在每台VDS上都部署一套程序，用来获取相应运营商连接目前已知的1786880个CloudFlare IP中速度最快的IP，并以接口形式提供出来。之后又花了半天时间写了一个脚本，脚本主要功能是调取接口将连接各运营商速度快的CloudFare IP自动解析到DNS域名服务商处。经过一个多月的使用测试，明显感觉到网站的访问速度和稳定性有所提升。

## 三、使用方法

#### 必要条件：

★ Cloudflare自选IP完成并已接入到DNSPOD，不知道怎么自选IP可以查看上个[CloudFlare自选IP](https://hostmonit.com/manually-select-ip/)的教程  
★ Linux\Windows、Python3、pip3环境

#### 用前必读：

1\. 网络环境错综复杂，适合我的不一定适合你，所以尽量先尝试免费的KEY或者购买试用版的KEY  
2\. 如果当前DNSPod有移动、联通、电信线路的解析将会覆盖掉  
3\. 至于为什么要选择性收费，这个标价我也根本不指望能赚钱，甚至不够我国内一台VDS的钱，况且后续会增加VDS节点，并且增加按区域解析的功能。(小声BB，因为前公司欠薪1年多)

### 方法一：GitHub Actions 运行（推荐）

  1. 登录[腾讯云后台](https://console.cloud.tencent.com/cam/capi),获取 SecretId、SecretKey

  2. Fork[项目](https://github.com/ddgth/cf2dns)到自己的仓库[![fork.png](https://img.hostmonit.com/images/2020/11/05/fork.png)](https://img.hostmonit.com/images/2020/11/05/fork.png)

  3. 进入第二步中Fork的项目，点击Settings->Secrets-New secret，分别是DOMAINS，KEY，SECRETID，SECRETKEY。

>      * DOMAINS 需改域名信息，填写时注意不要有换行 例如：`{"hostmonit.com": {"@": ["CM","CU","CT"], "shop": ["CM", "CU", "CT"], "stock": ["CM","CU","CT"]},"4096.me": {"@": ["CM","CU","CT"], "vv":["CM","CU","CT"]}}`
>      * KEY API密钥，从[商店](https://shop.hostmonit.com/)购买KEY，也可以使用这个KEY `o1zrmHAF` ，区别是 `o1zrmHAF` 是历史优选的Cloudflare IP(也可以从这个[网站](https://stock.hostmonit.com/CloudFlareYes)查到IP的信息)，而购买的KEY是15分钟内获取到的对各运营商速度最优的的Cloudflare IP
>      * SECRETID 第一部中从[腾讯云后台](https://console.cloud.tencent.com/cam/capi),获取到的 `SECRETID`
>      * SECRETKEY 第一部中从[腾讯云后台](https://console.cloud.tencent.com/cam/capi),获取到的 `SECRETKEY`

[![secret.png](https://img.hostmonit.com/images/2020/11/05/secret.png)](https://img.hostmonit.com/images/2020/11/05/secret.png)

  4. 修改您项目中的 `.github/workflows/run.yml` 文件，修改定时执行的时长(建议15分钟执行一次)，最后点击 `start commit` 提交即可在Actions中的build查看到执行情况，如果看到 `cf2dns` 执行日志中有 `CHANGE DNS SUCCESS` 详情输出，即表示运行成功。需要注意观察下次定时是否能正确运行，有时候GitHub Actions 挺抽风的

[![modify.png](https://img.hostmonit.com/images/2020/11/05/modify.png)](https://img.hostmonit.com/images/2020/11/05/modify.png)

[![commit.png](https://img.hostmonit.com/images/2020/11/05/commit.png)](https://img.hostmonit.com/images/2020/11/05/commit.png)

[![build.png](https://img.hostmonit.com/images/2020/11/05/build.png)](https://img.hostmonit.com/images/2020/11/05/build.png)

### 方法二：在自己的VPS或电脑中运行

  1. 安装依赖包

```
pip install -r requirements.txtCOPY

```

  2. 登录[腾讯云后台](https://console.cloud.tencent.com/cam/capi),获取 SecretId、SecretKey
  3. 将[GitHub中脚本](https://github.com/ddgth/cf2dns)下载到本地
  4. 将第一步中获取到的SecretId、SecretKey配置到cf2dns.py脚本中,并修改脚本中DOMAINS配置信息，可配置多个域名和多个子域名,但必须是在同一个DNSPOD账号下
  5. (可选)从[商店](https://shop.hostmonit.com/)购买KEY，当然也可以用脚本中自带的KEY，区别是脚本中自带的KEY是历史优选的Cloudflare IP（可以从[全球主机补货监控](https://stock.hostmonit.com/CloudFlareYes)中查看IP的信息），而购买的KEY是15分钟内获取到的连接到各运营商速度最优的Cloudflare IP。
  6. 运行程序，如果能够正常运行可以选择cron或Windows计划任务定时执行（建议15分钟执行一次）

```
python3 cf2dns.pyCOPY

```

## 四、总结

写这套程序和教程也耗费了站长很多精力，希望使用本教程的小伙伴能够在下方的留言区说出使用的效果和感受，更希望您能提出宝贵的建议。
