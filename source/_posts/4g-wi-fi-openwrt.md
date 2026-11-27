---
title: 4g 随身 Wi-Fi 刷 openwrt 变成软路由
date: '2024-09-28 12:00:00'
cover: /img/covers/4g-wi-fi-openwrt.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 首先感谢酷安「随身 Wi-Fi」 社区，里面有很多资料可以参看； 燕子博客 的教程也非常详细，以及 handsomehacker 开源的 debian 系统和「苏苏小亮亮」（酷安ID）编译的 openwrt，以及 Zy143L 博客 的拆解和帮助。 这是一个二十多块就能买到的，
---
![](https://oss.qust.me/img/202206022052349.JPG)

首先感谢酷安「随身 Wi-Fi」 社区，里面有很多资料可以参看；[燕子博客](https://yanziblog.top/291/)的教程也非常详细，以及 handsomehacker [开源的 debian](https://www.kancloud.cn/handsomehacker/openstick/2636505) 系统和「苏苏小亮亮」（酷安ID）编译的 openwrt，以及 [Zy143L 博客](https://momoe.ml/)的拆解和帮助。

这是一个二十多块就能买到的， 4G USB 随身 Wi-Fi，你可能不会想到它居然跑的是安卓系统。并且还能刷 debian 系统，甚至你还能刷 openwrt 成为软路由，更棒的是 4G 和 Wi-Fi 、USB 等功能都正常工作。

本教程不会讨论 ML 也不讨论使用自带的 esim 套餐，openwrt 只使用自己的卡。

## 前言

![](https://oss.qust.me/img/202206022035737.JPG)

购买一个随身 Wi-Fi 这里面门道确实挺多，也有点碰运气（因为卖家基本都不会标注具体的型号，你也别问卖家不会和你说）。你在淘宝、或者闲鱼搜随身 Wi-Fi 便宜的有从几块到几十不等的。

你可能会好奇为啥会这么便宜？ 首先便宜的随身 Wi-Fi 基本用的都是工模的方案，像是高通的 410、高通的 210、中兴微等方案，外观差别可能很大，内在或许都是同一种方案（同一种方案具体的板子也会有不同），当然也会有可能同一个商品发给买家不同的型号；其次低价的随声 Wi-Fi 商品基本都会有流量套餐选择，里面有一张 esim 卡，你扫码实名认证激活就能使用，当然大部分里面其实都是有一个实体卡槽的（也有坑的产品没有），可以使用自己的手机卡套餐，只是需要自己手动切卡（本教程是使用自己手机卡，如果你非要选择商家套餐，也推荐按月购买，坑就不多说了）。

商家标识的是单网能买吗？ 没啥问题。因为方案都完全一样的，实际大多数都是支持电信联通，移动也可以通过刷基带的办法解决实现三网通，就是移动会麻烦很多。

![](https://oss.qust.me/img/202206022127135.jpeg)

所以我应该哪买，买哪款？ 酷安「随身 Wi-Fi」 社区，你可以蹲到很多几块、十几元的便宜的车；或者嫌麻烦直接买别人标注了版本，刷好三网通的，甚至还有改好了风扇的。

默认基本的配置都是： 高通410 四核 1.2GHz CPU、512M 内存、4G emmc 闪存、默认 android 4.4 系统。

## 准备工作

  1. 高通410（msm8916）方案的随身 Wi-Fi：板子上的丝印是 UFI001B、UFI001C、UFI003、UFI-W-001 最好，或者 SP970（不推荐，细分版本目前13个太多，基本要短接才能进 9008 模式，然后现在的 openwrt Wi-Fi 也有问题）、UZ801 也 OK；需要带卡槽、能切卡。
  2. 一台 Windows 电脑（建议安装火绒，一些文件会被 Win 默认防护当病毒删除）
  3. 小卡转大卡 SIM 卡套
  4. 螺丝刀（拧随身 Wi-Fi 十字小螺丝）
  5. 下载刷机需要的工具文件 [百度云](https://pan.baidu.com/s/15a2Imo4NcdG9u7ijsuHSAA) 提取码：1fqr 或自建 [onedrive](https://share.qust.me/%E8%B7%AF%E7%94%B1%E5%99%A8/%E9%9A%8F%E8%BA%AB%20wifi) 和 [「苏苏小亮亮」编译的 openwrt](https://www.kancloud.cn/a813630449/ufi_car/2792820)

附带下我购买的 5 个产品的情况：

```

    铁恒信旗舰店 54 元款：UFI003 （后台密码 admin、切卡密码 UFIadmin1234）
    天天特卖工厂店 29 元款：SP970-Main-v2（后台：admin admin，切卡用酷安工具，无法直接进 9008，openwrt wifi 有问题不推荐）
    酷翼旗舰店 8.8 元款：UFI003 （后台密码 admin、切卡密码 无）
    纽皇 6.8 元款：可能是 UFI001W ？？？（后台密码 admin、切卡密码：qr0521）但会抽奖碰到高通 210 款
    天天特卖工厂店 28 元款 UFI001 C （后台密码 admin、切卡密码：UFIadmin1234，现在改成没卡槽了）
    

```

## 检查和备份

### 检查

![](https://oss.qust.me/img/202206011136328.JPG)

到手后第一件事，先插上电，连上随身 Wi-Fi 提供的 Wi-Fi，进入后台，检查下是否能正常工作，防止到手就是坏的；然后用螺丝刀拆开检查板子，是否有卡槽，以及上面的版本丝印。（可以看到我的这款有卡槽，丝印是：UFI003_MB_V002 ）

### 全量备份

做好全量备份就不会变砖，随时刷成到手的状态。

![](https://oss.qust.me/img/202206011221325.PNG)

首先安装下载好的 9008 驱动

![](https://oss.qust.me/img/202206011224831.JPG)![](https://oss.qust.me/img/202206011225387.PNG)

按住拇指位置的按钮插上电脑（一般不会有亮灯），在电脑设备管理器-端口设备里能看到 9008 的 COM 设备就说明连接上了。

![](https://oss.qust.me/img/202206011311176.PNG)![](https://oss.qust.me/img/202206011315425.PNG)

然后安装下载好的 miko，并将 Loader 移动到安装的路径下面（默认在 C:\Program Files (x86)\miko_service_tool_pro\miko_service_tool_pro），打开 Loader。

![](https://oss.qust.me/img/202206011320691.PNG)

然后在 miko 里依次选择 Read - Partition Backup/Earese - 点击左下角 Load Partition Structure 看到右边有系统信息的输出就说明连上了。

![](https://oss.qust.me/img/202206011323311.PNG)

然后点击 Read Full Image 选个路径，取个名字就开始全量备份救砖能用的 .bin 文件。过程会比较慢，可能要十几分钟。等到跑完进度条 100% 右边的输出显示 success 就备份好了，我们就能开始随意折腾。

## 切换网络（电信基本可跳过此步）

![](https://oss.qust.me/img/202206021434936.jpg)

你可以在默认的安卓系统下直接从默认的 esim 切到你自己的卡来验证是否有网，一般联通电信都是可以正常工作的，因为刷写 openwrt 会直接使用安卓系统里的基带分区，如果使用自己的卡网络正常，可以直接跳到下一步刷 openwrt，也就是说只有切卡不能正常使用你才需要刷基带，另外刷 openwrt 目前有个 BUG ：你只能使用在刷前安卓上正常工作的运营商的卡。

比如看图中我插入使用的是联通卡正常工作，我刷 openwrt 就只能使用联通的卡。

![](https://oss.qust.me/img/202206021756208.JPG)

插卡使用时，记得扣上这个「小帽子」，这是随身 Wi-Fi 的天线部分，如果不扣上信号会非常弱甚至没网。如果你要使用移动的卡，或者你联通卡不能正常工作，那你可能需要刷下基带。

## 刷入 openwrt

刷入 openwrt 十分简单，因为「苏苏小亮亮」已经做好了一键刷入的包。刷入前请确认你安卓里你插入使用的 SIM 卡正常工作。

### 进入 fastboot 模式

![](https://oss.qust.me/img/202206021811254.PNG)

随身 Wi-Fi 插在电脑会默认开启 adb ，我们打开搞机工具箱，选择线刷专区，重启到 Fastboot，一般重启 fastboot 后随身 Wi-Fi 会亮红灯。

### 刷写系统

![](https://oss.qust.me/img/202206021821886.PNG)

打开解压好对应版本的 openwrt 文件夹（如果是 UFI001W 刷 UFI001C 的包），然后双击 flash.bat 就能开始刷机。观察是否都正常刷入，如果有错误，可以重新打开 flash.bat 再重新插入随身 Wi-Fi 。

![](https://oss.qust.me/img/202206021817996.jpg)

能搜索到 HandsomeMod Wi-Fi 就是 openwrt 刷好了。默认的后台地址是 192.168.1.1 用户名是 root 没有密码。

### 检查 modem 网络

![](https://oss.qust.me/img/202206021825567.jpg)

在后台网络接口里，检查 MODEM 是否能正常获取 IP 地址，如果能那说明 SIM 卡能正常联网使用，你现在的 Wi-Fi 应该也是有网络的。

### 修改软件源

![](https://oss.qust.me/img/202206041344422.jpg)

在 openwrt 里的软件包里选择配置 OPKG，将 /etc/opkg.conf 里的内容替换为以下：

```

    dest root /
    dest ram /tmp
    lists_dir ext /var/opkg-lists
    option overlay_root /overlay
    arch all 1
    arch noarch 1
    arch aarch64_cortex-a53_neon 10
    arch aarch64_cortex-a53 100
    

```

将 /etc/opkg/distfeeds.conf 内容替换为：

```

    src/gz reboot_base http://mirrors.cloud.tencent.com/lede/releases/21.02.3/packages/aarch64_cortex-a53/base
    src/gz reboot_luci http://mirrors.cloud.tencent.com/lede/releases/21.02.3/packages/aarch64_cortex-a53/luci
    src/gz reboot_packages http://mirrors.cloud.tencent.com/lede/releases/21.02.3/packages/aarch64_cortex-a53/packages
    src/gz reboot_routing http://mirrors.cloud.tencent.com/lede/releases/21.02.3/packages/aarch64_cortex-a53/routing
    src/gz reboot_telephony http://mirrors.cloud.tencent.com/lede/releases/21.02.3/packages/aarch64_cortex-a53/telephony
    src/gz openwrt_kiddin9 https://op.supes.top/packages/aarch64_cortex-a53
    
    

```

然后点击保存，就能通过 opkg 安装需要的软件包了。

![](https://oss.qust.me/img/202206041352138.jpg)

比如给系统安装个好看点的 argon 主题。

### 安装 shellclash

![](https://oss.qust.me/img/202206021907402.jpg)

直接使用低版本的 wget 安装 shellclash。

```

    export url='http://shellclash.cf/' && wget -q -O /tmp/install.sh $url/install.sh  && sh /tmp/install.sh && source /etc/profile &> /dev/null
    

```

![](https://oss.qust.me/img/202206021911781.jpg)

配置好应该就能上网了，变成「随身翻」

![](https://oss.qust.me/img/202206021912268.jpg)

目前 4g 的网速确实不快，只有 4Mbps 左右，估计得靠 openwrt 更新优化了。

## 疑难杂症

### 刷写基带

酷安 qq 群：743509392 有很多这方面的资料。

大部分 UFI00X 丝印的随身 Wi-Fi 都是支持电信卡的，很多其实也支持联通，移动大概率默认是不支持的。当然因为产品众多，甚至丝印型号相同用的 modem 型号都有差别，当然最麻烦的其实也是这一步，不能保证你刷了基带后移动联通就能正常使用，还是更推荐电信或联通用户使用。

先使用搞机工具箱重启进入 fastboot 模式。

![](https://oss.qust.me/img/202206021934100.PNG)

然后打开星海工具箱-选择高通-选择高通基带擦除-一键执行，完成后会重启。(如果你的星海无法打开你可能得安装下[微软的这个包](https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170))

![](https://oss.qust.me/img/202206021947102.PNG)

然后勾选写入 QCN，选择全网通的基带写入。会可能一次写入不成功，多写入几次。重启随身 Wi-Fi，看看你的卡能不能正常工作。

### 默认没开 adb 的设备

![](https://oss.qust.me/img/202206022024769.PNG)

如果你的型号是 UFI001W 等，可能你到手设备并没有打开 adb 功能，你可以在 web 后台尝试重置，如果仍然不行。直接 9008 模式用 miflash 工具刷别人改好的包，浏览里选择下载解压好的包，刷新勾选设备，点击刷机即可。会直接开启adb、锁定插入的 SIM 卡、和 root 等功能。

### 从 openwrt 刷回原厂备份

[我的备份](https://pan.baidu.com/s/1_99uOa4M2RP_Ipix6t2zFQ)（如果你正好版本相同需要） 提取码：3cad

![](https://oss.qust.me/img/202206022026793.PNG)

如果你的 openwrt 有问题，或者你想刷回原厂也很简单。随身 Wi-Fi 9008 模式插上电脑，打开第一步备份使用的 miko loader 程序。选择 Flash - emmc block0 flasher - 双击勾选备份好的文件-选择 flash，等待进度条跑完，可能会很慢。

## 总结

目前这个阶段，高通 410 芯片的随身 Wi-Fi 刷 openwrt 更多还是像个有意思的玩具，你不能指望它有多快。当然目前的 openwrt 才刚刚出来，以后迭代可能会好很多。随身 Wi-Fi 刷 openwrt 其实很简单，进入 fastboot 一键脚本就能刷成，当前更多的问题是版本太多，基带的问题，换句话说如果你是电信用户，那么确实简单很多 。
