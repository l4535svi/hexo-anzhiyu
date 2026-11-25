---
title: 一图读懂BBR/BBR PLUS/BBR2加速方式区别
date: '2025-03-07 12:00:00'
tags:
- 科学上网
categories:
- 科学上网
description: 大家买到vps肯定都会安装bbr，但是bbr又有很多版本和加速方式，这篇文章就介绍了各种加速方式的区别，并给出了建议，供大家参考。 一、什么是BBR TCP BBR是谷歌出品的TCP拥塞控制算法。BBR目的是要尽量跑满带宽，并且尽量不要有排队的情况。BBR可以起到单边加速TCP连
---
大家买到vps肯定都会安装bbr，但是bbr又有很多版本和加速方式，这篇文章就介绍了各种加速方式的区别，并给出了建议，供大家参考。

## 一、什么是BBR  

TCP BBR是谷歌出品的TCP拥塞控制算法。BBR目的是要尽量跑满带宽，并且尽量不要有排队的情况。BBR可以起到单边加速TCP连接的效果。替代锐速再合适不过，毕竟免费。Google提交到Linux主线并发表在ACM queue期刊上的TCP-BBR拥塞控制算法。继承了Google“先在生产环境上部署，再开源和发论文”的研究传统。TCP-BBR已经再YouTube服务器和Google跨数据中心的内部广域网(B4)上部署。由此可见出该算法的前途。

TCP-BBR的目标就是最大化利用网络上瓶颈链路的带宽。一条网络链路就像一条水管，要想最大化利用这条水管，最好的办法就是给这跟水管灌满水。

BBR解决了两个问题：

再有一定丢包率的网络链路上充分利用带宽。非常适合高延迟，高带宽的网络链路。  
降低网络链路上的buffer占用率，从而降低延迟。非常适合慢速接入网络的用户。

