---
title: 【升级】docker部署PHP运行教程+项目分享（国内高清直播）
date: '2025-11-21 12:00:00'
tags:
- 影视大全
categories:
- 影视大全
description: 第一部分：PHP的部署 Docker一键部署PHP并运行 docker run -d --name php-runtime --restart=always -p 5080:80 -p 5090:8080 -e ADMIN_USER=admin -e ADMIN_PASS=123
---
### 第一部分：PHP的部署

Docker一键部署PHP并运行

`docker run -d --name php-runtime --restart=always -p 5080:80 -p 5090:8080 -e ADMIN_USER=admin -e ADMIN_PASS=123456 -v php-runtime_repo:/var/www/repo livecodesvip/php-runtime:latest`

 _![📝](https://cdn.jsdelivr.net/gh/twitter/twemoji@14/assets/72x72/1f4dd.png)备注: ADMIN_USER和ADMIN_PASS随便修改，5080和5090自己映射到宿主机的端口也可以随便修改，前提是宿主机这两个端口没有被使用_

直接访问：`http://ip:5090` _（后端管理）_  
项目访问：`http://ip:5080/xxx.php` _（前端网页）_

（可选操作）执行自动更新Docker容器的指令：

`docker run -d --name watchtower --restart=always -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower php-runtime --cleanup --interval 3600`

### 第二部分：PHP项目部署和实现（国内高清直播）

PHP文件下载：

链接：<https://pan.quark.cn/s/e343b2c4b038?pwd=CLAV>  
提取码：CLAV

============

_附录：_  
直播播放器推荐：<https://pan.quark.cn/s/99c686e2b3ab>

ok影视  
软件下载：<https://pan.quark.cn/s/71e11aee9313>
