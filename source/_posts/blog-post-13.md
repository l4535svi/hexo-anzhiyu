---
title: 全自动获取免费机场节点/订阅方法分享【立即实现代理节点自由】
date: '2024-11-10 12:00:00'
cover: /img/covers/blog-post-13.jpg
tags:
- 科学上网
categories:
- 科学上网
description: '利用大佬 wzdnzd 的 一站式代理抓取及聚合平台 的这个项目在GitHubAction上实现节点自由 欢迎加入 一休技术交流群 讨论更多使用方法 使用流程如下 一、fork作者的代码仓库： GitHub - wzdnzd/aggregator: 自动签到、自动注册、订阅聚合及'
---
利用大佬[wzdnzd](https://github.com/wzdnzd)的[一站式代理抓取及聚合平台](https://github.com/wzdnzd/aggregator)的这个项目在GitHubAction上实现节点自由  
欢迎加入[一休技术交流群](https://t.me/yxjsjl)讨论更多使用方法

## [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E4%BD%BF%E7%94%A8%E6%B5%81%E7%A8%8B%E5%A6%82%E4%B8%8B "使用流程如下")使用流程如下

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E4%B8%80%E3%80%81fork%E4%BD%9C%E8%80%85%E7%9A%84%E4%BB%A3%E7%A0%81%E4%BB%93%E5%BA%93%EF%BC%9AGitHub-wzdnzd-aggregator-%E8%87%AA%E5%8A%A8%E7%AD%BE%E5%88%B0%E3%80%81%E8%87%AA%E5%8A%A8%E6%B3%A8%E5%86%8C%E3%80%81%E8%AE%A2%E9%98%85%E8%81%9A%E5%90%88%E5%8F%8A%E7%88%AC%E5%8F%96%E8%84%9A%E6%9C%AC%E7%AD%89 "一、fork作者的代码仓库：GitHub - wzdnzd/aggregator: 自动签到、自动注册、订阅聚合及爬取脚本等")一、fork作者的代码仓库：[GitHub - wzdnzd/aggregator: 自动签到、自动注册、订阅聚合及爬取脚本等](https://github.com/wzdnzd/aggregator)

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E4%BA%8C%E3%80%81%E5%90%AF%E7%94%A8Actions%EF%BC%8C%E5%A6%82%E4%B8%8B%E5%9B%BE%EF%BC%9A "二、启用Actions，如下图：")二、启用Actions，如下图：

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_1.png](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_1.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E4%B8%89%E3%80%81%E5%BC%80%E5%90%AF%E5%BF%85%E8%A6%81%E7%9A%84workflow%EF%BC%8C%E6%AF%94%E5%A6%82Collect-Refresh%E5%92%8CCheckin%EF%BC%8C%E5%85%B7%E4%BD%93%E6%93%8D%E4%BD%9C%E5%A6%82%E4%B8%8B%E5%9B%BE%EF%BC%9A "三、开启必要的workflow，比如Collect,Refresh和Checkin，具体操作如下图：")三、开启必要的workflow，比如Collect,Refresh和Checkin，具体操作如下图：

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_2.png](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_2.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E5%9B%9B%E3%80%81%E5%88%9B%E5%BB%BAgist%E5%B9%B6%E8%8E%B7%E5%8F%96%E5%88%B0username-gist-id%EF%BC%88%E8%AE%B0%E5%BE%97%E4%BF%9D%E5%AD%98%EF%BC%8C%E7%A8%8D%E5%90%8E%E8%A6%81%E7%94%A8%EF%BC%89%EF%BC%8C%E6%89%93%E5%BC%80-https-gist-github-com-%EF%BC%8C%E9%9A%8F%E4%BE%BF%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%EF%BC%8C%E5%86%85%E5%AE%B9%E9%9A%8F%E4%BE%BF%E5%A1%AB%EF%BC%8C%E5%A6%82%E5%9B%BE%E6%89%80%E7%A4%BA "四、创建gist并获取到username/gist_id（记得保存，稍后要用），打开 https://gist.github.com ，随便创建一个，内容随便填，如图所示")四、创建gist并获取到username/gist_id（记得保存，稍后要用），打开 [https://gist.github.com](https://gist.github.com/) ，随便创建一个，内容随便填，如图所示

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_3.png](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_3.png)  
[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_4.png](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_4.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E4%BA%94%E3%80%81%E5%9B%9E%E5%88%B0-Sign-in-to-GitHub-%C2%B7-GitHub-%E7%82%B9%E5%87%BBGenerate-new-token%E6%8C%89%E9%92%AE%E5%88%9B%E5%BB%BA-PAT%E3%80%82%E5%90%8D%E5%AD%97%E9%9A%8F%E4%BE%BF%E5%A1%AB%EF%BC%8C%E8%BF%87%E6%9C%9F%E6%97%B6%E9%97%B4%E9%80%89%E5%BE%97%E4%B9%85%E4%B8%80%E7%82%B9%EF%BC%8C%E9%87%8D%E8%A6%81%E7%9A%84%E6%98%AF%E5%9C%A8Account-permissions%E9%87%8C%E6%8E%88%E4%BA%88Gists%E7%9A%84%E8%AF%BB%E5%86%99%E6%9D%83%E9%99%90%EF%BC%8C%E5%88%9B%E5%BB%BA%E5%A5%BD%E5%90%8E%E5%A4%8D%E5%88%B6%E7%94%9F%E6%88%90%E7%9A%84token%E7%A8%8D%E5%90%8E%E7%94%A8 "五、回到 Sign in to GitHub · GitHub 点击Generate new token按钮创建 PAT。名字随便填，过期时间选得久一点，重要的是在Account permissions里授予Gists的读写权限，创建好后复制生成的token稍后用")五、回到 [Sign in to GitHub · GitHub](https://github.com/settings/tokens?type=beta) 点击Generate new token按钮创建 PAT。名字随便填，过期时间选得久一点，重要的是在`Account permissions`里授予`Gists`的读写权限，创建好后复制生成的token稍后用

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_5.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_5.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_5.png)  
[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_6.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_6.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_6.png)  
[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_7.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_7.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_7.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E5%85%AD%E3%80%81%E5%88%B0%E4%BB%93%E5%BA%93%E9%A1%B5%E9%9D%A2%E7%9A%84Settings%E9%87%8C%E8%AE%BE%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%EF%BC%8C%E5%8F%98%E9%87%8F%E5%90%8D%E4%B8%BAGIST-LINK%E5%92%8CGIST-PAT%EF%BC%8C%E5%80%BC%E5%88%86%E5%88%AB%E4%B8%BA%E7%AC%AC4%E5%92%8C5%E4%B8%A4%E6%AD%A5%E8%8E%B7%E5%8F%96%E5%88%B0%E7%9A%84%E5%86%85%E5%AE%B9 "六、到仓库页面的Settings里设置环境变量，变量名为GIST_LINK和GIST_PAT，值分别为第4和5两步获取到的内容")六、到仓库页面的`Settings`里设置环境变量，变量名为`GIST_LINK`和`GIST_PAT`，值分别为第4和5两步获取到的内容

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_8.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_8.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_8.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E4%B8%83%E3%80%81%E6%89%8B%E5%8A%A8%E8%BF%90%E8%A1%8C%E6%B5%8B%E8%AF%95%E6%98%AF%E5%90%A6%E8%83%BD%E5%A4%9F%E6%AD%A3%E5%B8%B8%E6%89%A7%E8%A1%8C%E5%B9%B6%E6%88%90%E5%8A%9F%E6%8E%A8%E9%80%81%E5%88%B0gist "七、手动运行测试是否能够正常执行并成功推送到gist")七、手动运行测试是否能够正常执行并成功推送到gist

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_9.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_9.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_9.png)

