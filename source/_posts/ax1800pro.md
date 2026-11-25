---
title: 京东AX1800Pro最佳实践折腾记
date: '2025-08-25 12:00:00'
tags:
- 软路由
categories:
- 软路由
description: 最近买了个很火的路由，京东AX1800Pro，刷机神器，这篇文章记录一下改造过程的最佳实践，也是对用openwrt这么久以来的一个简单总结。 京东亚瑟AX1800Pro是一款用来挖京豆的PCDN路由器，现在各家ISP对滥用PCDN处罚越发严格，甚至是有可能导致封网，但并不妨碍刷机
---
* * *

![/d5262f31-4455-40d0-b94a-7df386c93119/jd1.jpg](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/jd1.jpg)

最近买了个很火的路由，京东AX1800Pro，刷机神器，这篇文章记录一下改造过程的最佳实践，也是对用openwrt这么久以来的一个简单总结。

京东亚瑟AX1800Pro是一款用来挖京豆的PCDN路由器，现在各家ISP对滥用PCDN处罚越发严格，甚至是有可能导致封网，但并不妨碍刷机后干掉原路由器系统，并大大扩展路由器的功能。

## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E5%88%B7%E6%9C%BA%E5%8F%8A%E5%9B%BA%E4%BB%B6%E8%AE%BE%E7%BD%AE)刷机及固件设置

iStoreOS是一个修改版的openwrt系统，在原系统上做了一定的优化和bug修复，亚瑟的路由iStore固件可以在这里下载: <https://fw.koolcenter.com/Lean/JDC_AX1800_Pro/>,在uboot中刷入用factory包，在iStoreOS中刷入用sysupgrade包。

理论上如果要刷超过60M的固件是要改大分区表，怎么刷机和改分区表的文章非常多了，供参考。

> ssh刷机（适合2204以前版本），刷CDT

