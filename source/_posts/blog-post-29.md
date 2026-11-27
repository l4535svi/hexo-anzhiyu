---
title: 携趣代理
date: '2022-04-30 12:00:00'
cover: /img/covers/blog-post-29.jpg
tags:
- 青龙全部
categories:
- 青龙全部
description: 携趣代理注册地址 https://www.xiequ.cn/index.html?2f4ff690 每天1000个免费IP 脚本如需开启代理，请在青龙环境变量中添加 xiequ 值 True 青龙环境变量中添加你的携趣代理【用户名】proxyU 值 你的用户名 青龙环境变量中添加
---
### 携趣代理注册地址 <https://www.xiequ.cn/index.html?2f4ff690>

##### 每天1000个免费IP

#### 脚本如需开启代理，请在青龙环境变量中添加 xiequ 值 True

青龙环境变量中添加你的携趣代理【用户名】proxyU 值 你的用户名  
青龙环境变量中添加你的携趣代理【密码】proxyP 值 你的密码

[![image.png](http://cxgc.top/upload/2022/03/image-a71ac3c6624c49cc9d71726bc56b591e.png)](http://cxgc.top/upload/2022/03/image-a71ac3c6624c49cc9d71726bc56b591e.png)

[image.png](http://cxgc.top/upload/2022/03/image-a71ac3c6624c49cc9d71726bc56b591e.png)

## 白名单一定要记得添加，待授权的公网IP地址就是你青龙服务器IP

青龙请在环境变量中添加你的携趣代理【IP提取地址】ipUrl 值 你的代理IP提取地址  
[![image.png](http://cxgc.top/upload/2022/03/image-891525f2154046ef96554b848a0f0ea4.png)](http://cxgc.top/upload/2022/03/image-891525f2154046ef96554b848a0f0ea4.png)

[image.png](http://cxgc.top/upload/2022/03/image-891525f2154046ef96554b848a0f0ea4.png)

访问 <https://www.xiequ.cn/redirect.aspx> >> 已购产品 >> API提取 >> 选择提取数量: 1、选择IP协议：HTTP/HTTPS、选择返回格式：JSON、其他随意 >> 生成链接）  
[![image.png](http://cxgc.top/upload/2022/03/image-4d0182b137aa463a99b82fd2f9ae1089.png)](http://cxgc.top/upload/2022/03/image-4d0182b137aa463a99b82fd2f9ae1089.png)

[image.png](http://cxgc.top/upload/2022/03/image-4d0182b137aa463a99b82fd2f9ae1089.png)

### 青龙一键安装依赖

```

    docker exec -it QL bash -c "$(curl -fsSL https://github.com/JDWXX/jd_job/blob/master/QLOneKeyDependency.sh | sh)"  
    

```

### 一键安装不行的试试手动安装依赖

```

    docker exec -it QL bash -c "npm install superagent-proxy"  
    docker exec -it QL bash -c "yarn add superagent"  
    

```

### 青龙面板脚本使用

#### 如需运行脚本必须开启代理

[![image.png](http://cxgc.top/upload/2022/03/image-161a11338e4642bdb9ed1929eccfce47.png)](http://cxgc.top/upload/2022/03/image-161a11338e4642bdb9ed1929eccfce47.png)

[image.png](http://cxgc.top/upload/2022/03/image-161a11338e4642bdb9ed1929eccfce47.png)

1.注册携趣代理：<https://www.xiequ.cn/index.html?2f4ff690>  
2.获取携趣代理所需参数：<http://cxgc.top/archives/xiequdaili>  
3.开启携趣代理 添加环境变量：xiequ，值填 True  
4.携趣用户名 添加环境变量：proxyU，值填 第二步骤里获取  
5.携趣密码 添加环境变量：proxyP，值填 第二步骤里获取  
6.携趣IP提取地址 添加环境变量：ipUrl，值填 第二步骤里获取
