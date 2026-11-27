---
title: 哪吒面板探针
date: '2022-03-17 12:00:00'
cover: /img/covers/blog-post-6.jpg
tags:
- 建站
categories:
- 建站
description: 今天看到有人说哪吒面板这款探针，看了一下，感觉挺不错的 自己尝试部署了一下，哪吒面板，YES! 好鸭探针 ，就此诞生 不过开发者的并没有写一个详细的部署教程，我这里就从头到尾说清楚一点吧 包括部署面板、添加服务器、配置SSL、套CDN 预览： https://tz.haoduck
---
今天看到有人说哪吒面板这款探针，看了一下，感觉挺不错的

自己尝试部署了一下，哪吒面板，YES!

[好鸭探针](https://haoduck.com/go.html?url=https://tz.haoduck.com/)，就此诞生

不过开发者的并没有写一个详细的部署教程，我这里就从头到尾说清楚一点吧

包括部署面板、添加服务器、配置SSL、套CDN

预览：[https://tz.haoduck.com/](https://haoduck.com/go.html?url=https://tz.haoduck.com/)

暂时有两个主题，图一默认，图二CakeMine-Hotaru。好鸭探针用的是默认的。

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/demo1.jpg)

## 一、域名解析需要的操作

开始之前，请先确定你搭建探针的域名

强烈建议用两个(子)域名做解析  
第一个是面板的域名，套CDN比较方便  
第二个仅仅解析到面板服务器的域名，用于客户端连接服务端试用(这个可以没有，但是不建议，如果直接用IP的话，迁移面板后会非常麻烦！)

比如我的`tz.haoduck.com`作为面板的域名，还有一个`tzzzz.haoduck.com`是用来记录面板服务器的IP(其实不是这个域名，因为我写出来就暴露了我的IP了，所以就当它是吧)

暂且将两个域名都解析到部署面板服务器的IP，我之前改本地hosts部署没有成功

## 二、GitHub上需要的操作

### 2.1 得到GitHub账号ID

如果没有Github账号，先注册

浏览器中打开`https://api.github.com/users/你的GitHub用户名`

返回的是Json的信息，第二行id对应的值就是你的ID，纯数字的。如图

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/github_id.jpg)

### 2.2 创建一个OAuth Apps

先打开：[https://github.com/settings/developers](https://haoduck.com/go.html?url=https://github.com/settings/developers)，然后点击New OAuth App按钮

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/OAuth_Apps.jpg)

在这里其实有一个分岔口，也就是你是否要反代(和WEB服务器共用80口)、配置SSL，那么填写的内容、后面操作的先后顺序也不同。我就只说其中一个方法，免得把各位看官绕晕了，还请先往下看吧！

参考图片填写，记得端口也填写上去，不填域名填IP也行，如果你只是用IP访问的话
[code]
    http://你的域名:8008http://你的域名:8008/oauth2/callback
[/code]

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/OAuth_Apps2.jpg)

### 2.3 OAuth Apps的Client ID和Client secrets

创建好OAuth Apps后看图操作

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/OAuth_Apps3.jpg)![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/OAuth_Apps4.jpg)

## 三、面板服务器上需要的操作

### 3.1 防火墙放行端口

需要放行`8008`、`5555`两个端口，这是默认的，如果你程序中改为其他的，防火墙放行相应的端口

### 3.2 部署面板服务

哪吒面板开发者提供了一键脚本
[code]
    curl -L https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.sh./nezha.sh
[/code]
[code]
    # 国内机器curl -L https://raw.sevencdn.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.shCN=true ./nezha.sh
[/code]

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/script.jpg)

输入`1`回车

接着就要输入前面记录下来的`GitHub账号ID`、`OAuth Apps的Client ID`、`OAuth Apps的Client secrets`了

按照提示输入

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/script2.jpg)

到这里面板服务算是完成了大部分了

可以访问`http://域名:8008`查看，用你的GitHub账号验证登录

### 3.3 反代、SSL、CDN

反代配置
[code]
    location /{    proxy_pass http://127.0.0.1:8008;    proxy_set_header Host $host;}location /ws{    proxy_pass http://127.0.0.1:8008;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "Upgrade";    proxy_set_header Host $host;}location /terminal{    proxy_pass http://127.0.0.1:8008;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "Upgrade";    proxy_set_header Host $host;}
[/code]

图片为宝塔的设置方法  
![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/nginx.jpg)

配置SSL就不用说了，常规建站怎么配置，这个就怎么配置

如果没有问题，就可以通过`https://域名/`来访问了

确保可以访问了，回到GitHub的OAuth Apps设置

打开：[https://github.com/settings/developers](https://haoduck.com/go.html?url=https://github.com/settings/developers)

看图操作

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/OAuth_Apps5.jpg)

改好之后就可以对`8008`端口取消放行了

关于套CDN，就和常规建站一样，比如我的，就将`tz.haoduck.com`解析到CDN服务商，回源地址填部署面板的服务器IP，但要注意的是CDN需要支持WebSocket协议

## 四、关于客户端(被监控机器)需要的操作

通过[https://tz.haoduck.com/](https://haoduck.com/go.html?url=https://tz.haoduck.com/)登录后台，如果没配置反代、SSL，那它将是[http://tz.haoduck.com:8008](https://haoduck.com/go.html?url=http://tz.haoduck.com:8008)

用你的GitHub账号验证登录后跳转到[https://tz.haoduck.com/server](https://haoduck.com/go.html?url=https://tz.haoduck.com/server)

按图操作

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/panel.jpg)

到需要被监控的机器执行脚本
[code]
    curl -L https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.sh./nezha.sh
[/code]
[code]
    # 国内机器curl -L https://raw.sevencdn.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.shCN=true ./nezha.sh
[/code]

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/script.jpg)

输入`8`回车

接着就要输入前面记录下来的`ID`、`密钥`了

按照提示输入

"解析到面板所在IP的域名"就是指本文中第一步的"第二个域名"，也可以直接填IP(不建议)

![哪吒面板，一个便携服务器状态监控面板搭建教程，不想拥有一个自己的探针吗？](https://pic.52nidea.cn/2020/12/nezha/script3.jpg)

如果没出错，到此就是完成了

有多台被监控机器时，按照此步骤在控制面板添加服务器，在被监控机执行脚本填写ID和密钥。

本文为自己部署的过程，如果有误请指出

## 常见问题

### 1\. 国内服务器出现curl: (7) Failed to connect to raw.githubusercontent.com
[code]
    echo 199.232.68.133 raw.githubusercontent.com >> /etc/hosts
[/code]

### 2\. 修改服务器备注后变成"离线"久不恢复

在安装客户端(被监控)的服务器上执行`systemctl restart nezha-agent`重启程序

### 启动nezha-agent还是一直显示离线

检查配置有没有写对`cat /etc/systemd/system/nezha-agent.service | grep ExecStart`

## 相关

项目地址：[https://github.com/naiba/nezha](https://haoduck.com/go.html?url=https://github.com/naiba/nezha)

~~[关于哪吒探针修改页面页脚、头像Logo等的方法教程](https://haoduck.com/687.html)~~ ，新版本可以在后台用CSS自定义了。
