---
title: colabvpnyoutube8kkbpsgptv2rayclashsingo
date: '2025-04-05 12:00:00'
tags:
- 节点分享
categories:
- 节点分享
description: 主页 每日免费节点更新，科学上网 一段代码简单在谷歌colab内搭建vpn，完全免费科学上网工具，全网高速免费机场节点抓取，可轻松观看YouTube视频8k十万kbps，优质节点几乎跑满宽带，白嫖优质节点当备用网络可解锁GPT,百分百成功！有手就行！支持v2ray/clash/s
---
[主页](https://kjgx668.blogspot.com/) __[每日免费节点更新，科学上网](https://kjgx668.blogspot.com/search/label/%E6%AF%8F%E6%97%A5%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91?&max-results=5) __一段代码简单在谷歌colab内搭建vpn，完全免费科学上网工具，全网高速免费机场节点抓取，可轻松观看YouTube视频8k十万kbps，优质节点几乎跑满宽带，白嫖优质节点当备用网络可解锁GPT,百分百成功！有手就行！支持v2ray/clash/singox，

# 一段代码简单在谷歌colab内搭建vpn，完全免费科学上网工具，全网高速免费机场节点抓取，可轻松观看YouTube视频8k十万kbps，优质节点几乎跑满宽带，白嫖优质节点当备用网络可解锁GPT,百分百成功！有手就行！支持v2ray/clash/singox，

[科技共享](https://www.blogger.com/profile/05924708293677118365 "科技共享")三月 31, 2025

 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk8KzHqf5eomRPkjY1IVpZ_dfYeG73xzNvO92Zaae5OlnQo9n9yDSDtYke-GnqWNS7FQHLEFBf67G9sKKr4dK9UV-y4FVTNs4rlAVc3xcrchnibD7dEHRNMfa6OBH70bCErryt5_dHNa6zp4rjBAp40LW6HGCfMte8_7QcOd0V-fHHJrQ-T0t24q-qB2WZ/w640-h368/Screenshot_2025-03-31-16-04-51-501_com.lemon.lv-e.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk8KzHqf5eomRPkjY1IVpZ_dfYeG73xzNvO92Zaae5OlnQo9n9yDSDtYke-GnqWNS7FQHLEFBf67G9sKKr4dK9UV-y4FVTNs4rlAVc3xcrchnibD7dEHRNMfa6OBH70bCErryt5_dHNa6zp4rjBAp40LW6HGCfMte8_7QcOd0V-fHHJrQ-T0t24q-qB2WZ/s1220/Screenshot_2025-03-31-16-04-51-501_com.lemon.lv-e.jpg)

  

  

能够自动爬取全网分享的订阅地址及代理节点，也能够自动注册/续期、订阅转换、节点存活检查等

作者项目地址【[点击直达](https://github.com/wzdnzd/aggregator)】

谷歌账号注册教程【[点击直达](https://www.youtube.com/watch?v=evEyYGwx03U&t=232s)】

  

**详细视频教程**

  

  

**谷歌colab【[点击直达](https://colab.research.google.com/)】**   （https://colab.research.google.com/）

*   * 在新建的笔记本中，运行以下命令以克隆项目仓库：​
[code]
        
        !git clone https://github.com/wzdnzd/aggregator.git
        
[/code]

* **安装依赖项** ：

  * 进入克隆的项目目录：​
[code]
        
        %cd aggregator
        
[/code]

  * 安装项目所需的 Python 依赖项：​
[code]
        
        !pip install -r requirements.txt​
[/code]

* **运行项目** ：

  * 在 Colab 中，使用以下命令运行 `process.py` 脚本：

!python -u subscribe/collect.py -s

  

  

查看节点文件：

!cat /content/aggregator/data/clash.yaml

下载节点文件

from google.colab import files  
files.download('/content/aggregator/data/clash.yaml')

  

**墙内运行方法：**

Github Action使用方法：（原始地址：https://linux.do/t/topic/96234）

不建议使用，此方法容易封Github账号。。。

  

流程如下：

  1. fork作者的代码仓库：<https://github.com/wzdnzd/aggregator>

  2. 启用Actions，如下图：

![d08d6c472dd5e012d5aa0989b45663ca](https://cdn.ldstatic.com/original/3X/0/0/00e06ee74d9efe54b36072dcbc14bdfdc12a4f59.png)

  3. 禁用不必要的workflow，比如Checkin和Process，具体操作如下：

![2ba4548d89d43af05590affc76b6708f](https://cdn.ldstatic.com/original/3X/a/9/a9fc585724d7d783839e6ed506bf2aae067a9842.png)

  4. 创建gist并获取到username/gist_id（记得保存，稍后要用），打开 [https://gist.github.com](https://gist.github.com/)，随便创建一个，内容随便填，如图所示

![image](https://cdn.ldstatic.com/original/3X/7/6/76f4749e1d67453d5d51807e12c7c9b33e718c0d.png)

  5. 回到 <https://github.com/settings/tokens?type=beta> 点击Generate new token按钮创建 PAT。名字随便填，过期时间选得久一点，重要的是在Account permissions里授予Gists的读写权限，创建好后复制生成的token稍后用

![1716447115285](https://cdn.ldstatic.com/original/3X/a/3/a33e968c73dfc8a82c829c23cb03de83270de29e.png)

![1716447232413](https://cdn.ldstatic.com/original/3X/5/c/5c02914d54889d9c5712637c74b0f690741881d2.png)

  6. 到仓库页面的Settings里设置环境变量，变量名为GIST_LINK和GIST_PAT，值分别为第4和5两步获取到的内容

![d4f38a97939b31716ddafcb22fb03933](https://cdn.ldstatic.com/original/3X/3/f/3f5221af22ffbdf667958bec79491be08e7b9483.png)

![1716448445246](https://cdn.ldstatic.com/original/3X/4/f/4ff0ac41dd2e654421a3df83b25723de3b287456.png)

  7. 手动运行测试是否能够正常执行并成功推送到gist

![4f8dcf7ad4708a3946b877b5635013dc](https://cdn.ldstatic.com/original/3X/4/2/429fbed134f8146583a2aa404499e122315b0545.png)

如果你看到类似以下内容，说明你跑成功了（也可以到刚刚新建的gist里查看内容）  
![1716461447974](https://cdn.ldstatic.com/original/3X/1/d/1d7c28ea6b21c759a3f0f96fc98752fa0edaeb46.png)

  8. 添加订阅到你的翻墙软件里，添加不了的可以先订阅转换一下

![c5d86e5808729e3c6214151fddadef2b](https://cdn.ldstatic.com/original/3X/9/d/9d63201fbb6cbfedb5180d29f9342d2384e9c06e.png)

![3eacfdf47992627ddfa438026e835952](https://cdn.ldstatic.com/original/3X/c/5/c55cbff16185b3c2d4f4b844d02894f6585f8aa6.png)
