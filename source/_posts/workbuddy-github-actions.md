---
title: 把 WorkBuddy 每日签到丢给 GitHub Actions：一次配置，永久不用管
date: '2026-09-23 12:00:00'
cover: /img/covers/workbuddy-github-actions.jpg
tags:
- GPT
categories:
- GPT
description: WorkBuddy 的「Buddy 加油站」每天签到给 100 积分，连续第 7 天再给 1000。规则不复杂，难的是 每天都不落 ——忙起来忘一次，连签天数清零，前面攒的连续奖励全作废。 这篇讲一个已经跑通的方案：把签到交给 GitHub Actions， 一次配置，之后电脑关
---
WorkBuddy 的「Buddy 加油站」每天签到给 100 积分，连续第 7 天再给 1000。规则不复杂，难的是**每天都不落** ——忙起来忘一次，连签天数清零，前面攒的连续奖励全作废。

这篇讲一个已经跑通的方案：把签到交给 GitHub Actions，**一次配置，之后电脑关不关机都不影响** 。整个部署过程你只需要复制一条命令。

## 一、为什么不挂在自家电脑上

大部分人第一反应是在本机设个定时任务。问题是：电脑一关机，任务就停了。WorkBuddy 签到的连签奖励是按自然日算的，漏一天就得从头再来。

常见的几条路对比一下：

| 本机定时任务| 青龙面板| Cloudflare Workers| **GitHub Actions**  
---|---|---|---|---  
电脑关机后| ❌ 停摆| ✅ 照常| ✅ 照常| ✅ 照常  
要额外设备| 不用| NAS / 服务器| 不用| 不用  
成本| 0| 设备电费| 免费额度| 0（免费额度足够）  
上手难度| 低| 中| 高（要写 Worker）| **低**  
  
GitHub Actions 的优势在于：**它本身就有一台不用你管的机器，还自带定时器** 。这个任务每次跑不到两分钟，私有仓库每月 2000 分钟免费额度，一天跑三次也只用掉 6 分钟左右。

## 二、准备工作（只做一次，五分钟）

需要两样东西——一个是跑任务的「遥控器」，一个是你的「钥匙」：

需要| 怎么检查| 没有的话  
---|---|---  
Python 3.9+| `python --version`| `winget install --id Python.Python.3.12`  
Git| `git --version`| `winget install --id Git.Git`  
GitHub CLI| `gh --version`| `winget install --id GitHub.cli`  
gh 已登录| `gh auth status`| `gh auth login`  
**本机登录过 WorkBuddy 桌面端**|  —| 打开客户端登录一次  
  
最后一条是关键：部署器会从**你本机的登录态文件** 里读取凭据，不需要你手抄任何 Token，也不会上传到除你自己 GitHub 仓库以外的任何地方。

## 三、三步跑起来

### 第一次运行会自动帮你完成 GitHub 授权

如果 `gh` 还没登录，脚本会**直接拉起官方授权流程** ——你按回车，然后在浏览器里填入一次性验证码就行，不用另开终端敲命令。

### ⚠️ 有个容易踩的网络坑

`gh` 和 `git` 走的**不是同一个网络通道** ，这点很多人不知道：

工具| 访问的目标| 说明  
---|---|---  
`git`（clone / push）| `github.com:443`| 你机器上若配了 `http.proxy`，它会走代理  
`gh api`| `api.github.com`| 通常直连也能通  
**`gh auth login`**| **`github.com/login/device/code`**| **直连 github.com，且不读 git 的代理配置**  
  
所以会出现这种很迷惑的组合：**`gh api` 一切正常、仓库也推得动，但授权流程就是卡住超时。**原因是 `gh` 只看 `HTTPS_PROXY` 环境变量，不理会你给 git 配的代理。

两条绕法，任选其一：

**方法一：让 gh 也走你 git 用的那个代理**

TERMINAL COMMAND复制命令
[code]
    # 先看看你自己的代理地址
    git config --get http.proxy
    
    # 然后把它传给部署器
    python deploy.py --gh-proxy http://127.0.0.1:10808
    复制BASH
[/code]

脚本在检测到「git 有代理但 gh 没有」时会自动提示你，不用自己记。

**方法二：用 PAT 登录（更省事，不依赖 github.com 可达）**

  1. 浏览器打开 GitHub → Settings → Developer settings → **Personal access tokens** ，新建一个 Classic token，勾选 **`repo`** 和 **`workflow`** 两个 scope
  2. 存成 `token.txt`，然后执行：

TERMINAL COMMAND复制命令
[code]
    gh auth login --with-token < token.txt
    复制BASH
[/code]

这条只依赖 `api.github.com`，在 github.com 被墙、也没配代理的网络下同样可用。授权完成后重跑 `python deploy.py` 就行。

