---
title: JDC-1800pro 亚瑟京东云 免拆刷机 基础刷uboot以及备份
date: '2026-11-05 12:00:00'
cover: /img/covers/jdc-1800pro-uboot.jpg
tags:
- 软路由
categories:
- 软路由
description: 二、现在执行最后验证 先执行： sync md5sum /dev/mmcblk0p13 md5sum /dev/mmcblk0p14 两个结果都必须是： 2266697f5106c170a91e283adf7a3d19 注意！！刷机风险！有可能会因为各种不确定因诉 导致设备永久性
---
## 二、现在执行最后验证

先执行：

```

    sync
    md5sum /dev/mmcblk0p13
    md5sum /dev/mmcblk0p14

```

两个结果都必须是：

```

    2266697f5106c170a91e283adf7a3d19

```

  

  

注意！！刷机风险！有可能会因为各种不确定因诉 导致设备永久性损坏！！请慎重考虑！！

  

注意！！刷机风险！有可能会因为各种不确定因诉 导致设备永久性损坏！！请慎重考虑！！

  

我也会尽量把细节说到位 把风险降到最低 如果是头次搞这个型号 最好就整体预览一遍教程 大概了解每一步要干什么 再跟着来

若想转载/摘抄本帖 请标明出处 免费教程~倒卖冚家铲！！！！

  
  

接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~

  

接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~接受风险请往下~

  

  

