---
title: fuwari博客(研究2天终于研究成功)
date: '2025-07-23 12:00:00'
cover: /img/covers/fuwari2.jpg
tags:
- 建站
categories:
- 建站
description: 不是你网络的问题，也不是 Stylus 包被彻底下架，而是刚刚发生了一个 安全事件 ：npm 因为发现 Stylus 包中存在恶意代码，于 2025 年 7 月 23 日凌晨左右 （UTC 时间）将所有 Stylus 版本从注册表中移除了，并发布了一个占位版本 0.0.1‑sec
---
[![](https://blogger.googleusercontent.com/img/a/AVvXsEh93-HES9DD989seIfF-mmm7QIxo5CtMzAcCV3AhZtG6y0v4_kZud3df3cRT3iEd772vOuJsU_PLoEDhI_1sM-v6O09catOve37S8R44PwTSu8ELjfjbYDLPWToA8c--nfpFBiBvc1ptDTk7E6cPmWRiIZetHVu7_M_bCAE4KmgMlvjzNRxP-s6SA95C9MK=w600-h232)](https://blogger.googleusercontent.com/img/a/AVvXsEh93-HES9DD989seIfF-mmm7QIxo5CtMzAcCV3AhZtG6y0v4_kZud3df3cRT3iEd772vOuJsU_PLoEDhI_1sM-v6O09catOve37S8R44PwTSu8ELjfjbYDLPWToA8c--nfpFBiBvc1ptDTk7E6cPmWRiIZetHVu7_M_bCAE4KmgMlvjzNRxP-s6SA95C9MK)

不是你网络的问题，也不是 Stylus 包被彻底下架，而是刚刚发生了一个**安全事件** ：npm 因为发现 Stylus 包中存在恶意代码，于 **2025 年 7 月 23 日凌晨左右** （UTC 时间）将所有 Stylus 版本从注册表中移除了，并发布了一个占位版本 `0.0.1‑security` 来阻止继续安装 [Hacker News+1npm+1](https://news.ycombinator.com/item?id=44655660&utm_source=chatgpt.com)。

import type {

    ExpressiveCodeConfig,

    LicenseConfig,

    NavBarConfig,

    ProfileConfig,

    SiteConfig,

} from "./types/config";

import { LinkPreset } from "./types/config";

  

export const siteConfig: SiteConfig = {

    title: "码境Code Realm",

    subtitle: "爱你一生",

    lang: "zh_CN", // 'en', 'zh_CN', 'zh_TW', 'ja', 'ko', 'es', 'th'

    themeColor: {

        hue: 250, // Default hue for the theme color, from 0 to 360. e.g. red: 0, teal: 200, cyan: 250, pink: 345

        fixed: false, // Hide the theme color picker for visitors

    },

    banner: {

        enable: true,

        src: "https://img.xn--ohqu9y07ujpb.dpdns.org/file/1754446851075_banner.DBvCl2Qg_ZBX2hI.webp", // Relative to the /src directory. Relative to the /public directory if it starts with '/'

        position: "center", // Equivalent to object-position, only supports 'top', 'center', 'bottom'. 'center' by default

        credit: {

            enable: true, // Display the credit text of the banner image

            text: "Pixiv @chokei", // Credit text to be displayed

            url: "https://www.pixiv.net/users/175341486", // (Optional) URL link to the original artwork or artist's page

        },

    },

    toc: {

        enable: true, // Display the table of contents on the right side of the post

        depth: 2, // Maximum heading depth to show in the table, from 1 to 3

    },

    favicon: [

        {

            src: "https://e5bf5984.cloudflare-imgbed-csc.pages.dev/file/1753414862012_0_b67f5a87763bc15d58d147d89ff8823c_1753414687712.webp", // Path of the favicon, relative to the /public directory

            theme: "light", // (Optional) Either 'light' or 'dark', set only if you have different favicons for light and dark mode

            sizes: "32x32", // (Optional) Size of the favicon, set only if you have favicons of different sizes

        },

    ],

};

  

export const navBarConfig: NavBarConfig = {

    links: [

        LinkPreset.Home,

        LinkPreset.Archive,

        LinkPreset.About,

        {

            name: "友链",

            url: "https://github.com/saicaca/fuwari", // Internal links should not include the base path, as it is automatically added

            external: false, // Show an external link icon and will open in a new tab

        },

        {

            name: "统计",

            url: "https://cloud.umami.is/share/azr29Ow6KU9YfL2U/kejidao.ggff.net", // Internal links should not include the base path, as it is automatically added

            external: true, // Show an external link icon and will open in a new tab

        },

        {

            name: "GitHub",

            url: "https://github.com/saicaca/fuwari", // Internal links should not include the base path, as it is automatically added

            external: true, // Show an external link icon and will open in a new tab

        },

    ],

};

  

export const profileConfig: ProfileConfig = {

    avatar: "assets/images/demo-tx.jpg", // Relative to the /src directory. Relative to the /public directory if it starts with '/'

    name: "码境Code Realm",

    bio: "Protect What You Love./爱你所爱！",

    links: [

        {

            name: "YouTube",

            icon: "fa6-brands:youtube", // Visit https://icones.js.org/ for icon codes

            // You will need to install the corresponding icon set if it's not already included

            // `pnpm add @iconify-json/<icon-set-name>`

            url: "https://www.youtube.com/@xs.903",

        },

        {

            name: "QQ",

            icon: "fa6-brands:qq",

            url: "https://wpa.qq.com/msgrd?v=3&uin=584524731&site=qq&menu=yes",

        },

        {

            name: "GitHub",

            icon: "fa6-brands:github",

            url: "https://github.com/wangai14/fuwari",

        },

        {

            name: "B站",

            icon: "fa6-brands:bilibili",

            url: "https://space.bilibili.com/485156002?spm_id_from=333.1007.0.0",

        },

    ],

};

  

export const licenseConfig: LicenseConfig = {

    enable: true,

    name: "CC BY-NC-SA 4.0",

    url: "https://creativecommons.org/licenses/by-nc-sa/4.0/",

};

  

export const expressiveCodeConfig: ExpressiveCodeConfig = {

    // Note: Some styles (such as background color) are being overridden, see the astro.config.mjs file.

    // Please select a dark theme, as this blog theme currently only supports dark background color

    theme: "github-dark",

};

  

  

### ✅ 2. 直接改成 GitHub 的未受污染源码

项目正在与 npm 官方沟通恢复，你可以暂时从 GitHub 源安装：
[code] 
    json
    
    复制编辑
    
    "overrides": {
      "stylus": "github:stylus/stylus#0.64.0"
    }
    
[/code]

这会从最新的官方源码安装 Stylus，而不是经过 npm 注册表 [Hacker News](https://news.ycombinator.com/item?id=44655660&utm_source=chatgpt.com)[Yarn](https://classic.yarnpkg.com/en/package/jstransformer-stylus?utm_source=chatgpt.com)。

## ✅ 1. 修改 `package.json`

请按照以下方法将 `stylus` 的依赖改为 GitHub 源代码安装：

### 👉 找到 `package.json` 中的 stylus 依赖，替换成这样：
[code]
    json
    
    复制编辑
    
    "dependencies": {
      "stylus": "github:stylus/stylus#master"
    }
    
[/code]

如果它是在 `devDependencies` 中，也一样替换。

* * *

## ✅ 2. 执行安装命令

确保你已经安装 `git`，然后运行：
[code]
    bash
    
    复制编辑
    
    npm install
    
[/code]

它会直接从 GitHub 上克隆并构建 Stylus 源码。

* * *

## ✅ 3. 可选：锁定某个提交（非 master）

如果你不想用 `master`（主分支可能变动），可以锁定到具体发布版本：
[code]
    json
    
    复制编辑
    
    "stylus": "github:stylus/stylus#0.54.8"
    
[/code]

你可以去这个页面查看所有发布 tag：  
<https://github.com/stylus/stylus/tags>

* * *

## 💡 示例 package.json 段落（完整参考）
[code]
    json
    
    复制编辑
    
    {
      "name": "fuwari",
      "version": "1.0.0",
      "dependencies": {
        "stylus": "github:stylus/stylus#0.54.8",
        "some-other-package": "^1.2.3"
      }
    }
    
[/code]

* * *

## ❗️注意事项

  * 你需要已安装 Git 命令行（否则 npm 无法拉取 GitHub 仓库）

  * 使用 GitHub 源安装的包不受 npm 自动审计保护，注意安全性

  * 若部署到 Vercel 或 CI/CD 平台，确保它们也能访问 GitHub（否则构建会失败）
