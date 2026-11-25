---
title: CFnat：Cloudflare优选新思路，专治泛播IP动态路由，提升网络体验！
date: '2024-11-17 12:00:00'
tags:
- 科学上网
categories:
- 科学上网
description: 首先声明，这款软件并非我原创开发，而是目前了解到由 股神 在 CF中转IP 频道 发布的一款实时筛选 Cloudflare 数据中心的软件。我所编写的脚本是在这位开发者的原始版本基础上进行的 二次开发 。 由于该 软件尚未开源 ，接下来我将根据作者的简介，结合我的理解进行说明。若
---
首先声明，这款软件并非我原创开发，而是目前了解到由 股神 在 [CF中转IP 频道](https://t.me/CF_NAT/38840) 发布的一款实时筛选 Cloudflare 数据中心的软件。我所编写的脚本是在这位开发者的原始版本基础上进行的二次开发。

由于该软件尚未开源，接下来我将根据作者的简介，结合我的理解进行说明。若有不当之处，欢迎指正。

CFnat 是一款自动查找并优化 Cloudflare IP 转发的工具，旨在解决泛播 IP 路由不稳定的问题。如果你曾找到过速度不错的 Cloudflare IP，CFnat 能帮助你快速筛选出最佳 IP 并实现端口转发，从而提升网络使用体验。因此，这款工具对于移动、广电网络用户来说尤为明显！

CFnat 使用场景也必须是在国内机子长期上运行，所以我的脚本就不另开GitHub仓库（放在上面你也没办法直接下载），文章的末尾会附上 CFnat 所有文件的下载链接，供各位直接调用二次开发。

* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E "免责声明")免责声明

CFnat 相关项目仅供教育、研究和安全测试目的而设计和开发。本项目旨在为安全研究人员、学术界人士及技术爱好者提供一个探索和实践网络通信技术的工具。  
在下载和使用本项目代码时，使用者必须严格遵守其所适用的法律和规定。使用者有责任确保其行为符合所在地区的法律框架、规章制度及其他相关规定。

### [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E4%BD%BF%E7%94%A8%E6%9D%A1%E6%AC%BE "使用条款")使用条款

  * 教育与研究用途：本软件仅可用于网络技术和编程领域的学习、研究和安全测试。
  * 禁止非法使用：严禁将 CFnat 用于任何非法活动或违反使用者所在地区法律法规的行为。
  * 使用时限：基于学习和研究目的，建议用户在完成研究或学习后，或在安装后的24小时内，删除本软件及所有相关文件。
  * 免责声明：CFnat 的创建者和贡献者不对因使用或滥用本软件而导致的任何损害或法律问题负责。
  * 用户责任：用户对使用本软件的方式以及由此产生的任何后果完全负责。
  * 无技术支持：本软件的创建者不提供任何技术支持或使用协助。
  * 知情同意：使用 CFnat 即表示您已阅读并理解本免责声明，并同意受其条款的约束。

请记住：本软件的主要目的是促进学习、研究和安全测试。作者不支持或认可任何其他用途。使用者应当在合法和负责任的前提下使用本工具。

* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E7%BB%8F%E9%AA%8C%E4%B9%8B%E8%B0%88 "经验之谈")经验之谈

  1. cfnat和梯子在同一台设备上运行时使用本地服务IP:端口连接。
  2. cfnat和梯子分别处在同一局域网内的两台设备上运行时使用内网服务IP:端口连接。
  3. 如果你是使用 [cmliu/edgetunnel](https://github.com/cmliu/edgetunnel) 的节点，可将本地服务IP:端口和内网服务IP:端口都添加至`ADD`变量里，直接订阅食用即可
  4. 移动/广电用户设置数据中心`HKG`直接起飞！电信/联通用户设置`SJC,LAX`！
  5. 在跑过一次优选之后，可在`colo`文件夹里可以看到`ip.csv`扫描结果, 里面就能看到你的当前网络网络环境下能跑出来的所有数据中心！
  6. 不推荐直接在OpenWRT上直接跑，除非你会设置cfnat不走代理！！！或者等一个大佬开发cfnat的luci界面？
  7. 那个AS209242的IP库就是个笑话，别用！

* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#CFnat-Windows-GUI "CFnat Windows GUI")[CFnat Windows GUI](https://github.com/cmliu/CFnat-Windows-GUI)

[![CFnat Windows GUI](https://xn--1uto7rutmzjk.us.kg/img/cfnat/gui.png)](https://xn--1uto7rutmzjk.us.kg/img/cfnat/gui.png)  
点击[CFnat Windows GUI](https://github.com/cmliu/CFnat-Windows-GUI/releases)下载，因EXE程序没有签名，会被杀软查杀是正常现象，请自行考虑放行与否。

  * 使用`cmd`带参执行原程序，例如：

cmd
[code]1  
        
[/code]

| 
[code]cfnat-windows-amd64.exe -addr="0.0.0.0:1234" -colo=HKG -delay=100 -port=80 -tls=false  
        
[/code]  
  
---|---  

* * *

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#GUI%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84 "GUI文件结构")GUI文件结构

shell
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    11  
    12  
    13  
    14  
    15  
    16  
    17  
    18  
    19  
    20  
    
[/code]

| 
[code]
    CFnat Windows GUI.exe      # GUI本体  
    cfnat.ini                  # GUI配置文件  
    cfnat-windows-386.exe      # cfnat x86_32位 原程序本体  
    cfnat-windows-amd64.exe    # cfnat x86_64位 原程序本体  
    cfnat-windows-arm.exe      # cfnat arm_32位 原程序本体  
    cfnat-windows-arm64.exe    # cfnat arm_64位 原程序本体  
    cfnat-windows7-386.exe     # cfnat Win7_x86_32位 原程序本体 Win7专用  
    cfnat-windows7-amd64.exe   # cfnat Win7_x86_64位 原程序本体 Win7专用  
    colo  
     ├─ colo-windows-386.exe   # colo x86_32位 用于生成缓存IP库  
     ├─ colo-windows-amd64.exe # colo x86_64位 用于生成缓存IP库  
     ├─ colo-windows-arm.exe   # colo arm_32位 用于生成缓存IP库  
     ├─ colo-windows-arm64.exe # colo arm_64位 用于生成缓存IP库  
     ├─ ip.csv                 # colo 扫描结果 用于生成缓存IP库  
     ├─ ips-v4.txt             # IPv4库  
     ├─ ips-v6.txt             # IPv6库  
     └─ locations.json         # CF数据中心json文件  
    ips-v4.txt                 # 缓存IPv4库  
    ips-v6.txt                 # 缓存IPv6库  
    locations.json             # CF数据中心json文件  
    
[/code]  
  
---|---  
  
* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#CFnat-%E4%B8%80%E9%94%AE%E8%84%9A%E6%9C%AC "CFnat 一键脚本")CFnat 一键脚本

[![cfnat](https://xn--1uto7rutmzjk.us.kg/img/cfnat/cfnat.png)](https://xn--1uto7rutmzjk.us.kg/img/cfnat/cfnat.png)

> 适用场景：拥有干净网关的Linux设备，OpenWRT软路由使用时必须保证 cfnat 处于直连环境！！！

* * *

  * 终端命令

shell
[code]1  
        
[/code]

| 
[code]bash <(curl -Ls https://raw.cmliussss.com/cfnat.sh)  
        
[/code]  
  
---|---  
  * 或

shell
[code]1  
        2  
        
[/code]

| 
[code]curl -sSL https://raw.cmliussss.com/cfnat.sh -o ~/cfnat.sh && chmod +x ~/cfnat.sh  
        bash ~/cfnat.sh  
        
[/code]  
  
---|---  
  
> 在正式运行之前，推荐先配置 cfnat参数后调试运行 cfnat  
> 如`系统/架构`识别不正确，则需要`7`手动设置系统架构  
> 在调试运行 cfnat测试无误后`Ctrl+C`取消运行，后再次进入脚本选择`2`启动 cfnat即可  
> 不推荐手机用户使用后台运行，直接使用调试运行 cfnat即可

  * 无交互命令

shell
[code]1  
        2  
        3  
        4  
        5  
        
[/code]

| 
[code]# 无交互直接跑SJC,LAX优选，需要提前将脚本下载到~目录  
        cfnat SJC,LAX   
          
        # 无交互直接跑HKG优选  
        bash <(curl -Ls https://raw.cmliussss.com/cfnat.sh) HKG  
        
[/code]  
  
---|---  
  
> 注意使用无交互启动后，脚本会使用`crontab`对cfnat进程进行守护，关闭需要进入脚本`bash cfnat.sh`选择3即可停止cfnat进程并清理`crontab`。

* * *

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E8%84%9A%E6%9C%AC%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84 "脚本文件结构")脚本文件结构

shell
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    
[/code]

| 
[code]
    cfnat.sh            # sh脚本 本体  
    cfnat  
     ├─ cfnat-linux-*   # cfnat 原程序本体  
     ├─ cfnat.conf      # sh脚本 相关参数配置文件  
     ├─ ips-v4.txt      # IPv4库  
     ├─ ips-v6.txt      # IPv6库  
     └─ locations.json  # CF数据中心json文件  
    
[/code]  
  
---|---  
  
> 所谓的卸载就是删除cfnat文件夹

* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#CFnat-Docker "CFnat Docker")[CFnat Docker](https://github.com/cmliu/CFnat-Docker)

[![CFnat Docker](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://xn--1uto7rutmzjk.us.kg/img/cfnat/hub-docker-com-r-cmliu-cfnat.png)

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95 "使用方法")使用方法

### [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E4%B8%80%E9%94%AE%E5%91%BD%E4%BB%A4 "一键命令")一键命令

  * 官方仓库拉取

shell
[code]
    1  
    
[/code]

| 
[code]
    docker run -d --name mycfnat --restart always -p 1234:1234 cmliu/cfnat:latest  
    
[/code]  
  
---|---  
  
  * 镜像仓库拉取

shell
[code]
    1  
    
[/code]

| 
[code]
    docker run -d --name mycfnat --restart always -p 1234:1234 docker.fxxk.dedyn.io/cmliu/cfnat:latest  
    
[/code]  
  
---|---  
  
### [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E5%88%9B%E5%BB%BA-docker-compose-yml "创建 docker-compose.yml")创建 `docker-compose.yml`

yml
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    11  
    12  
    13  
    14  
    15  
    16  
    17  
    18  
    19  
    20  
    21  
    
[/code]

| 
[code]
    version: '3'  
      
    services:  
      cfnat:  
        container_name: mycfnat  
        image: cmliu/cfnat:latest  
        environment:  
          - colo=HKG,SJC,LAX  # 筛选数据中心例如 HKG,SJC,LAX.电信/联通 推荐 SJC,LAX.移动/广电 推荐 HKG"  
          - delay=300  # 有效延迟（毫秒），超过此延迟将断开连接  
          - ips=4  # 指定生成IPv4还是IPv6地址  
          - port=443  # 转发的目标端口  
          - tls=true  # 是否为 TLS 端口  
          - random=true  # 是否随机生成IP，如果为false，则从CIDR中拆分出所有IP  
          - ipnum=10  # 提取的有效IP数量  
          - num=10  # 目标负载 IP 数量  
          - task=100  # 并发请求最大协程数  
          - code=200  # HTTP/HTTPS 响应状态码  
          - domain=cloudflaremirrors.com/debian # 响应状态码检查的域名地址  
        ports:  
          - "1234:1234"  # 将主机的 1234 端口映射到容器的 1234 端口  
        restart: always  
    
[/code]  
  
---|---  
  
## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B "使用案例")使用案例

  * 数据中心(colo): HKG
  * 有效延迟(delay): 160
  * IP类型(ips): 6

shell
[code]1  
        
[/code]

| 
[code]docker run -d -e colo="HKG" -e delay=160 -e ips=6 --restart always -p 1234:1234 cmliu/cfnat:latest  
        
[/code]  
  
---|---  

* * *

  * 数据中心(colo): HKG
  * 有效延迟(delay): 160
  * IP类型(ips): 4
  * 转发端口(port): 80
  * tls: false
  * 本地映射端口: 8080

shell
[code]1  
        
[/code]

| 
[code]docker run -d -e colo="HKG" -e delay=160 -e ips=4 -e port=80 -e tls=false --restart always -p 8080:1234 cmliu/cfnat:latest  
        
[/code]  
  
---|---  

* * *

  * 数据中心(colo): SJC,LAX
  * 有效延迟(delay): 300
  * IP类型(ips): 4

shell
[code]1  
        
[/code]

| 
[code]docker run -d -e colo="SJC,LAX" -e delay=300 -e ips=4 --restart always -p 1234:1234 cmliu/cfnat:latest  
        
[/code]  
  
---|---  

* * *

  * 数据中心(colo): LAX
  * 有效延迟(delay): 300
  * IP类型(ips): 4
  * 转发端口(port): 80
  * tls: false
  * 随机IP(random): true
  * 有效IP数(ipnum): 10
  * 负载IP数(num): 10
  * 最大并发请求数(task): 100
  * 响应状态码(code): 200
  * 检查域名(domain): “cloudflaremirrors.com/debian”

shell
[code]1  
        2  
        3  
        4  
        5  
        6  
        7  
        8  
        9  
        10  
        11  
        12  
        13  
        14  
        15  
        
[/code]

| 
[code]docker run -d \  
            -e colo="LAX" \  
            -e delay=300 \  
            -e ips=4 \  
            -e port=80 \  
            -e tls=false \  
            -e random=true \  
            -e ipnum=10 \  
            -e num=10 \  
            -e task=100 \  
            -e code=200 \  
            -e domain="cloudflaremirrors.com/debian" \  
            --restart always \  
            -p 1234:1234 \  
            cmliu/cfnat:latest  
        
[/code]  
  
---|---  

* * *

  * 使用`docker-compose.yml`同时启动多个cfnat容器

yml
[code]1  
        2  
        3  
        4  
        5  
        6  
        7  
        8  
        9  
        10  
        11  
        12  
        13  
        14  
        15  
        16  
        17  
        18  
        19  
        20  
        21  
        22  
        23  
        24  
        25  
        26  
        27  
        28  
        29  
        30  
        31  
        32  
        33  
        34  
        35  
        36  
        37  
        38  
        39  
        40  
        41  
        42  
        43  
        44  
        45  
        46  
        47  
        48  
        49  
        50  
        51  
        52  
        53  
        54  
        55  
        56  
        57  
        58  
        59  
        
[/code]

| 
[code]version: '3'  
          
        services:  
              cfnat1:  
                    container_name: cfnathkg443  
                    image: cmliu/cfnat:latest  
                    environment:  
                          - colo=HKG  # 筛选数据中心例如 HKG,SJC,LAX.电信/联通 推荐 SJC,LAX.移动/广电 推荐 HKG  
                          - delay=160  # 有效延迟（毫秒），超过此延迟将断开连接  
                          #- ips=4  # 指定生成IPv4还是IPv6地址  
                          - port=443  # 转发的目标端口  
                          #- tls=true  # 是否为 TLS 端口  
                          #- random=true  # 是否随机生成IP，如果为false，则从CIDR中拆分出所有IP  
                          #- ipnum=10  # 提取的有效IP数量  
                          #- num=10  # 目标负载 IP 数量  
                          - task=64  # 并发请求最大协程数  
                          #- code=200  # HTTP/HTTPS 响应状态码  
                          #- domain=cloudflaremirrors.com/debian # 响应状态码检查的域名地址  
                    ports:  
                          - "443:1234"  # 将主机的 443 端口映射到容器的 1234 端口  
                    restart: always  
          
              cfnat2:  
                    container_name: cfnathkg80  
                    image: cmliu/cfnat:latest  
                    environment:  
                          - colo=HKG  # 筛选数据中心例如 HKG,SJC,LAX.电信/联通 推荐 SJC,LAX.移动/广电 推荐 HKG  
                          - delay=160  # 有效延迟（毫秒），超过此延迟将断开连接  
                          #- ips=4  # 指定生成IPv4还是IPv6地址  
                          - port=80  # 转发的目标端口  
                          - tls=false  # 是否为 TLS 端口  
                          #- random=true  # 是否随机生成IP，如果为false，则从CIDR中拆分出所有IP  
                          #- ipnum=10  # 提取的有效IP数量  
                          #- num=10  # 目标负载 IP 数量  
                          - task=64  # 并发请求最大协程数  
                          #- code=200  # HTTP/HTTPS 响应状态码  
                          #- domain=cloudflaremirrors.com/debian # 响应状态码检查的域名地址  
                    ports:  
                          - "80:1234"  # 将主机的 80 端口映射到容器的 1234 端口  
                    restart: always  
                
              cfnat3:  
                    container_name: mycfnat  
                    image: cmliu/cfnat:latest  
                    environment:  
                          - colo=SJC,LAX  # 筛选数据中心例如 HKG,SJC,LAX.电信/联通 推荐 SJC,LAX.移动/广电 推荐 HKG  
                          - delay=300  # 有效延迟（毫秒），超过此延迟将断开连接  
                          #- ips=4  # 指定生成IPv4还是IPv6地址  
                          - port=443  # 转发的目标端口  
                          #- tls=true  # 是否为 TLS 端口  
                          #- random=true  # 是否随机生成IP，如果为false，则从CIDR中拆分出所有IP  
                          #- ipnum=10  # 提取的有效IP数量  
                          #- num=10  # 目标负载 IP 数量  
                          - task=64  # 并发请求最大协程数  
                          #- code=200  # HTTP/HTTPS 响应状态码  
                          #- domain=cloudflaremirrors.com/debian # 响应状态码检查的域名地址  
                    ports:  
                          - "1234:1234"  # 将主机的 1234 端口映射到容器的 1234 端口  
                    restart: always  
        
[/code]  
  
---|---  

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E6%9F%A5%E7%9C%8B%E6%97%A5%E5%BF%97 "查看日志")查看日志

shell
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    
[/code]

| 
[code]
    # 查看cfnat容器执行日志  
    docker logs 容器ID  
    docker logs -f 容器ID    # 实时查看日志  
      
    # 查看cfnat容器启动日志  
    docker exec 容器ID cat cfnat.log  
    
[/code]  
  
---|---  
  
* * *

# [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#CFnat-%E5%8E%9F%E7%A8%8B%E5%BA%8F "CFnat 原程序")CFnat 原程序

[![cfnat](https://xn--1uto7rutmzjk.us.kg/img/cfnat/c.jpg)](https://xn--1uto7rutmzjk.us.kg/img/cfnat/c.jpg)

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E5%91%BD%E4%BB%A4 "命令")命令

  * 下载并赋权，示例（`cfnat-linux-amd64`程序名架构自行对照[下载目录](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E4%B8%8B%E8%BD%BD%E7%9B%AE%E5%BD%95)修改）：

shell
[code]1  
        
[/code]

| 
[code]curl -sSL https://raw.cmliussss.com/cfnat/cfnat-linux-amd64 -o cfnat-linux-amd64 && chmod +x cfnat-linux-amd64  
        
[/code]  
  
---|---  
  * 执行命令，示例：

shell
[code]1  
        
[/code]

| 
[code]./cfnat-linux-amd64 -addr="0.0.0.0:1234" -colo=HKG -delay=100  
        
[/code]  
  
---|---  

* * *

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E4%B8%8B%E8%BD%BD%E7%9B%AE%E5%BD%95 "下载目录")下载目录

  * 下载地址`https://raw.cmliussss.com/cfnat/*`，自行替换`*`为下载文件名：

cmd
[code]1  
        2  
        3  
        4  
        5  
        6  
        7  
        8  
        9  
        10  
        11  
        12  
        13  
        14  
        15  
        16  
        17  
        18  
        19  
        20  
        21  
        22  
        23  
        24  
        25  
        26  
        27  
        28  
        29  
        30  
        31  
        32  
        33  
        34  
        35  
        36  
        37  
        38  
        39  
        40  
        41  
        42  
        
[/code]

| 
[code]cfnat-android-arm64  
        cfnat-darwin-amd64  
        cfnat-darwin-arm64  
        cfnat-dragonfly-amd64  
        cfnat-freebsd-386  
        cfnat-freebsd-amd64  
        cfnat-freebsd-arm  
        cfnat-freebsd-arm64  
        cfnat-linux-386  
        cfnat-linux-amd64  
        cfnat-linux-armv5  
        cfnat-linux-armv6  
        cfnat-linux-armv7  
        cfnat-linux-arm64  
        cfnat-linux-mips  
        cfnat-linux-mips64  
        cfnat-linux-mips64le  
        cfnat-linux-mipsle  
        cfnat-linux-ppc64  
        cfnat-linux-ppc64le  
        cfnat-linux-riscv64  
        cfnat-linux-s390x  
        cfnat-netbsd-386  
        cfnat-netbsd-amd64  
        cfnat-netbsd-arm  
        cfnat-netbsd-arm64  
        cfnat-openbsd-386  
        cfnat-openbsd-amd64  
        cfnat-openbsd-arm  
        cfnat-openbsd-arm64  
        cfnat-plan9-386  
        cfnat-plan9-amd64  
        cfnat-solaris-amd64  
        cfnat-termux  
        cfnat-windows-386.exe  
        cfnat-windows-amd64.exe  
        cfnat-windows-arm.exe  
        cfnat-windows-arm64.exe  
        cfnat-windows7-386.exe  
        cfnat-windows7-amd64.exe  
        ips-v4.txt  
        ips-v6.txt  
        
[/code]  
  
---|---  

## [](https://xn--1uto7rutmzjk.us.kg/p/cfnat/#%E5%8F%82%E6%95%B0%E5%91%BD%E4%BB%A4 "参数命令")参数命令

shell
[code]
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    11  
    12  
    13  
    14  
    15  
    16  
    17  
    18  
    19  
    20  
    21  
    22  
    23  
    24  
    25  
    
[/code]

| 
[code]
    Usage of cfnat:  
      -addr string  
            本地监听的 IP 和端口 (default "0.0.0.0:1234")  
      -code int  
            HTTP/HTTPS 响应状态码 (default 200)  
      -colo string  
            筛选数据中心例如 HKG,SJC,LAX (多个数据中心用逗号隔开,留空则忽略匹配)  
      -delay int  
            有效延迟（毫秒），超过此延迟将断开连接 (default 300)  
      -domain string  
            响应状态码检查的域名地址 (default "cloudflaremirrors.com/debian")  
      -ipnum int  
            提取的有效IP数量 (default 20)  
      -ips string  
            指定生成IPv4还是IPv6地址 (4或6) (default "4")  
      -num int  
            目标负载 IP 数量 (default 10)  
      -port int  
            转发的目标端口 (default 443)  
      -random  
            是否随机生成IP，如果为false，则从CIDR中拆分出所有IP (default true)  
      -task int  
            并发请求最大协程数 (default 100)  
      -tls  
            是否为 TLS 端口 (default true)  
    
[/code]  
  
---|---  
  
* * *

新人[Youtuber](https://www.youtube.com/@CMLiussss)，需要您的支持，请务必帮我点赞、关注、打开小铃铛， _十分感谢！！！_
