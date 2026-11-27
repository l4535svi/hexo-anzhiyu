---
title: 7.5机场脚本升级codex优化
date: '2026-07-05 12:00:00'
cover: /img/covers/75codex.jpg
tags:
- 节点搭建
categories:
- 节点搭建
description: 安装命令用这个： REPO_URL=https://github.com/sosoveooo-bit/xboard-one-click.git BRANCH=codex/fix-xboard-update-env bash <(curl -fsSL https://raw.git
---
####  安装命令用这个：  
`REPO_URL=https://github.com/sosoveooo-bit/xboard-one-click.git BRANCH=codex/fix-xboard-update-env bash <(curl -fsSL https://raw.githubusercontent.com/sosoveooo-bit/xboard-one-click/codex/fix-xboard-update-env/bootstrap.sh)  
`安装完成后菜单命令：  
`xb  
`健康检查：  
`cd /root/xboard-one-click  
``./healthcheck.sh``  
`可以，下面是使用我现在改好的脚本部署 VPS 的教程。
[code]
    ## **一键安装命令  
    ** 在 VPS 用 root 登录后执行：  
    apt update -y  
    apt install -y curl git
    REPO_URL=https://github.com/sosoveooo-bit/xboard-one-click.git BRANCH=codex/fix-xboard-update-env bash <(curl -fsSL https://raw.githubusercontent.com/sosoveooo-bit/xboard-one-click/codex/fix-xboard-update-env/bootstrap.sh)  
    安装时会让你输入端口，建议这样填：  
    NPM HTTP 端口: 80  
    NPM HTTPS 端口: 443  
    NPM 管理后台端口: 35612  
    Xboard 对外端口: 35613  
    Xboard 管理员邮箱: admin@demo.com  
    如果 80/443 被占用，脚本会尽量自动处理。安装完成后执行：  
    xb  
    选择：  
    4. 查看访问信息  
    里面会显示：  
    Xboard 管理面板地址  
    Xboard 登录账号  
    Xboard 登录密码  
    NPM 管理后台地址  
    **服务器防火墙 / 安全组  
    ** 你的云服务器安全组必须放行这些端口：  
    80  
    443  
    35612  
    35613  
    如果你添加了额外 HTTPS 端口，比如 36333 -> 443，也要放行：  
    36333  
    **NPM 反代设置  
    ** 打开 NPM：  
    http://你的服务器IP:35612  
    进入 NPM 后新增 Proxy Host：  
    Domain Names: 你的域名  
    Scheme: http  
    Forward Hostname / IP: 服务器公网 IP  
    Forward Port: 35613  
    Websockets Support: 开启  
    Block Common Exploits: 开启  
    域名解析到 VPS 后，再在 NPM 里申请 Let's Encrypt SSL 证书。  
    **以后更新  
    ** 不要点 Xboard 面板里的系统更新。用脚本菜单：  
    xb  
    选择：  
    2. 安全更新 Xboard / NPM  
    这个会先备份，失败会自动回滚。  
    **常用命令  
    ** 查看信息：  
    xb  
    健康检查：  
    cd /root/xboard-one-click  
    bash healthcheck.sh  
    修复登录、数据库、配置：  
    cd /root/xboard-one-click  
    bash repair.sh  
    备份迁移包：  
    cd /root/xboard-one-click  
    bash backup.sh
[/code]
