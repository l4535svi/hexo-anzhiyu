---
title: OpenClaw 官方已经内置了备份命令
date: '2026-03-15 12:00:00'
cover: /img/covers/openclaw-15-2.jpg
tags:
- OpenClaw
categories:
- OpenClaw
description: 一、最简单的本地备份（推荐） 直接在终端运行： openclaw backup create --output ~/Backups/ 作用： 自动打包 OpenClaw 重要数据 生成一个备份压缩包 保存到 ~/Backups/ 目录 备份内容包括： openclaw.json
---
# 一、最简单的本地备份（推荐）

直接在终端运行：

```
 
    openclaw backup create --output ~/Backups/

```

作用：

  * 自动打包 OpenClaw 重要数据

  * 生成一个备份压缩包

  * 保存到 `~/Backups/` 目录

备份内容包括：

  * `openclaw.json`（核心配置）

  * `workspace/`（SOUL / MEMORY / AGENTS.md）

  * `agents/`（Agent配置 + session）

  * `cron/`（定时任务配置）

**不会备份：**

  * logs

  * 缓存

  * 临时文件

所以备份包通常比较小。

* * *

# 二、恢复备份

如果换电脑或重装系统：

```
 
    openclaw backup restore <backup-file>

```

例如：

```
 
    openclaw backup restore ~/Backups/openclaw-2026-03-08.tar.gz

```

恢复后：

  * agent 会回来

  * memory 会回来

  * 对话历史会恢复

  * workspace 会恢复

几分钟就能恢复环境。

* * *

# 三、自动每天备份（强烈建议）

可以加一个 cron 任务：

```
 
    crontab -e

```

添加：

```
 
    0 2 * * * openclaw backup create --output ~/Backups/

```

含义：

每天凌晨 **2 点自动备份**

* * *

# 四、云端备份（更安全）

官方建议：

1️⃣ 创建 **GitHub 私有仓库**

2️⃣ 定期 push

例如脚本：

```
 
    cd ~/Backups  
    git add .  
    git commit -m "backup"  
    git push

```

再配合 cron 自动执行。

* * *

# 五、最推荐的备份方案（我自己建议）

组合：

```
 
    OpenClaw  
       ↓  
    每日本地备份  
       ↓  
    Backups目录  
       ↓  
    GitHub私有仓库

```

优点：

  * 本地恢复快

  * 云端防丢

  * 自动化

* * *

# 六、检查备份是否成功

备份后看目录：

```
 
    ls ~/Backups

```

会看到类似：

```
 
    openclaw-backup-2026-03-08.tar.gz

```

