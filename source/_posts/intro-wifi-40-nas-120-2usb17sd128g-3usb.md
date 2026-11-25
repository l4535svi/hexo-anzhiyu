---
title: intro-wifi-40-nas-120-2usb17sd128g-3usb
date: '2024-09-06 12:00:00'
description: Intro 哈喽伙计们，大家好啊，你们一直让我做小雅的教程，那么这期它来了，我相信我这个这个应该是目前全网价格最低的方式了，其实本来我是准备拿这个（拿起来动作）随身wifi搞了一下，发现是自己想多了，这个东西的玩法很多，感兴趣的可以看我以前的视频，那么咱们退而求其次，就是用玩客云
---
## Intro

* * *

哈喽伙计们，大家好啊，你们一直让我做小雅的教程，那么这期它来了，我相信我这个这个应该是目前全网价格最低的方式了，其实本来我是准备拿这个（拿起来动作）随身wifi搞了一下，发现是自己想多了，这个东西的玩法很多，感兴趣的可以看我以前的视频，那么咱们退而求其次，就是用玩客云了，很多人说太卡无法使用，我用了一段时间没任何问题，视频的最后有一些需要注意的地方，一定要看到最后

最终成本不超过40块？ 一张电影票吧，一起动手，不是nas玩不起，只是垃圾佬就喜欢折腾。

1、机器20块

2、硬盘（可以是usb，机械硬盘（17），固态硬盘，sd卡）反正你有什么用什么，大于128g

3、风扇+废旧usb线+皮筋

直接开始

首先这个视频还是要感谢各位大佬，本期视频用到的内容都是各位大佬提供的，只是在巨人的肩膀上继续二次创作，并综合和分析一下遇到的问题，再次感谢。

## 一、刷机

* * *

1、玩客云armbian固件下载地址：<https://github.com/hzyitc/armbian-onecloud/releases>

下载armbian的底包，刷底包

刷机流程可以看之前的视频，实在不懂的可以看我的公众号文字版。

这边我就快速进行了，不会解释的很详细。

安装所需工具（usb_burning/diskgenius/diskimage/7z）下载：[](https://www.123pan.com/s/YzlRVv-QvxWA.html%E6%8F%90%E5%8F%96%E7%A0%81:2DCq)[https://www.123pan.com/s/YzlRVv-QvxWA.html提取码:2DCq](https://www.123pan.com/s/YzlRVv-QvxWA.html%E6%8F%90%E5%8F%96%E7%A0%81:2DCq)2、安装casaos

通过ssh软件登录 ，账号root密码1234

然后使用老G大佬的一键脚本

## 二、安装小雅alist

* * *
[code] 
    bash -c "$(curl <http://docker.xiaoya.pro/update_new.sh>)" -s host
    
[/code]

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/c2775636-9f30-408a-8e35-d6c8db330690/58b089bc-8b5c-4e55-9bab-37c6c046325b/Untitled.png)

一、获取token等三个链接 1、mytoken.txt的token获取链接（二选一） <https://aliyuntoken.vercel.app/https://alist.nn.ci/zh/guide/drivers/aliyundrive.html>

2、myopentoken.txt的token获取链接 <https://alist.nn.ci/zh/guide/drivers/aliyundrive_open.html>

3、temp_transfer_folder_id.txt的阿里云盘转存目录ID获取链接 （实测在阿里云资源盘的资源库里新建一个文件夹复制浏览器的URL就行了，以下是小雅官方提供的方法）

先转存这个<https://www.aliyundrive.com/s/rP9gP3h9asE> 到自己网盘（选择资源盘），然后浏览器打开转存后的目录，浏览器的url  <https://www.aliyundrive.com/drive/file/resource/640xxxxxxxxxxxxxxxxxxxca8a> 最后一串就是，记得这个目录不要删，里面的内容可以定期删除

如果不能用的情况，需要修改源
