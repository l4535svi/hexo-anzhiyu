---
title: 2024年最佳电子玩具-极限榨取只需20元的玩客云全部性能！casaos轻NAS+小雅原版ALIST+Emby海报墙+Openwrt 千兆软路由+青龙面板
date: '2024-09-06 12:00:00'
cover: /img/covers/2024-20casaosnasalistembyopenwrt.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 前我们给大家分享了如何在20元的玩客云里安装casaoc轻NAS,然后我们再在上面安装了一个原版的小雅ALIST, 有小伙伴还不满足，接着我们又装了一个Emby海报墙，现在我们要极限榨干它的全部性能，我们再在上面安装一个OPENWRT作为旁路由来实现科学上网。 所需的原料：20元
---
前我们给大家分享了如何在20元的玩客云里安装casaoc轻NAS,然后我们再在上面安装了一个原版的小雅ALIST, 有小伙伴还不满足，接着我们又装了一个Emby海报墙，现在我们要极限榨干它的全部性能，我们再在上面安装一个OPENWRT作为旁路由来实现科学上网。

所需的原料：20元的垃圾玩客云一台，冰镇肥宅水一瓶，为什么？哈哈，因为天气太热了！

步骤：一. 原版玩客云刷机，前面已经介绍过了，请点击[原版玩客云刷机](https://blog.pcbtech.tk/index.php/2024/06/30/%e5%8e%9f%e7%89%88%e7%8e%a9%e5%ae%a2%e4%ba%91%e5%88%b7%e6%9c%ba%e6%95%99%e7%a8%8b%ef%bc%8c%e6%89%8b%e6%8a%8a%e6%89%8b%e6%95%99%e6%82%a8%e5%88%b7armbian%e5%ba%95%e5%8c%85%e5%ae%89%e8%a3%85casaos/)，

二. 玩可以按照casaos+小雅Emby,请点击[玩客云安装原版小雅](https://blog.pcbtech.tk/index.php/2024/05/25/%e9%80%80%e5%9d%91%e9%bb%91%e7%be%a4%e6%99%96%ef%bc%8c%e8%bd%ac%e6%8a%9520%e4%ba%91%e7%8e%a9%e5%ae%a2%e4%ba%91%e5%ae%89%e8%a3%85%e5%8e%9f%e7%89%88%e5%b0%8f%e9%9b%85alist%e6%9e%b6%e8%ae%be%e5%ae%b6/)

三. 安装OpenWrt

首先打开网卡混杂模式
[code]
    ip link set eth0 promisc on
[/code]

然后创建OpenWrt网络(自行替换网段，网关)，如果你的主路由是192.168.0.1的网关，我们需要将网关更改为192.168.0.1，docker network create -d macvlan –subnet=192.168.0.0/24 –gateway=192.168.0.1 -o parent=eth0 macnet，（subnet的最后那位必须是0）
[code]
    docker network create -d macvlan --subnet=192.168.5.0/24 --gateway=192.168.5.1 -o parent=eth0 macnet
[/code]

## 解决目前Docker Hub国内无法访问方法

2023年5月中旬， hub.docker.com “不知” 何种原因国内均无法正常访问了。当时只是官网不能访问，但是不影响pull镜像。

2024年6月，国内几家Docker Hub 镜像服务平台均被要求下架，停止服务。

**解决方案：配置加速地址**

配置加速地址：适用于Ubuntu 16.04+、Debian 8+、CentOS 7+

使用以下命令设置registry mirror：但是需要重启docker服务
[code]
    sudo mkdir -p /etc/docker
    sudo tee /etc/docker/daemon.json <<-'EOF'
    {
        "registry-mirrors": [
            "https://do.nark.eu.org",
            "https://dc.j8.work",
            "https://docker.m.daocloud.io",
            "https://dockerproxy.com",
            "https://docker.mirrors.ustc.edu.cn",
            "https://docker.nju.edu.cn"
        ]
    }
    EOF
    sudo systemctl daemon-reload
    sudo systemctl restart docker
[/code]

创建容器
[code]
    docker pull dreamwsbg/openwrt:12.0
[/code]

安装并启动容器
[code]
    docker run -d --name="openwrt" --restart unless-stopped --network macnet --privileged dreamwsbg/openwrt:12.0 /sbin/init
[/code]

［此固件默认IP为10.0.0.1 密码root］

修改默认IP，如果是做旁路由，可以把lan 的IP 更改为主路由同段的一个不和其他设备重复的IP,比如192.168.0.10

修改后台地址  
 进入容器后台
[code]
    docker exec -it openwrt bash
[/code]

修改网络  
  

vim /etc/config/network
[code]
    修改部分选项（按需修改。按“i”输入 ;     按“ESC” ,输入":" ,"w" , "q" 保存退出）
      
      config interface ‘lan’
      option proto ‘static’
      option ipaddr ‘192.168.0.5’（opwrt地址）
      option netmask ‘255.255.255.0’(子网掩码)
      option ip6assign ’60’
      option gateway ‘192.168.0.1’(网关)
      option broadcast ‘192.168.0.255’
      option dns ‘192.168.0.111’(dns)
[/code]

重启网络
[code]
     /etc/init.d/network restart 
[/code]

到这应该已经可以进入后台了  
192.168.0.6  
初始后台默认：root/root

passwall 导入梯子……愉快的翻墙啦！

四. 安装青龙面板（挂JD）把玩客云的价值利用干净

安装docker  
4.1.1 输入以下指令：(依次执行)
[code]
    docker pull whyour/qinglong:latest
    
[/code]

4.1.2创建青龙面板容器  

[code]
    docker run -dit \
      -v /home/docker/ql/config:/ql/config \
      -v /home/docker/ql/log:/ql/log \
      -v /home/docker/ql/db:/ql/db \
      -p 5700:5700 \
      --name qinglong \
      --hostname qinglong \
      whyour/qinglong:latest
    
[/code]

以上命令将创建一个名为`qinglong`的Docker容器，并将青龙面板的配置文件、日志和数据库等数据挂载到本地目录，同时将容器的5700端口映射到主机的5700端口。

4.2.2 建好容器后等两分钟，然后在浏览器中输入IP:5700，就安装完成。这个IP和casaos一样，例如<http://192.168.0.40:5700/>

通过`docker ps -a`查看正在运行的容器，可以看到刚才创建的青龙面板容器和我们的OPENWRT

五. 全部安装完成！玩客元都快被整哭了！
