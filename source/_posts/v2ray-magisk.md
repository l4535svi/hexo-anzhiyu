---
title: V2ray-magisk模块使用教程
date: '2022-03-01 12:00:00'
cover: https://picsum.photos/seed/v2ray-magisk/800/450
tags:
- 免流搭建安卓
- 科学上网
categories:
- 免流搭建安卓
description: V2ray-magisk模块优点： 1.跳点低，本人测试10G跳1M 2.无需后台，节省内存，不会自动关闭 3.开机自启，无需手动打开 4.可任意放行TCP&UDP（教程写在后面） 5.可选择代理WiFi和流量，实现无缝切换，既不影响不需要代理的WiFi，也不影响需要免流的流量。
---
### V2ray-magisk模块优点：

#### 1.跳点低，本人测试10G跳1M

#### 2.无需后台，节省内存，不会自动关闭

#### 3.开机自启，无需手动打开

#### 4.可任意放行TCP&UDP（教程写在后面）

#### 5.可选择代理WiFi和流量，实现无缝切换，既不影响不需要代理的WiFi，也不影响需要免流的流量。

#### 6.可以直接开热点，省去繁杂的软件和设置。即开即用。

### 

### 安装教程

1.首先在Magisk中刷入V2ray模块-4.40.1

刷入成功后重启手机，在magisk可以看到v2ray模块已经刷入，如图

![](https://telegra.ph/file/3c38c11caebce92ab3eda.jpg)

2.使用MT管理器，授予MT管理器Root权限，点开左上角打开侧栏，点击根目录

![](https://telegra.ph/file/a9633b83f738a4da74a9f.png)

依次点击data

![](https://telegra.ph/file/c9bd28d91a26b20578533.jpg)

以及data目录下v2文件夹

![](https://telegra.ph/file/4b0a65e4cb519b48da74a.jpg)

进入v2文件夹后，查看两处标记处路径及文件是否一致

![](https://telegra.ph/file/2ad00739b79d3c5a3c726.jpg)

如果一致，则刷入成功，否则重新刷入V2ray-Magisk模块

3.点击一键导入订阅.sh，点击编辑，

![](https://telegra.ph/file/60147873f8956bd77ae5c.jpg)

按照顺序依次填写

1处填写你在官网复制的订阅链接

![](https://telegra.ph/file/d1b6c0abfc998b40efd99.png)

2处填写你需要用的混淆

更多混淆请加入Tg群，查看置顶消息

3处填写订阅名称，此处随意填写，不强求

![](https://telegra.ph/file/65bba178654f1156354a6.jpg)

保存退出。

![](https://telegra.ph/file/6345106217958cca49820.jpg)

4.执行一键导入订阅.sh

![](https://telegra.ph/file/d6f0084d82f15b6548ccd.jpg)

z执行完成后进入节点选择文件夹

![](https://telegra.ph/file/819b02dd8a280272e08dc.jpg)![](https://telegra.ph/file/8b8eeacdf365c7346b187.jpg)

点击你需要使用的节点，再次执行

![](https://telegra.ph/file/102fcbab1a9bceb09d377.png)

退回到上一个文件夹，点击开启v2.sh，执行

![](https://telegra.ph/file/f8b23882f8bece404ad85.jpg)![](https://telegra.ph/file/b021c6223f67ebba79d5a.png)

如下图所示

Core：后两个都是√

以及IP地址IP位置出现变化，v2ray就开启成功了

![](https://telegra.ph/file/444a289bef8878b2c8a8e.jpg)

### V2ray-magisk模块放行TCP&UDP教程

![](https://telegra.ph/file/529bc1dfd50a7c31801bb.jpg)![](https://telegra.ph/file/9f37b0a25389d14cd1bc8.jpg)![](https://telegra.ph/file/c2b57ffd37823335cbbbf.jpg)![](https://telegra.ph/file/985464e005f4294ff4914.jpg)

### 包名或者UID二选一即可

![](https://telegra.ph/file/ac4049683f6a2ba6debfd.jpg)编辑config.ini![](https://telegra.ph/file/509a87a78ebcf269e4281.jpg)

### 保存退出，再次执行开启v2.sh
