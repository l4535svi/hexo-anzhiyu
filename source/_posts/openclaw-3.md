---
title: openclaw创建生图机器人
date: '2026-04-15 12:00:00'
tags:
- OpenClaw
categories:
- OpenClaw
description: 视频教程 414晚上发布 创建生图机器人 先创建一个飞书机器人(https://open.feishu.cn/page/openclaw?form=multiAgent) 创建Agent并绑定 之前我们讲过如何使用招聘HR来创建Agent，现在我们来创建一个图片助手的Agent
---
# 视频教程

414晚上发布

# 创建生图机器人

先创建一个飞书机器人(https://open.feishu.cn/page/openclaw?form=multiAgent)

![](https://guantou.site/upload/image-Ywvu.png)

![](https://guantou.site/upload/image-QCeA.png)

![](https://guantou.site/upload/image-pJDP.png)

# 创建Agent并绑定

之前我们讲过如何使用招聘HR来创建Agent，现在我们来创建一个图片助手的Agent

![](https://guantou.site/upload/image-AWnx.png)![](https://guantou.site/upload/image-Ewjk.png)![](https://guantou.site/upload/image-FlGR.png)![](https://guantou.site/upload/image-lzvG.png)

# 选择中转站

国内的话直接使用nanobanana的话，有很多限制，所以最好选择一个中转站来使用模型。

使用VAPI这个中转站，他接入了Nanobanana2模型,注册地址在 [VAPI ](https://api.gpt.ge/register?aff=qMCL)https://api.gpt.ge/register?aff=qMCL 点击就可以去注册了。

注册完成后，会有赠送金额，直接用就行.首先你需要在下图位置创建一个令牌Key来作为你的图片模型接入的令牌。这种中转站一般是提供模型中转，但是大多比直接买官网的要便宜很多，所以可以解决国内不方便并且还想要性价比的问题。

![](https://guantou.site/upload/image-ATJH.png)

创建完成后，可以来到模型广场，查看生图模型。我这里推荐Gemini家的生图模型nanobanana2，这个可以算是目前顶尖的生图模型了，我之前的好多图片都是用它生成的，对中文支持也很好。还可以在下面进行体验。看看生图如何。

![](https://guantou.site/upload/image-iIDO.png)![](https://guantou.site/upload/image-JMix.png)

## 需要准备的东西

  1. 刚刚创建的令牌Key

  2. 模型的名称

  3. API端点(可以看上图)

# 安装生图技能

之前我们创建好了飞书机器人，现在需要给机器人Agent安装一个生图的Skill来控制生图质量。

安装这个Skill https://github.com/XY121718/baoyu-skills/,直接让Agent安装即可。

> 如果国内用户安装失败的话，从这里下载zip文件让龙虾安装也可以 https://pan.quark.cn/s/d398d19601e7

![](https://guantou.site/upload/image-TsDH.png)

安装完技能后，需要将之前准备的中转站信息，发给Agent去自己配置。

![](https://guantou.site/upload/image-rubo.png)![](https://guantou.site/upload/image-zBXB.png)![](https://guantou.site/upload/image-Wogr.png)

# 更多参考的风格指令

https://github.com/XY121718/baoyu-skills/blob/main/README.zh.md
