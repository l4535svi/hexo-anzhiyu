---
title: 来！让我们用Vercel来分享你的OneDrive！
date: '2025-11-29 12:00:00'
cover: https://picsum.photos/seed/vercelonedrive/800/450
tags:
- Azure薅羊毛
categories:
- Azure薅羊毛
description: 正式开始 你可以根据 前文 免费拿E3，得到至高免费5T的OneDrive存储空间，也可以用你个人永久免费的5G空间，都可以！ 前往 高级 - OneDrive Vercel Index 拿到 clientid 和 secret 前往该页面，点击快速部署 onedrive-ind
---
[![](https://blogger.googleusercontent.com/img/a/AVvXsEhv9bAAFkTao58jdWE0j_Zm75gCe1WTbrMy1W_WPadBhn9QZlaPmjWavA3sGYrYB9Dsfc4J_JNjJ4tRV_114ucsx_3k3i40vuY3bXDDWuLv0FIKnyNj4ctafZ2hym63yi-FEeb2XQBXI6Cov8hrzxr_ad9sN6rs9kHBMI-QwI4f9YmVfSc_sehCiw-f61ap=w523-h220)](https://blogger.googleusercontent.com/img/a/AVvXsEhv9bAAFkTao58jdWE0j_Zm75gCe1WTbrMy1W_WPadBhn9QZlaPmjWavA3sGYrYB9Dsfc4J_JNjJ4tRV_114ucsx_3k3i40vuY3bXDDWuLv0FIKnyNj4ctafZ2hym63yi-FEeb2XQBXI6Cov8hrzxr_ad9sN6rs9kHBMI-QwI4f9YmVfSc_sehCiw-f61ap)

# 正式开始

你可以根据[前文](https://2x.nz/posts/ms-e3/)免费拿E3，得到至高免费5T的OneDrive存储空间，也可以用你个人永久免费的5G空间，都可以！

前往 [高级 - OneDrive Vercel Index](https://ovi.swo.moe/zh/docs/advanced#%E4%BD%BF%E7%94%A8%E4%BD%A0%E8%87%AA%E5%B7%B1%E7%9A%84-client-id-%E4%B8%8E-secret) 拿到 clientid 和 secret

前往该页面，点击快速部署 [onedrive-index/README.zh-CN.md at main · iRedScarf/onedrive-index](https://github.com/iRedScarf/onedrive-index/blob/main/README.zh-CN.md#%E9%83%A8%E7%BD%B2%E5%88%B0vercel)

填写必须的5个环境变量

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjY_G8PBTQ5b3NQOuzWD-NwOxbbb6Eo0yxqqn8Pl6tU9zI0rLp-0cEeVtpIdhKFEBw7yLIXJQ0r_VWO60YLXoejWHhiJovyhxn5BhIz-IVKqDniol3Z4CDqWL1u5EqMyJhr9OqQN43dvKqFkHwu1UBlOFT8JTY83oddkZIJnIbnkkd-98qRm77oMRqEf5PK)](https://blogger.googleusercontent.com/img/a/AVvXsEjY_G8PBTQ5b3NQOuzWD-NwOxbbb6Eo0yxqqn8Pl6tU9zI0rLp-0cEeVtpIdhKFEBw7yLIXJQ0r_VWO60YLXoejWHhiJovyhxn5BhIz-IVKqDniol3Z4CDqWL1u5EqMyJhr9OqQN43dvKqFkHwu1UBlOFT8JTY83oddkZIJnIbnkkd-98qRm77oMRqEf5PK)

  

其中，USER_PRINCIPAL_NAME为类似 [huding@Smartree233.onmicrosoft.com](mailto:huding@Smartree233.onmicrosoft.com) 的电子邮箱，也就是你登陆OneDrive的用户名

Vercel部署完毕后，会报错连不上Redis，因为我们还没创建和绑定，现在我们开始做

前往 <https://vercel.com/integrations/upstash> 点击 Install

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiZfkm7LsFZfPNYosGFphKiH0XyP8n9tBOBpqR3t39Vel33u5qvZw3DoORrJKGa2lhiIZDzsfTiTAH6f5cZ9z9WRaRc-pU-fxB6RulhDxs3b1zdC6VmTCeyBNMYauAaL2jgAqjtM4GEEx424cVQgsBkIWDCV-SMFABjWWoDFbmtnH28TxOZ73zXFRPZtOwm)](https://blogger.googleusercontent.com/img/a/AVvXsEiZfkm7LsFZfPNYosGFphKiH0XyP8n9tBOBpqR3t39Vel33u5qvZw3DoORrJKGa2lhiIZDzsfTiTAH6f5cZ9z9WRaRc-pU-fxB6RulhDxs3b1zdC6VmTCeyBNMYauAaL2jgAqjtM4GEEx424cVQgsBkIWDCV-SMFABjWWoDFbmtnH28TxOZ73zXFRPZtOwm)

  
  

来到Vercel的环境变量页面，这就是绑定成功了

随便打开一个部署，点击 Redeploy 重新部署，就能成功连接数据库了

接下来访问你的项目域名，进入OneDrive-Index的引导，需要打开微软的一个链接授权

授权后会重定向到一个localhost的域名，复制该URI，粘贴回OneDrive-Index即可（仅需一次）

成功部署！

这里有些高级设置，你可能需要了解一下。

## [使用你自己的 client id 与 secret](https://ovi.swo.moe/zh/docs/advanced#%E4%BD%BF%E7%94%A8%E4%BD%A0%E8%87%AA%E5%B7%B1%E7%9A%84-client-id-%E4%B8%8E-secret)

如果你的账户没有管理权限，那么你就无法使用项目提供的 `clientId` 与 `clientSecret`。这个情况下，你就要生成你自己的 client id 与 secret 了。

### [注册一个应用程序](https://ovi.swo.moe/zh/docs/advanced#%E6%B3%A8%E5%86%8C%E4%B8%80%E4%B8%AA%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F)

打开以下链接：

  * [Microsoft Azure App registrations](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)（ OneDrive 国际版、企业版与教育版，E5 订阅专用）
  * [Microsoft Azure.cn App registrations](https://portal.azure.cn/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)（OneDrive 世纪互联专用）

创建一个应用程序：

  1. 登入你的微软账户，点击 _New registration_ 。

  2. 输入一个名字，例如 my-onedrive-vercel-index。

  3. 将 _Supported account types_  设置为：
[code]Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)
         
[/code]

OneDrive 世纪互联用户设置为 - 任何组织目录（任何 Azure AD 目录 - 多租户）中的帐户。

  4. 将 _Redirect URI (optional)_  设置为 `Web`（在下拉菜单里）以及 `http://localhost`。

  5. 点击注册。

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272048%27%20height=%271420%27/%3e)  

### [获取你的 client id 与 secret](https://ovi.swo.moe/zh/docs/advanced#%E8%8E%B7%E5%8F%96%E4%BD%A0%E7%9A%84-client-id-%E4%B8%8E-secret)

你的应用 (client) ID 就是 `api.config.js` 里的 `clientId` ，它应该出现在 _Overview_  > _Essentials_ 。

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272100%27%20height=%27654%27/%3e)![Your application \(client\) ID](https://ovi.swo.moe/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fget-client-id.7f11595f.png&w=3840&q=75)

你的 client secret 需要手动获取

  1. 点击 _Certificates & secrets_。
  2. 点击 _New client secret_ 。
  3. 创建一个新 secret ，描述为 `client_secret`。
  4. 将 _Expires_  设置为 `Custom`。
  5. 将 _Start_  与 _End_  设置为能设置的最长时间。

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272398%27%20height=%271488%27/%3e)![Generate a client secret](https://ovi.swo.moe/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcreate-client-secret.3c3eb9c9.png&w=3840&q=75)

最后，点击 _Add_  ，然后复制 client_secret 的值并妥善保管。（只有一次复制机会）

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271846%27%20height=%27416%27/%3e)![Copy your client secret](https://ovi.swo.moe/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcopy-your-client-secret.8590835d.png&w=3840&q=75)

### [修改 API 权限](https://ovi.swo.moe/zh/docs/advanced#%E4%BF%AE%E6%94%B9-api-%E6%9D%83%E9%99%90)

Microsoft Graph API 可以设置 API 范围，我们只需要以下三个（ `api.config.js` 里要求的）：
[code]
    user.read files.read.all offline_access
    
[/code]

点击 _API permissions_ ，再点击 _Microsoft Graph_ ，再点击 _Delegated permissions_ ，然后搜索：

  * User.Read（这应该一开始就勾上了）
  * Files.Read.All
  * offline_access

选择全部三个并点击 _Add permissions_ 。

![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271700%27%20height=%271862%27/%3e)![Modify Microsoft Graph API permissions](https://ovi.swo.moe/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadd-required-permissions.c28bba24.png&w=3840&q=75)

现在，你就准备好你自己的 `clientId` 与 `clientSecret` 了。

### [修改 `api.config.js`](https://ovi.swo.moe/zh/docs/advanced#%E4%BF%AE%E6%94%B9-apiconfigjs)

你可以直接将 `clientId` 修改为你自己的 `clientId`。

但是，client secret 需要保密，你需要在下面进行 AES 加密：

Obfuscate your client secret 👇

Your client secret:

Your obfuscated client secret:

填写 client secret 后，你应该得到一个长得像这样的字符串：
[code]
    U2FsdGVkX1830zo3/pFDqaBCVBb37iLw3WnBDWGF9GIB2f4apzv0roemp8Y+iIxI3Ih5ecyukqELQEGzZlYiWg==
    
[/code]

将它替换到 `obfuscatedClientSecret` 里。

如果你修改了 `redirectUri` 为其他值，你也要在 `api.config.js` 里设置好。

详情请参考 [关于使用自己的 secret 进行 AES 加密方式的小白解决办法](https://github.com/spencerwooo/onedrive-vercel-index/discussions/234)。（重要必须加密才能成功）、

可能很多像我一样的小白想使用自己的secret，但又不知道如何加密。我折腾了很久才摸索出来，使用这个在线加密工具 <https://www.dute.org/aes> ，原始文本填入自己的secret，秘钥填入`onedrive-vercel-index`，`加/解密模式`选择`CBC (Cipher Block Chaining, Default)`，点击`AES 加密`就可以了。我也是这样将作者内置的secret反向解密出来的，加密方式试了一遍又一遍~
