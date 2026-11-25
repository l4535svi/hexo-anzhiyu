---
title: 代理软件合集(持续更新中)
date: '2025-04-03 12:00:00'
tags:
- 科学上网
categories:
- 科学上网
description: Windows端 V2rayN V2rayN是一个基于 V2Ray 内核的 Windows 平台图形化客户端，专为用户提供网络代理服务。它可以帮助用户通过代理服务器访问被封锁的内容、保护隐私以及加速网络连接。v2rayN 支持多种协议，包括 Vmess、Shadowsocks、S
---
## Windows端

## [V2rayN](https://github.com/2dust/v2rayN/releases)

V2rayN是一个基于 V2Ray 内核的 Windows 平台图形化客户端，专为用户提供网络代理服务。它可以帮助用户通过代理服务器访问被封锁的内容、保护隐私以及加速网络连接。v2rayN 支持多种协议，包括 Vmess、Shadowsocks、Socks5 等，使用起来非常灵活且强大。

主要功能：  
多协议支持：v2rayN 支持 Vmess、Shadowsocks、Socks5、HTTP 等多种代理协议，适用于不同的网络环境和需求。  
多平台兼容：虽然 v2rayN 是专为 Windows 开发的客户端，但它的核心 V2Ray 支持多种操作系统，如 Linux、macOS、Android 等。  
高级加密：支持多种加密方式，确保用户的数据传输安全可靠。  
自动配置更新：通过订阅功能，用户可以自动更新节点列表，简化配置过程。  
丰富的代理设置：支持自定义路由规则，可以实现按需代理特定网站或 IP 地址。  
网络监控与日志：内置网络连接状态监控与详细日志功能，方便排查问题。

v2rayN是一个高度自定义和灵活的工具，适合对网络代理有一定需求的用户使用。

安装包选择  
在下载安装包栏中有很多 zip 压缩包选择，我们推荐第一次安装的用户下载 v2rayN-With-Core.zip 压缩包。安装时会自动提示安装[Microsoft .NET 6.0 Desktop Runtime]。

v2rayN-With-Core.zip :包含所有Core文件，如您第一次请下载此包  
v2rayN-With-Core-SelfContained.7z:包含所有Core文件；独立包，不需要下载安装[Microsoft .NET 6.0 Desktop Runtime]  
v2rayN-32.zip:不包含Core文件  
v2rayN-arm64.zip:不包含Core文件

系统代理  
系统代理分为：清除系统代理、自动配置系统代理、不改变系统代理、PAC模式

清除系统代理：关闭代理，恢复原先的网络。  
自动配置系统代理：开启代理  
不改变系统代理：什么都不做.作用就是保留其他软件设定的代理  
PAC模式：也就是智能分流模式，根据规则去匹配你访问的网站，仅加速国外网站，国内网站不受影响。  
日常使用时推荐自动配置系统代理即可。  
开机自启：设置——v2rayN设置——开机启动  
路由  
全局: 所有数据都走代理出站  
黑名单：除了黑名单内的网站，其余网站都通过节点服务器代理上网  
绕过大陆: 从geo文件中判断目标是否cn的,如果是走直连出站,其他走代理出站(局域网也已绕过)  
总结下，在我们平时使用过程中保持一下选择即可：

系统代理 选择 自动配置系统代理  
路由高级功能 选择 绕过大陆

相关视频：<https://t.me/xiaoqiziyuanku/47>  
网盘下载：<https://t.me/xiaoqiziyuanku/47?comment=7726>

## [Clash](https://github.com/lantongxue/clash_for_windows_pkg/releases)（停止维护）

Clash（第三方下载）是目前最受欢迎的科学上网工具之一（目前已停止更新），尤其在开发者 “Dreamacro” 因各种原因暂停了维护和更新后，Clash的社区用户和开源贡献者们接手了开发工作。虽然原作者“跑路”这一说法存在，但社区的活跃性和强大的开源生态依然让 Clash保持了长期的生命力。

