---
title: 【青龙面板】Centos用Docker安装青龙面板以及多青龙面板教程
date: '2025-01-17 12:00:00'
cover: https://picsum.photos/seed/centosdocker/800/450
tags:
- 青龙全部
categories:
- 青龙全部
description: 前言 相信现在很多人都在用青龙面板，今天写一篇用centos操作系统利用docker安装青龙面板以及多青龙面板教程。 青龙面板拉取 使用下面命令进行单独的青龙面板 镜像拉取 。前提您操作系统已经安装了 Docker docker pull whyour/qinglong:late
---
## 前言

相信现在很多人都在用青龙面板，今天写一篇用centos操作系统利用docker安装青龙面板以及多青龙面板教程。

## 青龙面板拉取

  1. **使用下面命令进行单独的青龙面板`镜像拉取`。前提您操作系统已经安装了`Docker`**
[code]docker pull whyour/qinglong:latest
[/code]

Copy

  2. **如果您的拉取出现拉取`过慢`，或者`拉取不下来`问题，可以去`Docker的配置文件`修改`加速地址`配置。或者使用`命令修改`即可。（请`替换`[ "[https://Docker加速网址](https://xn--docker-8e4jr91ar77gee9a/)"] 里面的`地址`），替换完毕后记得`重启docker`才可生效**
[code]sudo tee /etc/docker/daemon.json <
[/code]

Copy
[code]systemctl restart  docker
[/code]

Copy

[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626094551888644.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626094551888644.webp)

## 青龙面板创建（单容器）

  1. **我们首先通过`ssh工具`连接你的`服务器`，这里我使用的是`FinalShell`工具连接。输入你服务器的`正确IP`或者`本地IP`和`端口`，输入`用户`和`密码`确认即可。**  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626095128744441.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626095128744441.webp)
  2. **连接完毕后我们就使用下面命令进行创建容器，这里记住，[-v $PWD/`ql`/data:/ql/data] 里前面的`ql`是可以更改的,[-p `5700`:5700] 里面:前面的`5700`可以`更改`，这就是`映射`出来的`端口号`，也是你后续`网页端`要输入的`端口号`。后面的默认`5700不动`，因为后面的是`容器端口`，每个容器都是`独立`的，不会冲突。[--name `qinglong`和--hostname `qinglong`]里面的`qinglon`g也是可以`更改`的。修改代码后回车即可！**
[code]docker run -dit \
         -v $PWD/ql/data:/ql/data \
         -p 5700:5700 \
         --name qinglong \
         --hostname qinglong \
         --restart always \
         whyour/qinglong:latest
[/code]

Copy

[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626095455184844.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626095455184844.webp)  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626095828693197.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626095828693197.webp)

  3. **然后我们去`浏览器`，输入你搭建青龙面板的服务器`IP`和`端口号`，进入`青龙面板web`。出来后点击`开始安装`**  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103559037759.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103559037759.webp)
  4. **通知方式就不选择，直接`跳过`即可**  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103648735430.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103648735430.webp)
  5. **用户设置这里设置你登录这个青龙面板的`帐号`和`密码`等信息。**  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103723967644.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103723967644.webp)  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103734667781.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103734667781.webp)
  6. **上述配置完毕后，我们就可以`跳转`到登录页面了，直接`输入`你刚才设置的用户名和密码。登录进入就完毕了。**  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103819493879.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103819493879.webp)  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103829138199.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103829138199.webp)

## 青龙面板创建（多容器）

### 示例图

**我们创建`多容器`的命令按照图内的提示进行`更改`，我也会在`文末`提供`五个`多容器的`命令`，方便你直接`复制黏贴`就创建`多个容器`，当然`端口号`和`昵称`你可以`自定义`，切记`端口`和`昵称`有冲突！**  
[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626103939320326.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626103939320326.webp)

### 多容器命令

  * **容器1**
[code]docker run -dit \
        -v $PWD/ql1/data:/ql/data \
        -p 5701:5700 \
        --name ql1 \
        --hostname ql1 \
        --restart always \
        whyour/qinglong:latest
[/code]

Copy

  * **容器2**
[code]docker run -dit \
        -v $PWD/ql2/data:/ql/data \
        -p 5702:5700 \
        --name ql2 \
        --hostname ql2 \
        --restart always \
        whyour/qinglong:latest
[/code]

Copy

  * **容器3**
[code]docker run -dit \
        -v $PWD/ql3/data:/ql/data \
        -p 5703:5700 \
        --name ql3 \
        --hostname ql3 \
        --restart always \
        whyour/qinglong:latest
[/code]

Copy

  * **容器4**
[code]docker run -dit \
        -v $PWD/ql4/data:/ql/data \
        -p 5704:5700 \
        --name ql4 \
        --hostname ql4 \
        --restart always \
        whyour/qinglong:latest
[/code]

Copy

  * **容器5**
[code]docker run -dit \
        -v $PWD/ql5/data:/ql/data \
        -p 5705:5700 \
        --name ql5\
        --hostname ql5\
        --restart always \
        whyour/qinglong:latest
[/code]

Copy

## 删除青龙容器和镜像

### 删除青龙面板容器

**命令`docker ps`列出`所有`容器，然后找到你的青龙容器`CREATED`下面你设置的`容器name`。用命令`docker rm -f 容器name`删除,注意下面的`qinglong`要自己更改`CREATED`下面显示的。**
[code]
    docker ps
[/code]

Copy
[code]
    docker rm -f qinglong
[/code]

Copy

[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626113741168366.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626113741168366.webp)

### 删除青龙面板镜像

**下面的命令`删除镜像`，但是前提你需要先`删除`依赖此镜像的容器才可以`删除镜像`。**
[code]
    docker rmi whyour/qinglong:latest
[/code]

Copy

[![file](https://lmu5.com/wp-content/uploads/2024/06/20240626114145096810.webp)](https://lmu5.com/wp-content/uploads/2024/06/20240626114145096810.webp)

## 基础命令

  * 更新青龙
[code]docker exec -it qinglong ql update
[/code]

Copy

  * 更新青龙并编译
[code]docker exec -it qinglong ql restart
[/code]

Copy

  * 删除7天前的所有日志
[code]docker exec -it qinglong ql rmlog 7
[/code]

Copy

  * 启动bot
[code]docker exec -it qinglong ql bot
[/code]

Copy

  * 导出互助码
[code]docker exec -it qinglong ql code
[/code]

Copy

  * 通知测试
[code]docker exec -it qinglong notify test test
[/code]

Copy

  * 立即执行脚本
[code]docker exec -it qinglong task test.js now
[/code]

Copy

  * 并行执行脚本
[code]docker exec -it qinglong task test.js conc
[/code]