固件下载-->[00-iStoreOS-jdcloud_ax1800-pro-R23.09.09-ipq60xx-generic-squashfs-factory.zip - 蓝奏云](https://lanzouv.com/ijRaK2upcnyh)

http服务器-->[hfs.exe--密码0000](https://lanzouv.com/iAp953fiigyf)

(开源固件 不太完善  但是不用大分区就能刷上  觉得可以直接用也没问题。想进阶玩的 还是备份完了到时候刷到大分区

  
支持最新的4546版本开启telnet: (有刷机需要的赶紧! 不然估计很快连夜ota !  
进入路由器后台使用F12开发者控制台执行下面指令  

  1. (async () => {  

  2.   const session = document.cookie.split('; ').find(r => r.startsWith('sessionid='))?.split('=')[1];  

  3.   if (!session) {  

  4.     console.error('未登录，请先登录京东云路由器后台');  

  5.     return;  

  6.   }  

  7.   const exec = async (cmd) => {  

  8.     await fetch('/jdcapi', {  

  9.       method: 'POST',  

  10.       body: JSON.stringify({  

  11.         jsonrpc: '2.0',  

  12.         id: 1,  

  13.         method: 'call',  

  14.         params: [session, 'jdcapi.static', 'set_port_forward', {  

  15.           'on-off': 1,  

  16.           name: 't1',  

  17.           proto: 'TCP',  

  18.           'src-dport': `1234;\\`${cmd}\\``,  

  19.           ipaddr: '192.168.1.100',  

  20.           'dest-port': '80',  

  21.           edit: 1  

  22.         }]  

  23.       })  

  24.     });  

  25.   };  

  26.   try {  

  27.     await exec('factory_hm info telnet 1');  

  28.     await exec('telnetd');  

  29.     console.log('Telnet 已开启，连接地址：路由后台ip地址 账号root 密码:后台管理密码');  

  30.   } catch (e) {  

  31.     console.error('开启失败', e);  

  32.   }  

  33. })();

![](https://www.right.com.cn/forum/data/attachment/forum/202606/14/035118a9dr5b2byrvyrn2h.png)  
  
  

telnet刷uboot: (回复可见  

#### 本帖隐藏的内容

打开hfs 并同意网络 将uboot文件拖入hfs服务端

然后路由telnet窗口执行拉取并刷uboot以及清除BOOTCONFIG/1 电脑静态192.168.68.11 路由后台192.168.68.1 文件下载请往下-uboot文件以及大分区下载

(还有拉不过去就检查端口 还有关闭win防火墙 win+R运行 firewall.cpl 启用或关闭防火墙 专用网络和访客网络都关闭防火墙 拉取成功后可启用防火墙)

md5要和下面的一模一样！！！不然停止执行并检查文件完整性 ！！！不然直接刷入可能会重启砖头！！！如果报错未找到文件 请检查文件是否有正确上传

uboot来自沉心大佬-->[github-chenxin527-ipq6000-emmc新版uboot](https://github.com/chenxin527/uboot-ipq60xx-emmc-build)

  1. wget -P /tmp http://192.168.68.11/uboot-ipq60xx-emmc-jdcloud_re-ss-01-260102.153309.bin  

  2. md5sum /tmp/uboot-ipq60xx-emmc-jdcloud_re-ss-01-260102.153309.bin  

  3. ##2266697f5106c170a91e283adf7a3d19--确保md5值一样再刷入  

  4. dd if=/dev/zero of=/dev/mmcblk0p2  

  5. dd if=/dev/zero of=/dev/mmcblk0p3  

  6. dd if=/tmp/uboot-ipq60xx-emmc-jdcloud_re-ss-01-260102.153309.bin of=/dev/mmcblk0p13  

  7. dd if=/tmp/uboot-ipq60xx-emmc-jdcloud_re-ss-01-260102.153309.bin of=/dev/mmcblk0p14

  

  

  

备份 方法二选一即可 (强烈建议备份之后再折腾 有备无患

1-----ax6600底层分区 以及原厂跑分认证信息备份磁盘镜像 备份到内置跑分分区：

指令在下 备份需要几分钟的样子 取决于CPU还有mmc的读写速度  
保存到内置跑分配置分区：（确保有足够空间 备份出的文件1111m

原厂开启smb文件共享 注意：需要在备份指令执行之前完成本地网盘切换 否则切换后跑分分区里面的里面文件将被清除

或者在保留原来分区表刷wrt后 ssh/文件传输/smb 下载/mnt/mmcblk0p27/1.95g-ax6600.img

  1. dd if=/dev/mmcblk0 bs=1M count=1111 of=/mnt/mmcblk0p27/ax1800-1111m.img

2-----ax6600底层分区 以及原厂跑分认证信息备份磁盘镜像 备份到U盘:

保存到usb硬盘/u盘的设备分区：（确保有足够空间 备份出的文件2.5g '/mnt/sda/'替换为实际文件路径

  1. dd if=/dev/mmcblk0 bs=1M count=1111 of=/mnt/sda/ax1800-1111m.img

备份/恢复更详细----->[京东云亚瑟ax1800pro/雅典娜ax6600 备份原厂跑分底层数据-OPENWRT专版-恩山无线论坛 - Powered by Discuz!](https://www.right.com.cn/forum/thread-8471788-1-1.html)

进阶大分区等--->[亚瑟ax1800pro/雅典娜ax6600/太乙ER1 京东云 进阶gpt cdt-OPENWRT专版-恩山无线论坛 - Powered by Discuz!](https://www.right.com.cn/forum/thread-8426276-1-1.html)

系统已经起不来拆机刷机教程--->[(保姆级) 亚瑟ax1800pro 京东云 刷机 基础刷uboot以及备份-OPENWRT专版-恩山无线论坛 - Powered by Discuz!](https://www.right.com.cn/forum/thread-8424961-1-1.html)

  

uboot文件以及ssh客户端下载：

#### 本帖隐藏的内容

文件下载[jdc-ax1800pro-shua.zip - 蓝奏云](https://lanzouv.com/iuRFB3r4ejyh)

  

  

广告区：

如不想自己动手刷 或有改内存 或者其他技术支持的需要

可到海鲜市场找--->[鲜鱼直达](https://m.tb.cn/h.i64sw6j?tk=2Edy5a3URV6)

若链接失效 直接搜索: V_2333
