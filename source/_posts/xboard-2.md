---
title: XBoard 机场全新部署方案全网首发
date: '2026-05-07 12:00:00'
cover: /img/covers/xboard-2.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 1、设置逻辑思路 2、添加节点 节点添加方案一：添加现有服务器节点 节点添加方案二：【 点击进入 】 wget -N https://raw.githubusercontent.com/wyx2685/V2bX-script/master/install.sh && bash i
---
[![](https://blogger.googleusercontent.com/img/a/AVvXsEigT41MIGdz34pEJTDy7wucFx6AgNgogT7LuyJLVSe_r5ZILW_GMDEa_abjE7DOsdV1b_JCV2AV0d_Jj3iLxChe_WeaARM3Kip4nt9FK2swTaZ1RU-MbaufbOx1m7WrW9sI7UukmbrlVbquEFUOktaOB75zhA8e81u70lo-i1F9E2_8pXdSRDzSLKniy4P1=w736-h237)](https://blogger.googleusercontent.com/img/a/AVvXsEigT41MIGdz34pEJTDy7wucFx6AgNgogT7LuyJLVSe_r5ZILW_GMDEa_abjE7DOsdV1b_JCV2AV0d_Jj3iLxChe_WeaARM3Kip4nt9FK2swTaZ1RU-MbaufbOx1m7WrW9sI7UukmbrlVbquEFUOktaOB75zhA8e81u70lo-i1F9E2_8pXdSRDzSLKniy4P1)

  
  

1、设置逻辑思路

![](https://naiyous.com/wp-content/uploads/2025/05/%E8%8A%82%E7%82%B9%E8%AE%BE%E7%BD%AE%E9%80%BB%E8%BE%91-1024x374.png)

2、添加节点

  * 节点添加方案一：添加现有服务器节点

  * 节点添加方案二：【[点击进入](https://github.com/wyx2685/V2bX)】

```

    wget -N https://raw.githubusercontent.com/wyx2685/V2bX-script/master/install.sh && bash install.sh

```

Copy

3、订阅模板（参考）

```

    更快的网络
    流媒体解锁
    不限制设备数
    500 GB流量/月
    500英里限速 

```

在线客服售后保障 

准备工作

  * 下载并安装SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

  * 做好域名解析Cloudflare：【[点击进入](https://dash.cloudflare.com/login)】
    * 准备两个域名：一个给面板、一个给节点TLS

1、一键部署Xboard开源项目：【[点击进入](https://github.com/slobys/xboard-one-click)】

  * Xboard开源项目：【[点击进入](https://github.com/cedar2025/Xboard)】

  * 一键部署

```

    bash <(curl -fsSL https://raw.githubusercontent.com/slobys/xboard-one-click/main/bootstrap.sh)

```

Copy

2、节点如果需要开启TLS，则按下面步骤设置

  * 流量路径如下（红色端口部分根据实际情况填写）：

```

    客户端 → jp.naiyou163.xyz:36332 → NPM 容器 443 → 反代到宿主机 51012 → xboard-node

```

Copy

  * 给TLS做好域名解析，添加一个和面板不一样的域名

  * 在NPM面板中添加代理服务（按下图设置）
    * 注意（易错）：
      * 转发端口要填xboard上的服务端口，但是放行的时候，要放行连接端口（重要）
      * 图二部分，点击保存之后，要再次点开，再点到SSL，把强制SSL和HTTP/2支持打开

![](https://naiyous.com/wp-content/uploads/2026/04/image-7-869x1024.png)

![](https://naiyous.com/wp-content/uploads/2026/04/image-6.png)

  * 证书路径（默认在root下安装）：

```

    /root/xboard-one-click/runtime/nginx-proxy-manager/letsencrypt/archive

```

