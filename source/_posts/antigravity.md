---
title: '[图文]手把手教你Antigravity反代，全程不用敲代码，小白也能看懂的保姆教程'
date: '2026-02-26 12:00:00'
cover: /img/covers/antigravity.jpg
tags:
- Clawdbot
categories:
- Clawdbot
description: 一、安装/升级 反代工具CLIProxyAPI Windows 直接下载最新的文件，解压后就能使用，如果有更新，也是从这个链接中查找就行。 比如写文章时的最新版为： CLIProxyAPI_6.6.84_windows_amd64.zip https://github.com/r
---
# 一、安装/升级 反代工具CLIProxyAPI

### Windows

直接下载最新的文件，解压后就能使用，如果有更新，也是从这个链接中查找就行。

比如写文章时的最新版为：CLIProxyAPI_6.6.84_windows_amd64.zip
[code]
    https://github.com/router-for-me/CLIProxyAPI/releases
[/code]

本教程中我解压到了`D:\Tools\CLIProxyAPI_6.6.84_windows_amd64` 目录下，你可以解压到自己需要的目录，路径要全英文的，并且不能有空格。

### Ubuntu/Linux

使用一键脚本安装或升级，都用这个命令就行
[code]
    curl -fsSL https://raw.githubusercontent.com/brokechubb/cliproxyapi-installer/refs/heads/master/cliproxyapi-installer | bash
[/code]

### MacOS

使用brew安装命令
[code]
    brew install cliproxyapi
[/code]

后续升级命令
[code]
    brew upgrade cliproxyapi
[/code]

# 二、修改配置文件，启用后台管理

### Windows

安装目录下把`config.example.yaml`复制一份，复制的改名为`config.yaml`，然后修改里面的内容。

### Ubuntu/Linux

家(Home)目录下找`cliproxyapi/config.yaml`，即`~/cliproxyapi/config.yaml`，然后修改里面的内容。

### MacOS

`/opt/homebrew/etc`目录下找`cliproxyapi.conf`，即绝对路径为：`/opt/homebrew/etc/cliproxyapi.conf`，然后修改里面的内容。

### 修改文件如下内容(登录密码最好改成你自己的，我这里设置的是my-password)
[code]
    allow-remote: true  
    secret-key: "my-password"
[/code]

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJxMuCt3DJSwxtmwDNbJmuG0IWVZseqGibibHGkUCTb2p7Piasswr0BCxnA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)Windows版本: 先复制出config.yaml，然后修改配置

# 三、 启动CLIProxyAPI， 并登录网页后台查看：

### Windows

进入到刚才解压后的目录下直接exe执行就可以了，比如我刚才安装到了`D:\Tools\CLIProxyAPI_6.6.84_windows_amd64` 下。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJQM443aTrnpTsjprN2BiccXOqqymC9lcyGcdiadowf6TvvdqCJMmmZOzQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)Windows版本: 双击cli-proxy-api.exe，会自动打开后台服务  

### Ubuntu/Linux

进入到`~/cliproxyapi/`目录后，启动。
[code]
    cd ~/cliproxyapi/  
    ./cli-proxy-api 
[/code]

### MacOS

不需要进入任何目录，直接启动即可。
[code]
    brew services restart cliproxyapi
[/code]

### 登录网页后台

注意地址，本机的直接访问右边这个地址就行，首次登录密码是刚才设置的 my-password ：http://localhost:8317/management.html  
服务器的话要填服务器的地址或域名，比如你部署到了服务器的ip是`1.2.3.4`，则访问：`http://1.2.3.4:8317/management.html`  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJOMgEAUG04fWWUfcPvCxhrwgl5FFRnIn3x5762g3rSYT1rHLYShusMg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)访问网页后台，并使用密码登录  
登录后台成功后，可以看到仪表盘。建议把使用统计打开，这样后面用模型我能能看到用了多少的Tokens。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJMHWFPjY1M0W5xbHhZuIXXBhg59toj4wgATEQPlndKibwGKD2LpgNBXA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)登录成功后的仪表盘，可以开启使用统计，方便后续看用量

# 四、从网页登录Antigravity，成功后拷贝网址:

按照图示登录Antigravity，并等待自动认证成功，认证成功后登录网页会自动关闭。  
如果登录界面没有自动关闭(如图)，需要你手动把登录成功的网址复制粘贴回来，然后手动点击`提交回调URL`。  
如果还登录不上，可以尝试重启机器，然后别的软件先别开，这时打开反代服务 + 开启TUN魔法 + 挂到美国IP，再登录下试试。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJwA7p7VJX3UONvPkfydUCGUnuhmvh7SxqMfD0KPVkn6cK0dmzHowfIg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)登录Antigravity，如果没有自动成功并关闭，则手动把登录成功的网址再贴回来提交  
你还可以登录Gemini CLI ，这样就有更多的Gemini额度了。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJUkgpUy05s1dQG3nYXlXeASpCdWnHAf47kDb8ekqcd001HBCFqwL2fA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)登录Gemini CLI，获取更多Gemini模型额度登录认证成功后，后台就能看到认证信息了。我这里即反代了Antigravity，也反代了Gemini CLI, 如图：  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJQ2yXKm2ial2YMjpwKQnjIsEUNxBckSVfDfUUeEbz23PrjPKxtJRU8RA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)登陆成功后，认证文件管理页  
反代出来的模型，可以在`中心信息`中查看到。后面使用模型时，需要来这里复制模型名，不能随便写模型名。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJqg6SZs6AWAwdDlia51moeFbDUGxPbzicia9YQcdV6Rq9PTPzfkbsibp6aA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)反代出来的所有模型，后续使用时需要来这里复制模型名称，不可乱填模型名

