---
title: ArgoSB一键无交互小钢炮脚本💣：极简 + 轻量 + 快速
date: '2025-08-30 12:00:00'
tags:
- 节点分享
categories:
- 节点分享
description: 【ArgoSB当前版本：V25.8.27】 1、基于Sing-box + Xray + Cloudflared-Argo 三内核自动分配 2、支持Linux类主流VPS系统，SSH脚本支持非root环境运行，几乎无需依赖，无脑一次回车搞定 3、支持Docker镜像部署，公开镜像库
---
[![0cbc3f82134b4fc99afd6cee37e98be](https://private-user-images.githubusercontent.com/121604513/465203077-a76ca418-badb-4e9a-a771-6682ec713e06.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDY1MjAzMDc3LWE3NmNhNDE4LWJhZGItNGU5YS1hNzcxLTY2ODJlYzcxM2UwNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNzlhMWRkMTY1MTQ1MmJiZjIwMmM2NTFhNTU0YjFhY2M1N2Y4ZWY5Yjc3NmVmOGRiZmRkYTI1ZmM4YzA4NDM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.pOxosATDMpJ8vS9Kah7iqsLjMQkEHfDI1Z9J_eWZMmA)](https://private-user-images.githubusercontent.com/121604513/465203077-a76ca418-badb-4e9a-a771-6682ec713e06.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDY1MjAzMDc3LWE3NmNhNDE4LWJhZGItNGU5YS1hNzcxLTY2ODJlYzcxM2UwNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNzlhMWRkMTY1MTQ1MmJiZjIwMmM2NTFhNTU0YjFhY2M1N2Y4ZWY5Yjc3NmVmOGRiZmRkYTI1ZmM4YzA4NDM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.pOxosATDMpJ8vS9Kah7iqsLjMQkEHfDI1Z9J_eWZMmA)

### 【ArgoSB当前版本：V25.8.27】

[](https://github.com/yonggekkk/ArgoSB#argosb%E5%BD%93%E5%89%8D%E7%89%88%E6%9C%ACv25827)

* * *

#### 1、基于Sing-box + Xray + Cloudflared-Argo 三内核自动分配

[](https://github.com/yonggekkk/ArgoSB#1%E5%9F%BA%E4%BA%8Esing-box--xray--cloudflared-argo-%E4%B8%89%E5%86%85%E6%A0%B8%E8%87%AA%E5%8A%A8%E5%88%86%E9%85%8D)

#### 2、支持Linux类主流VPS系统，SSH脚本支持非root环境运行，几乎无需依赖，无脑一次回车搞定

[](https://github.com/yonggekkk/ArgoSB#2%E6%94%AF%E6%8C%81linux%E7%B1%BB%E4%B8%BB%E6%B5%81vps%E7%B3%BB%E7%BB%9Fssh%E8%84%9A%E6%9C%AC%E6%94%AF%E6%8C%81%E9%9D%9Eroot%E7%8E%AF%E5%A2%83%E8%BF%90%E8%A1%8C%E5%87%A0%E4%B9%8E%E6%97%A0%E9%9C%80%E4%BE%9D%E8%B5%96%E6%97%A0%E8%84%91%E4%B8%80%E6%AC%A1%E5%9B%9E%E8%BD%A6%E6%90%9E%E5%AE%9A)

#### 3、支持Docker镜像部署，公开镜像库：`ygkkk/argosb`

[](https://github.com/yonggekkk/ArgoSB#3%E6%94%AF%E6%8C%81docker%E9%95%9C%E5%83%8F%E9%83%A8%E7%BD%B2%E5%85%AC%E5%BC%80%E9%95%9C%E5%83%8F%E5%BA%93ygkkkargosb)

#### 4、支持NIX容器系统，特别推荐IDX-Google、Clawcloud爪云、CloudCat的服务器

[](https://github.com/yonggekkk/ArgoSB#4%E6%94%AF%E6%8C%81nix%E5%AE%B9%E5%99%A8%E7%B3%BB%E7%BB%9F%E7%89%B9%E5%88%AB%E6%8E%A8%E8%8D%90idx-googleclawcloud%E7%88%AA%E4%BA%91cloudcat%E7%9A%84%E6%9C%8D%E5%8A%A1%E5%99%A8)

#### 5、根据Sing-box与Xray不同内核，可选15种WARP出站组合，更换落地IP为WARP的IP，解锁流媒体

[](https://github.com/yonggekkk/ArgoSB#5%E6%A0%B9%E6%8D%AEsing-box%E4%B8%8Exray%E4%B8%8D%E5%90%8C%E5%86%85%E6%A0%B8%E5%8F%AF%E9%80%8915%E7%A7%8Dwarp%E5%87%BA%E7%AB%99%E7%BB%84%E5%90%88%E6%9B%B4%E6%8D%A2%E8%90%BD%E5%9C%B0ip%E4%B8%BAwarp%E7%9A%84ip%E8%A7%A3%E9%94%81%E6%B5%81%E5%AA%92%E4%BD%93)

#### 6、所有代理协议都无需域名（除了argo固定隧道），支持单个或多个代理协议任意组合并快速重置更换

[](https://github.com/yonggekkk/ArgoSB#6%E6%89%80%E6%9C%89%E4%BB%A3%E7%90%86%E5%8D%8F%E8%AE%AE%E9%83%BD%E6%97%A0%E9%9C%80%E5%9F%9F%E5%90%8D%E9%99%A4%E4%BA%86argo%E5%9B%BA%E5%AE%9A%E9%9A%A7%E9%81%93%E6%94%AF%E6%8C%81%E5%8D%95%E4%B8%AA%E6%88%96%E5%A4%9A%E4%B8%AA%E4%BB%A3%E7%90%86%E5%8D%8F%E8%AE%AE%E4%BB%BB%E6%84%8F%E7%BB%84%E5%90%88%E5%B9%B6%E5%BF%AB%E9%80%9F%E9%87%8D%E7%BD%AE%E6%9B%B4%E6%8D%A2)

【 已支持：AnyTLS、Any-reality、Vless-xhttp-reality、Vless-reality-vision、Shadowsocks-2022、Vmess-ws、Hysteria2、Tuic、Argo临时/固定隧道 】

#### 7、如需要多样的功能，推荐使用VPS专用四合一脚本[Sing-box-yg](https://github.com/yonggekkk/sing-box-yg)

[](https://github.com/yonggekkk/ArgoSB#7%E5%A6%82%E9%9C%80%E8%A6%81%E5%A4%9A%E6%A0%B7%E7%9A%84%E5%8A%9F%E8%83%BD%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8vps%E4%B8%93%E7%94%A8%E5%9B%9B%E5%90%88%E4%B8%80%E8%84%9A%E6%9C%ACsing-box-yg)

* * *

## 一、自定义变量参数说明：

[](https://github.com/yonggekkk/ArgoSB#%E4%B8%80%E8%87%AA%E5%AE%9A%E4%B9%89%E5%8F%98%E9%87%8F%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)

变量意义| 变量名称| 在变量值""之间填写| 删除变量| 在变量值""之间留空| 变量要求及说明  
---|---|---|---|---|---  
1、启用vless-reality-vision| vlpt| 端口指定| 关闭vless-reality-vision| 端口随机| 必选之一 【xray内核：TCP】  
2、启用vless-xhttp-reality| xhpt| 端口指定| 关闭vless-xhttp-reality| 端口随机| 必选之一 【xray内核：TCP】  
3、启用shadowsocks-2022| sspt| 端口指定| 关闭shadowsocks-2022| 端口随机| 必选之一 【xray内核：TCP】  
4、启用anytls| anpt| 端口指定| 关闭anytls| 端口随机| 必选之一 【singbox内核：TCP】  
5、启用any-reality| arpt| 端口指定| 关闭any-reality| 端口随机| 必选之一 【singbox内核：TCP】  
6、启用vmess-ws| vmpt| 端口指定| 关闭vmess-ws| 端口随机| 必选之一 【xray/singbox内核：TCP】  
7、启用hysteria2| hypt| 端口指定| 关闭hy2| 端口随机| 必选之一 【singbox内核：UDP】  
8、启用tuic| tupt| 端口指定| 关闭tuic| 端口随机| 必选之一 【singbox内核：UDP】  
9、warp开关| warp| 详见下方15种warp出站模式图| 关闭warp| singbox与xray内核协议都启用warp全局V4+V6| 可选，详见下方15种warp出站模式图  
10、argo开关| argo| 填写y| 关闭argo隧道| 关闭argo隧道| 可选，填写y时，vmess变量vmpt必须启用，且固定隧道必须填写vmpt端口  
11、argo固定隧道域名| agn| 托管在CF上的域名| 使用临时隧道| 使用临时隧道| 可选，argo填写y才可激活固定隧道  
12、argo固定隧道token| agk| CF获取的ey开头的token| 使用临时隧道| 使用临时隧道| 可选，argo填写y才可激活固定隧道  
13、uuid密码| uuid| 符合uuid规定格式| 随机生成| 随机生成| 可选  
14、reality域名（仅支持reality类协议）| reym| 符合reality域名规定| amd官网| amd官网| 可选，使用CF类域名时，可用作ProxyIP/客户端地址反代IP（建议高位端口或纯IPV6下使用，以防被扫泄露）  
15、vmess客户端host地址| cdnym| IP解析的CF域名| vmess为直连| vmess为直连| 可选，使用80系CDN或者回源CDN时可设置，否则客户端host地址需手动更改为IP解析的CF域名  
16、切换ipv4或ipv6配置| ippz| 填写4或者6| 自动识别IP配置| 自动识别IP配置| 可选，4表示IPV4配置输出，6表示IPV6配置输出  
17、添加所有节点名称前缀| name| 任意字符| 默认协议名前缀| 默认协议名前缀| 可选  
18、【仅容器类docker】监听端口，网页查询| PORT| 端口指定| 3000| 3000| 可选  
19、【仅容器类docker】启用vless-ws-tls| DOMAIN| 服务器域名| 关闭vless-ws-tls| 关闭vless-ws-tls| 可选，vless-ws-tls可独立存在，uuid变量必须启用  
  
[![a8dd55d7606084a147580c4d292b5d10](https://private-user-images.githubusercontent.com/121604513/481360314-17509155-ad47-43bd-9943-fc7c57b72e42.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDgxMzYwMzE0LTE3NTA5MTU1LWFkNDctNDNiZC05OTQzLWZjN2M1N2I3MmU0Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NzEzM2NkNmRmNjA2MDlhYTgzMTc2YjM3OTljZmI3NzkyYzhiMWExNTQ5YzcxOTQ0ZjY4ODVmY2M5NzlmZDI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.3WBuS-mTEhrN_mwbdp1Ssg_HQfApixykUCFsxHeGPlk)](https://private-user-images.githubusercontent.com/121604513/481360314-17509155-ad47-43bd-9943-fc7c57b72e42.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDgxMzYwMzE0LTE3NTA5MTU1LWFkNDctNDNiZC05OTQzLWZjN2M1N2I3MmU0Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NzEzM2NkNmRmNjA2MDlhYTgzMTc2YjM3OTljZmI3NzkyYzhiMWExNTQ5YzcxOTQ0ZjY4ODVmY2M5NzlmZDI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.3WBuS-mTEhrN_mwbdp1Ssg_HQfApixykUCFsxHeGPlk) [![1b05db3ba201b35f440b139e8f0ee4b1](https://private-user-images.githubusercontent.com/121604513/480348085-dfd9e034-baeb-460e-94e2-32bf88f3112a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDgwMzQ4MDg1LWRmZDllMDM0LWJhZWItNDYwZS05NGUyLTMyYmY4OGYzMTEyYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jNmFmZjAzMmU0OTJkNjJmMzI4NGQyNWQ1MjY2ZTE4Nzc0NjU4M2UxZGI0MTM1YjFkYWNhZTZhNzk2NDVhMTAwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2m2OdFVqWCZGe1-GiFdIGiwB9XhljwzqsRXMfD7Ou80)](https://private-user-images.githubusercontent.com/121604513/480348085-dfd9e034-baeb-460e-94e2-32bf88f3112a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDgwMzQ4MDg1LWRmZDllMDM0LWJhZWItNDYwZS05NGUyLTMyYmY4OGYzMTEyYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jNmFmZjAzMmU0OTJkNjJmMzI4NGQyNWQ1MjY2ZTE4Nzc0NjU4M2UxZGI0MTM1YjFkYWNhZTZhNzk2NDVhMTAwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2m2OdFVqWCZGe1-GiFdIGiwB9XhljwzqsRXMfD7Ou80) [![57d7a7f615b225d40f882702b2a668be](https://private-user-images.githubusercontent.com/121604513/482492411-08b6bf37-71d3-472f-97f4-56f58569055d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDgyNDkyNDExLTA4YjZiZjM3LTcxZDMtNDcyZi05N2Y0LTU2ZjU4NTY5MDU1ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zZDkxMzZmN2Y1ZDk3NzhkMzg2YjA1NDJiMmU5MWE1Njg5ODYzNzAwZjgzYmVmNTUzN2VhYzRjODFmMjYwODg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Gb3tgDnVD_aef5omLVHUPgKbbmGB9qYd7eejqBYXReM)](https://private-user-images.githubusercontent.com/121604513/482492411-08b6bf37-71d3-472f-97f4-56f58569055d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDgyNDkyNDExLTA4YjZiZjM3LTcxZDMtNDcyZi05N2Y0LTU2ZjU4NTY5MDU1ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zZDkxMzZmN2Y1ZDk3NzhkMzg2YjA1NDJiMmU5MWE1Njg5ODYzNzAwZjgzYmVmNTUzN2VhYzRjODFmMjYwODg0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Gb3tgDnVD_aef5omLVHUPgKbbmGB9qYd7eejqBYXReM)

* * *

## 二、SSH一键变量脚本模版说明：

[](https://github.com/yonggekkk/ArgoSB#%E4%BA%8Cssh%E4%B8%80%E9%94%AE%E5%8F%98%E9%87%8F%E8%84%9A%E6%9C%AC%E6%A8%A1%E7%89%88%E8%AF%B4%E6%98%8E)

### 脚本以 `变量名称="变量值"的单个或多个组合 + 主脚本` 的形式运行

[](https://github.com/yonggekkk/ArgoSB#%E8%84%9A%E6%9C%AC%E4%BB%A5-%E5%8F%98%E9%87%8F%E5%90%8D%E7%A7%B0%E5%8F%98%E9%87%8F%E5%80%BC%E7%9A%84%E5%8D%95%E4%B8%AA%E6%88%96%E5%A4%9A%E4%B8%AA%E7%BB%84%E5%90%88--%E4%B8%BB%E8%84%9A%E6%9C%AC-%E7%9A%84%E5%BD%A2%E5%BC%8F%E8%BF%90%E8%A1%8C)

  * 默认主脚本curl：`bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)`

  * 如报错curl not found 可换用主脚本wget：`bash <(wget -qO- https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh) `

  * 必选其一的协议端口变量：`vmpt=""`、`vmpt="" argo="y"`、`vlpt=""`、`xhpt=""`、`anpt=""`、`arpt=""`、`hypt=""`、`tupt=""`、`sspt=""`

  * 可选的功能类变量：`warp=""`、`uuid=""`、`reym=""`、`cdnym=""`、`argo=""`、`agn=""`、`agk=""`、`ippz=""`、`name=""`

请参考`一、自定义变量参数说明`中变量的作用说明，变量值填写在`" "`之间，变量之间空一格，不用的变量可以删除

* * *

  * ### 模版1：多个任意协议组合运行

[](https://github.com/yonggekkk/ArgoSB#%E6%A8%A1%E7%89%881%E5%A4%9A%E4%B8%AA%E4%BB%BB%E6%84%8F%E5%8D%8F%E8%AE%AE%E7%BB%84%E5%90%88%E8%BF%90%E8%A1%8C)

[code]
    sspt="" vlpt="" vmpt="" hypt="" tupt="" xhpt="" anpt="" arpt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

  * ### 模版2：主流TCP或UDP单个协议运行

[](https://github.com/yonggekkk/ArgoSB#%E6%A8%A1%E7%89%882%E4%B8%BB%E6%B5%81tcp%E6%88%96udp%E5%8D%95%E4%B8%AA%E5%8D%8F%E8%AE%AE%E8%BF%90%E8%A1%8C)

Vless-Reality-Vision协议节点
[code]
    vlpt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Vless-Xhttp-Reality协议节点
[code]
    xhpt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Shadowsocks-2022协议节点
[code]
    sspt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

AnyTLS协议节点
[code]
    anpt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Any-Reality协议节点
[code]
    arpt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Vmess-ws协议节点
[code]
    vmpt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Hysteria2协议节点
[code]
    hypt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Tuic协议节点
[code]
    tupt="" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

  * ### 模版3：开启CDN优选的节点运行

[](https://github.com/yonggekkk/ArgoSB#%E6%A8%A1%E7%89%883%E5%BC%80%E5%90%AFcdn%E4%BC%98%E9%80%89%E7%9A%84%E8%8A%82%E7%82%B9%E8%BF%90%E8%A1%8C)

Argo临时/固定隧道运行优选节点，类似无公网的IDX-Google-VPS容器推荐使用此脚本，快速一键内网穿透获取节点

Argo临时隧道CDN优选节点
[code]
    vmpt="" argo="y" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

Argo固定隧道CDN优选节点，必须填写端口(vmpt)、域名(agn)、token(agk)
[code]
    vmpt="端口" argo="y" agn="解析的CF域名" agk="CF获取的token" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

80系端口、回源端口的CDN优选节点
[code]
    vmpt="80系端口、指定随机端口" cdnym="ip已解析的CF域名" bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/argosb/main/argosb.sh)
    
[/code]

* * *

## 三、多功能SSH快捷方式命令组

[](https://github.com/yonggekkk/ArgoSB#%E4%B8%89%E5%A4%9A%E5%8A%9F%E8%83%BDssh%E5%BF%AB%E6%8D%B7%E6%96%B9%E5%BC%8F%E5%91%BD%E4%BB%A4%E7%BB%84)

#### 说明：首次安装成功后需重连SSH，`agsb 命令`的快捷方式才可生效；如未生效，请使用`主脚本 命令`的快捷方式

[](https://github.com/yonggekkk/ArgoSB#%E8%AF%B4%E6%98%8E%E9%A6%96%E6%AC%A1%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F%E5%90%8E%E9%9C%80%E9%87%8D%E8%BF%9Esshagsb-%E5%91%BD%E4%BB%A4%E7%9A%84%E5%BF%AB%E6%8D%B7%E6%96%B9%E5%BC%8F%E6%89%8D%E5%8F%AF%E7%94%9F%E6%95%88%E5%A6%82%E6%9C%AA%E7%94%9F%E6%95%88%E8%AF%B7%E4%BD%BF%E7%94%A8%E4%B8%BB%E8%84%9A%E6%9C%AC-%E5%91%BD%E4%BB%A4%E7%9A%84%E5%BF%AB%E6%8D%B7%E6%96%B9%E5%BC%8F)

1、查看Argo的固定域名、固定隧道的token、临时域名、当前已安装的节点信息命令：`agsb list` 或者 `主脚本 list`

2、更换代理协议变量组命令：`自定义各种协议变量组 agsb rep` 或者 `自定义各种协议变量组 主脚本 rep`

3、更新脚本命令：`原已安装的自定义各种协议变量组 主脚本 rep`

4、重启脚本命令：`agsb res` 或者 `主脚本 res`

5、卸载脚本命令：`agsb del` 或者 `主脚本 del`

6、临时切换IPV4/IPV6节点配置 (双栈VPS专享)：

显示IPV4节点配置：`ippz=4 agsb list`或者`ippz=4 主脚本 list`

显示IPV6节点配置：`ippz=6 agsb list`或者`ippz=6 主脚本 list`

* * *

#### 相关教程可参考[甬哥博客](https://ygkkk.blogspot.com/2025/08/argosb.html)，视频教程如下：

[](https://github.com/yonggekkk/ArgoSB#%E7%9B%B8%E5%85%B3%E6%95%99%E7%A8%8B%E5%8F%AF%E5%8F%82%E8%80%83%E7%94%AC%E5%93%A5%E5%8D%9A%E5%AE%A2%E8%A7%86%E9%A2%91%E6%95%99%E7%A8%8B%E5%A6%82%E4%B8%8B)

更新中……

最新推荐：[ArgoSB一键无交互小钢炮脚本💣（三）：内置15种WARP出站组合，轻松替代独立的WARP脚本](https://youtu.be/iywjT8fIka4)

[ArgoSB一键无交互小钢炮脚本💣（二）：代理节点的IP、端口被封依旧可用！ArgoSB脚本套CDN优选4大方案教程](https://youtu.be/RnUT1CNbCr8)

[ArgoSB一键无交互小钢炮脚本💣（一）：VPS/nat VPS在主协议下的应用；仅按一次回车，多协议自由搭配](https://youtu.be/CiXmttY7mhw)

[Clawcloud爪云、IDX Google VPS的福音：解决服务器IP访问困扰！Argosb脚本新增WARP出站功能，轻松更换落地IP为Cloudflare WARP IP](https://youtu.be/HO_XLBmIYJw)

[Claw.cloud免费VPS搭建代理最终教程（五）：ArgoSB脚本docker镜像更新支持AnyTLS、Xhttp-Reality](https://youtu.be/-mhZIhHRyno)

[Claw.cloud免费VPS搭建代理最终教程（四）：最低仅1美分，4套价格+7组协议的套餐组合任你选；查看节点、重启升级、更换IP、更改配置的操作说明](https://youtu.be/xOQV_E1-C84)

[Claw.cloud免费VPS搭建代理最终教程（三）：ArgoSB全能docker镜像发布，支持网页实时更新节点；TCP/UDP直连协议设置客户端"CDN"免墙域名](https://youtu.be/JEXyj9UoMzU)

[Claw.cloud免费VPS搭建代理最终教程（二）：最低仅需2美分；支持Argo | Reality | Vmess | Hysteria2 | Tuic代理协议任意组合](https://youtu.be/NnuMgnJqon8)

[Claw.cloud免费VPS搭建代理最终教程（一）：全网最简单 | 两大无交互回车脚本 | 套CDN优选IP | workers反代 | ArgoSB隧道搭建](https://youtu.be/Esofirx8xrE)

[IDX Google免费VPS代理搭建教程（三）：NIX容器最新工作区方式搭建Argo免费节点 | 一次回车搞定一切 | Argo固定隧道一键复活](https://youtu.be/0I5eI1KKx08)

[IDX Google免费VPS代理搭建教程（四）：支持重置后自动启动代理节点功能 | 最简单的保活方法](https://youtu.be/EGrz6Wvevqc)

* * *

### 交流平台：[甬哥博客地址](https://ygkkk.blogspot.com/)、[甬哥YouTube频道](https://www.youtube.com/@ygkkk)、[甬哥TG电报群组](https://t.me/+jZHc6-A-1QQ5ZGVl)、[甬哥TG电报频道](https://t.me/+DkC9ZZUgEFQzMTZl)

[](https://github.com/yonggekkk/ArgoSB#%E4%BA%A4%E6%B5%81%E5%B9%B3%E5%8F%B0%E7%94%AC%E5%93%A5%E5%8D%9A%E5%AE%A2%E5%9C%B0%E5%9D%80%E7%94%AC%E5%93%A5youtube%E9%A2%91%E9%81%93%E7%94%AC%E5%93%A5tg%E7%94%B5%E6%8A%A5%E7%BE%A4%E7%BB%84%E7%94%AC%E5%93%A5tg%E7%94%B5%E6%8A%A5%E9%A2%91%E9%81%93)

* * *

### 感谢支持！微信打赏甬哥侃侃侃ygkkk

[](https://github.com/yonggekkk/ArgoSB#%E6%84%9F%E8%B0%A2%E6%94%AF%E6%8C%81%E5%BE%AE%E4%BF%A1%E6%89%93%E8%B5%8F%E7%94%AC%E5%93%A5%E4%BE%83%E4%BE%83%E4%BE%83ygkkk)

[![41440820a366deeb8109db5610313a1](https://private-user-images.githubusercontent.com/121604513/437250168-e5b1f2c0-bd2c-4b8f-8cda-034d3c8ef73f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDM3MjUwMTY4LWU1YjFmMmMwLWJkMmMtNGI4Zi04Y2RhLTAzNGQzYzhlZjczZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNDliNWMyMzg4NDg4OWJlNTM2ZDk1ZThkMmE1OTEyNTExZDgzMzg4ZjAzODIwZjNiYjIxNzg2MTJlNThmOWNlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2sllwmEPxCOJyOH8QdXnPGHDc3QftBbiNNCauxZdSmo)](https://private-user-images.githubusercontent.com/121604513/437250168-e5b1f2c0-bd2c-4b8f-8cda-034d3c8ef73f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY1MzkzMTYsIm5iZiI6MTc1NjUzOTAxNiwicGF0aCI6Ii8xMjE2MDQ1MTMvNDM3MjUwMTY4LWU1YjFmMmMwLWJkMmMtNGI4Zi04Y2RhLTAzNGQzYzhlZjczZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgzMFQwNzMwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNDliNWMyMzg4NDg4OWJlNTM2ZDk1ZThkMmE1OTEyNTExZDgzMzg4ZjAzODIwZjNiYjIxNzg2MTJlNThmOWNlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2sllwmEPxCOJyOH8QdXnPGHDc3QftBbiNNCauxZdSmo)