核心功能

  1. 多协议支持  
Shadowsocks、ShadowsocksR、VMess、VLESS、Trojan等
  2. 策略路由  
Clash 提供了非常强大的路由策略功能，允许用户通过自定义配置文件来定义流量路由规则。你可以根据域名、IP 地址或流量类型来决定哪些流量使用代理，哪些流量直接访问互联网。这种细粒度的流量控制极大地优化了网络性能，尤其适合跨区域访问和绕过网络封锁。
  3. 订阅和自动更新  
Clash 支持从远程订阅链接获取代理节点信息，用户只需通过订阅方式，便可以自动获取最新的服务器配置，避免了手动添加节点的繁琐。同时，Clash 会定期更新订阅内容，确保节点的可用性和稳定性。
  4. 开源透明  
尽管最初的开发者已经不再继续维护 Clash，但由于其是开源项目，全球的开发者社区接手了维护工作。用户可以在 GitHub 上查看源代码，进行安全审计，并根据自己的需求进行二次开发。这保证了工具的安全性、透明性和长期可用性。
  5. 跨平台支持  
Clash 支持主流操作系统，包括 Windows、macOS、Linux、Android 和 iOS。这意味着你可以在不同设备间保持一致的配置和使用体验。此外，还有社区开发的图形化客户端，如 Clash for Windows（CFW） 和 ClashX（macOS），使得配置和管理更加直观简便。
  6. 插件和扩展功能  
Clash 支持通过插件扩展更多功能，比如与 DNS 服务集成、广告过滤器等。高级用户可以借助这些扩展来进一步定制和优化他们的网络体验。

使用场景

  1. 科学上网：Clash 常被用来解决网络审查问题，使用户可以自由访问被封锁的网站和服务，如 YouTube、Google、Twitter 等。
  2. 隐私保护：通过代理加密和流量混淆，Clash 有效保护用户的上网隐私，防止流量被窃取或监控。
  3. 多节点切换：Clash 允许用户快速切换不同国家和地区的代理服务器，实现更好的网络速度和稳定性，尤其适合游戏、视频流等需要较高带宽的应用场景。
  4. 企业和个人用户：Clash 还适合企业或专业用户对网络进行管理和控制，如通过策略路由精确控制公司内部网络的流量分发。

无论你是技术新手还是高级用户，Clash 都能提供强大的自定义能力和卓越的代理功能来满足你的网络需求。Clash不推荐汉化，因为汉化会有很多bug，常用的功能也就那几个，大家可以试着翻译下。如果实在是觉得英文别扭的话，可以看下方Clash的衍生软件。

相关视频：<https://t.me/xiaoqiziyuanku/49>  
网盘下载：<https://t.me/xiaoqiziyuanku/49?comment=8562>

## [Clash Verge](https://github.com/zzzgydi/clash-verge/releases)（停止维护）

