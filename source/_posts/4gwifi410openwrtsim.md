---
title: 4g随身wifi高通410刷openwrt软路由插sim卡无法识别问题解决方案！
date: '2024-09-30 12:00:00'
cover: https://picsum.photos/seed/4gwifi410openwrtsim/800/450
tags:
- 科学上网
categories:
- 科学上网
description: 工具 百度连接： 链接： https://pan.baidu.com/s/1tmvK9bpOeXIMYLLA2hy72Q?pwd=rs99 提取码：rs99 --来自百度网盘超级会员V4的分享 合集工具：随身Wi-Fi.7z 合集工具里包含了所有东西 ①驱动 :ADB驱动安装工具
---
工具

 

百度连接：

链接：<https://pan.baidu.com/s/1tmvK9bpOeXIMYLLA2hy72Q?pwd=rs99> 提取码：rs99 \--来自百度网盘超级会员V4的分享

 

 

合集工具：随身Wi-Fi.7z

合集工具里包含了所有东西

①驱动 :ADB驱动安装工具(通用)、vivo9008drivers.exe

②救砖备份  ：MiKo、QualcommPremiumTool、星海

③图形化桌面

④调试 ：搞机工具箱V9.10

⑤固件包：苏苏小亮亮固件包debian/openwrt

容我偷个懒不想重复造轮子（才不是步骤多不想写）详细的教程可以去 这位博主的论坛>>>> <https://qust.me/post/msm8916>

上面的合集工具都出自他，他的教程也不错，让我都不想写了。

 

重点的重点！！ 

## 

[](https://blog.baily.life/article/87dc57ee-aa63-4f4c-b5c4-75ee7ddac63b#05b0014e2c524c3e98f53386aa81f04e "一定要切好卡能上网之后保存的xxx.bin备份文件！ 不然是无法插卡识别的！")一定要切好卡能上网之后保存的xxx.bin备份文件！ 不然是无法插卡识别的！

 

关于openwrt下接口提示：错误: 正在拆卸调制解调器载体。

![notion image](https://songw.top/wp-content/uploads/2023/03/QQ%E6%88%AA%E5%9B%BE20230315005052.png?t=dd046f33-a343-4a6e-8e50-c4c13d411768)

1.可以用miko备份的文件包xxx.bin文件里面的 0.modem.fat （可以用7z压缩工具打开提取）

![notion image](https://songw.top/wp-content/uploads/2023/03/QQ%E6%88%AA%E5%9B%BE20230315005322.png?t=782942f8-f61e-4043-b6c5-f513e057b7ef)

2.在提取 0.modem.fat （可以用7z压缩工具打开提取）到一个文件夹

![notion image](https://songw.top/wp-content/uploads/2023/03/QQ%E6%88%AA%E5%9B%BE20230315005329.png?t=91b71af4-6ad4-43a9-92b4-ab21e5d37f50)

网盘中也有我提取的 ufi103s_v02_提取的modem.7z 建议同一主板印编号的用

3.在用WinSCP等工具登录ssh 上传到root文件夹里 ，上传完毕后执行ssh命令：

把image下面的所有文件复制到 /lib/firmware/ ，reboot重启棒子

`cd image/`

`cp ./* /lib/firmware/`

`du -sh /lib/firmware/`

`reboot`

例子：

### plain
[code]
    root@HandsomeMod:~# ls
    image
    root@HandsomeMod:~# cd image/
    root@HandsomeMod:~/image# ls
    cmnlib.b00 keymaste.b01 modem.b01 modem.b10 modem.b17 modem.b25 playread.mdt wcnss.b09 widevine.b02
    cmnlib.b01 keymaste.b02 modem.b02 modem.b11 modem.b18 modem.mdt wcnss.b00 wcnss.b10 widevine.b03
    cmnlib.b02 keymaste.b03 modem.b03 modem.b13 modem.b19 playread.b00 wcnss.b01 wcnss.b11 widevine.mdt
    cmnlib.b03 keymaste.mdt modem.b04 modem.b14 modem.b22 playread.b01 wcnss.b02 wcnss.mdt
    cmnlib.mdt mba.mbn modem.b05 modem.b15 modem.b23 playread.b02 wcnss.b04 widevine.b00
    keymaste.b00 modem.b00 modem.b08 modem.b16 modem.b24 playread.b03 wcnss.b06 widevine.b01
    root@HandsomeMod:~/image# du -sh ./44.2M ./
    root@HandsomeMod:~/image# cp ./* /lib/firmware/
    root@HandsomeMod:~/image# du -sh /lib/firmware/45.6M /lib/firmware/
[/code]

Plain text

Copy

重启后接口正常了

![notion image](https://songw.top/wp-content/uploads/2023/03/QQ%E6%88%AA%E5%9B%BE20230315011156.png?t=410e9fdf-c7e8-421a-b390-3593bbc2e457)

补充：这个方法同时可以解决 debian 不读卡没网络问题
