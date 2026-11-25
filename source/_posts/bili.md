---
title: 拉取Bili库(青龙重要文件)
date: '2025-01-10 12:00:00'
cover: https://picsum.photos/seed/bili/800/450
tags:
- 青龙全部
categories:
- 青龙全部
description: '拉取Bili库:ql repo https://github.com/RayWangQvQ/BiliBiliToolPro.git "bili_task_" 必须这个定时规则: 2 2 28 * * 1、部署青龙并登陆，版本不用追新，稳定才好，推荐whyour/qinglong:'
---
拉取Bili库:ql repo https://github.com/RayWangQvQ/BiliBiliToolPro.git "bili_task_"

必须这个定时规则:2 2 28 * *

1、部署青龙并登陆，版本不用追新，稳定才好，推荐whyour/qinglong:2.17.9镜像部署。

2、到订阅管理创建订阅并运行；正确配置[参考](https://github.com/6dylan6/jdpro/issues/22)

3、订阅执行完，到定时任务搜索依赖安装（jd_indeps.sh)任务执行；

4、到环境变量，创建变量，名称: JD_COOKIE,值：抓的CK（要安全就手抓），多个每行建一个，不要全写在一个；

5、配置通知，通知的key填写到配置管理config.sh文件；

## 6dy

[](https://github.com/6dylan6/jdpro#6dy)

声明: 此库所有内容仅用于个人学习！！！

### [TG CHANEL](https://t.me/dylan_jdpro)

[](https://github.com/6dylan6/jdpro#tg-chanel)

国内机（带代理）：

解释
[code]
    ql repo https://js.okyago.com/https://github.com/6dylan6/jdpro.git "jd_|jx_|jddj_" "backUp" "^jd[^_]|USER|JD|function|sendNotify|utils"
    
    
[/code]

国外机：

解释
[code]
    ql repo https://github.com/6dylan6/jdpro.git "jd_|jx_|jddj_" "backUp" "^jd[^_]|USER|JD|function|sendNotify|utils"
    
    
[/code]

线报监控类，[入口](https://github.com/6dylan6/jdm.git)

京东

### 京东定时任务库

下方缙哥哥整理 GitHub 上的一些任务库，通过添加任务，并设置定时规则，使其自动拉取、更新羊毛任务。

这个库是不是会更新，如果你有所需要，可以评论留言，将会接收到邮件提醒。

6dylan6/jdpro（集合库），任务定时建议十分钟一次。

复制
[code]
    ql repo https://github.com/6dylan6/jdpro.git "jd_|jx_|jddj_" "backUp" "^jd[^_]|USER|JD|function|sendNotify|utils"
[/code]

[Faker2](https://github.com/shufflewzc/faker2) 助力池

复制
[code]
    ql repo https://github.com/shufflewzc/faker2.git "jd_|jx_|gua_|jddj_|jdCookie" "activity|backUp" "^jd[^_]|USER|function|utils|sendNotify|ZooFaker_Necklace.js|JDJRValidator_|sign_graphics_validate|ql|JDSignValidator|magic|depend|h5sts" "main"
[/code]

[Faker3](https://github.com/shufflewzc/faker3) 纯净版

复制
[code]
    ql repo https://github.com/shufflewzc/faker3.git "jd_|jx_|gua_|jddj_|jdCookie" "activity|backUp" "^jd[^_]|USER|function|utils|sendNotify|ZooFaker_Necklace.js|JDJRValidator_|sign_graphics_validate|ql|JDSignValidator|magic|depend|h5sts" "main"
[/code]

咱们为了防止漏掉某些羊毛，上方所有的库新建定时任务拉取，里面有重复脚本禁用脚本，重复的内容会被禁用的。

具体示例如下： 

0 0 1 * * ? #每天 1 点触发 

0 10 1 ? * * #每天 1:10 触发 

*/5 * * * * ? #每隔 5 秒执行一次 

0 */1 * * * ? #每隔 1 分钟执行一次 

0 0 2 1 * ? * #每月 1 日的凌晨 2 点执行一次 

0 0 1 * * ? #每天 23 点执行一次 

0 0 1 * * ? #每天凌晨 1 点执行一次 

0 0 1 1 ? * #每月 1 日凌晨 1 点执行一次 

0 26,29,33 * * * ? #在 26 分、29 分、33 分执行一次 

0 0 0,13,18,21 * * ? #每天的 0 点、13 点、18 点、21 点都执行一次 

0 0 10,14,16 * * ? #每天上午 10 点，下午 2 点，4 点执行一次 

0 0/30 9-17 * * ? #每天朝九晚五工作时间内每半小时执行一次 

0 * 14 * * ? #每天下午 2 点到 2:59 期间的每 1 分钟触发 

0 */5 14 * * ? #每天下午 2 点到 2:55 期间的每 5 分钟触发 

0 */5 14,18 * * ? #每天下午 2 点到 2:55 期间和下午 6 点到 6:55 期间的每 5 分钟触发 

0 0-5 14 * * ? #每天下午 2 点到 2:05 期间的每 1 分钟触发 

0 15 10 15 ？ * #每月 15 日上午 10:15 触发 

视频中用到的资料： 仓库：https://github.com/6dylan6/jdpro.git JD_COOKIE pt_key=**********************; pt_pin=******************; 手动安装依赖： 【NodeJs 依赖如下】 request canvas cheerio js-base64 dotenv magic tough-cookie ws@7.4.3 require requests date-fns ts-md5 typescript json5 axios@v0.27.2 crypto-js @types/node png-js node-telegram-bot-api fs jsdom form-data jieba tslib ds jsdom -g prettytable ql common node-jsencrypt juejin-helper moment global-agent Copy \---------------------------------------------------------------------- 【Python3 依赖如下】 bs4 telethon cacheout jieba PyExecJS ping3 canvas Crypto ds requests pycryptodome Copy \------------------------------------------------------------------ 【Linux 依赖如下】 bizCode bizMsg lxml libc-dev gcc g++ libffi-dev python3-dev \-------------------------------------------------------------------- 自动抓取cookie软件蓝奏网盘： 下载:https://wwej.lanzn.com/ihBS82hrlwuf 密码:atpi

新版青龙拉库方式，在订阅管理创建订阅，然后运行订阅，等待完成，到定时任务查看  
[![image](https://private-user-images.githubusercontent.com/86815944/280519491-bff861be-4bc6-4ca2-9282-1b54ae64ce42.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDg1ODUyOTgsIm5iZiI6MTc0ODU4NDk5OCwicGF0aCI6Ii84NjgxNTk0NC8yODA1MTk0OTEtYmZmODYxYmUtNGJjNi00Y2EyLTkyODItMWI1NGFlNjRjZTQyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTMwVDA2MDMxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc5NjcyMTMzOTNmYmVjYWZkZWNhMGRiOWVjOTk2ZTI3YWEwZGM3YjI2N2FiOGQwNzY2YWIxNDA4YjI3M2Q1ZTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.-q8ufnDVsPQll0z309ui3VyNIG7xC7yAoXHLDil_2zk)](https://private-user-images.githubusercontent.com/86815944/280519491-bff861be-4bc6-4ca2-9282-1b54ae64ce42.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDg1ODUyOTgsIm5iZiI6MTc0ODU4NDk5OCwicGF0aCI6Ii84NjgxNTk0NC8yODA1MTk0OTEtYmZmODYxYmUtNGJjNi00Y2EyLTkyODItMWI1NGFlNjRjZTQyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTMwVDA2MDMxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc5NjcyMTMzOTNmYmVjYWZkZWNhMGRiOWVjOTk2ZTI3YWEwZGM3YjI2N2FiOGQwNzY2YWIxNDA4YjI3M2Q1ZTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.-q8ufnDVsPQll0z309ui3VyNIG7xC7yAoXHLDil_2zk)  
下拉  
[![image](https://private-user-images.githubusercontent.com/86815944/311431117-e5388e4b-ab95-49f5-a9bc-552d34171737.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDg1ODUyOTgsIm5iZiI6MTc0ODU4NDk5OCwicGF0aCI6Ii84NjgxNTk0NC8zMTE0MzExMTctZTUzODhlNGItYWI5NS00OWY1LWE5YmMtNTUyZDM0MTcxNzM3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTMwVDA2MDMxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY1MDg1MmY2ZmI2NGRiYTJhOWI5MjQwYmUzY2NiMjIxZDdmZDMyMzIxMTc2ZGMwZjZjODEzNGU0MjA0ZjI0MzEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.D99T3vdmY14cIexIr__GkzE73oVufJmrEV0ru0v1rTw)](https://private-user-images.githubusercontent.com/86815944/311431117-e5388e4b-ab95-49f5-a9bc-552d34171737.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDg1ODUyOTgsIm5iZiI6MTc0ODU4NDk5OCwicGF0aCI6Ii84NjgxNTk0NC8zMTE0MzExMTctZTUzODhlNGItYWI5NS00OWY1LWE5YmMtNTUyZDM0MTcxNzM3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTMwVDA2MDMxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY1MDg1MmY2ZmI2NGRiYTJhOWI5MjQwYmUzY2NiMjIxZDdmZDMyMzIxMTc2ZGMwZjZjODEzNGU0MjA0ZjI0MzEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.D99T3vdmY14cIexIr__GkzE73oVufJmrEV0ru0v1rTw)

2.13及之前老版本青龙直接在定时任务里新建任务就行，例图  
[![image](https://user-images.githubusercontent.com/86815944/234491091-b1bd4ae9-fcdc-4265-99eb-d632cfe973b4.png)](https://user-images.githubusercontent.com/86815944/234491091-b1bd4ae9-fcdc-4265-99eb-d632cfe973b4.png)

定时注意不要填错，不要每秒或每分钟拉一次

## Activity

[![](https://avatars.githubusercontent.com/u/86815944?s=64&v=4)6dylan6](https://github.com/6dylan6)

pinned this issue [on Jun 7, 2023](https://github.com/6dylan6/jdpro/issues/22#event-9451779777)

[![Jone2008](https://avatars.githubusercontent.com/u/70353049?u=aa68953afa47784956039d09441bca9d71ed354e&v=4&size=80)](https://github.com/Jone2008)

### Jone2008 commented on Jun 7, 2023

[Jone2008](https://github.com/Jone2008)

[on Jun 7, 2023](https://github.com/6dylan6/jdpro/issues/22#issuecomment-1579661550) · edited by [Jone2008](https://github.com/Jone2008)

Edits

ql repo <https://github.com/6dylan6/jdpro.git> "jd_|jx_|jddj_" "backUp" "^jd[^_]|USER|JD|function|sendNotify" "main"

新版青龙，拉库命令的最后，可以加上默认分支main，
