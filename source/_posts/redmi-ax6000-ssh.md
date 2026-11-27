---
title: Redmi AX6000 解锁SSH 和 科学上网教程
date: '2024-10-03 12:00:00'
cover: /img/covers/redmi-ax6000-ssh.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 二、红米AX6000科学上网教程： 视频教程：▶ https://youtu.be/zMQfO3AezgM Clash安装源： export url=' https://fastly.jsdelivr.net/gh/juewuy/ShellCrash@master ' && sh
---
二、红米AX6000科学上网教程：

[视频教程：▶ ](https://youtu.be/zMQfO3AezgM)<https://youtu.be/zMQfO3AezgM>

Clash安装源：  
export url='<https://fastly.jsdelivr.net/gh/juewuy/ShellCrash@master>' && sh -c "$(curl -kfsSl $url/install.sh)" && source /etc/profile &> /dev/null

备用安装源：  
#1  
export url='<https://raw.githubusercontent.com/juewuy/ShellClash/master>' && sh -c "$(curl -kfsSl $url/install.sh)" && source /etc/profile &> /dev/null

#2  
export url='<https://fastly.jsdelivr.net/gh/juewuy/ShellClash@master>' && sh -c "$(curl -kfsSl $url/install.sh)" && source /etc/profile &> /dev/null

[#3](https://github.com/kjfx/AX6000/issues/3)  
export url='<https://gh.jwsc.eu.org/master>' && sh -c "$(curl -kfsSl $url/install.sh)" && source /etc/profile &> /dev/null

[#4](https://github.com/kjfx/AX6000/issues/4)  
export url='<https://raw.githubusercontent.com/juewuy/ShellClash/master>' && wget -q --no-check-certificate -O /tmp/install.sh $url/install.sh && sh /tmp/install.sh && source /etc/profile &> /dev/null

[#5](https://github.com/kjfx/AX6000/issues/5)  
export url='<https://fastly.jsdelivr.net/gh/juewuy/ShellClash@master>' && wget -q --no-check-certificate -O /tmp/install.sh $url/install.sh && sh /tmp/install.sh && source /etc/profile &> /dev/null

[#6](https://github.com/kjfx/AX6000/issues/6)  
export url='[http://t.jwsc.eu.org](http://t.jwsc.eu.org/)' && wget -q -O /tmp/install.sh $url/install.sh && sh /tmp/install.sh && source /etc/profile &> /dev/null

* * *

Clash管理地址：<http://192.168.31.1:9999/ui/> (如果打不开请按Ctrl+F5 刷新)

Clash核心和dashboard管理面板下载失败解决方法：[点击下载>>](https://github.com/kjfx/AX6000/releases/download/redmi_ax6000_ssh/dashboard.zip)

✈我使用的机场：[](http://www.txyun.xyz/)<http://www.txyun.xyz/>
