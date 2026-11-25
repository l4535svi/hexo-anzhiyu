---
title: windows-fuse-winfsp-rclone-winfsp
date: '2025-11-21 12:00:00'
tags:
- Azure薅羊毛
categories:
- Azure薅羊毛
description: 'rclone 想在 Windows 上用 FUSE 方式挂载盘符，但系统里 找不到 WinFsp 驱动 ，所以挂载失败。 下载rclone安装，然后下载下面的程序 ✅ 二、缓存在哪里？ 用 最小命令挂载（不要加其它参数）※： .\rclone.exe mount one: X:'
---
rclone 想在 Windows 上用 FUSE 方式挂载盘符，但系统里 **找不到 WinFsp 驱动** ，所以挂载失败。

下载rclone安装，然后下载下面的程序

# ✅ 二、缓存在哪里？

用 最小命令挂载（不要加其它参数）※： .\rclone.exe mount one: X: -vv --log-file=mount.log

  

通常在：
[code]
    C:\Users\你的用户名\AppData\Local\rclone\
    
[/code]

里面有：
[code]
    vfs\
    vfsMeta\
    one\
    
[/code]

甚至多几个随机名文件夹。

### 你现在需要做的事

  1. **安装 / 重新安装 WinFsp**

     1. 打开浏览器，搜索 `WinFsp github`，进到官方页面下载最新版安装包（`.msi`）。

     2. 双击安装，**全程用默认选项** ，不用改。

     3. 装完最好重启一下电脑。

  2. **管理员权限重新挂载**

     * 用“以管理员身份运行”打开 PowerShell 或 CMD。

     * 进到 rclone 目录，例如：
[code] cd D:\rclone-v1.71.2-windows-amd64\
           
[/code]

     * 执行挂载命令（你的是 remote 叫 `one`，盘符可以换成 R: / X:）：
[code] .\rclone.exe mount one: R: --vfs-cache-mode full --fuse-flag sync_read
           
[/code]

> 如果之前加了 `--network-mode` 也行，但先用上面这个简单版本测试。

  3. **如果提示“已经在运行 / 端口占用”**

     * 先关掉所有旧的 rclone 窗口，或者执行：
[code] taskkill /f /im rclone.exe
           
[/code]

     * 再重新跑上面的挂载命令。

  4. **挂载成功后**

     * PowerShell 窗口会一直“挂着”不退出，这是正常的。

     * 在“此电脑”里就能看到新盘符（比如 R: 或 X:），直接当本地盘用。

# ✅ **从零开始配置 OneDrive Business（完整命令流程）**

## **步骤 1：进入 rclone 文件夹**
[code] 
    cd D:\huansuan\rclone-v1.71.2-windows-amd64\
    
[/code]

## **步骤 2：开始配置**
[code] 
    .\rclone.exe config
    
[/code]

出现提示后：
[code] 
    n/s/q>
    
[/code]

输入：
[code] 
    n
    
[/code]

新建一个 remote

* * *

# 🔵 **配置步骤（每一步填写什么我全部写好）**

下面是全部正确选项，你逐项照着输入：

* * *

## **① remote name（名字随便，建议）**

输入：
[code] 
    one
    
[/code]

* * *

## **② 选择 storage 类型**

出现大列表时，输入：
[code] 
    38
    
[/code]

也就是：
[code] 
    Microsoft OneDrive (onedrive)
    
[/code]

* * *

## **③ client_id**

直接回车（留空）
[code] 
    client_id>
    
[/code]

* * *

## **④ client_secret**

直接回车（留空）
[code] 
    client_secret>
    
[/code]

* * *

## **⑤ region（区域）**

出现：
[code] 
    1) global
    2) us
    3) de
    4) cn
    
[/code]

你使用的是 **国际 OneDrive 5T / E5**  
输入：
[code] 
    1
    
[/code]

* * *

## **⑥ tenant（组织租户）**

这里 **必须空着**  
直接回车：
[code] 
    tenant>
    
[/code]

* * *

## **⑦ advanced config**
[code] 
    y/n>
    
[/code]

输入：
[code] 
    n
    
[/code]

* * *

## **⑧ 使用浏览器授权**
[code] 
    y/n>
    
[/code]

输入：
[code] 
    y
    
[/code]

浏览器会跳出微软登录窗口 → 登录你的 OneDrive（必须是 Business/E5 账号）

登录成功后网页会显示：
[code] 
    Success! All done.
    
[/code]

PowerShell 会显示获得 token。

* * *

## **⑨ Type of connection（非常关键）**

