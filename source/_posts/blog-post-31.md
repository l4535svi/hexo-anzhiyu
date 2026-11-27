---
title: 哪吒探针显示流量使用进度
date: '2025-08-01 12:00:00'
cover: /img/covers/blog-post-31.jpg
tags:
- 哪吒探针
categories:
- 哪吒探针
description: NEZHA配置生成器 根据个人情况填写参数，然后生成和复制代码。 监控的服务器id在这里： 多个服务器id中间可以用逗号‘，’隔开。 这个时候我们在将以下代码添加到美化代码的下方即可： <script> /* window.TrafficScriptConfig = { show
---
### [NEZHA配置生成器](https://nzcfg.pages.dev/)

![1e0a2d7ee5752c78001.webp](https://img.211200.xyz/i/2025/07/04/1e0a2d7ee5752c78001.webp)  
根据个人情况填写参数，然后生成和复制代码。  
监控的服务器id在这里：  
![4e71bcf7137a5d5c001.webp](https://img.211200.xyz/i/2025/07/04/4e71bcf7137a5d5c001.webp)  
多个服务器id中间可以用逗号‘，’隔开。  
![e8d436226552a76b001.webp](https://img.211200.xyz/i/2025/07/04/e8d436226552a76b001.webp)  
![42c281d457cf7e0a001.webp](https://img.211200.xyz/i/2025/07/04/42c281d457cf7e0a001.webp)  
这个时候我们在将以下代码添加到美化代码的下方即可：
[code]
    <script>
    /*
      window.TrafficScriptConfig = {
        showTrafficStats: true,    // 显示流量统计, 默认开启
        insertAfter: true,         // 如果开启总流量卡片, 是否放置在总流量卡片后面, 默认为true
        interval: 60000,           // 60秒刷新缓存, 单位毫秒, 默认60秒
        toggleInterval: 5000,      // 4秒切换流量进度条右上角内容, 0秒不切换, 单位毫秒, 默认5秒
        duration: 500,             // 缓出缓进切换时间, 单位毫秒, 默认500毫秒
        enableLog: false           // 开启日志, 默认关闭
      };
    */
    </script>
    <script src="https://cdn.jsdelivr.net/gh/8730062/installnet@main/jdt.js"></script>
    
[/code]

直接添加在我们之前美化代码的末尾之后就行  
![79eb8bf3d75bf1da001.webp](https://img.211200.xyz/i/2025/07/04/79eb8bf3d75bf1da001.webp)  
这样流量进度条就显示出来了  
![25aba4e3d399381c001.webp](https://img.211200.xyz/i/2025/07/04/25aba4e3d399381c001.webp)
