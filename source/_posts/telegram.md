---
title: Telegram超智能群组机器人  免费开源、一键部署
date: '2026-10-26 12:00:00'
cover: /img/covers/telegram.jpg
tags:
- TG
categories:
- TG
description: 一．准备工作 确保网络可以魔法上网 服务器配置：推荐普通版 1 vCPU、512 MB 可用内存、1 GB 可用硬盘 ；OCR 版建议 2 vCPU、2 GB 内存 ，构建镜像还需额外临时空间。 下载并安装SSH连接工具Finalshell：【 点击进入 】 二．创建服务器并更改
---
# 一．准备工作

确保网络可以魔法上网

服务器配置：推荐普通版 1 vCPU、512 MB 可用内存、1 GB 可用硬盘；OCR 版建议 2 vCPU、2 GB 内存，构建镜像还需额外临时空间。

下载并安装SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

# 二．创建服务器并更改root密码

一键更改root密码（此命令只针对谷歌云服务器，其他服务器根据实际情况调整）

  * 注意：红色部分为密码，可以自定义

```

    echo root:ZKrjSvGT9n5jXAfa |sudo chpasswd root
    sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config
    sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config
    sudo reboot

```

Copy

# 三．创建群组机器人

1．在 Telegram 打开 [@BotFather](https://t.me/BotFather)，发送 `/newbot`，按提示设置名称和用户名。

2．保存 BotFather 提供的 Token，安装时输入。

3．把机器人加入测试群，删除消息和限制成员权限。

4．私聊机器人发送`/start`，选择群组，通过按钮设置；群内`/check`可检查权限，`/panel`可打开管理入口

# 四．GroupGuard开源项目：【[点击进入](https://github.com/slobys/telegram-group-manager)】

[在线使用文档](https://slobys.github.io/telegram-group-manager/)

一键部署

```

    bash -o pipefail -c 'curl -fsSL https://raw.githubusercontent.com/slobys/telegram-group-manager/main/install.sh | bash'

```

Copy

打开菜单与更新

```

    gg

```

Copy

  * 更新快捷命令（常用）

```

    gg update

```

Copy

  * 安装OCR

```

    gg ocr

```

