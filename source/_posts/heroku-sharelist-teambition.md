---
title: 通过 Heroku 部署 ShareList 挂载 Teambition
date: '2022-05-09 12:00:00'
cover: /img/covers/heroku-sharelist-teambition.jpg
tags:
- 建站
categories:
- 建站
description: 通过 Heroku 部署 ShareList 挂载 Teambition 最后更新时间：2021年07月26日 注册 Heroku 注册 Github , Fork 下面这两个项目 sharelist sharelist-heroku 在自己 Fork 的 sharelist-h
---
# 通过 Heroku 部署 ShareList 挂载 Teambition

* * *

最后更新时间：2021年07月26日

注册 [Heroku](https://signup.heroku.com/login)

注册 [Github](https://github.com/signup) , Fork 下面这两个项目

  1. [sharelist](https://github.com/reruin/sharelist)
  2. [sharelist-heroku](https://github.com/reruin/sharelist-heroku)

在自己 Fork 的 sharelist-heroku 点击 Deploy to Heroku 按钮  
[![](https://www.2025168.xyz/usr/uploads/2021/07/112865936.png)](https://www.2025168.xyz/usr/uploads/2021/07/112865936.png "点击放大图片")

App name 随便填，CONFIG 配置文件填下面这个，替换成 Fork 的 sharelist 仓库里的对应的 json 地址
[code]
    https://raw.githubusercontent.com/reruin/sharelist/master/package.json
[/code]

点击 deploy app 按钮

[![](https://www.2025168.xyz/usr/uploads/2021/07/2310961895.png)](https://www.2025168.xyz/usr/uploads/2021/07/2310961895.png "点击放大图片")

部署成功后，点击 view 按钮

[![](https://www.2025168.xyz/usr/uploads/2021/07/2051602717.png)](https://www.2025168.xyz/usr/uploads/2021/07/2051602717.png "点击放大图片")

填写口令和虚拟路径，点击保存

[![](https://www.2025168.xyz/usr/uploads/2021/07/4271034734.png)](https://www.2025168.xyz/usr/uploads/2021/07/4271034734.png "点击放大图片")

填写 Teambition 手机号及密码，初始地址按照挂载向导提示填写要绑定的项目或网盘的地址，点击确定  
[![](https://www.2025168.xyz/usr/uploads/2021/07/210239359.png)](https://www.2025168.xyz/usr/uploads/2021/07/210239359.png "点击放大图片")

等待页面自动跳转 ShareList 挂载 Teambition 就完成了

Heroku 免费套餐有休眠策略，即30分钟内无访问 APP 就会休眠，且唤醒后会初始化，导致挂载的云盘被重置

挂载并设置好 ShareList 后点击导出配置

[![](https://www.2025168.xyz/usr/uploads/2021/07/3079667799.jpg)](https://www.2025168.xyz/usr/uploads/2021/07/3079667799.jpg "点击放大图片")

复制导出的配置，打开 Heroku ,找到 settings 里面的变量 CONFIG ，将复制的配置粘帖进去

[![](https://www.2025168.xyz/usr/uploads/2021/07/813942501.jpg)](https://www.2025168.xyz/usr/uploads/2021/07/813942501.jpg "点击放大图片")

这样唤醒时就会自动配置，每次修改后都要导出配置，修改变量 CONFIG

 168

  * [![](https://www.2025168.xyz/usr/themes/Akina/images/wechat.png)](http://qr.liantu.com/api.php?text=https://www.2025168.xyz/index.php/archives/164/)
  * [![](https://www.2025168.xyz/usr/themes/Akina/images/qzone.png)](http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=https://www.2025168.xyz/index.php/archives/164//&title=%E9%80%9A%E8%BF%87%20Heroku%20%E9%83%A8%E7%BD%B2%20ShareList%20%E6%8C%82%E8%BD%BD%20Teambition)
  * [![](https://www.2025168.xyz/usr/themes/Akina/images/sina.png)](http://service.weibo.com/share/share.php?url=https://www.2025168.xyz/index.php/archives/164//&title=%E9%80%9A%E8%BF%87%20Heroku%20%E9%83%A8%E7%BD%B2%20ShareList%20%E6%8C%82%E8%BD%BD%20Teambition)
  * [![](https://www.2025168.xyz/usr/themes/Akina/images/douban.png)](http://shuo.douban.com/!service/share?https://www.2025168.xyz/index.php/archives/164//&title=%E9%80%9A%E8%BF%87%20Heroku%20%E9%83%A8%E7%BD%B2%20ShareList%20%E6%8C%82%E8%BD%BD%20Teambition)



 [默认分类](https://www.2025168.xyz/index.php/category/default/)

声明：Blog on Euserv|版权所有，违者必究|如未注明，均为原创|本网站采用[BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/3.0/)协议进行授权

转载：转载请注明原文链接 - [通过 Heroku 部署 ShareList 挂载 Teambition](https://www.2025168.xyz/index.php/archives/164/)

[PREVIOUS POSTDocker - 实现本地镜像的导出、导入（export、import、save、load）

* * *](https://www.2025168.xyz/index.php/archives/167/)

[NEXT POST使用 ShareX 截图后自动上传到 IPFS

* * *](https://www.2025168.xyz/index.php/archives/154/)

![](https://q.qlogo.cn/g?b=qq&nk=10086&s=100)
