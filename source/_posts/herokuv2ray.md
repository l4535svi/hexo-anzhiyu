---
title: Heroku部署V2ray节点教程
date: '2022-04-14 12:00:00'
tags:
- 建站
categories:
- 建站
description: 准备材料 一枚GitHub账号 一枚Heroku账号 一枚CloudFlare账号 部署步骤 注册好GitHub账号 打开 仓库 ，并Fork一份 进入“Settings”，输入名称，改名 将README.md中的部署链接的的原仓库地址改成自己的仓库地址 注册并登录Heroku账
---
## 准备材料

  * 一枚GitHub账号
  * 一枚Heroku账号
  * 一枚CloudFlare账号

## [](https://owo.misaka.rest/herov2/#%E9%83%A8%E7%BD%B2%E6%AD%A5%E9%AA%A4 "部署步骤")部署步骤

  1. 注册好GitHub账号
  2. 打开[仓库](https://github.com/DaoChen6/Heroku-v2ray)，并Fork一份
  3. 进入“Settings”，输入名称，改名

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225241.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225241.png)

  4. 将README.md中的部署链接的的原仓库地址改成自己的仓库地址

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225333.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225333.png)

  5. 注册并登录Heroku账号
  6. 输入名称和生成的UUID，没有可以从[这里](https://www.uuidgenerator.net/)生成一个，输入节点类型，点击“Deploy APP”等待部署完成

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225506.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225506.png)

  7. 注册并登录[CloudFlare](https://www.cloudflare.com/)账号
  8. 点击Workers，点击“Create Service”按钮

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225744.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225744.png)

  9. 输入自己想要的名称，其他默认，点击“Create Service”按钮

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225817.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225817.png)

  10. 点击“Quick Edit”

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225915.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129225915.png)

  11. 复制以下代码，粘贴到Worker中

单账号

JAVASCRIPT
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    
[/code]

| 
[code]
    addEventListener(  
        "fetch",event => {  
            let url=new URL(event.request.url);  
            url.hostname="appname.herokuapp.com";  
            let request=new Request(url,event.request);  
            event. respondWith(  
                fetch(request)  
            )  
        }  
    )  
    
[/code]  
  
---|---  
  
双账号

JAVASCRIPT
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    11  
    12  
    13  
    14  
    15  
    16  
    17  
    18  
    19  
    20  
    
[/code]

| 
[code]
    const SingleDay = 'app0.herokuapp.com'  
    const DoubleDay = 'app1.herokuapp.com'  
    addEventListener(  
        "fetch",event => {  
          
            let nd = new Date();  
            if (nd.getDate()%2) {  
                host = SingleDay  
            } else {  
                host = DoubleDay  
            }  
              
            let url=new URL(event.request.url);  
            url.hostname=host;  
            let request=new Request(url,event.request);  
            event. respondWith(  
                fetch(request)  
            )  
        }  
    )  
    
[/code]  
  
---|---  
  
  12. 点击“Save and deploy”，点击“Send”按钮
  13. 出现200OK即为成功反代

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129230144.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129230144.png)

  14. 转到V2rayN，设置一个服务器，如图所示

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129230539.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/tuchuang/20220129230539.png)

> PS: 不会优选IP？看[这里](https://owo.misaka.rest/cf-ip/)
