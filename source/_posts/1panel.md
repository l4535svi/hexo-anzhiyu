---
title: 1Panel脚本
date: '2025-01-11 12:00:00'
tags:
- 建站
categories:
- 建站
description: ✅ 卸载1Panel命令行 ✅只要在Linux终端输入1pctl uninstall就能卸载掉1panel。 解释 1pctl uninstall 全选代码 复制 💥上面的卸载命令行，百度和官网找都找不到。 💥最后是在github 关闭的问题里才找到这个卸载1panel 的命令行
---
[![GitHub License](https://camo.githubusercontent.com/026312e46b6ca33936435fc3198e6d8a3103dd8a69e5cdc413b8b4c76cbe2e12/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f77756b6f6e676461696c792f4f72616e676550695368656c6c3f6c6162656c436f6c6f723d25323346463435303026636f6c6f723d626c61636b)](https://camo.githubusercontent.com/026312e46b6ca33936435fc3198e6d8a3103dd8a69e5cdc413b8b4c76cbe2e12/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f77756b6f6e676461696c792f4f72616e676550695368656c6c3f6c6162656c436f6c6f723d25323346463435303026636f6c6f723d626c61636b) [![](https://camo.githubusercontent.com/80de211fbc1a86c4c2f00cbe5e9f50d21fc57b3712ff61263ada42deee8f38eb/68747470733a2f2f6261646765732e746f6f7a68616f2e636f6d2f6261646765732f30314a444b5054445846515959574845505333325153443458542f6f72616e67652e737667)](https://camo.githubusercontent.com/80de211fbc1a86c4c2f00cbe5e9f50d21fc57b3712ff61263ada42deee8f38eb/68747470733a2f2f6261646765732e746f6f7a68616f2e636f6d2f6261646765732f30314a444b5054445846515959574845505333325153443458542f6f72616e67652e737667) [![Bilibili](https://camo.githubusercontent.com/1679ed37639fcdf60c7744dab4d24f924c9698dec285b89b8c38495d054d9f23/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42696c6962696c692d3132333435363f6c6f676f3d62696c6962696c69266c6f676f436f6c6f723d666666266c6162656c436f6c6f723d666237323939)](https://www.bilibili.com/video/BV1ND421T7nB) 

## ✅ 卸载1Panel命令行

✅只要在Linux终端输入1pctl uninstall就能卸载掉1panel。
[code]
    解释
    
    1pctl uninstall
[/code]

全选代码

复制

💥上面的卸载命令行，百度和官网找都找不到。

💥最后是在github 关闭的问题里才找到这个卸载1panel 的命令行

## ✅ Linux 各系统安装1panel

RedHat / CentOS
[code]
    解释
[/code]

curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sh quick_start.sh[![YouTube](https://camo.githubusercontent.com/1f5f74f7ba35dd265d06f593a01c854ef3303f46f9cbd628aeb4104a31cbb704/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f596f75547562652d3132333435363f6c6f676f3d796f7574756265266c6162656c436f6c6f723d666630303030)](https://youtu.be/Ym4d7uCo9eg)

### Armbian/Ubuntu/Debian/Synology 7.2等基于Debian的Linux

[](https://github.com/wukongdaily/OrangePiShell#armbianubuntudebiansynology-72%E7%AD%89%E5%9F%BA%E4%BA%8Edebian%E7%9A%84linux)

解释
[code]
    wget -qO pi.sh https://cafe.cpolar.top/wkdaily/zero3/raw/branch/main/zero3/pi.sh && chmod +x pi.sh && ./pi.sh
    
[/code]

### OpenWrt/iStoreOS 软路由系统

[](https://github.com/wukongdaily/OrangePiShell#openwrtistoreos-%E8%BD%AF%E8%B7%AF%E7%94%B1%E7%B3%BB%E7%BB%9F)

解释
[code]
    wget -qO op.sh https://cafe.cpolar.top/wkdaily/zero3/raw/branch/main/zero3/op.sh && chmod +x op.sh && ./op.sh
    
[/code]

### 其它项目：[RunFilesBuilder——为iStoreOS制作run文件](https://github.com/wukongdaily/RunFilesBuilder)

[](https://github.com/wukongdaily/OrangePiShell#%E5%85%B6%E5%AE%83%E9%A1%B9%E7%9B%AErunfilesbuilder%E4%B8%BAistoreos%E5%88%B6%E4%BD%9Crun%E6%96%87%E4%BB%B6)

### 其它项目：[DockerTarBuilder 利用github action 轻松获得docker离线包](https://github.com/wukongdaily/DockerTarBuilder)

[](https://github.com/wukongdaily/OrangePiShell#%E5%85%B6%E5%AE%83%E9%A1%B9%E7%9B%AEdockertarbuilder-%E5%88%A9%E7%94%A8github-action-%E8%BD%BB%E6%9D%BE%E8%8E%B7%E5%BE%97docker%E7%A6%BB%E7%BA%BF%E5%8C%85)

### debian/飞牛OS [一键安装KVM虚拟机脚本:ARM机型也玩虚拟机](https://github.com/wukongdaily/OneKVM)

[](https://github.com/wukongdaily/OrangePiShell#debian%E9%A3%9E%E7%89%9Bos-%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85kvm%E8%99%9A%E6%8B%9F%E6%9C%BA%E8%84%9A%E6%9C%ACarm%E6%9C%BA%E5%9E%8B%E4%B9%9F%E7%8E%A9%E8%99%9A%E6%8B%9F%E6%9C%BA)

### [TVBOX APK 下载地址](https://tvhelper.cpolar.top/)

[](https://github.com/wukongdaily/OrangePiShell#tvbox-apk-%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80)

### 通过ssh 连接到zero3,举例

[](https://github.com/wukongdaily/OrangePiShell#%E9%80%9A%E8%BF%87ssh-%E8%BF%9E%E6%8E%A5%E5%88%B0zero3%E4%B8%BE%E4%BE%8B)

使用主机名连接ssh `ssh orangepi@orangepizero3.lan`  
或使用ip地址连接ssh `ssh orangepi@192.168.66.106`

  * 默认用户名:`orangepi`
  * 默认密码:`orangepi`  

## ❤️准备：首次使用 如果时间不正确可以先检查硬件时钟时间,举例说明

[](https://github.com/wukongdaily/OrangePiShell#%EF%B8%8F%E5%87%86%E5%A4%87%E9%A6%96%E6%AC%A1%E4%BD%BF%E7%94%A8-%E5%A6%82%E6%9E%9C%E6%97%B6%E9%97%B4%E4%B8%8D%E6%AD%A3%E7%A1%AE%E5%8F%AF%E4%BB%A5%E5%85%88%E6%A3%80%E6%9F%A5%E7%A1%AC%E4%BB%B6%E6%97%B6%E9%92%9F%E6%97%B6%E9%97%B4%E4%B8%BE%E4%BE%8B%E8%AF%B4%E6%98%8E)

解释
[code]
    root@orangepizero3:~# hwclock -r
    1970-01-02 08:03:46.251744+08:00
    root@orangepizero3:~# date -s "2024-08-13 08:54:00"
    Tue Aug 13 08:54:00 CST 2024
    root@orangepizero3:~# hwclock -w
    root@orangepizero3:~# hwclock -r
    2024-08-13 08:54:07.738915+08:00
    root@orangepizero3:~#
    # 上述代码我们分别查询了硬件时钟时间,发现是1970年是错的,接着我们手动设置了当前时间,然后保存硬件时钟时间。
    再次读取硬件时钟时间就正确了。
    此时,你在执行wget等下载操作,就能成功下载脚本了。
    
    
[/code]

  

> 调用命令之前最好先切后到root模式 ubuntu/synology 使用 `sudo -i`  
> debian 使用 `su -`

### QNAP 威联通docker-compose 搭建小雅全家桶

[](https://github.com/wukongdaily/OrangePiShell#qnap-%E5%A8%81%E8%81%94%E9%80%9Adocker-compose-%E6%90%AD%E5%BB%BA%E5%B0%8F%E9%9B%85%E5%85%A8%E5%AE%B6%E6%A1%B6)

解释
[code]
    bash -c "$(curl -fsSL https://cafe.cpolar.top/wkdaily/zero3/raw/branch/main/xiaoya/xiaoya-all.sh)" 
[/code]

### 扩展知识

[](https://github.com/wukongdaily/OrangePiShell#%E6%89%A9%E5%B1%95%E7%9F%A5%E8%AF%86)

> 如何快速获得docker离线镜像  
> <https://github.com/wukongdaily/DockerTarBuilder>

### 网盘

[](https://github.com/wukongdaily/OrangePiShell#%E7%BD%91%E7%9B%98)

  * docker 离线包：<https://wwl.lanzouq.com/s/zero3> 密码:3c60
  * 免费内网穿透工具:<https://i.cpolar.com/m/5Ij6>
  * docker全部离线包：<https://drive.google.com/drive/folders/1lN14zlHeLu0zckHNftpW8kPlqGZHolL8?usp=sharing>
  * zero3开发版 Ubuntu Server(需要解压后再写入TF卡):<https://pan.baidu.com/s/1EKlmccM6STFDb_01rv-qQQ?pwd=2gc7>
  * TF卡写盘工具：<https://etcher.balena.io/>
  * 教学视频：<https://www.bilibili.com/video/BV1ND421T7nB/>
  * 教学视频2:<https://youtu.be/Ym4d7uCo9eg>

# 兼容的系统（ARM64 / AMD64）

[](https://github.com/wukongdaily/OrangePiShell#%E5%85%BC%E5%AE%B9%E7%9A%84%E7%B3%BB%E7%BB%9Farm64--amd64)

系统| 或| 机型  
---|---|---  
Ubuntu ✅| Debian ✅| Deepin ✅  
OpenWrt ✅| iStoreOS ✅| MT-3000 ✅  
NanoPi-R2S ✅| NanoPi-R4S ✅| NanoPi-Neo3 ✅  
Synology 7.2✅| QNAP ✅| UNRAID ✅  
Raspberrypi ✅| Armbian ✅| Zero3 ✅  
  
# 常见问题汇总⬇️⬇️⬇️

[](https://github.com/wukongdaily/OrangePiShell#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB%EF%B8%8F%EF%B8%8F%EF%B8%8F)

[filebrowser 如何设置自定义端口](https://github.com/wukongdaily/OrangePiShell/wiki/filebrowser-%E5%A6%82%E4%BD%95%E8%AE%BE%E7%BD%AE%E8%87%AA%E5%AE%9A%E4%B9%89%E7%AB%AF%E5%8F%A3)

[常见问题总结（持续更新中](https://github.com/wukongdaily/OrangePiShell/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)

[常见问题总结（持续更新中）](https://cafe.cpolar.top/wkdaily/zero3/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB)

# 如何定时重启小雅？

[](https://github.com/wukongdaily/OrangePiShell#%E5%A6%82%E4%BD%95%E5%AE%9A%E6%97%B6%E9%87%8D%E5%90%AF%E5%B0%8F%E9%9B%85)

[使用1panel 添加定时任务即可](https://cafe.cpolar.top/wkdaily/zero3/wiki/%E5%A6%82%E4%BD%95%E5%AE%9A%E6%97%B6%E9%87%8D%E5%90%AF%E5%B0%8F%E9%9B%85)

# 小雅alsit 和 小雅tvbox 有啥区别吗？

[](https://github.com/wukongdaily/OrangePiShell#%E5%B0%8F%E9%9B%85alsit-%E5%92%8C-%E5%B0%8F%E9%9B%85tvbox-%E6%9C%89%E5%95%A5%E5%8C%BA%E5%88%AB%E5%90%97)

解释
[code]
    截止到我做视频的时候，小雅alist 和 小雅tvbox 是有如下区别的。
    1、小雅alist 是比较轻量化的docker。主要是影音库或者理解为一个云端的数据库。它占用内存较低，最多200M内存吧，
    如果你的宿主机内存不大，那么我建议安装这个（视频里演示的那种）。而小雅tvbox，是针对tvbox 这款软件做了一些定制的，
    貌似是用java写的后端？我也不确定，实际测试这款docker大约占用600M内存。x86和arm 都是如此。
    
    2、小雅tvbox 集成了友好的WebUI管理页面，你可以很方便的在4567端口的web页，添加阿里、pikpak账号。
    你还可以定制化tvbox的订阅，详细的文档建议参考作者的项目
    https://github.com/power721/alist-tvbox/blob/master/doc/README_zh.md
    （该作者写的文档相当的细致 爆赞👍）功能很多，配合tvbox 堪称完美！
    
    3、小雅alist 搭建后，最好是配合安装小雅转存清理工具xiaoya-keeper，因为它每次播放或者用播放器搜刮的时候
    可能会转存一份到自己的云盘。如果有这个清理工具就能帮助它迅速删除。避免占用自己的空间。而小雅tvbox 则不需要。
    因为小雅tvbox默认900秒清理一次文件。不过这个数值可以更改为60秒。就在4567网页的高级配置里。
    
    4、小雅alist 的影音数据库的更新操作依赖于容器的重启。因此最好设置一个定时任务，定时重启。（这只是目前为止，
    或许以后作者会加入定时更新的功能，大家还是自行观察每天数据库到底有没有更新，以实际为准。）
    而小雅tvbox，由于在4567的web页面 已经默认开启了定时更新功能，并且还能设置更新的时间。
    
    5、小雅alist默认端口号5678，小雅tvbox默认端口号5344，这个端口号很重要，webdav 如果写错了端口号是无法读取的。
    
    6、小雅alist 和 小雅tvbox 大家二选一就行。尽量别重复搭建。因为小雅tvbox搭建的时候应该也会拉取小雅alist
    这样就重复了。
    
    
    
[/code]

👉👉👉[关于小雅tvbox的介绍可以参考本视频11分后](https://www.bilibili.com/video/BV1ED421V7Dr/?share_source=copy_web&vd_source=0bb92241fb28a55c32c2e5132116b594&t=677) 👈👈👈
