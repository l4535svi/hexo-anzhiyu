---
title: xboard机场搭建教程
date: '2025-07-01 12:00:00'
cover: /img/covers/xboard.jpg
tags:
- 建站
categories:
- 建站
description: 准备工作 下载并安装SSH连接工具Finalshell：【 点击进入 】 做好域名解析Cloudflare：【 点击进入 】 1、关闭防火墙 sudo ufw disable Copy 2、一键安装NPM反向代理面板 sudo apt install git -y && git
---
准备工作

  * 下载并安装SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

  * 做好域名解析Cloudflare：【[点击进入](https://dash.cloudflare.com/login)】

1、关闭防火墙

```

    sudo ufw disableCopy

```

2、一键安装NPM反向代理面板

```

    sudo apt install git -y && git clone https://github.com/slobys/npm.git && cd npm && chmod +x npm.sh && ./npm.shCopy

```

3、安装XBoard机场面板：【[点击进入](https://github.com/cedar2025/Xboard)】

```

    git clone -b compose --depth 1 https://github.com/cedar2025/Xboard && \
    cd Xboard && \
    docker compose run -it --rm \
        -e ENABLE_SQLITE=true \
        -e ENABLE_REDIS=true \
        -e ADMIN_ACCOUNT=admin@demo.com \
        web php artisan xboard:install && \
    docker compose up -dCopy

```

4、更新镜像

```

    docker compose build
    docker compose up -dCopy

```

5、进阶玩法（修改UUID）

  * 查看容器名字

```

    docker psCopy

```

  * 进入容器

```

    docker exec -it <你的容器名> shCopy

```

  * 进入项目目录

```

    cd /wwwCopy

```

  * 进入 SQLite 数据库

```

    sqlite3 .docker/.data/database.sqliteCopy

```

  * 查看当前用户 UUID

```

    SELECT id, email, uuid FROM v2_user;Copy

```

  * 修改 UUID 为你希望的新密码（如 `my-new-password-123`）

```

    UPDATE v2_user SET uuid = 'my-new-password-123' WHERE id = 1;Copy

```

  * 退出 SQLite

```

    .quitCopy

```

  * 退出容器

```

    exitCopy

```

  * 重启 XBoard

```

    docker compose restartCopy

```

  * 一键脚本（红色部分替换成自己想要的UUID）

```

    docker exec -i xboard-web-1 sh -c "cd /www && sqlite3 .docker/.data/database.sqlite \"UPDATE v2_user SET uuid = '$(uuidgen)' WHERE id = 1;\""

```

