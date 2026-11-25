---
title: ap
date: '2026-11-10 12:00:00'
description: '我看了你的截图，不是 eMMC 硬盘损坏，而是 ImmortalWrt 系统没有安装 mmc 检测工具。 你的终端报错： -ash: mmc: not found 说明系统找不到 mmc 命令，所以暂时无法查询 eMMC 寿命。 而且从截图来看，你的京东云亚瑟已经成功运行 Imm'
---
我看了你的截图，不是 eMMC 硬盘损坏，而是 ImmortalWrt 系统没有安装 `mmc` 检测工具。

你的终端报错：
[code]
    -ash: mmc: not found
[/code]

说明系统找不到 `mmc` 命令，所以暂时无法查询 eMMC 寿命。

而且从截图来看，你的京东云亚瑟已经成功运行 ImmortalWrt SNAPSHOT 系统了。

## 一、先检查软件包管理器

在你现在的 ImmortalWrt 网页终端中，复制执行：
[code]
    command -v apk
    command -v opkg
    cat /etc/openwrt_release
[/code]

这三条命令用来确定系统使用哪种软件包管理方式。

## 二、安装 eMMC 检测工具

你的 ImmortalWrt SNAPSHOT 大概率使用 `apk`，可以尝试：
[code]
    apk update
    apk add mmc-utils
[/code]

ImmortalWrt 25.12 及后续版本采用 APK 包管理器，而且官方 SNAPSHOT 软件仓库提供 `mmc-utils`。

MirrorZ Help+1

如果第一步查出只有 `opkg`，则使用：
[code]
    opkg update
    opkg install mmc-utils
[/code]

## 三、安装后查询寿命
[code]
    mmc extcsd read /dev/mmcblk0 | grep -Ei 'life.time|pre.eol'
[/code]

可能看到：
[code]
    Life Time Estimation A: 0x02
    Life Time Estimation B: 0x03
    Pre EOL information: 0x01
[/code]

表示 A、B 两类寿命估算分别消耗约 10%～20% 和 20%～30%，预警状态正常，并非精确寿命百分比。

另外，你的截图顶部有红色提示「未设置密码」，建议顺手运行：
[code]
    passwd
[/code]

给 root 设置一个管理密码，避免路由器被未经授权访问。

你先运行 `apk update` 和 `apk add mmc-utils`，把输出发给我。 如果安装报错，我再帮你处理软件源，之后就能查看这块 64GB eMMC 的实际磨损等级。