项目地址:[https://github.com/google/bbr](https://github.com/google/bbr)

这里虾皮路来总结一下，一般经常测试，没有设置过BBR的VPS的G口带宽主机，平时下载速度如果是3MB/s的话，安装BBR脚本后，一般能达到下载速度为50-100MB/s，提速非常明显。

## 二、选择VPS主机及BBR脚本  

BBR加速脚本虾皮路直接选择安装Loc论坛上的不卸载内核的BBR脚本
[code]
    解释
    
    wget -N --no-check-certificate "https://github.000060000.xyz/tcpx.sh" && chmod +x tcpx.sh && ./tcpx.sh
[/code]

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图1](http://www.zmrbk.com/wp-content/uploads/a5263c0e77f1e94d3678a00b6df42887.jpg)](http://www.zmrbk.com/wp-content/uploads/a5263c0e77f1e94d3678a00b6df42887.jpg)

因为脚本比较多，但是效果基本都在BBR算法和BBR PLUS算法及BBR2算法几种，因此虾皮路也是主要测试这几种。

为了公平起见，每次测试完虾皮路都会重新安装一次系统，这里选择的是Linux Centos 7 X86 64 Minimal。

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图2](http://www.zmrbk.com/wp-content/uploads/e36f9460edfcd053bc7c512b568dae6b.jpg)](http://www.zmrbk.com/wp-content/uploads/e36f9460edfcd053bc7c512b568dae6b.jpg)

注意：每个VPS主机的环境和设置都不一样，本次脚本测试仅供参考，并不具备直接指导意义，因此对自己随意安装设置BBR脚本所带来的后果概不负责。

测试的脚本虾皮路选择老鬼的测试脚本
[code]
    解释
    
    wget -qO- git.io/superbench.sh | bash
[/code]

## 三、BBR/BBR PLUS/BBR2加速脚本对比测试  

### 1、默认的cubic算法脚本  

先上一个未安装任何脚本的测试图，默认的机器的内核是3.10，TCP算法是cubic，实际上也很不错了，就移动线路差了点

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图3](http://www.zmrbk.com/wp-content/uploads/2dabbb47d4707442ee9112f42c1d048b.jpg)](http://www.zmrbk.com/wp-content/uploads/2dabbb47d4707442ee9112f42c1d048b.jpg)

### 2、秋水逸冰BBR加速  

刚开始选择流行的秋水逸冰BBR安装脚本进行测试

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图4](http://www.zmrbk.com/wp-content/uploads/dc31cc4655ebf7625054a21ef53f7b87.jpg)](http://www.zmrbk.com/wp-content/uploads/dc31cc4655ebf7625054a21ef53f7b87.jpg)

安装后，上面显示的是内核提升到了5.9.8-1.el7.elrepo.x86_64，同时为BBR+FQ算法。测试如下

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图5](http://www.zmrbk.com/wp-content/uploads/a2c4d62bc5bf1ac5b30f5c7c5003e72a.png)](http://www.zmrbk.com/wp-content/uploads/a2c4d62bc5bf1ac5b30f5c7c5003e72a.png)

提速非常明显，基本都有几倍的速度的提升。

### 3、BBR原版内核+BBR+CAKE  

这里需要安装BBR原版内核，不过内核升级到了5.9.6，只不过加速算法设置成BBR+CAKE

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图6](http://www.zmrbk.com/wp-content/uploads/55b845679440ab9e10b62ee19573dd56.png)](http://www.zmrbk.com/wp-content/uploads/55b845679440ab9e10b62ee19573dd56.png)

然后运行脚本进行测试

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图7](http://www.zmrbk.com/wp-content/uploads/3df183b12cdfb7dbee460e96328e769e.png)](http://www.zmrbk.com/wp-content/uploads/3df183b12cdfb7dbee460e96328e769e.png)

提速也很不错。基本和上面的秋水逸冰BBR算法持平。

### 4、BBR PLUS+FQ加速  

这里要重新安装主机的内核，选择安装BBR PLUS的129版本，而不是选择182版本，因为很多小伙伴经常反馈，安装182版本后不稳定。

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图8](http://www.zmrbk.com/wp-content/uploads/45599c2e2bc754290c12d904703c30df.png)](http://www.zmrbk.com/wp-content/uploads/45599c2e2bc754290c12d904703c30df.png)

再运行脚本进行测试

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图9](http://www.zmrbk.com/wp-content/uploads/aa9003817edf084343199a6b98f5f75e.png)](http://www.zmrbk.com/wp-content/uploads/aa9003817edf084343199a6b98f5f75e.png)

这里虾皮路发现，内核版本在5.9以上，连硬盘的IO都高一点，目前BBR PLUS内核是4.14.129，硬盘的IO会低一些。在提速效果这块，速度和上面差别不大。

### 5、BBR2+FQ+ECN加速  

安装完BBR2内核，有时候会安装不成功，安装完后记得用脚本查看一下当前加载的内核。安装成功后如下显示

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图10](http://www.zmrbk.com/wp-content/uploads/7c669ec51cd8810fed3aab76380434a9.png)](http://www.zmrbk.com/wp-content/uploads/7c669ec51cd8810fed3aab76380434a9.png)

运行脚本进行测试

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图11](http://www.zmrbk.com/wp-content/uploads/8acb9ac6eaab935bcb83cb2721320126.png)](http://www.zmrbk.com/wp-content/uploads/8acb9ac6eaab935bcb83cb2721320126.png)

### 6、BBR2+CAKE+ECN加速  

这里再换一个加速算法BBR2+CAKE+ECN加速，BBR2的内核不动，如下

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图12](http://www.zmrbk.com/wp-content/uploads/3924c711db0fb05d52b0275ab950ccc4.png)](http://www.zmrbk.com/wp-content/uploads/3924c711db0fb05d52b0275ab950ccc4.png)

运行脚本测试

[![哪个BBR/BBR PLUS/BBR2加速脚本最快最好 最新脚本及设置详细评测插图13](http://www.zmrbk.com/wp-content/uploads/7a37fab6442ca5edd42bdcf4510522c2.png)](http://www.zmrbk.com/wp-content/uploads/7a37fab6442ca5edd42bdcf4510522c2.png)

## 四、各个BBR加速脚本总结  

经过上面的测试，虾皮路总结了一下各个BBR的加速脚本，如下

选择脚本| 内核| IO读写平均值| 加速效果  
---|---|---|---  
默认cubic| 3.10| 174.3MB/s| ★★  
秋水逸冰BBR(BBR+FQ)| 5.9.8| 173.3MB/s| ★★★★  
BBR+CAKE| 5.9.6| 170.0MB/s| ★★★★☆  
BBR PLUS+FQ| 4.14.129| 142.7MB/s| ★★★★  
BBR2+FQ+ECN| 5.4.0-rc6| 180.7MB/s| ★★★☆  
BBR2+CAKE+ECN| 5.4.0-rc6| 181.3MB/s| ★★★☆  
  
其实以上仅供参考，毕竟测试的时候有误差。虾皮路建议，海外的VPS是一定要BBR加速脚本的，至于安装哪个脚本，则根据个人喜好。其中用得比较多的一般是BBR+FQ或者BBR+CAKE及BBR PLUS+FQ这3个。而BBR2的话建议不要安装，毕竟稳定性有些不足。因此综上所述，建议选择BBR+FQ或者BBR+CAKE均可。

来源：https://www.xiapilu.com/web/web-tutorial/bbr-vs-plus-vs-bbr2.html
