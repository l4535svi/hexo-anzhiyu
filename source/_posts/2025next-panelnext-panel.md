---
title: 2025年最新NeXT Panel面板搭建机场教程，超详细！从零开始搭机场|机场搭建优化方案，一个视频看完机场搭建过程，NeXT Panel面板功能更加完善，设置、节点对接更加简单#一瓶奶油
date: '2025-02-21 12:00:00'
cover: /img/covers/2025next-panelnext-panel.jpg
tags:
- 科学上网
categories:
- 科学上网
description: 准备工作： 一台服务器（本教程使用的环境：Ubuntu 24.04/x86_64） 提前解析好域名Cloudflare：【 点击进入 】 安装SSH连接工具Finalshell：【 点击进入 】 1、开源项目：【 点击进入 】 安装文档：【 点击进入 】 2、申请SSL证书（ 注
---
![](https://naiyous.com/wp-content/uploads/2025/02/%E6%90%AD%E5%BB%BANeXT-Panel%E6%9C%BA%E5%9C%BA%E9%9D%A2%E6%9D%BF-1024x576.jpg)

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fnaiyous.com%2F7154.html) [](http://twitter.com/share?url=https%3A%2F%2Fnaiyous.com%2F7154.html&text=2025%E5%B9%B4%E6%9C%80%E6%96%B0NeXT%20Panel%E9%9D%A2%E6%9D%BF%E6%90%AD%E5%BB%BA%E6%9C%BA%E5%9C%BA%E6%95%99%E7%A8%8B%EF%BC%8C%E8%B6%85%E8%AF%A6%E7%BB%86%EF%BC%81%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E6%90%AD%E6%9C%BA%E5%9C%BA%7C%E6%9C%BA%E5%9C%BA%E6%90%AD%E5%BB%BA%E4%BC%98%E5%8C%96%E6%96%B9%E6%A1%88%EF%BC%8C%E4%B8%80%E4%B8%AA%E8%A7%86%E9%A2%91%E7%9C%8B%E5%AE%8C%E6%9C%BA%E5%9C%BA%E6%90%AD%E5%BB%BA%E8%BF%87%E7%A8%8B%EF%BC%8CNeXT%20Panel%E9%9D%A2%E6%9D%BF%E5%8A%9F%E8%83%BD%E6%9B%B4%E5%8A%A0%E5%AE%8C%E5%96%84%EF%BC%8C%E8%AE%BE%E7%BD%AE%E3%80%81%E8%8A%82%E7%82%B9%E5%AF%B9%E6%8E%A5%E6%9B%B4%E5%8A%A0%E7%AE%80%E5%8D%95%23%E4%B8%80%E7%93%B6%E5%A5%B6%E6%B2%B9&hashtags=vultr%E4%BA%91,%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91) [](https://pinterest.com/pin/create/bookmarklet/?media=https://naiyous.com/wp-content/uploads/2025/02/%E6%90%AD%E5%BB%BANeXT-Panel%E6%9C%BA%E5%9C%BA%E9%9D%A2%E6%9D%BF.jpg&url=https%3A%2F%2Fnaiyous.com%2F7154.html&description=2025%E5%B9%B4%E6%9C%80%E6%96%B0NeXT%20Panel%E9%9D%A2%E6%9D%BF%E6%90%AD%E5%BB%BA%E6%9C%BA%E5%9C%BA%E6%95%99%E7%A8%8B%EF%BC%8C%E8%B6%85%E8%AF%A6%E7%BB%86%EF%BC%81%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E6%90%AD%E6%9C%BA%E5%9C%BA|%E6%9C%BA%E5%9C%BA%E6%90%AD%E5%BB%BA%E4%BC%98%E5%8C%96%E6%96%B9%E6%A1%88%EF%BC%8C%E4%B8%80%E4%B8%AA%E8%A7%86%E9%A2%91%E7%9C%8B%E5%AE%8C%E6%9C%BA%E5%9C%BA%E6%90%AD%E5%BB%BA%E8%BF%87%E7%A8%8B%EF%BC%8CNeXT%20Panel%E9%9D%A2%E6%9D%BF%E5%8A%9F%E8%83%BD%E6%9B%B4%E5%8A%A0%E5%AE%8C%E5%96%84%EF%BC%8C%E8%AE%BE%E7%BD%AE%E3%80%81%E8%8A%82%E7%82%B9%E5%AF%B9%E6%8E%A5%E6%9B%B4%E5%8A%A0%E7%AE%80%E5%8D%95#%E4%B8%80%E7%93%B6%E5%A5%B6%E6%B2%B9) [](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fnaiyous.com%2F7154.html&title=2025%E5%B9%B4%E6%9C%80%E6%96%B0NeXT+Panel%E9%9D%A2%E6%9D%BF%E6%90%AD%E5%BB%BA%E6%9C%BA%E5%9C%BA%E6%95%99%E7%A8%8B%EF%BC%8C%E8%B6%85%E8%AF%A6%E7%BB%86%EF%BC%81%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E6%90%AD%E6%9C%BA%E5%9C%BA%7C%E6%9C%BA%E5%9C%BA%E6%90%AD%E5%BB%BA%E4%BC%98%E5%8C%96%E6%96%B9%E6%A1%88%EF%BC%8C%E4%B8%80%E4%B8%AA%E8%A7%86%E9%A2%91%E7%9C%8B%E5%AE%8C%E6%9C%BA%E5%9C%BA%E6%90%AD%E5%BB%BA%E8%BF%87%E7%A8%8B%EF%BC%8CNeXT+Panel%E9%9D%A2%E6%9D%BF%E5%8A%9F%E8%83%BD%E6%9B%B4%E5%8A%A0%E5%AE%8C%E5%96%84%EF%BC%8C%E8%AE%BE%E7%BD%AE%E3%80%81%E8%8A%82%E7%82%B9%E5%AF%B9%E6%8E%A5%E6%9B%B4%E5%8A%A0%E7%AE%80%E5%8D%95%23%E4%B8%80%E7%93%B6%E5%A5%B6%E6%B2%B9&source=%E5%A5%B6%E6%B2%B9%E4%B9%8B%E5%AE%B6)

准备工作：

  * 一台服务器（本教程使用的环境：Ubuntu 24.04/x86_64）

  * 提前解析好域名Cloudflare：【[点击进入](https://dash.cloudflare.com/)】

  * 安装SSH连接工具Finalshell：【[点击进入](https://www.hostbuf.com/t/988.html)】

1、开源项目：【[点击进入](https://github.com/The-NeXT-Project/NeXT-Panel)】

  * 安装文档：【[点击进入](https://nextpanel.dev/docs/installation/ubuntu)】

2、申请SSL证书（注意：脚本自带关闭防火墙功能，适合Vultr使用，其他平台可在控制台中添加规则放行所有端口）

  * 一键申请SSL证书脚本

[code]
    解释
    
    sudo apt install git -y  &&  git clone https://github.com/slobys/SSL-Renewal.git /tmp/acme && mv /tmp/acme/* /root && bash acme_2.0.shCopy
[/code]

3、安装 Nginx

  * 安装必要的软件

[code]
    解释
    
    apt install -y curl gnupg2 ca-certificates lsb-release ubuntu-keyringCopy
[/code]

  * 添加官方 Nginx PGP 密钥

[code]
    解释
    
    curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/nullCopy
[/code]

  * 将官方Nginx源配置写入nginx.list

[code]
    解释
    
    echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" | sudo tee /etc/apt/sources.list.d/nginx.listCopy
[/code]

  * 将官方 Nginx 源设置为比系统内置源具有更高的优先级

[code]
    解释
    
    echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" | sudo tee /etc/apt/preferences.d/99nginxCopy
[/code]

  * 更新 APT 缓存

[code]
    解释
    
    apt updateCopy
[/code]

  * 安装 Nginx

[code]
    解释
    
    apt install nginxCopy
[/code]

  * 启动Nginx服务并将其设置为开机启动。

[code]
    解释
    
    systemctl start nginx
    systemctl enable nginxCopy
[/code]

4、安装 PHP

  * 使用来自 deb.sury.org 的 PPA 源安装 PHP

[code]
    解释
    
    add-apt-repository ppa:ondrej/phpCopy
[/code]

  * 更新APT缓存

[code]
    解释
    
    apt updateCopy
[/code]

  * 安装所需的PHP模块

[code]
    解释
    
    apt install -y php8.4-{bcmath,bz2,cli,common,curl,fpm,gd,igbinary,mbstring,mysql,opcache,readline,redis,xml,yaml,zip}Copy
[/code]

  * 启动php-fpm服务并设置为开机启动

[code]
    解释
    
    systemctl start php8.4-fpm
    systemctl enable php8.4-fpmCopy
[/code]

5、安装 MariaDB

  * 安装必要的软件包并导入 GPG 密钥

[code]
    解释
    
    apt install -y apt-transport-https curl && mkdir -p /etc/apt/keyrings && curl -o /etc/apt/keyrings/mariadb-keyring.pgp 'https://mariadb.org/mariadb_release_signing_key.pgp'Copy
[/code]

  * 进入/etc/apt/sources.list.d，创建mariadb.sources文件并写入以下配置

[code]
    解释
    
    X-Repolib-Name: MariaDB
    Types: deb
    URIs: https://deb.mariadb.org/11.4/ubuntu
    Suites: noble
    Components: main main/debug
    Signed-By: /etc/apt/keyrings/mariadb-keyring.pgpCopy
[/code]

  * 更新 APT 缓存

[code]
    解释
    
    apt updateCopy
[/code]

  * 安装 MariaDB 11.4

[code]
    解释
    
    apt install -y mariadb-serverCopy
[/code]

  * 启动MariaDB服务并将其设置为开机启动

[code]
    解释
    
    systemctl start mariadb
    systemctl enable mariadbCopy
[/code]

  * 运行 MariaDB 的初始设置（重要）

[code]
    解释
    
    mariadb-secure-installationCopy
[/code]

6、安装 Redis

  * 导入 GPG 密钥

[code]
    解释
    
    curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpgCopy
[/code]

  * 将Redis官方源配置写入redis.list

[code]
    解释
    
    echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.listCopy
[/code]

  * 更新 APT 缓存

[code]
    解释
    
    apt updateCopy
[/code]

  * 安装 redis-server

[code]
    解释
    
    apt install -y redisCopy
[/code]

  * 启动 redis-server 服务并将其设置为开机启动

[code]
    解释
    
    systemctl start redis-server
    systemctl enable redis-serverCopy
[/code]

7、部署NeXT Panel

  * 打开`/etc/nginx/nginx.conf`​文件，把` _user nginx;_`改成 _`user www-data;`_

  * 进入/etc/nginx/conf.d目录，然后创建website-domain-you-set.conf文件

  * 把以下代码添加进去（红色部分根据自己实际情况填写）

[code]
    解释
    
    # 监听 80 端口，并重定向到 HTTPS
    server {
        listen 80;
        listen [::]:80;
        server_name 你的域名; 
    
        # 301 永久重定向到 HTTPS
        return 301 https://$host$request_uri;
    }
    
    # HTTPS 服务器配置
    server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        server_name 你的域名; 
    
        root /var/www/nextpanel/public; # 你的网站路径
        index index.php;
    
        ssl_certificate /etc/letsencrypt/live/aa.naiyou168.xyz/fullchain.pem;  # 证书路径
        ssl_certificate_key /etc/letsencrypt/live/aa.naiyou168.xyz/privkey.pem;  # 私钥路径
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        
        # 主要的 location 配置
        location / {
            try_files $uri /index.php$is_args$args;
        }
    
        # 处理 PHP 请求
        location ~ \.php$ {
            try_files $fastcgi_script_name =404;
            include fastcgi_params;
            fastcgi_index index.php;
            fastcgi_buffers 8 16k;
            fastcgi_buffer_size 32k;
            fastcgi_pass unix:/run/php/php-fpm.sock;
            fastcgi_param DOCUMENT_ROOT $realpath_root;
            fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        }
    }Copy
[/code]

  * 重启Nginx

[code]
    解释
    
    systemctl restart nginxCopy
[/code]

  * 创建 `/var/www` 目录并进入

[code]
    解释
    
    mkdir -p /var/www
    cd /var/wwwCopy
[/code]

  * 下载 NeXT-Panel（红色部分根据实际情况替换成最新版本）

[code]
    解释
    
    wget https://github.com/SSPanel-NeXT/NeXT-Panel/releases/download/24.5.1/NeXT-Panel-24.5.1.zipCopy
[/code]

  * 解压并移除文件

[code]
    解释
    
    unzip NeXT-Panel-24.5.1.zip -d /var/www/nextpanel ; rm -f NeXT-Panel-24.5.1.zipCopy
[/code]

  * 设置网站目录的整体权限

[code]
    解释
    
    chmod -R 755 *
    chown -R www-data:www-data *Copy
[/code]

  * 登录 MariaDB 服务器，开始创建数据库

[code]
    解释
    
    mariadb -u root -pCopy
[/code]

  * 输入刚创建的密码，使用编码`utf8mb4_unicode_ci`和创建一个数据库，以 sspanel 为例

[code]
    解释
    
    CREATE DATABASE sspanel CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;Copy
[/code]

  * 创建一个本地数据库用户，并将用户的权限限制到新创建的数据库，使用 sspanel 作为用户名，使用 sspanel-password 作为用户密码（输入exit即可退出）

[code]
    解释
    
    CREATE USER 'sspanel'@'localhost';
    GRANT ALL PRIVILEGES ON sspanel.* TO 'sspanel'@'localhost' IDENTIFIED BY 'sspanel-password';
    FLUSH PRIVILEGES;Copy
[/code]

  * 进入网站根目录

[code]
    解释
    
    cd /var/www/nextpanelCopy
[/code]

  * 复制示例配置文件，并创建实际的配置文件

[code]
    解释
    
    cp config/.config.example.php config/.config.php
    cp config/appprofile.example.php config/appprofile.phpCopy
[/code]

  * 进入/var/www/nextpanel/config，打开.config.php，然后输入前面设置好的数据库账号、密码

  * 执行以下站点初始化设置

[code]
    解释
    
    php xcat Migration newCopy
[/code]
[code]
    解释
    
    php xcat Tool importSettingCopy
[/code]
[code]
    解释
    
    php xcat Tool createAdminCopy
[/code]
[code]
    解释
    
    sudo -u www-data /usr/bin/php xcat ClientDownloadCopy
[/code]

  * 设置定时任务，输入crontab -e，然后选择1，在最后面添加一下代码（输入完成后按Ctrl+X退出，然后输入y，回车）

[code]
    解释
    
    */5 * * * * /usr/bin/php /path/to/your/site/xcat CronCopy
[/code]

8、提高系统安全性和性能

  * 禁用一些危险的 PHP 函数

[code]
    解释
    
    sed -i 's@^disable_functions.*@disable_functions = passthru,exec,system,chroot,chgrp,chown,shell_exec,proc_open,proc_get_status,ini_alter,ini_restore,dl,readlink,symlink,popepassthru,stream_socket_server,fsocket,popen@' /etc/php/8.4/fpm/php.ini
    sed -i 's@^disable_functions.*@disable_functions = passthru,exec,system,chroot,chgrp,chown,shell_exec,proc_open,proc_get_status,ini_alter,ini_restore,dl,readlink,symlink,popepassthru,stream_socket_server,fsocket,popen@' /etc/php/8.4/cli/php.iniCopy
[/code]

  * 修改后需要重启PHP-FPM服务

[code]
    解释
    
    systemctl restart php8.4-fpmCopy
[/code]

  * 进入/etc/php/8.4/fpm/conf.d，打开10-opcache.ini，然后添加一下代码

[code]
    解释
    
    zend_extension=opcache.so
    opcache.file_cache=/tmp
    opcache.interned_strings_buffer=64
    opcache.jit=on
    opcache.jit_buffer_size=256M
    opcache.max_accelerated_files=65535
    opcache.memory_consumption=512
    opcache.revalidate_freq=60
    opcache.validate_permission=on
    opcache.validate_root=onCopy
[/code]

  * 修改完之后还需要重启PHP-FPM服务

[code]
    解释
    
    systemctl restart php8.4-fpm
[/code]