### [](https://yixiu.icu/2024/11/07/zidongjiedian/#%E5%85%AB%E3%80%81%E6%B7%BB%E5%8A%A0%E8%AE%A2%E9%98%85%E5%88%B0%E4%BD%A0%E7%9A%84%E7%BF%BB%E5%A2%99%E8%BD%AF%E4%BB%B6%E9%87%8C%EF%BC%8C%E6%B7%BB%E5%8A%A0%E4%B8%8D%E4%BA%86%E7%9A%84%E5%8F%AF%E4%BB%A5%E5%85%88%E8%AE%A2%E9%98%85%E8%BD%AC%E6%8D%A2%E4%B8%80%E4%B8%8B "八、添加订阅到你的翻墙软件里，添加不了的可以先订阅转换一下")八、添加订阅到你的翻墙软件里，添加不了的可以先订阅转换一下

[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_10.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_10.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_10.png)  
[![https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_11.png](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_11.png)](https://github.com/yixiu001/Figurebed/raw/main/blog/post/zidongjiedian/img_11.png)  
如果你也在用，可以去给项目作者点个star，更新挺频繁，也很贴心  
启用Action后如果中途你不想搞了，一定要禁用workflow或Action，因为默认每两小时自动执行一次

➖➖➖➖➖➖➖➖➖➖➖➖➖  
▶️ `新人`[YouTube](https://www.youtube.com/channel/UCMtXiCoKFrc2ovAGc1eywDg/) 需要您的支持，请务必帮我`点赞`、`关注`、`打开小铃铛`，十分感谢！！！ ✅  
🎁 不要只是下载或Fork。请 `follow` 我的[GitHub](https://github.com/yixiu001)、给我所有项目一个 `Star` 星星（拜托了）！你的支持是我不断前进的动力！ 💖

➖➖➖➖➖广告位➖➖➖➖  
【红杏加速器】优惠机场,专属全场套餐5折,低至5元左右222G,数量有限,先到先得!!!  
点击官网[【注册地址】](https://hongxingdl.com/web/#/login?code=fOEo9d4m)注册  
🎁5折优惠码：`Yixiu`  
✅多条高速IEPL专线，独家定制极速机场专线，玩游戏首选，支持奈飞，chatGPT,tiktok等8K流媒体。  
✅纯净IP，注册serv00毫无压力  
✅点击加入群聊不定期抽取机场会员[【点击加入】](https://t.me/yxjsjl)  
➖➖➖➖➖➖➖➖➖➖➖➖➖  
【小地球仪】免费VPN  
点击官网[【注册地址】](https://www.xiaodiqiuyi.com/)注册  
✅福利码:`174425`  
🎁注册输入福利码可以获得6天60gb的流量，和首次网页充值享受9折优惠  
✅注册只能在手机端注册  
✅支持免费试用  
✅纯净IP，注册serv00毫无压力  
➖➖➖➖➖➖➖➖➖➖➖➖➖  
【云狐VPN】专线机场  
点击官网[【注册地址】](https://yunfox.cc/#/register?code=rR44HXim)注册  
✔️无视晚高峰，高清流畅体验Netflix、Disney+等，可配置中转静态住宅IP，Chat GPT专线，海外社交流媒体全解锁。  
✔️月流量600GB，大额流量，满足所有用户使用。价格和流量绝对有性价比。  
➖➖➖➖➖➖➖➖➖➖➖➖➖
