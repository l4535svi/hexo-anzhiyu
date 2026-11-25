---
title: SSPanel-Metron为Github开源项目，目前由BobS9维护开发中
date: '2022-04-18 12:00:00'
tags:
- 建站
categories:
- 建站
description: 将机器的IP与域名进行绑定 1.配置aaPanel 你需要在 aaPanel 选择你的系统获得安装方式。这里以 CentOS 7+ 作为系统环境进行安装。 ⚠️请务必使用 CentOS 7+ 安装aaPanel，其他系统可能会有未知问题。 // 最新脚本可以在aaPanel官网获
---
## 将机器的IP与域名进行绑定

# 1.配置aaPanel

你需要在 aaPanel 选择你的系统获得安装方式。这里以 CentOS 7+ 作为系统环境进行安装。

⚠️请务必使用 CentOS 7+ 安装aaPanel，其他系统可能会有未知问题。
[code]
    // 最新脚本可以在aaPanel官网获取  
    yum install -y wget && wget -O install.sh http://www.aapanel.com/script/install_6.0_en.sh && bash install.sh
[/code]

执行完毕后，会显示类似下面的宝塔面板的登录信息，请保存好此信息
[code]
    Bt-Panel: http://xxx.xxx.xx.xx:8888/xxxxxxx  
    username: xxxxxxx  
    password: xxxxxxxx  
    
[/code]

安装完成后我们登陆 aaPanel 进行环境的安装。  
选择使用LNMP的环境安装方式勾选如下信息

☑️ Nginx 1.17  
☑️ MySQL 5.6  
☑️ PHP 7.2

选择 Fast 快速编译后进行安装。  
需要一段时间才能安装完成，请等待完成。

# 2.配置PHP

打开 aaPanel 面板 > App Store > 你安装的PHP > Setting，在 Disabled functions一栏删除 `system`、`proc_open`、`proc_get_status`、`putenv`、`pcntl_signal`。

# 3.安装Metron主题

aaPanel 面板 > Website > Add site。输入你的域名和建一个数据库，点击提交
[code]
    cd /www/wwwroot/你的网站文件夹名
[/code]

上传您的源码

源码github 官网 ：[BobCoderS9/SSPanel-Metron: SSPanel-Metron主题，目前由@Bobs9维护开发中。 (github.com)](https://github.com/BobCoderS9/SSPanel-Metron)

或官网下载链接[点击下载](https://github.com/BobCoderS9/SSPanel-Metron/archive/refs/heads/master.zip)

（因为一些原因，不再提供旧版源码，请前去GitHub自行下载最新版，需要添加QQ客服接口，下载[menu.tpl](https://blog.lvuy.xyz/wp-content/uploads/2022/03/%E5%9C%A8%E7%BA%BFQQ%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.rar) 自行替换

使用composer安装依赖
[code]
    wget https://getcomposer.org/installer -O composer.phar  
    php composer.phar  
    php composer.phar install
[/code]

用composer安装依赖时如果内存不够的话，可以使用 宝塔面版 > 首页 > Linux工具箱 > Swap/虚拟内存 增加虚拟内存

# 4.复制配置文件
[code]
    cp config/.config.example.php config/.config.php  
    cp config/.metron_setting.example.php config/.metron_setting.php  
    cp config/appprofile.example.php config/appprofile.php
[/code]

# 5.配置站点目录及伪静态

添加完成后编辑添加的站点 > Site directory > Running directory 选择 /public 保存。  
取消勾选 防跨站攻击。  
添加完成后编辑添加的站点 > URL rewrite 填入伪静态信息。
[code]
    location / {  
    try_files $uri /index.php$is_args$args;  
    }
[/code]

在SSH里的网站目录下执行，给网站文件755权限
[code]
    cd ../  
    chmod -R 755 你的文件夹名/  
    chown -R www:www 你的文件夹名/
[/code]

# 6.数据库操作

首次迁移: 导入网站目录下的`sql/metron.sql` 文件

# 7.修改根目录配置文件

编辑 config.php  
将你的数据库名字，用户名和密码填入.config.php里，类似下面这样
[code]
    $_ENV['baseUrl'] = 'https://www.xxxx.com'; //站点地址  
    $_ENV['db_database'] = 'sspanel'; //数据库名  
    $_ENV['db_username'] = 'sspanel'; //数据库用户名  
    $_ENV['db_password'] = 'sspanel_password'; //用户名对应的密码
[/code]

## 创建管理员账号以及其它初始化工作
[code]
    cd /www/wwwroot/域名/  
    php xcat User createAdmin  
    php xcat User resetTraffic  
    php xcat SyncRadius syncusers  
    php xcat Tool initQQWry  
    php xcat Tool initdownload
[/code]

# 8.使用宝塔面板的计划任务配置
[code]
    每日任务 (必须)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：每天 0 小时 0 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat Job DailyJob  
      
    检测任务 (必须)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat Job CheckJob  
      
    用户账户相关任务 (必须)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：每小时  
    脚本内容：php /www/wwwroot/你的网站目录/xcat Job UserJob  
      
    定时检测邮件队列 (必须)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat Job SendMail  
      
    每日流量报告 (给开启每日邮件的用户发送邮件)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：每天 0 小时 0 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat SendDiaryMail  
      
    审计封禁 (建议设置)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat DetectBan  
      
    检测被墙 (可选)  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat DetectGFW  
      
    Radius (可选)  
    synclogin  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat SyncRadius synclogin  
      
    syncvpn  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat SyncRadius syncvpn  
      
    syncnas  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：N分钟 1 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat SyncRadius syncnas  
    自动备份 (可选)  
      
    整体备份  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：自己设置, 可以设置每30分钟左右  
    脚本内容：php /www/wwwroot/你的网站目录/xcat Backup full  
      
    只备份核心数据  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：自己设置, 可以设置每30分钟左右  
    脚本内容：php /www/wwwroot/你的网站目录/xcat Backup simple  
    财务报表 (可选)  
      
    日报  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：每天 0 小时 0 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat FinanceMail day  
      
    周报  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：每星期 周日 0 小时 0 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat FinanceMail week  
      
    月报  
    任务类型：Shell 脚本  
    任务名称：自行填写  
    执行周期：每月 1 日 0 小时 0 分钟  
    脚本内容：php /www/wwwroot/你的网站目录/xcat FinanceMail month
[/code]
