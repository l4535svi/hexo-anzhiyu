---
title: ➖Cloudflare部署机场订阅转换链接
date: '2026-07-01 12:00:00'
cover: /img/covers/cloudflare-2.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 2. Vercel 部署 点击上方按钮即可快速部署到 Vercel，系统会自动引导你配置必要的环境变量。或者手动操作： 在 Vercel 控制台导入 Fork 仓库。 前往 Settings → Environment Variables 写入 KV_REST_API_URL 和
---
## 2\. Vercel 部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/7Sageer/sublink-worker&env=KV_REST_API_URL,KV_REST_API_TOKEN&envDescription=Vercel%20KV%20credentials%20for%20data%20storage&envLink=https://vercel.com/docs/storage/vercel-kv)

点击上方按钮即可快速部署到 Vercel，系统会自动引导你配置必要的环境变量。或者手动操作：

  1. 在 Vercel 控制台导入 Fork 仓库。
  2. 前往 `Settings → Environment Variables` 写入 `KV_REST_API_URL` 和 `KV_REST_API_TOKEN`（若使用 Vercel KV 会自动生成）。
  3. 执行 `vercel deploy`，即可得到 `/api/index.js` 驱动的无服务器应用。

搭建教程

[![](https://blogger.googleusercontent.com/img/a/AVvXsEibXRj-U2rEdDkulauMeGsVDLCFN52Nh7PrWn9pxP34VyG1H9Uxjwrotyt6-dnj62bbAyqqjO9YAl2utZ4_I3_JRZLyQwLbkWO6vV_qzGsT8y1C_mATUlJyFU_yGTxk6wM4jl7_64EEvGAgX72_jbZB3lVPKTJ77qP4LeRFR1xHW7ZLSgMQgcs0lqLh3Pug=w674-h308)](https://blogger.googleusercontent.com/img/a/AVvXsEibXRj-U2rEdDkulauMeGsVDLCFN52Nh7PrWn9pxP34VyG1H9Uxjwrotyt6-dnj62bbAyqqjO9YAl2utZ4_I3_JRZLyQwLbkWO6vV_qzGsT8y1C_mATUlJyFU_yGTxk6wM4jl7_64EEvGAgX72_jbZB3lVPKTJ77qP4LeRFR1xHW7ZLSgMQgcs0lqLh3Pug)

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi5domaKg5gNkLwcrxjbd8iwBvoyrunAnqkQPS6RNiBhmH_meGkBCNZu6XUm6nks7yyp_IIOxgIJnTb6rllYJ2D6zco6U9Wougn2_8k4nOOVJzLYcQ19E3VaSZa9_p1vIEeGTtgHwjyM513iUe8lZ0KwkBRocK269qEUIm21mm5-bgCe3O3V6VbK-bQ1jIs=w766-h313)](https://blogger.googleusercontent.com/img/a/AVvXsEi5domaKg5gNkLwcrxjbd8iwBvoyrunAnqkQPS6RNiBhmH_meGkBCNZu6XUm6nks7yyp_IIOxgIJnTb6rllYJ2D6zco6U9Wougn2_8k4nOOVJzLYcQ19E3VaSZa9_p1vIEeGTtgHwjyM513iUe8lZ0KwkBRocK269qEUIm21mm5-bgCe3O3V6VbK-bQ1jIs)

  

## 正确操作流程

### Step 1

## 

点击：
[code] 
    Upstash
[/code]
[/code]

* * *

### Step 2

## 

点：
[code] 
    Create Database
[/code]
[/code]

* * *

### Step 3

## 

创建 Redis 后你会看到：
[code] 
    REST URL  
    REST TOKEN  
    
    
    V_REST_API_READ_ONLY_TOKEN="ggAAAAAAAZKoAAIgcDGPDd3QfcDNNImndCeqtrf3PSv2cPULHbPQvUleb0bKMg"
    KV_REST_API_TOKEN="gQAAAAAAAZKoAAIgcDEwZTRkNDhkMWU1YWI0MDIzYTBlMmMxMGI0NGVjMDg0ZQ"
    KV_REST_API_URL="https://glowing-monster-103080.upstash.io"
    KV_URL="rediss://default:gQAAAAAAAZKoAAIgcDEwZTRkNDhkMWU1YWI0MDIzYTBlMmMxMGI0NGVjMDg0ZQ@glowing-monster-103080.upstash.io:6379"
    REDIS_URL="rediss://default:gQAAAAAAAZKoAAIgcDEwZTRkNDhkMWU1YWI0MDIzYTBlMmMxMGI0NGVjMDg0ZQ@glowing-monster-103080.upstash.io:6379"如何配置啊
    
    结论先行：你这组环境变量**已经完整正确了，不需要再“计算”，只需要“按名称拆分填进 Vercel 环境变量”** 。
    
    
    
    
    * * *
    
    
    
[/code]
[/code]

## 一、跳出背景（你现在的问题本质）

## 
[code]
    
    
    你拿到的是 Upstash 自动生成的一整套 Redis/KV 连接信息：
    
    
    
    
    包含两类：
    
    
    
    
    
    
        1. 
         KV 标准接口（Vercel KV 用）
         
    
    
        2. 
         Redis 原生连接（REDIS_URL / KV_URL）
         
    
    
    
    
    
    但 __这个项目只需要 KV_REST_API__ 那一组_*
    
    
    
    
    * * *
    
    
    
[/code]
[/code]

## 二、必须填哪些（核心）

## 
[code]
    
    
    在 Vercel → Settings → Environment Variables 里只需要：
    
    
    
[/code]
[/code]

### 1）KV_REST_API_URL

## 
[code]
    https://glowing-monster-103080.upstash.io
[/code]
[/code]

### 2）KV_REST_API_TOKEN

## 
[code]
    gQAAAAAAAZKoAAIgcDEwZTRkNDhkMWU1YWI0MDIzYTBlMmMxMGI0NGVjMDg0ZQ
[/code]
[/code]

### 3）KV_REST_API_READ_ONLY_TOKEN（可选）

## 
[code]
    ggAAAAAAAZKoAAIgcDGPDd3QfcDNNImndCeqtrf3PSv2cPULHbPQvUleb0bKMg
[/code]
[/code]

  

  

  

AI 总结

Sublink Worker 是一款旨在降低订阅转换与分发工具自托管门槛的工具。针对部分机场订阅缺乏分流（影响AI等应用使用）以及使用公共转换工具存在安全风险的问题，该项目支持利用 Cloudflare Workers 搭建私有的转换服务。用户可以通过 Cloudflare 与 GitHub 实现一键式快速部署，也可以通过手动 Fork 仓库、配置 Cloudflare KV 命名空间并修改配置文件等步骤进行手动部署，以便于后续的维护与更新。

![sublinkworker.png](https://imgbed.diggoo.xyz/file/blog/1782709166030_sublinkworker.png)
[code]
     很多机场的订阅链接没有做分流，比如要用AI，经常会使用到香港节点，
     导致不支持使用，这个时候就需要用到订阅转换。
     而订阅转换工具网上有很多，但毕竟是别人的后端，安全性不敢保证.
     所有利用强大的Cloudflare部署一个自己的订阅转换工具就很有必要。
    
    Sublink Worker 的核心目标是**尽可能降低订阅转换/分发工具的自托管门槛**。
    
[/code]

## 视频教程

* * *

YouTube：

BiliBili：

## 项目地址

* * *

[7Sageer/sublink-worker: One Worker, All Subscriptions](https://github.com/7Sageer/sublink-worker)

第一种方法一键Fork仓库部署，为了方便更新，我们使用第二种方法，手动部署。

## 1\. Cloudflare Workers 一键部署

[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/7Sageer/sublink-worker)

> 如果你之前通过Cloudflare部署过Github应用，可能会出现`An unknown error occurd`错误，可参考[FAQ](https://sublink.works/guide/faq#cloudflare%E5%BF%AB%E9%80%9F%E9%83%A8%E7%BD%B2%E6%8A%A5%E9%94%99-an-unknown-error-occurd)。

点击上方按钮即可自动完成 Fork 和部署。或者手动操作：

  1. 进入 [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/workers-and-pages/create)，选择 Workers & Pages → Create application → Pages → Connect to Git。
  2. 授权 GitHub 并选择 Fork 后的 `sublink-worker` 仓库。
  3. 在 Build 设置中：
     * Framework preset：`None`。
     * Build command：`npm run deploy`。
     * Build output directory：保持默认。
  4. 绑定自定义域名（可选），避免 `*.workers.dev` 在国内不可访问的问题。

部署完成后，Cloudflare 会注入 KV 以及 Worker 环境变量，默认即可运行；若需绑定 Redis/Upstash，请继续阅读[运行与存储](https://sublink.works/guide/runtime)。

## 2\. 手动部署

  1. 先Fork仓库，[点击Fork](https://github.com/ZhangShengFan/Pakr/fork)
  2. 进入[Cloudflare](https://dash.cloudflare.com/)，创建一个名为`SUBLINK_KV`的命名空间，可以是别的名字。  
点击左侧`存储和数据库`，选择`Workers KV`  
![sublinkworker7.png](https://imgbed.diggoo.xyz/file/blog/1782711591298_sublinkworker7.png)

![sublinkworker8.png](https://imgbed.diggoo.xyz/file/blog/1782711685449_sublinkworker8.png)  
![sublinkworker9.png](https://imgbed.diggoo.xyz/file/blog/1782711719937_sublinkworker9.png)

3.复制对应kv的ID，到GitHub项目库里面的`wrangler.toml`修改成你自己的id  
![sublinkworker14.png](https://imgbed.diggoo.xyz/file/blog/1782715563790_sublinkworker14.png)

  4. 回到Cloudflare 点击`计算`，`Wrokers和Pages`，点击右上角`创建应用程序`  
![sublinkworker2.png](https://imgbed.diggoo.xyz/file/blog/1782710325726_sublinkworker2.png)

5.选择`Continue with GitHub`

![sublinkworker3.png](https://imgbed.diggoo.xyz/file/blog/1782710457231_sublinkworker3.png)

6.选择`sublink-worker`仓库，点击下一步

![sublinkworker4.png](https://imgbed.diggoo.xyz/file/blog/1782710691398_sublinkworker4.png)

7.然后什么都不需要改动，直接点击部署

![sublinkworker5.png](https://imgbed.diggoo.xyz/file/blog/1782710799654_sublinkworker5.png)
