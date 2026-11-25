---
title: Myurls-Railway
date: '2022-04-26 12:00:00'
tags:
- 建站
categories:
- 建站
description: 在 Railway 上运行 Myurls 短网址程序 Installation 部署 通过上方链接一键部署到Railway，并填入以下参数 参数说明： DOMAIN - 短链接域名，必填项，不需要添加https:// (如 abc.com) TTL - 短链接有效期，单位(天)，
---
在 [Railway](https://railway.app/) 上运行 [Myurls](https://github.com/CareyWang/MyUrls) 短网址程序

## [](https://github.com/King-stark/Myurls-Railway#installation)Installation

### [](https://github.com/King-stark/Myurls-Railway#%E9%83%A8%E7%BD%B2)部署

[![Deploy on Railway](https://camo.githubusercontent.com/081df3dd8cff37aab35044727b02b94a8e948052487a8c6253e190f5940d776d/68747470733a2f2f7261696c7761792e6170702f627574746f6e2e737667)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fpzcn%2FMyurls-Railway&plugins=redis&envs=ENV_DOMAIN%2CENV_TTL%2CPORT&ENV_DOMAINDesc=Your+domain.&ENV_TTLDesc=Short+link+validity+period+%28day%29&PORTDesc=DO+NOT+CHANGE&ENV_TTLDefault=180&PORTDefault=80)

通过上方链接一键部署到Railway，并填入以下参数

参数说明：

  * `DOMAIN` \- 短链接域名，必填项，不需要添加https:// (如 abc.com)
  * `TTL` \- 短链接有效期，单位(天)，默认180天 (default 180)
  * `PORT` \- 端口，保持80，请勿修改

### [](https://github.com/King-stark/Myurls-Railway#%E6%B7%BB%E5%8A%A0%E5%9F%9F%E5%90%8D)添加域名

在Cloudflare中添加域名，并配置SSL/TLS为完全及以上，并在Railway中接入该域名，参考[官方文档](https://docs.railway.app/deploy/exposing-your-app#lets-encrypt-ssl-certificates)。

## [](https://github.com/King-stark/Myurls-Railway#contributing)Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## [](https://github.com/King-stark/Myurls-Railway#license)License

[MIT](https://choosealicense.com/licenses/mit/)
