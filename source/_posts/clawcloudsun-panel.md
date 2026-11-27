---
title: 如何在ClawCloud上搭建Sun-Panel个人标签面板
date: '2025-05-10 12:00:00'
cover: /img/covers/clawcloudsun-panel.jpg
tags:
- Docker项目
categories:
- Docker项目
description: 'Sun-Panel 一个NAS、服务器导航面板、简易docker管理器、Homepage、浏览器首页。 ClawCloud 部署 Sun-Panel项目地址： 点击直达 Sun-Panel文档： 点击直达 Claw Cloud： 链接直达 1 hslr/ sun -pane l:'
---
# Sun-Panel

一个NAS、服务器导航面板、简易docker管理器、Homepage、浏览器首页。

# [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#ClawCloud)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#ClawCloud "ClawCloud")ClawCloud

## [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E9%83%A8%E7%BD%B2)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E9%83%A8%E7%BD%B2 "部署")部署

Sun-Panel项目地址：[点击直达](https://github.com/hslr-s/sun-panel)  
Sun-Panel文档：[点击直达](https://doc.sun-panel.top/zh_cn/introduce/project.html)  
Claw Cloud：[链接直达](https://ap-northeast-1.run.claw.cloud/signin)

```

    1  
    

```

| 

```

    hslr/sun-panel:latest  
    VIM

```
  
  
---|---  
  
如下图配置  
[![](https://img.skilladd.org/sun-panel/sun1.png)](https://img.skilladd.org/sun-panel/sun1.png)

最后添加磁盘映射  
[![](https://img.skilladd.org/sun-panel/sun2.png)](https://img.skilladd.org/sun-panel/sun2.png)

## [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81 "修改密码")修改密码

默认

  * 账号：`admin@sun.cc`
  * 密码：**12345678**

使用**默认密码登录** 之后，在**右上角设置** ，**账号管理** 添加一个新的管理员账号，并删除旧的管理员账号，这样，就只有你设置的账号才能登录了。

[![](https://img.skilladd.org/sun-panel/sun4.png)](https://img.skilladd.org/sun-panel/sun4.png)

# [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E9%A3%9F%E7%94%A8)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E9%A3%9F%E7%94%A8 "食用")食用

点击**添加** 的按钮，输入标签的地址的链接。  
[![](https://img.skilladd.org/sun-panel/sun5.png)](https://img.skilladd.org/sun-panel/sun5.png)

点击**获取图标** ，如果网站图标不是**xxxx.ico** 格式的，则会获取失败。  
[![](https://img.skilladd.org/sun-panel/sun7.png)](https://img.skilladd.org/sun-panel/sun7.png)

## [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9B%BE%E6%A0%87)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9B%BE%E6%A0%87 "自定义图标")自定义图标

点击**在线图标库**  
[![](https://img.skilladd.org/sun-panel/sun8.png)](https://img.skilladd.org/sun-panel/sun8.png)

找到自己想要设置的图标，复制**图标的名称** ，

[![](https://img.skilladd.org/sun-panel/sun9.png)](https://img.skilladd.org/sun-panel/sun9.png)

粘贴一下名称，这时候就可以查看到当前图标的样式了，然后我们保存一下。

[![](https://img.skilladd.org/sun-panel/sun10.png)](https://img.skilladd.org/sun-panel/sun10.png)

## [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E5%88%86%E7%BB%84%E8%AE%BE%E7%BD%AE)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E5%88%86%E7%BB%84%E8%AE%BE%E7%BD%AE "分组设置")分组设置

在右上角设置中，选择**分组管理** ，这样就可以自己自定义分组了。  
[![](https://img.skilladd.org/sun-panel/sun11.png)](https://img.skilladd.org/sun-panel/sun11.png)

## [](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E6%A0%87%E7%AD%BE%E6%89%B9%E9%87%8F%E8%AE%BE%E7%BD%AE)[](https://skilladd.org/2025/05/06/19.%E5%A6%82%E4%BD%95%E5%9C%A8ClawCloud%E4%B8%8A%E6%90%AD%E5%BB%BASun-Panel%E4%B8%AA%E4%BA%BA%E6%A0%87%E7%AD%BE%E9%9D%A2%E6%9D%BF/#%E6%A0%87%E7%AD%BE%E6%89%B9%E9%87%8F%E8%AE%BE%E7%BD%AE "标签批量设置")标签批量设置

如果，你之前使用该工具也可以批量**导入和导出** 。  
[![](https://img.skilladd.org/sun-panel/sun12.png)](https://img.skilladd.org/sun-panel/sun12.png)