Clash Verge是 Clash 项目的一个分支（目前已停止更新）针对更现代化、用户体验友好的界面做了优化。Clash Verge 提供了简洁直观的界面，方便用户更轻松地配置代理服务。与经典的 Clash 相比，Clash Verge 在功能上保持了相同的强大性，尤其是支持的代理协议方面。相似的Clash还有好几种，例如：[Clash.net](https://github.com/TgDaoSheng/Clash.Net/releases)（停止维护）[Clash Verge-Rev](https://github.com/clash-verge-rev/clash-verge-rev) （正常更新）都是基于Clash衍生的代理软件，功能的话都差不多，新的版本可能会支持更多协议。具体的话可以看相关的项目官网介绍。

由于 2023 年 11 月 2 日 Clash for Windows 作者删库事件，Clash Verge 作为多个相关 GUI 客户端项目之一，也受到了影响。但我们已发布的版本仍然是正常可用的，当然，你也可以选择在持续维护更新的后继版本Clash Verge-Rev。

相关视频：<https://t.me/xiaoqiziyuanku/52>  
网盘下载：<https://t.me/xiaoqiziyuanku/52?comment=10650>

## [Qv2ray](https://github.com/Qv2ray/Qv2ray)（已停止维护）

Qv2ray 是一个跨平台的 V2Ray 图形用户界面（GUI）客户端，旨在简化 V2Ray 的使用和配置。通过 Qv2ray，用户无需手动修改配置文件，能够轻松地管理和配置代理节点。它具有多协议支持、灵活的路由规则，以及丰富的扩展功能，是一个功能强大的代理工具，适合需要科学上网、隐私保护或绕过网络审查的用户。

支持协议 ：Shadowsocks、ShadowsocksR、VMess、VLESS、Trojan等

安装内核：需安装4.45.2版本，其他不推荐：[https://github.com/v2fly/v2ray-core/releases?q=v4.45.2&expanded=true](https://github.com/v2fly/v2ray-core/releases?q=v4.45.2&expanded=true)

Shadowsocks插件下载：<https://github.com/Qv2ray/QvPlugin-SS/releases>  
SSR插件下载：<https://github.com/Qv2ray/QvPlugin-SSR/releases>  
Trojan插件下载：<https://github.com/Qv2ray/QvPlugin-Trojan/releases>  
Trojan-go插件下载：<https://github.com/Qv2ray/QvPlugin-Trojan-Go/releases>

插件使用方法：下载完成后，将其中的文件移动至Qv2ray目录下的config/plugins文件夹中，重启Qv2ray即可生效

相关视频：<https://t.me/newxqkjfenxiang/12145>  
网盘下载：<https://t.me/xiaoqiziyuanku/56?comment=12146>

## [Winxray](https://github.com/TheMRLL/WinXray)（已停止维护）

Winxray是一款专为 Windows 操作系统设计的网络代理工具，通常用于科学上网，帮助用户绕过网络限制，访问受限网站。它支持多种代理协议，包括 Shadowsocks、V2Ray、Trojan 等，能够有效加密用户的网络流量，提升网络隐私和安全性。WinXray 的界面友好，易于配置，适合新手和高级用户使用。

其核心功能包括：

多协议支持：支持多种主流代理协议，灵活应对不同网络环境。  
加密传输：通过加密技术保护用户的上网隐私，防止流量被第三方监控。  
跨平台兼容：虽然主要面向 Windows 用户，但代理协议支持其他设备如手机或路由器。  
服务器切换：用户可快速切换不同地区的服务器，优化网络连接速度和稳定性。  
定期更新：开发者会对软件进行更新，保证兼容性和安全性。  
WinXray 适合希望提升网络隐私、突破地区限制，或是在网络封锁环境中自由访问网络资源的用户使用。

相关视频：<https://t.me/newxqkjfenxiang/12145>  
网盘下载：<https://t.me/xiaoqiziyuanku/56?comment=12146>

## [FlClash](https://github.com/chen08209/FlClash)

基于ClashMeta的多平台代理客户端，简单易用，开源且无广告。多平台：Android、Windows、macOS 和 Linux。自适应多种屏幕尺寸，多种颜色主题可供选择。

若订阅链接不支持Clash格式可在最后加上 &flag=clash 即可导入

相关视频：  
网盘下载：

## iOS端/Mac端（Apple芯片）

## [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)

一款在iOS平台上使用的网络代理工具，主要用于科学上网和隐私保护。它可以帮助用户通过代理服务器访问被限制的网站和服务。Shadowrocket支持多种代理协议，包括Shadowsocks和Vmess等。

## [Quantumult](https://apps.apple.com/us/app/quantumult/id1252015438)（停止维护）

一款流行的网络代理工具，主要用于iOS平台，提供科学上网和隐私保护功能。它允许用户通过代理服务器访问被限制的网站和服务，支持多种代理协议，如Shadowsocks、Vmess和HTTP/SOCKS5等。

## [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620)

是Quantumult的高级版本，专为iOS平台设计，具有更强大的功能和更灵活的配置选项。更强大的分流功能，它不仅支持科学上网，还提供了更多的网络管理和监控工具。

## [Loon](https://apps.apple.com/us/app/loon/id1373567447)

一款专为iOS平台设计的网络代理工具，旨在提供科学上网和隐私保护功能。它具有直观的用户界面和强大的功能，适合需要灵活网络管理的用户。

## [i2Ray](https://apps.apple.com/us/app/i2ray/id1445270056)

一款基于V2Ray核心的网络代理工具，主要用于科学上网和隐私保护，支持多种协议和功能。它通常用于在iOS设备上绕过网络限制，访问被屏蔽的网站和服务。

## [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)

是一款功能强大的网络代理工具，主要用于科学上网，支持多种代理协议（如Shadowsocks、Vmess、Trojan等），在iOS和其他平台上广泛使用。它通常用于绕过网络限制，保护用户的隐私。

## [Kitsunebi](https://apps.apple.com/us/app/kitsunebi-proxy-utility/id1446584073)

是一款在iOS/Android平台上使用的网络代理工具，旨在提供科学上网和隐私保护功能。它支持多种代理协议，如Shadowsocks、Vmess和Trojan，帮助用户绕过网络限制，访问被屏蔽的网站和服务。

## [LanceX](https://apps.apple.com/us/app/lancex/id1536754048)

是一款针对iOS平台的网络代理工具，主要用于科学上网和隐私保护。它通常支持多种代理协议，如Shadowsocks、Vmess和Trojan，帮助用户绕过网络限制，访问被屏蔽的内容。

## [Potatso](https://apps.apple.com/us/app/potatso/id1239860606)（免费）

是一款专为iOS平台设计的网络代理工具，主要用于科学上网和隐私保护。它支持多种代理协议，如Shadowsocks、Vmess和HTTP/SOCKS5等，帮助用户绕过网络限制，访问被屏蔽的网站和服务。

## Android端

## [V2rayNG](https://github.com/2dust/v2rayNG)

V2rayNG是一款针对Android平台的网络代理工具，基于V2Ray核心，主要用于科学上网和隐私保护。它支持多种代理协议，如Vmess、Shadowsocks和Trojan，帮助用户绕过网络限制，访问被屏蔽的网站和服务。

## [Clash for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)（停止维护）

是一款功能强大的网络代理工具，基于Clash核心，主要用于科学上网和隐私保护。它支持多种代理协议，如Vmess、Shadowsocks、Trojan等，帮助用户绕过网络限制，访问被屏蔽的网站和服务。

## [Surfboard](https://github.com/getsurfboard/surfboard/releases/tag/tv-1.0.2)

简称：“冲浪板” 是一款用于科学上网的网络代理工具，主要针对Android平台。它支持多种代理协议，包括Shadowsocks、Vmess和Trojan，旨在帮助用户绕过网络限制，保护隐私。

## [NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid)

是一款用于Android平台的网络代理工具，主要用于科学上网和隐私保护。它支持多种代理协议，如Shadowsocks和Vmess，帮助用户绕过网络限制，访问被屏蔽的网站和服务。

## Mac（Intel版本）

## [v2rayU](https://github.com/yanue/V2rayU/releases/tag/v4.2.5)

是一款适用于macOS的图形化V2Ray客户端，旨在简化V2Ray的使用和配置。它提供了友好的用户界面，方便用户进行科学上网和代理设置。

## [ClashX](https://github.com/bannedbook/ClashX)

是一款适用于macOS的网络代理工具，基于Clash核心，主要用于科学上网和隐私保护。它支持多种代理协议，如Vmess、Shadowsocks、Trojan等，并提供了灵活的分流设置。

## [Qv2ray](https://github.com/Qv2ray/Qv2ray)（停止维护）

是一款跨平台的图形化V2Ray客户端，支持Windows、macOS和Linux。它旨在简化V2Ray的使用，使用户能够更方便地配置和管理网络代理。

## Apple芯片请可以参考iOS端