出现：
[code] 
    1) OneDrive Personal or Business
    2) Root Sharepoint site
    3) Sharepoint site URL
    4) Search Sharepoint site
    5) driveID
    6) siteID
    7) path
    
[/code]

你必须输入：
[code] 
    1
    
[/code]

这是正常 OneDrive 而不是 SharePoint。

* * *

## **⑩ 选择 drive**

如果你的账号是 5T，会显示一条：
[code] 
    1) OneDrive (business)
    
[/code]

输入：
[code] 
    1
    
[/code]

* * *

## **⑪ Drive OK？**
[code] 
    y/n>
    
[/code]

输入：
[code] 
    y
    
[/code]

* * *

## **⑫ 保存并退出**
[code] 
    e/n/d/r/c/s/q>
    
[/code]

输入：
[code] 
    q
    
[/code]

* * *

# 🎉 **配置完成！**

现在你可以挂载：
[code] 
    .\rclone.exe mount one: X: --vfs-cache-mode full --fuse-flag sync_read
[/code]

## 一、这个报错到底是什么

日志里关键一句是：

> Failed to cancel multipart upload: Delete "https://…uploadSession…": **context canceled**

意思是：

  * 之前有一个**分片上传的任务** （那个 Flutter 的 svg 文件），OneDrive 这边还保留着一个 uploadSession。

  * rclone 在挂载时顺便想把这个“残留的上传会话”清掉，结果请求被中止（context canceled），所以报了一句错。

  * 这不是账号被封、空间不够之类的问题，就是**一次旧的上传记录清理失败** 。

但是注意：  
这条错误出来之后，rclone 直接退出回到了 `PS D:\...>` 提示符，也就是说：

> **挂载没有成功，rclone 进程已经结束了，所以磁盘不会出现。**

* * *

## 二、先清理一下再挂载

建议你按下面顺序做一遍，把之前残留的上传记录和缓存都清掉。

### 1\. 确认没有 rclone 正在后台跑

在 PowerShell 里执行（管理员权限更好）：
[code] 
    taskkill /f /im rclone.exe
    
[/code]

如果提示“没有找到进程 rclone.exe”就无所谓，说明已经没有了。

* * *

### 2\. 清理 rclone 本地缓存

在资源管理器打开：
[code] 
    C:\Users\你的Windows用户名\AppData\Local\rclone\
    
[/code]

把里面的 `vfs`、`vfsMeta` 之类的缓存文件夹全部删掉（删不掉的先跳过，重启后再试也行）。

* * *

### 3\. 让 OneDrive 服务器端也清理残留上传

在 rclone 目录里（有 rclone.exe 的那个文件夹）打开 PowerShell，执行：
[code] 
    .\rclone.exe cleanup one:
    
[/code]

这个命令就是专门用来告诉 OneDrive：  
“把这个网盘里没用的 uploadSession / 未完成上传 清理掉”。

执行完如果没有特别红色大错误就行。

* * *

## 三、重新挂载（先用一个相对保守、兼容性好的命令）

还是在 rclone 所在目录，先试一个**简单稳定版** 挂载命令，不加 `--fuse-flag sync_read` 这些花活：
[code] 
    .\rclone.exe mount one: X: `
      --vfs-cache-mode full `
      --vfs-cache-max-size 20G `
      --vfs-cache-max-age 24h `
      --dir-cache-time 12h `
      --poll-interval 1m `
      --buffer-size 32M `
      --transfers 4 `
      --multi-thread-streams 4 `
      -vv
    
[/code]

几条关键说明：

  * 这条命令**正常情况下会一直卡在那儿不返回** ，这是好现象：  
说明挂载成功、rclone 正在前台运行。  
你就保留这个窗口，最小化别关。

  * 这时你就去“此电脑”里看，应该能看到一个新的 `X:` 盘。

  * 如果这里一切正常，之后你再考虑把 `--fuse-flag sync_read` 加回去测试。

* * *

## 四、如果还报错 / 仍然无法挂载

如果按上面步骤做完，挂载仍直接报错退出：

  1. 先发我**新的错误截图** （尤其是最后几行 `ERROR` / `CRITICAL`），因为刚才那张里主要是“取消上传失败”，我需要看清现在最新的报错内容。

  2. 确认一下：

     * WinFsp 是否安装的是 **1.11 或 2.x 正式版** ；

     * PowerShell 是否是用“以管理员身份运行”开的；

     * 没有其他类似 RaiDrive、AirLiveDrive 正在同时占用同一个盘符。
