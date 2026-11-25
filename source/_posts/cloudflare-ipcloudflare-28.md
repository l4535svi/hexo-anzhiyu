---
title: 试试Cloudflare IP优选！让Cloudflare在国内再也不是减速器！
date: '2025-06-28 12:00:00'
cover: https://picsum.photos/seed/cloudflare-ipcloudflare-28/800/450
tags:
- CF优选域名
categories:
- CF优选域名
description: 'Worker路由反代全球并优选（新） # 本方法的原理为通过Worker反代你的源站，然后将Worker的入口节点进行优选。此方法不是传统的优选，源站接收到的Hosts头仍然是直接指向源站的解析 以下代码是原Github全站反代代码的二改以实现Worker路由接入优选，可能有多余'
---
# Worker路由反代全球并优选（新）[#](https://www.afo.im/posts/cf-fastip/#worker%E8%B7%AF%E7%94%B1%E5%8F%8D%E4%BB%A3%E5%85%A8%E7%90%83%E5%B9%B6%E4%BC%98%E9%80%89%E6%96%B0)

> 本方法的原理为通过Worker反代你的源站，然后将Worker的入口节点进行优选。此方法不是传统的优选，源站接收到的Hosts头仍然是直接指向源站的解析
> 
> 以下代码是原Github全站反代代码的二改以实现Worker路由接入优选，可能有多余逻辑或者不完全适配于优选需求

创建一个Cloudflare Worker，写入代码
[code]
    // 域名前缀映射配置
    const domain_mappings = {
      '源站.com': '最终访问头.',
    //例如：
    //'gitea.072103.xyz': 'gitea.',
    //则你设置Worker路由为gitea.*都将会反代到gitea.072103.xyz
    };
    
    addEventListener('fetch', event => {
      event.respondWith(handleRequest(event.request));
    });
    
    async function handleRequest(request) {
      const url = new URL(request.url);
      const current_host = url.host;
    
      // 强制使用 HTTPS
      if (url.protocol === 'http:') {
        url.protocol = 'https:';
        return Response.redirect(url.href, 301);
      }
    
      const host_prefix = getProxyPrefix(current_host);
      if (!host_prefix) {
        return new Response('Proxy prefix not matched', { status: 404 });
      }
    
      // 查找对应目标域名
      let target_host = null;
      for (const [origin_domain, prefix] of Object.entries(domain_mappings)) {
        if (host_prefix === prefix) {
          target_host = origin_domain;
          break;
        }
      }
    
      if (!target_host) {
        return new Response('No matching target host for prefix', { status: 404 });
      }
    
      // 构造目标 URL
      const new_url = new URL(request.url);
      new_url.protocol = 'https:';
      new_url.host = target_host;
    
      // 创建新请求
      const new_headers = new Headers(request.headers);
      new_headers.set('Host', target_host);
      new_headers.set('Referer', new_url.href);
    
      try {
        const response = await fetch(new_url.href, {
          method: request.method,
          headers: new_headers,
          body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : undefined,
          redirect: 'manual'
        });
    
        // 复制响应头并添加CORS
        const response_headers = new Headers(response.headers);
        response_headers.set('access-control-allow-origin', '*');
        response_headers.set('access-control-allow-credentials', 'true');
        response_headers.set('cache-control', 'public, max-age=600');
        response_headers.delete('content-security-policy');
        response_headers.delete('content-security-policy-report-only');
    
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: response_headers
        });
      } catch (err) {
        return new Response(`Proxy Error: ${err.message}`, { status: 502 });
      }
    }
    
    function getProxyPrefix(hostname) {
      for (const prefix of Object.values(domain_mappings)) {
        if (hostname.startsWith(prefix)) {
          return prefix;
        }
      }
      return null;
    }
[/code]

创建路由

![](https://free-eo-r2.afo.im/myblog/img/56752d54-26a5-46f1-a7d9-a782ad9874cb.webp)

类似这样填写

![](https://free-eo-r2.afo.im/myblog/img/d025398c-39e3-4bd7-8d8f-2ce06a45007d.webp)

最后写一条DNS解析 `CNAME gitea.afo.im --> 社区优选域名，如 cf.090227.xyz` 即可

# 针对于A、AAAA、CNAME（SaaS接入）[#](https://www.afo.im/posts/cf-fastip/#%E9%92%88%E5%AF%B9%E4%BA%8Eaaaaacnamesaas%E6%8E%A5%E5%85%A5)

> 我们需要两个域名（比如：onani.cn和acofork.cn）。
> 
> 如果在同一CF账号下不可用，请尝试将俩域名放置在不同账号

这里我们让onani.cn成为主力域名，让acofork.cn成为辅助域名