# 五、Claude Code中使用

### 从网页后台获取api key，配置claude

注意`your-api-key-1`要配置成网页后台中的真正的api key，我这里演示的是默认的。  
模型的名称也要从网页后台拷贝，不要自己手写。  
base url 填写为 `"http://localhost:8317"`  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJQuCmN0TGTPXcdX3r32KHomLpmUJbZjARgZ7LycbbR4cMtsUDiaCu5lw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)网页后台的API KEY获取位置
[code]
      
    {  
        "env": {  
            "ANTHROPIC_BASE_URL": "http://localhost:8317",  
            "ANTHROPIC_AUTH_TOKEN": "your-api-key-1",  
            "ANTHROPIC_DEFAULT_OPUS_MODEL": "gemini-claude-opus-4-5-thinking",  
            "ANTHROPIC_DEFAULT_SONNET_MODEL": "gemini-claude-sonnet-4-5-thinking",  
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": "gemini-claude-sonnet-4-5",  
            "ANTHROPIC_MODEL": "gemini-claude-opus-4-5-thinking",  
            "ANTHROPIC_SMALL_FAST_MODEL": "gemini-claude-sonnet-4-5-thinking"  
        }  
    }  
    
[/code]

# 六、其它OpenAI兼容接口中使用

注意！base url 要改为： `http://localhost:8317/v1`  
 api key 和模型名和刚才一样，从网页后台复制就行了。  
vscode中可以通过`oai`插件(`OAI Compatible Provider for Copilot`)来添加到copilot中。

# 七、后台用量查看

**配额管理** ：点击刷新按钮，可以查看当前时段剩余的用量额度。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJSRfAtjDn5kXQHVppFvWic3cLpRvZCDSh4GfA07hmT2fuk2lP1JfxyWw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)配额管理，可以刷新查看当前时段剩余的额度  
**使用统计** ：查看请求次数和Tokens消耗等统计。  
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/EpgANI0GJ9vUdvp4gG2ebtvYy0bzpMfJNAzKBgF3jUuvHo7fH4hylSRmzIzjY8KPFFX9nXLbRN3FDzUwQZN12w/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)使用统计，可以查看访问次数和Tokens消耗等统计信息。

# Q&A

### Q1：有没有被封号的风险？

我在各个社区中还没看到有被封的(仅针对个人用户)。不过仍不建议用自己的大号搞，因为确实逆向了有风险，建议用小号搞吧。

### Q2：需要Google AI会员吗?

免费版的每周都有额度，但是额度很少，可以先试一下，把流程跑通了。付费会员或教育优惠会员，都是每5小时刷新额度，自己用一般是足够的，并且Gemin Pro\Gemini Flash\Claude这三组额度是独立的。  
然后可以考虑某鱼上买个成品号，关键字:`geminipro一年`，20左右(不知道最近涨价没)。

### Q3：我高强度使用，5小时额度不够怎么办啊？

最快速的是把谷歌的Gemini CLI工具也反代了，这个工具中只有Gemini系列的模型，并且额度和Antigravity中的不互通，是独立的。

其次有个被社区称为`升天`的方法：其实就是家庭组，Pro账号可以邀请最多5个人进入家庭(算上自己共6人)。家庭里每个账号的Antigravity和Gemini CLI的额度是独立的，所以可以创建几个小号，来组建家庭后把小号也反代了。

最后，还是那句话，不建议用自己的主号这么搞，最好拿某鱼买的号来搞。

### Q4：API KEY(API 密钥)是怎么生成的，从哪里拿？

API KEY在我们安装时，配置文件中会默认携带2个，你可以从网页上直接编辑-复制后使用。也可以在网页上把这两个KEY修改掉，或者自己新建后使用。

### Q5：OAI插件是什么？

OAI插件是搭配vscode copilot使用的，因为官方的copilot不支持自定义的模型和地址，所以需要这个插件来实现。

### Q6：OAI安装后没有右下角的 Ready显示怎么办？

首次安装后可以按 `Ctrl` + `Shift` + `P`，然后输入`oai`关键字，点击`Open Configuration UI`进入。

### Q7：OAI配置好了地址和模型，从copilot中访问失败怎么办？

大概率是地址配置错误，记得OpenAI格式的请求都需要加上`/v1`后缀，比如`http://10.126.12.162:8317/v1`。

### Q8: Windows上第二天就不能用了，访问不到模型了？

可能是关机了，或CLIProxyAPI被关掉了，然后反代的登录信息就失效了，下次开机或启动后，还需要重新登陆以下。  
如果是在服务器上部署的，并且一直执行，是不会失效的，因为CLIProxyAPI会周期性的去刷新下登录信息，保持一直登陆的状态。

### Q9: 能用Nano Banana Pro画图吗？

可以的，接入自己的画图工具就行了。有限额，但具体多少我不太清楚了。  
比如群友有使用CherryStudio的：https://www.cherry-ai.com/download
