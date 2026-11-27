---
title: 2024最新的一键脚本搭建frp内网穿透，在外轻松远程访问内网设备|远程桌面！非常简单的配置流程，搭配openwrt软路由来使用，非常好用！windows配置#一瓶奶油
date: '2025-03-30 12:00:00'
cover: /img/covers/2024frpopenwrtwindows.jpg
tags:
- 建站
categories:
- 建站
description: 1、OpenWrt软路由固件：【 点击进入 】 更多固件可参考此文章：【 点击进入 】 SSH连接工具Finalshell：【 点击进入 】 2、FRP开源项目地址：【 点击进入 】 3、FRP一键脚本地址：【 点击进入 】 一键安装脚本 解释 wget https://gite
---
1、OpenWrt软路由固件：【[点击进入](https://github.com/sirpdboy/openwrt#%E5%9B%BA%E4%BB%B6%E4%B8%8B%E8%BD%BD)】

  * 更多固件可参考此文章：【[点击进入](https://naiyous.com/2336.html)】

  * SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

2、FRP开源项目地址：【[点击进入](https://github.com/fatedier/frp)】

3、FRP一键脚本地址：【[点击进入](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file)】

  * 一键安装脚本

[code]
    解释
    
    wget https://gitee.com/mvscode/frps-onekey/raw/master/install-frps.sh -O ./install-frps.sh
    chmod 700 ./install-frps.sh
    ./install-frps.sh installCopy
[/code]

  * 设置后台运行

[code]
    解释
    
    nohup ./frps -c frps.ini >/dev/null 2>&1 &Copy
[/code]

  * 防火墙相关（国内服务器可以直接设置防火墙规则）

[code]
    解释
    
    Debian或Ubuntu系统放行端口：
    ufw allow 端口号
    iptables -A INPUT -p tcp --dport 端口号 -j ACCEPT
    
    CentOS系统放行端口：
    firewall-cmd --zone=public --add-port=端口号/tcp --permanentCopy
[/code]

  * FRP常用命令

[code]
    解释
    
    开启FRP：frps start
    
    停止FRP：frps stop
    
    重启FRP：frps restart
    
    打开配置文件：frps config
    
    查看FRP版本：frps version
    
    检查FRP运行状态：frps statusCopy
[/code]

4、openwrt设置

  * 安装frpc
    * frpc下载：【[点击进入](https://github.com/kuoruan/openwrt-frp/releases)】
    * luci-app-frpc和汉化包下载：【[点击进入](https://github.com/kuoruan/luci-app-frpc/releases)】
    * 查看CPU架构

[code]
    解释
    
    cat /etc/os-release |grep ARCHCopy
[/code]

  * 设置

![](https://naiyous.com/wp-content/uploads/2024/03/image-1024x532.png)![](https://naiyous.com/wp-content/uploads/2024/03/image-1-1024x565.png)  

 _Frp 是一个高性能的反向代理应用，可以帮助您轻松地进行内网穿透，对外网提供服务，支持 tcp, http, https 等协议类型，并且 web 服务支持根据域名进行路由转发。_

  * Detail(详情)：fatedier[![github](https://camo.githubusercontent.com/80f282072e3d7cc023bc81b19e36d8ee01ed44b31f2d72d15630d01a0c383ea1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622f66617465646965722f6672702d3864613063623f7374796c653d666f722d7468652d6261646765266c6162656c436f6c6f723d353535353535266c6f676f3d676974687562)](https://github.com/fatedier/frp)
  * Script author（脚本原作者）：clangcn [![github](https://camo.githubusercontent.com/2433ba0fc35f65cb69a753b16251c39d4f499c50fd63064187aee65a6b818675/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622f636c616e67636e2f6f6e656b65795f696e7374616c6c5f7368656c6c2d3864613063623f7374796c653d666f722d7468652d6261646765266c6162656c436f6c6f723d353535353535266c6f676f3d676974687562)](https://github.com/clangcn/onekey-install-shell)

## Frps-Onekey-Install-Shell For CentOS/Debian/Ubuntu/Fedora (32bit/64bit)

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#frps-onekey-install-shell-for-centosdebianubuntufedora-32bit64bit)

### Install（安装）

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#install%E5%AE%89%E8%A3%85)

#### Gitee

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#gitee)

解释
[code]
    wget https://gitee.com/mvscode/frps-onekey/raw/master/install-frps.sh -O ./install-frps.sh
    chmod 700 ./install-frps.sh
    ./install-frps.sh install
[/code]

#### Github

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#github)

解释
[code]
    wget https://raw.githubusercontent.com/mvscode/frps-onekey/master/install-frps.sh -O ./install-frps.sh
    chmod 700 ./install-frps.sh
    ./install-frps.sh install
[/code]

### Uninstall（卸载）

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#uninstall%E5%8D%B8%E8%BD%BD)

解释
[code]
    ./install-frps.sh uninstall
[/code]

### Update（更新）

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#update%E6%9B%B4%E6%96%B0)

解释
[code]
    ./install-frps.sh update
[/code]

### Server management（服务管理器）

[](https://github.com/MvsCode/frps-onekey?tab=readme-ov-file#server-management%E6%9C%8D%E5%8A%A1%E7%AE%A1%E7%90%86%E5%99%A8)

解释
[code]
    Usage: /etc/init.d/frps {start|stop|restart|status|config|version}
[/code]
