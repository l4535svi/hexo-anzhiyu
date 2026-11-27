---
title: 亚瑟扩容1G内存后如何刷入1G的CDT文件
date: '2026-02-02 12:00:00'
cover: /img/covers/1g1gcdt.jpg
tags:
- 软路由
categories:
- 软路由
description: 亚瑟已经由512M内存改为1G了，也由CDT文件但不知道怎么刷进去，系统已挂在的分区如下： 按照兆能M2的方式，分区是不一样的，请叫各位高手，感谢。 把cdt文件放入tmp文件夹，重命名为cdt-Arthur_1G_DDR3.bin，ssh登录路由器，依次输入 cd /tmp d
---
亚瑟已经由512M内存改为1G了，也由CDT文件但不知道怎么刷进去，系统已挂在的分区如下：  
  
  
  
![](https://www.right.com.cn/forum/data/attachment/forum/202408/16/132544um0djcaloanqormz.jpg)  
  
  
按照兆能M2的方式，分区是不一样的，请叫各位高手，感谢。  
[![](https://blogger.googleusercontent.com/img/a/AVvXsEj4JHAyEztyVGWi-FpulbkHufFMrqO0KCUaknCl4Xvt55TKd--f0ZKZtkWaHWj2crdKudsf7s6-koDY8BNPXoda-hmUZgeXtXwHDUEdrhzwLPbQeBHAWN6xIm49CXshnqFlqzkeUjLFa3MGloRYnJm3lGJ0qWPG7DK-KoYA13898GSOZNAUqjwHXB8up6jo)](https://blogger.googleusercontent.com/img/a/AVvXsEj4JHAyEztyVGWi-FpulbkHufFMrqO0KCUaknCl4Xvt55TKd--f0ZKZtkWaHWj2crdKudsf7s6-koDY8BNPXoda-hmUZgeXtXwHDUEdrhzwLPbQeBHAWN6xIm49CXshnqFlqzkeUjLFa3MGloRYnJm3lGJ0qWPG7DK-KoYA13898GSOZNAUqjwHXB8up6jo)  
| 把cdt文件放入tmp文件夹，重命名为cdt-Arthur_1G_DDR3.bin，ssh登录路由器，依次输入  
cd /tmp  
dd if=/tmp/cdt-Arthur_1G_DDR3.bin of=/dev/mmcblk0p10  
dd if=/tmp/cdt-Arthur_1G_DDR3.bin of=/dev/mmcblk0p11  
sync  
重启，收工  
---