[小白也能看懂的京东云亚瑟 AX1800 Pro 刷机教程](https://www.yindan.me/tutorial/jdc-ax1800-pro.html)

> 2204以后版本刷机

[京东云AX1800 Pro亚瑟超神！免拆开启SSH刷机＆看这一篇就够了](https://mao.fan/article/72)

另外根据我刷机的情况来讲，这个机器内存太小，运行起来很容易出现OOM问题（暴内存），虽然加SWAP可以解决问题，但是运行速度还是会很受影响的，所以强烈推荐改到1G的内存，我在闲鱼上找了一家花了50改机成功。

### [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E8%B0%83%E6%95%B4%E5%88%86%E5%8C%BA%E8%A1%A8)调整分区表

ssh远程，安装cfdisk
[code]
    1
    2
    
[/code]

| 
[code]
    opkg update
    opkg install cfdisk
    
[/code]  
  
---|---  
  
cfdisk /dev/mmcblk0，选择Free sapce, 再最下面的菜单选择New, 直接按回车选择剩余空间分配。选择Write, 回车。选择quite退出。

还可以合并一些不需要用的分区，注意有些特殊的分区不能合并，会破坏uboot变砖，fdisk -l，可以看到现在多了一个100多G的/dev/mmcblk0pxx(数字为分区的最后一个)分区了。

格式化分区mkfs.ext4 /dev/mmcblk0pxx，打开iStoreOS后台，在系统-挂载点-生成配置, 然后在挂载点找到刚刚的新分区

修改选择刚刚的新分区, 启用此挂载点，推荐挂载到/opt目录下, 重启iStoreOS

### [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E9%AD%94%E6%B3%95%E4%B8%8A%E7%BD%91%E6%8F%92%E4%BB%B6%E5%BC%80%E5%90%AF)魔法上网插件开启

因为这个固件是基于lean的openwrt的修改版本，所以有个魔法开关
[code]
    1
    
[/code]

| 
[code]
    echo 0xDEADBEEF > /etc/config/google_fu_mode
    
[/code]  
  
---|---  
  
刷新页面即可使用需要的插件

### [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E5%BC%80%E5%90%AFswap)开启swap

即使改了1G的ram，也建议打开swap，很可能运行进程过多依然会有oom问题，我在这里开启了1GB的swap，在内存不足的时候，系统则会用swap文件扩容内存，在挂载的/opt路径下，运行如下命令
[code]
    1
    2
    
[/code]

| 
[code]
    dd if=/dev/zero of=/opt/swapfile bs=1M count=1024
    mkswap /opt/swapfile
    
[/code]  
  
---|---  
  
创建开机脚本如下，命令:
[code]
    1
    
[/code]

| 
[code]
    vi /etc/init.d/swap
    
[/code]  
  
---|---  
  
在vi中粘如下代码
[code]
    1
    2
    3
    4
    5
    6
    7
    8
    
[/code]

| 
[code]
    #!/bin/sh /etc/rc.common
    START=99
    start() {
        swapon /opt/swapfile
    }
    stop() {
        swapoff /opt/swapfile
    }
    
[/code]  
  
---|---  
  
运行命令使swap开机启动生效:
[code]
    1
    2
    
[/code]

| 
[code]
    chmod +x /etc/init.d/swap
    /etc/init.d/swap enable
    
[/code]  
  
---|---  
  
## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E9%98%BF%E9%87%8C%E4%BA%91ipv6%E5%8A%A8%E6%80%81dns%E8%AE%BE%E7%BD%AE)阿里云IPv6动态DNS设置

这个功能主要的作用是方便我们离家时可以随时想连回来做准备，另外IPv4基本上家宽是拿不到公网IP的，可以不用考虑IPv4的动态DNS问题了，

默认WAN口的IPv6是开启的，需要和宽带服务商协商好，打开IPv6和IPv4的双栈拨号，这是前提。

打开iSotreOS管理台，服务->动态DNS，添加中随便取个名，进入配置。

在基本设置里，查询主机名就填我们已经有的（可以弄个二级域名，记录类型设置为AAAA），IP地址版本选IPv6地址

DDNS服务提供商这里我选的是阿里云(aliyun.com)，当然其他的服务提供商这里也支持，看你的域名托管在哪里。域名填写跟前面一样。用户名和密码填写阿里云授权的用户名和密码

可以在阿里云控制台中找到访问控制->身份管理->用户，新建一个用户，再添加权限，找到AliyunDNSFullAccess勾选确认。点击用户名，创建AccessKey，这里创建成功的AccessKey和密钥即为上面要求的用户名和密码

回到iStoreOS的DDNS设置，选择高级设置。IP地址来源选择接口，接口选择pppoe-wan，全部保存应用，正常来说IPv6的DDNS就启用成功了。

## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#wireguard%E8%AE%BE%E7%BD%AE)WireGuard设置

WireGuard是一个内核支持的VPN，在我们设置好动态DNS后，如果想在家以外的地方连回内网，VPN的设置也是必不可少的。

  1. 在网络->接口->创建新接口，新接口协议选择WireGuard VPN。新接口名称随便取，比如用WG0

  2. 每一个终端需要一个公钥和私钥，公钥和私钥的生成在新版本的插件上是很方便可以自动的（但这里是老版本没这种功能，而且别乱升插件，库文件不匹配很容易导致路由挂掉）

生成密钥，在ubuntu下需要安装wireguard `apt install wireguard`
[code]
    1
    2
    3
    4
    5
    
[/code]

| 
[code]
    #生成私钥
    $ wg genkey > private1.key
    
    # 生成公钥
    $ wg pubkey < private1.key > public1.key
    
[/code]  
  
---|---  
  
同样的方法生成第二对公私钥待用。（这里用priv1 pub1 priv2 pub2分别代表第一二对公私密钥对）。

回到iStoreOS的wireguard设置，在一般设置，私钥处填（priv1的内容）。监听端口填你喜欢且不冲突的。

IP地址填和内网网段不冲突的，比如 (192.168.26.1/24) (fd12:26::1/64)

  3. 在peers下，公钥填 (pub2的内容) ，允许ip填（192.168.26.0/24）（fd12:26::0/112），其他项可以忽略。

  4. 自己写一个conf扩展名的文件，内容如下:

[code]
    1
    2
    3
    4
    5
    6
    7
    8
    9
    
[/code]

| 
[code]
    [Interface]
    Address = 192.168.26.10/32, fd12:26::10/128
    PrivateKey =（priv2的内容）
    MTU = 1420
    [Peer]
    PublicKey = (pub1的内容)
    AllowedIPs = 0.0.0.0/0, ::/0 
    Endpoint = （DDNS设置中IPv6的解析域名）:（监听端口号）
    PersistentKeepalive = 25
    
[/code]  
  
---|---  
  
  5. 这个conf配置导入到wiregurad的app配置中，正常来说，在有IPv6支持的网络下，我们就可以直连到家庭内网中了

## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#frp%E9%9A%A7%E9%81%93%E5%BC%80%E5%90%AF)frp隧道开启

隧道的作用在于打通内网端口到公网，例如如果想在IPv4下支持wireguard接入，那么就需要用frp打通wireguard的v4的UDP端口号，因为提供frp服务很多，就不做推荐了。

第一步，在系统->软件包中找到luci-app-frpc，安装

打开服务->frp 内网穿透，基本设置。在基本设置中，服务器，商品，令牌，用户名，这些都可以在frp服务的配置中一一对应进行设置。

服务列表中，选添加，再进行进一步的配置，关键点是内网主机地址和内网主机端口，需要映射什么服务端口由自己定义和在服务端配置，例如上一个wireguard的UDP端口就可以配置一条隧道穿透，这个并不复杂。

## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E8%BF%9C%E7%A8%8B%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7gopeed)远程下载工具gopeed

远程下载工具中最有名的还是aria2，但是配置过于复杂，如果想自己拉tracker等还需要复杂的脚本配置，所以相对来说，在这个小路由上，远程下载还是用新明星项目gopeed比较合适。

下载地址如下：<https://github.com/GopeedLab/gopeed/releases>，选择linux arm64版本。

在gopeed同目录下写入配置文件config.json
[code]
    1
    2
    3
    4
    5
    6
    
[/code]

| 
[code]
    {
      "port": 9999,
      "username": "<用户名>",
      "password": "<密码>",
      "storageDir": "<下载路径>"
    }
    
[/code]  
  
---|---  
  
配置gopeed下载开机启动
[code]
    1
    
[/code]

| 
[code]
    vi /etc/init.d/gopeed
    
[/code]  
  
---|---  
  
在vi中粘如下代码
[code]
    1
    2
    3
    4
    5
    6
    7
    8
    
[/code]

| 
[code]
    #!/bin/sh /etc/rc.common
    START=100
    start() {
       <路径/>gopeed > /opt/gop.log
    }
    stop() {
      ps -ef | grep gopeed | grep -v grep | awk '{print $1}' | xargs -r kill
    }
    
[/code]  
  
---|---  
  
开机生效使能
[code]
    1
    2
    
[/code]

| 
[code]
    chmod +x /etc/init.d/gopeed
    /etc/init.d/gopeed enable
    
[/code]  
  
---|---  
  
gopeed启动后，在http://路由ip:9999，即可访问并使用远程下载

## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E4%B8%80%E4%BA%9B%E9%97%AE%E9%A2%98)一些问题

  * wifi不可连接问题

经过使用一段时间，发现wifi隔几天就会出现不可连接，可能是由于驱动什么原因，解决办法是定时每天重启。

  * 重启问题

在gopeed开启后，会阻止操作系统重启，所以这里需要用一些技巧

  1. 在系统->软件包中搜索reboot，删除reboot插件。（此插件会引起其他重启任务失效）

  2. 在系统->计划任务中，添加一行

[code]
    1
    
[/code]

| 
[code]
    0 5 * * * ps -ef | grep gopeed | grep -v grep | awk '{print $1}' | xargs -r kill && sleep 10 && touch /etc/banner && reboot
    
[/code]  
  
---|---  
  
点提交，正常来说，这里就设置成功了每天凌晨5点自动重启。

## [](https://oser.space/d5262f31-4455-40d0-b94a-7df386c93119/#%E6%80%BB%E7%BB%93)总结

总的来说，京东AX1800Pro还是一个可玩性很高的路由器，经过这些折腾后，现在稳定的使用了几个月也没出现过什么大问题，平时也差不多可以跑满千兆宽带，信号也不错。

平时即使不在家，也可以用手机方便的连回VPN随时scientific上网，实乃一大人生乐事。
