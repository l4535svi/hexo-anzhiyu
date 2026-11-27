---
title: 使用BT宝塔Nginx反向代理导致 后台无法登录的解决方法
date: '2022-04-18 12:00:00'
cover: /img/covers/btnginx.jpg
tags:
- 建站
categories:
- 建站
description: 很多人都喜欢用BT宝塔面板做站，其中比较受大家欢迎的有BT宝塔面板里的反向代理功能，非常简单实用，直接配置就可以用，但是因为BT宝塔面板自带的反向代理默认是利用Nginx的反向代理原理，因此默认的配置存在一些问题 关闭缓存后仍然缓存； 开启反向代理缓存后不能正常登陆； 无法针对某
---
很多人都喜欢用BT宝塔面板做站，其中比较受大家欢迎的有BT宝塔面板里的反向代理功能，非常简单实用，直接配置就可以用，但是因为BT宝塔面板自带的反向代理默认是利用Nginx的反向代理原理，因此默认的配置存在一些问题

  * 关闭缓存后仍然缓存；
  * 开启反向代理缓存后不能正常登陆；
  * 无法针对某个目录进行针对性缓存；

针对于以上问题，我一直在捣鼓和研究，后来终于解决了。现在分享给大家对应的配置方法。

缓存问题原因分析

其实以上问题都是针对缓存的配置所导致的。因为Nginx的缓存配置默认直接在代码里面配置，BT宝塔面板则是分开设置，最终组合在一起导致缓存的问题。

宝塔官方是默认对JS/CSS等静态文件缓存，但是如果设置了typecho伪静态的话，那将会对页面也缓存进去。比如设置某个页面伪静态后地址为：https://www.ovz.cc/125.html ，那么该页面就被缓存了，因此就会导致不能正常登陆。因为缓存的页面默认是没有登录的状态，你再次访问则为缓存页面。

### 解决方法：

话不多说，直接上代码，这里我们要登录代理机的BT宝塔面板，找到对应的网站，点击配置文件

![](https://www.ovz.cc/wp-content/uploads/2021/02/2161146027.png)

```

    #PROXY-START/  
    location /  
    {  
    #缓存媒体文件  
    location ~* .jpg|.png|.gif|.jpeg|.ttf|.webp|.woff|.woff2|.ico$  
    {  
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;  
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
    proxy_set_header REMOTE-HOST $remote_addr;  
    proxy_pass http://你的域名;  
    proxy_cache cache_one;  
    proxy_cache_valid 30d;  
    proxy_ignore_headers Cache-Control;  
    add_header X-Cache "$upstream_cache_status from $server_addr";  
    }  
      
    #缓存css、js、html  
    location ~* .css|.js|.html$  
    {  
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;  
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
    proxy_set_header REMOTE-HOST $remote_addr;  
    proxy_pass http://你的域名;  
    proxy_cache cache_one;  
    proxy_cache_valid 3d;  
    proxy_ignore_headers Cache-Control;  
    add_header X-Cache "$upstream_cache_status from $server_addr";  
    }  
      
    proxy_pass http://你的域名;  
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;  
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
    proxy_set_header REMOTE-HOST $remote_addr;  
      
    #持久化连接相关配置  
    #proxy_connect_timeout 30s;  
    #proxy_read_timeout 86400s;  
    #proxy_send_timeout 30s;  
    #proxy_http_version 1.1;  
    #proxy_set_header Upgrade $http_upgrade;  
    #proxy_set_header Connection "upgrade";  
    #add_header X-Cache $upstream_cache_status;  
      
    #expires 12h;  
    }  
    #PROXY-END/

```

针对以上代码的说明

因为宝塔里的反向代理文件默认是全局缓存，我们没有用其代码，直接采用分类缓存的方式。大家只需将上面的域名换成自己的域名即可，如果需要修改缓存的话可以根据以上缓存类型进行更换即可。

比如不希望缓存html，缓存的话容易出现typecho登陆后还是显示没有登陆的界面问题。那么就可以将以上代码的html部分去掉即可。

### 如何对某些目录设置不缓存

比如我们不希望缓存网站的某些目录，比如不希望缓存站点下的admin文件夹。那么可以进行相应的设置，将如下代码加入最后

```

    location /admin {  
    proxy_pass http://你的域名;  
    proxy_cache_valid any 0s;  
    }

```

修改域名为自己的网站，如果有多个目录的话，那么分别增加如上代码即可。