### 第 1 步：下载并解压

下载地址（约 31 KB）：

[提取文件 · 爱搜云盘输入 5 位取件码即可提取爱搜云盘中的文件，支持有效期校验与过期提示。![](https://static.ghost.org/v5.0.0/images/link-icon.svg)▤提取文件 ↗](https://pan.ailxw.com/pickup/53199?ref=isoziyuan.com)

解压到任意目录，里面只有 5 个文件，**不需要安装任何 Python 第三方包** 。

### 第 2 步：先预演，不动任何东西

TERMINAL COMMAND复制命令
[code]
    cd 解压后的目录
    python deploy.py --dry-run复制BASH
[/code]

这一步会把所有前置条件检查一遍，并打印出「待会儿到底要干什么」。全绿了再往下走。如果哪一项报红，它会直接告诉你缺什么、怎么补。

### 第 3 步：正式部署

TERMINAL COMMAND复制命令
[code]
    python deploy.py复制BASH
[/code]

接下来它会自动完成这些事，你只需要看着：

TERMINAL COMMAND复制命令
[code]
    [1] 检查运行环境
        ✓ git   git version 2.55.0
        ✓ gh    gh version 2.89.0
        ✓ gh 已登录：your-name
        ✓ 令牌权限：repo / workflow 齐备
        ✓ git 凭据助手：已接入 gh
    
    [2] 读取本机 WorkBuddy 登录态
        · 来源：C:\Users\you\AppData\Local\CodeBuddyExtension\...\workbuddy-desktop.info
        ✓ 账号 133****84    AT 1331 字符 / RT 700 字符
        · AT 剩余 55 天（至 2026-11-16 16:34）
    
    [3] 换算定时任务（北京 → UTC）
        ✓ 北京 07:00  →  cron 0 23 * * *
        ✓ 北京 12:00  →  cron 0 4 * * *
        ✓ 北京 23:30  →  cron 30 15 * * *
    
    [5] 准备代码        · 工作目录模式：临时目录（默认，跑完自动清理）
    [8] 写入 Secret     ✓ WORKBUDDY_REFRESH_TOKEN  已写入（加密，不可回读）
    [10] 触发一次验证运行
        ✓ 已触发运行 #35711817988，等待完成…
        ✓ 运行 #35711817988 成功复制BASH
    
    展开全部代码 (22 行)
[/code]

最后会直接打印这次的真实运行结果，比如：

TERMINAL COMMAND复制命令
[code]
    📊 各账号运行报告
       💰 主套餐剩余 1363.42 积分（共 7320，已用 5956.58）
       📊 共 46 类资源，本月已使用 2241 次
       🌱 等级 14 | 连签 22 天 | 能量 5
    📊 ══ 总计 ══复制BASH
[/code]

看到这个就说明整条链路通了。

## 四、它到底替你做了多少事

这套脚本的重点不是「点一下签到」——签到只是其中一项。它实际会跑完 WorkBuddy 成长中心的一整套任务：

类别| 数量| 例子  
---|---|---  
成长中心任务| 18 项（17 项全自动）| 设计创意模式、探索灵感、桌面端对话、尝鲜热门技能、体验资料库、召唤专家团、AI 对话 ×5、夜猫子活动…  
开学季活动| 5 项（4 项自动）| 分享活动、AI 对话 ×3、召唤开学季专家 + 幸运大转盘抽奖  
小程序任务| 3 项（全自动）| 小程序内对话、选中专家对话、校园日打卡  
互动玩法| 8 项| 抽奖、盲盒、派猫猫旅行、连签兑换、补签卡、徽章…  
每日签到| 1 项| 就是那 100 积分  
  
实测一次运行的完整输出大概是这样：

TERMINAL COMMAND复制命令
[code]
    ✅签到: 今天已签到，请明天再来
    🎁领奖[Hp_Appearance]: +100积分+5能量
    🎁领奖[Expert_team_use_3]: +100积分+5能量
    🎁领奖[Sequential_Tasks_1]: +100积分+5能量
    🎁领奖[school_season]: +100积分+5能量
    📦盲盒: 星际喵(SR)、咒语喵(R)、摸鱼喵(R)
    🐱Buddy: 暗影喵 (SR), 安全守护者
    🐾旅行: ✅已出发，约4小时后到达（下次运行自动领取）
    🏅徽章: 8个
    🏫 lottery → 6积分
    🏁 完成 14/19  等级14  剩余: 公益专家, 发现应用, 企鹅教师助手, 关注公众号, 夜猫子活动复制BASH
[/code]

有 3 项是**设计上做不了** 的，别被「全自动」误导：公益专家需要真实捐款、学生认证需要微信实名、关注公众号需要你自己扫码。剩下的会在后续运行里逐步补齐。

## 五、为什么配一次就不用再管

这是这套方案和普通签到脚本最大的区别。普通脚本只吃一个 `accessToken`，大约 60 天过期，到期后你得再去本机把 Token 抠出来换一遍。

这里用的是 **AT + RT（refreshToken）三元组** ，逻辑是：

TERMINAL COMMAND复制命令
[code]
    距上次刷新 > 10 天  或  AT 7 天内即将过期
            ↓
    用 RT 换发全新的 AT + RT，立即写回仓库
            ↓
    下次运行读到的就是新令牌复制BASH
[/code]

因为每次刷新都会轮换新令牌并落盘，所以**理论上配一次就永续** 。Actions 会自动把令牌状态提交回你的私有仓库，不需要你介入。

顺带一个好处：令牌库大约每 10 天产生一次提交，让仓库保持活跃，**避免 GitHub 因为 60 天无活动自动停用定时工作流** 。

## 六、安全边界（这一段请务必看完）

部署器动的东西只有这些：

动作| 说明  
---|---  
建一个**私有** 仓库| 在你自己的 GitHub 账号下，名字默认 `WorkBuddy-Daily`  
写入代码| 从开源项目 `L0NE-6/WorkBuddy-Daily` 克隆（MIT 协议）  
写入 1 个 Secret| 加密存储，**写进去之后连你自己也读不出明文**  
开一个定时任务| 每天 07:00 / 12:00 / 23:30（北京时间）  
改你本机什么| 默认**什么都不留** ——用临时目录，跑完自动删  
  
**它不会做的** ：不碰你的 WorkBuddy 客户端、不改系统设置、不装任何常驻程序。脚本只调用 `gh` 和 `git` 两个命令，没有任何自己的数据上报。

唯一要记住的事：那个私有仓库里会有一份 `wb_refresh_tokens.json`（Actions 自动续期需要它，里面是明文 refreshToken）。**永远不要把这个仓库改成 Public** ——那等于把账号控制权公开。部署器每次运行都会校验可见性，发现是公开的会直接中止，但你自己别手滑。

## 七、排障速查

现象| 处理  
---|---  
提示缺 Python / Git / gh| 按前面表格里的命令装，装完重开终端  
`gh auth status` 报未登录| `gh auth login`，按提示走一遍浏览器授权  
提示令牌缺少权限| `gh auth refresh -s repo,workflow`  
找不到 WorkBuddy 登录态| 先在 **本机** 打开 WorkBuddy 桌面端登录一次  
定时到点没跑| GitHub 的定时在高峰期会延迟几分钟到几十分钟，属正常；也可在 Actions 页面点 _Run workflow_ 手动触发  
日志报 `TOKEN_EXPIRED`| 重新登录桌面端，再跑一次 `python deploy.py --force-secret`  
  
想随时看状态：

TERMINAL COMMAND复制命令
[code]
    python deploy.py --check复制BASH
[/code]

想改签到时间（比如只在早上跑一次）：

TERMINAL COMMAND复制命令
[code]
    python deploy.py --schedule 09:10复制BASH
[/code]

重复运行是安全的——部署器会复用已有仓库，只提交真正的差异。

## 八、几个常见疑问

**Q：会不会重复领取？**  
不会。签到接口是幂等的，当天已签过会直接跳过，脚本也做了先查状态再操作的处理。把定时设成一天三次是为了容错，不是为了多领。

**Q：会不会把我的账号信息传到别处？**  
不会。凭据只通过 stdin 写进你自己仓库的 Secret，脚本本身没有任何外部上报。你可以自己解压看 `deploy.py`，标准库实现，没有任何第三方依赖。

**Q：积分什么时候用？**  
活动积分多数当月有效、不结转。领了就用，别攒着。

**Q：接口会不会变？**  
会。所有这类工具调的都是客户端在用的非公开接口，官方改版就可能失效。所以建议偶尔看一眼 Actions 的运行记录，发现连续失败就去项目页看有没有更新。

## 九、说在最后

签到这件事的价值不在于当天那 100 积分，而在于**连续不断的复利** ——而这恰恰是最反人性的部分。把规律、重复、低决策的事交给自动化，注意力留给真正要动脑的地方。

一次配置三分钟，之后你可以彻底忘掉这件事。

>   
> 解压后先跑 `python deploy.py --dry-run` 确认环境，再跑 `python deploy.py` 正式部署。

本部署器封装的是开源项目 [L0NE-6/WorkBuddy-Daily](https://github.com/L0NE-6/WorkBuddy-Daily?ref=isoziyuan.com)（MIT 协议，版权归原作者）。本工具为部署封装，
