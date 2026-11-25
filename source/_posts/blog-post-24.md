---
title: 临时邮箱一键部署指南
date: '2026-03-13 12:00:00'
tags:
- 临时邮箱
categories:
- 临时邮箱
description: 1. 首先点击 Deploy to Cloudflare 2 登陆账号后会进入，推荐选择亚洲地区（当然不选择亚洲也没关系） 不要修改数据库名称和R2名称 可能导致无法查询 3. 点击创建部署，然后耐心等待克隆部署 4. 点击继续处理项目，绑定必须的环境变量 5. 添加完成后点击部
---
#### 1\. 首先点击 Deploy to Cloudflare

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#1-%E9%A6%96%E5%85%88%E7%82%B9%E5%87%BB--deploy-to-cloudflare)

#### 2 登陆账号后会进入，推荐选择亚洲地区（当然不选择亚洲也没关系）

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#2-%E7%99%BB%E9%99%86%E8%B4%A6%E5%8F%B7%E5%90%8E%E4%BC%9A%E8%BF%9B%E5%85%A5%E6%8E%A8%E8%8D%90%E9%80%89%E6%8B%A9%E4%BA%9A%E6%B4%B2%E5%9C%B0%E5%8C%BA%E5%BD%93%E7%84%B6%E4%B8%8D%E9%80%89%E6%8B%A9%E4%BA%9A%E6%B4%B2%E4%B9%9F%E6%B2%A1%E5%85%B3%E7%B3%BB)

`不要修改数据库名称和R2名称 可能导致无法查询` [![5a0cc80913848aca4b5f4058538ad6aa|690x333](https://github.com/idinging/freemail/raw/master/pic/v4/depl1.png)](https://github.com/idinging/freemail/blob/master/pic/v4/depl1.png)

#### 3\. 点击创建部署，然后耐心等待克隆部署

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#3-%E7%82%B9%E5%87%BB%E5%88%9B%E5%BB%BA%E9%83%A8%E7%BD%B2%E7%84%B6%E5%90%8E%E8%80%90%E5%BF%83%E7%AD%89%E5%BE%85%E5%85%8B%E9%9A%86%E9%83%A8%E7%BD%B2)

[![5a0cc80913848aca4b5f4058538ad6aa|690x333](https://github.com/idinging/freemail/raw/master/pic/v4/depl2.png)](https://github.com/idinging/freemail/blob/master/pic/v4/depl2.png)

#### 4\. 点击继续处理项目，绑定必须的环境变量

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#4-%E7%82%B9%E5%87%BB%E7%BB%A7%E7%BB%AD%E5%A4%84%E7%90%86%E9%A1%B9%E7%9B%AE%E7%BB%91%E5%AE%9A%E5%BF%85%E9%A1%BB%E7%9A%84%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)

[![5a0cc80913848aca4b5f4058538ad6aa|690x333](https://github.com/idinging/freemail/raw/master/pic/v4/depl.png)](https://github.com/idinging/freemail/blob/master/pic/v4/depl.png)

[![5a0cc80913848aca4b5f4058538ad6aa|690x333](https://github.com/idinging/freemail/raw/master/pic/v4/depl5.png)](https://github.com/idinging/freemail/blob/master/pic/v4/depl5.png)

#### 5\. 添加完成后点击部署即可

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#5-%E6%B7%BB%E5%8A%A0%E5%AE%8C%E6%88%90%E5%90%8E%E7%82%B9%E5%87%BB%E9%83%A8%E7%BD%B2%E5%8D%B3%E5%8F%AF)
[code]
    `注：这三个变量是必须的，其他变量例如 管理员名称，发邮件密钥可自行决定是否添加`
    
    最后就可以打开对应的worker连接登陆了
    
[/code]

[![5a0cc80913848aca4b5f4058538ad6aa|690x333](https://github.com/idinging/freemail/raw/master/pic/v4/depl5.jpeg)](https://github.com/idinging/freemail/blob/master/pic/v4/depl5.jpeg)

#### 6\. 默认管理员账号为 admin

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#6-%E9%BB%98%E8%AE%A4%E7%AE%A1%E7%90%86%E5%91%98%E8%B4%A6%E5%8F%B7%E4%B8%BA-admin)

#### 7\. 记得将域名邮箱的catch-all 绑定到worker上（不绑定无法接收到邮件）

[](https://github.com/idinging/freemail/blob/master/docs/yijianbushu.md#7-%E8%AE%B0%E5%BE%97%E5%B0%86%E5%9F%9F%E5%90%8D%E9%82%AE%E7%AE%B1%E7%9A%84catch-all-%E7%BB%91%E5%AE%9A%E5%88%B0worker%E4%B8%8A%E4%B8%8D%E7%BB%91%E5%AE%9A%E6%97%A0%E6%B3%95%E6%8E%A5%E6%94%B6%E5%88%B0%E9%82%AE%E4%BB%B6)

[![5a0cc80913848aca4b5f4058538ad6aa|690x333](https://github.com/idinging/freemail/raw/master/pic/v4/depl6.png)](https://github.com/idinging/freemail/blob/master/pic/v4/depl6.png)
