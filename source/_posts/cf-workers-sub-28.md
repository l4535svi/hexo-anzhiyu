---
title: 自建订阅！CF-Workers-SUB 教你如何将多节点多订阅汇聚合并为一个订阅！
date: '2025-01-28 12:00:00'
tags:
- 节点分享
categories:
- 节点分享
description: 定制汇聚订阅 CF-Workers-SUB 汇聚订阅 是将 多个节点 和 多个订阅 合并为 一个订阅链接 的工具，简化了订阅管理，并提供了自动适配和自定义分流等高级功能，极大地方便了小白的使用。 汇聚订阅有哪些优点？ 节点链接自动转换成base64订阅链接： 这是最基础的功能，可
---
# [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#%E5%AE%9A%E5%88%B6%E6%B1%87%E8%81%9A%E8%AE%A2%E9%98%85-CF-Workers-SUB "定制汇聚订阅 CF-Workers-SUB")[定制汇聚订阅 CF-Workers-SUB](https://github.com/cmliu/CF-Workers-SUB)

> 汇聚订阅是将多个节点和多个订阅合并为一个订阅链接的工具，简化了订阅管理，并提供了自动适配和自定义分流等高级功能，极大地方便了小白的使用。

## [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#%E6%B1%87%E8%81%9A%E8%AE%A2%E9%98%85%E6%9C%89%E5%93%AA%E4%BA%9B%E4%BC%98%E7%82%B9%EF%BC%9F "汇聚订阅有哪些优点？")汇聚订阅有哪些优点？

  1. 节点链接自动转换成base64订阅链接： 这是最基础的功能，可以将您的节点自动转换为base64格式的订阅链接；
  2. 将多个base64订阅汇聚成一个订阅链接： 可以将多个订阅（例如不同的机场）合并成一个订阅，只需使用一个订阅地址即可获取所有节点；
  3. 自动适配不同梯子的格式订阅链接： 依托[订阅转换](https://sub.fxxk.dedyn.io/)服务，自动将订阅转换为不同梯子所需的格式，实现一条订阅适配多种梯子；
  4. 专属代理分流规则： 通过自定义分流规则，可以实现个性化的分流模式，摆脱机场提供的简单分流规则；
  5. 更多高级功能等待您发掘…

[![CF-Workers-SUB](https://xn--1uto7rutmzjk.us.kg/img/404.jpg)](https://github.cmliussss.com/https://raw.githubusercontent.com/cmliu/CF-Workers-SUB/refs/heads/main/sub.png)

* * *

## [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#%E4%BB%80%E4%B9%88%E6%98%AF%E8%AE%A2%E9%98%85%EF%BC%9F "什么是订阅？")什么是订阅？

在早期，代理协议非常简单，只有`IP:端口`和`密码`等几个参数。然而，随着GFW的不断进化，代理协议也变得越来越复杂，附带的参数越来越多。为了方便节点的分享传播，开发者们制定了标准的LINK格式的分享链接，例如：

解释

plaintext
[code]
    1  
    2  
    3  
    
[/code]

| 
[code]
    trojan://34ec6bdf-602c-4bbe-933a-5c0823524201@cmc6.5gsieuvip.vn:443?security=tls&allowInsecure=1&type=tcp&headerType=none#%E4%BA%9A%E5%A4%AA%E5%9C%B0%E5%8C%BA1  
    vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIlx1NEZDNFx1N0Y1N1x1NjVBRjIiLA0KICAiYWRkIjogIjE5NC44Ny42OS4yNDQiLA0KICAicG9ydCI6ICIzNjY0MSIsDQogICJpZCI6ICIxY2M1OWEzYS05NjI1LTQwZjctYjBlNi1lMjMzMjg2YWU4MmQiLA0KICAiYWlkIjogIjAiLA0KICAic2N5IjogImF1dG8iLA0KICAibmV0IjogIndzIiwNCiAgInR5cGUiOiAibm9uZSIsDQogICJob3N0IjogIiIsDQogICJwYXRoIjogIi8iLA0KICAidGxzIjogIiIsDQogICJzbmkiOiAiIiwNCiAgImFscG4iOiAiIiwNCiAgImZwIjogIiINCn0=  
    ss://YWVzLTI1Ni1nY206S2l4THZLendqZWtHMDBybQ%3D%3D@38.114.114.77:5500#%E7%BE%8E%E5%9B%BD3  
    
[/code]  
  
---|---  
  
然而，随着越来越多的小白用户自建节点，一条条复制粘贴节点链接变得不再高效。于是，开发者们制定了订阅的标准，即将节点的LINK链接进行一次[base64编码](https://tool.chinaz.com/tools/base64.aspx)处理。通俗地说，就是将节点链接进行了一次打包处理，例如：

解释

plaintext
[code]
    1  
    
[/code]

| 
[code]
    dHJvamFuOi8vMzRlYzZiZGYtNjAyYy00YmJlLTkzM2EtNWMwODIzNTI0MjAxQGNtYzYuNWdzaWV1dmlwLnZuOjQ0Mz9zZWN1cml0eT10bHMmYWxsb3dJbnNlY3VyZT0xJnR5cGU9dGNwJmhlYWRlclR5cGU9bm9uZSMlRTQlQkElOUElRTUlQTQlQUElRTUlOUMlQjAlRTUlOEMlQkExCnZtZXNzOi8vZXcwS0lDQWlkaUk2SUNJeUlpd05DaUFnSW5Ceklqb2dJbHgxTkVaRE5GeDFOMFkxTjF4MU5qVkJSaklpTEEwS0lDQWlZV1JrSWpvZ0lqRTVOQzQ0Tnk0Mk9TNHlORFFpTEEwS0lDQWljRzl5ZENJNklDSXpOalkwTVNJc0RRb2dJQ0pwWkNJNklDSXhZMk0xT1dFellTMDVOakkxTFRRd1pqY3RZakJsTmkxbE1qTXpNamcyWVdVNE1tUWlMQTBLSUNBaVlXbGtJam9nSWpBaUxBMEtJQ0FpYzJONUlqb2dJbUYxZEc4aUxBMEtJQ0FpYm1WMElqb2dJbmR6SWl3TkNpQWdJblI1Y0dVaU9pQWlibTl1WlNJc0RRb2dJQ0pvYjNOMElqb2dJaUlzRFFvZ0lDSndZWFJvSWpvZ0lpOGlMQTBLSUNBaWRHeHpJam9nSWlJc0RRb2dJQ0p6Ym1raU9pQWlJaXdOQ2lBZ0ltRnNjRzRpT2lBaUlpd05DaUFnSW1ad0lqb2dJaUlOQ24wPQpzczovL1lXVnpMVEkxTmkxblkyMDZTMmw0VEhaTGVuZHFaV3RITURCeWJRJTNEJTNEQDM4LjExNC4xMTQuNzc6NTUwMCMlRTclQkUlOEUlRTUlOUIlQkQz  
    
[/code]  
  
---|---  
  
这就是小白用户经常看到的“乱码”，实际上这是base64格式的订阅内容。将这些内容导入到梯子（代理工具）后，所有节点信息将会显示出来，非常方便。

随着代理工具的功能越来越强大，我们的需求也不仅仅是翻墙这么简单。我们需要不同的站点使用不同的节点，以实现分流的目的。然而，订阅只包含节点信息，无法很好地传递分流规则。因此，[clash（mihomo）](https://wiki.metacubex.one/)和[singbox](https://sing-box.sagernet.org/zh/)应运而生，它们是市面上两大可以设置复杂分流规则的代理内核。

于是，出现了clash专用的`yml订阅格式`和singbox专用的`json订阅格式`。然而，这些订阅文件的编写对于小白用户来说门槛太高。因此，提供[订阅转换](https://sub.fxxk.dedyn.io/)服务的公益站点应运而生，可以将代理节点搭配[分流规则](https://raw.githubusercontent.com/cmliu/ACL4SSR/refs/heads/main/Clash/config/ACL4SSR_Online.ini)，在线转换成对应代理工具需要的订阅格式。

这就是订阅的来历。

* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#%E5%A6%82%E4%BD%95%E9%83%A8%E7%BD%B2 "如何部署")如何部署

## [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#Pages-%E9%83%A8%E7%BD%B2%E6%96%B9%E6%B3%95 "Pages 部署方法")Pages 部署方法

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#1-%E9%83%A8%E7%BD%B2-Cloudflare-Pages%EF%BC%9A "1. 部署 Cloudflare Pages：")1\. 部署 Cloudflare Pages：

  * 在 [Github](https://github.com/cmliu/CF-Workers-SUB) 上先 Fork 项目，并点上 Star !!!
  * 在 Cloudflare Pages 控制台中选择 `连接到 Git`后，选中 `CF-Workers-SUB`项目后点击 `开始设置`。

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#2-%E7%BB%99-Pages%E7%BB%91%E5%AE%9A-%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9F%9F%EF%BC%9A "2. 给 Pages绑定 自定义域：")2\. 给 Pages绑定 自定义域：

  * 在 Pages控制台的 `自定义域`选项卡，下方点击 `设置自定义域`。
  * 填入你的自定义次级域名，注意不要使用你的根域名，例如：  
您分配到的域名是 `fuck.cloudns.biz`，则添加自定义域填入 `sub.fuck.cloudns.biz`即可；
  * 按照 Cloudflare 的要求将返回你的域名DNS服务商，添加 该自定义域 `sub`的 CNAME记录 `CF-Workers-SUB.pages.dev` 后，点击 `激活域`即可。

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#3-%E4%BF%AE%E6%94%B9-%E5%BF%AB%E9%80%9F%E8%AE%A2%E9%98%85%E5%85%A5%E5%8F%A3-%EF%BC%9A "3. 修改 快速订阅入口 ：")3\. 修改 快速订阅入口 ：

例如您的pages项目域名为：`sub.fuck.cloudns.biz`；

  * 添加 `TOKEN` 变量，快速订阅访问入口，默认值为: `auto` ，获取订阅器默认节点订阅地址即 `/auto` ，例如 `https://sub.fuck.cloudns.biz/auto`

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#4-%E6%B7%BB%E5%8A%A0%E4%BD%A0%E7%9A%84%E8%8A%82%E7%82%B9%E5%92%8C%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%9A "4. 添加你的节点和订阅链接：")4\. 添加你的节点和订阅链接：

  1. 绑定变量名称为`KV`的KV命名空间；
  2. 访问 `https://sub.fuck.cloudns.biz/auto`，添加你的自建节点链接和机场订阅链接，确保每行一个链接，例如：

解释

plaintext
[code]1  
         2  
         3  
         4  
         
[/code]

| 
[code]vless://b7a392e2-4ef0-4496-90bc-1c37bb234904@cf.090227.xyz:443?encryption=none&security=tls&sni=edgetunnel-2z2.pages.dev&fp=random&type=ws&host=edgetunnel-2z2.pages.dev&path=%2F%3Fed%3D2048#%E5%8A%A0%E5%85%A5%E6%88%91%E7%9A%84%E9%A2%91%E9%81%93t.me%2FCMLiussss%E8%A7%A3%E9%94%81%E6%9B%B4%E5%A4%9A%E4%BC%98%E9%80%89%E8%8A%82%E7%82%B9  
         vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIuWKoOWFpeaIkeeahOmikemBk3QubWUvQ01MaXVzc3Nz6Kej6ZSB5pu05aSa5LyY6YCJ6IqC54K5PuiLseWbvSDlgKvmlabph5Hono3ln44iLA0KICAiYWRkIjogImNmLjA5MDIyNy54eXoiLA0KICAicG9ydCI6ICI4NDQzIiwNCiAgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsDQogICJhaWQiOiAiMCIsDQogICJzY3kiOiAiYXV0byIsDQogICJuZXQiOiAid3MiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAicHBmdjJ0bDl2ZW9qZC1tYWlsbGF6eS5wYWdlcy5kZXYiLA0KICAicGF0aCI6ICIvamFkZXIuZnVuOjQ0My9saW5rdndzIiwNCiAgInRscyI6ICJ0bHMiLA0KICAic25pIjogInBwZnYydGw5dmVvamQtbWFpbGxhenkucGFnZXMuZGV2IiwNCiAgImFscG4iOiAiIiwNCiAgImZwIjogIiINCn0=  
         https://sub.xf.free.hr/auto  
         https://hy2sub.pages.dev  
         
[/code]  
  
---|---  

* * *

## [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#Workers-%E9%83%A8%E7%BD%B2%E6%96%B9%E6%B3%95 "Workers 部署方法")Workers 部署方法

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#1-%E9%83%A8%E7%BD%B2-Cloudflare-Worker%EF%BC%9A "1. 部署 Cloudflare Worker：")1\. 部署 Cloudflare Worker：

  * 在 Cloudflare Worker 控制台中创建一个新的 Worker。
  * 将 [worker.js](https://github.com/cmliu/CF-Workers-SUB/blob/main/_worker.js) 的内容粘贴到 Worker 编辑器中。

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#2-%E4%BF%AE%E6%94%B9-%E8%AE%A2%E9%98%85%E5%85%A5%E5%8F%A3-%EF%BC%9A "2. 修改 订阅入口 ：")2\. 修改 订阅入口 ：

例如您的workers项目域名为：`sub.cmliussss.workers.dev`；

  * 通过修改 `mytoken` 赋值内容，达到修改你专属订阅的入口，避免订阅泄漏。

解释

plaintext
[code]1  
        
[/code]

| 
[code]let mytoken = 'auto';  
        
[/code]  
  
---|---  
如上所示，你的订阅地址则如下：

解释

plaintext
[code]1  
        
[/code]

| 
[code]https://sub.cmliussss.workers.dev/auto  
        
[/code]  
  
---|---  

### [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#3-%E6%B7%BB%E5%8A%A0%E4%BD%A0%E7%9A%84%E8%8A%82%E7%82%B9%E6%88%96%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%EF%BC%9A "3. 添加你的节点或订阅链接：")3\. 添加你的节点或订阅链接：

  1. 绑定变量名称为`KV`的KV命名空间；
  2. 访问 `https://sub.cmliussss.workers.dev/auto`，添加你的自建节点链接和机场订阅链接，确保每行一个链接，例如：

解释

plaintext
[code]1  
         2  
         3  
         4  
         
[/code]

| 
[code]vless://b7a392e2-4ef0-4496-90bc-1c37bb234904@cf.090227.xyz:443?encryption=none&security=tls&sni=edgetunnel-2z2.pages.dev&fp=random&type=ws&host=edgetunnel-2z2.pages.dev&path=%2F%3Fed%3D2048#%E5%8A%A0%E5%85%A5%E6%88%91%E7%9A%84%E9%A2%91%E9%81%93t.me%2FCMLiussss%E8%A7%A3%E9%94%81%E6%9B%B4%E5%A4%9A%E4%BC%98%E9%80%89%E8%8A%82%E7%82%B9  
         vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIuWKoOWFpeaIkeeahOmikemBk3QubWUvQ01MaXVzc3Nz6Kej6ZSB5pu05aSa5LyY6YCJ6IqC54K5PuiLseWbvSDlgKvmlabph5Hono3ln44iLA0KICAiYWRkIjogImNmLjA5MDIyNy54eXoiLA0KICAicG9ydCI6ICI4NDQzIiwNCiAgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsDQogICJhaWQiOiAiMCIsDQogICJzY3kiOiAiYXV0byIsDQogICJuZXQiOiAid3MiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAicHBmdjJ0bDl2ZW9qZC1tYWlsbGF6eS5wYWdlcy5kZXYiLA0KICAicGF0aCI6ICIvamFkZXIuZnVuOjQ0My9saW5rdndzIiwNCiAgInRscyI6ICJ0bHMiLA0KICAic25pIjogInBwZnYydGw5dmVvamQtbWFpbGxhenkucGFnZXMuZGV2IiwNCiAgImFscG4iOiAiIiwNCiAgImZwIjogIiINCn0=  
         https://sub.xf.free.hr/auto  
         https://hy2sub.pages.dev  
         
[/code]  
  
---|---  

* * *

## [](https://xn--1uto7rutmzjk.us.kg/p/CF-Workers-SUB/#%E5%8F%98%E9%87%8F%E8%AF%B4%E6%98%8E "变量说明")变量说明

变量名| 示例| 备注  
---|---|---  
TOKEN| `auto`| 快速订阅内置节点的订阅路径地址 /auto  
TGTOKEN| `6894123456:XXXXXXXXXX0qExVsBPUhHDAbXXXXXqWXgBA`| 发送TG通知的机器人token  
TGID| `6946912345`| 接收TG通知的账户数字ID  
SUBNAME| `CF-Workers-SUB`| 订阅名称  
SUBAPI| `subapi.fxxk.dedyn.io`| clash、singbox等 订阅转换后端  
SUBCONFIG| [https://raw.github.../ACL4SSR_Online_MultiCountry.ini](https://raw.githubusercontent.com/cmliu/ACL4SSR/main/Clash/config/ACL4SSR_Online_MultiCountry.ini)| clash、singbox等 订阅转换配置文件  
  
> TGTOKEN和TGID在使用时需要先到Telegram注册并获取。其中，TGTOKEN是telegram bot的凭证，TGID是用来接收通知的telegram用户或者组的id。

* * *

新人[Youtuber](https://www.youtube.com/@CMLiussss)，需要您的支持，请务必帮我点赞、关注、打开小铃铛， _十分感谢！！！_
