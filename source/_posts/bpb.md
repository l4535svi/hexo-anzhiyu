---
title: 免费代理面板，BPB面板更新，支持大部分代理软件
date: '2024-10-04 12:00:00'
cover: /img/covers/bpb.jpg
tags:
- 节点分享
categories:
- 节点分享
description: 步骤 1：Fork GitHub 项目到你的账户 打开浏览器并前往项目的 GitHub 仓库页面 https://github.com/bia-pain-bache/BPB-Worker-Panel 。 在右上角找到并点击 Fork 按钮，将这个项目 Fork 到你自己的 Git
---
### 步骤 1：Fork GitHub 项目到你的账户

  1. 打开浏览器并前往项目的 GitHub 仓库页面 [https://github.com/bia-pain-bache/BPB-Worker-Panel](https://github.com/bia-pain-bache/BPB-Worker-Panel)。

  2. 在右上角找到并点击 **Fork**  按钮，将这个项目 Fork 到你自己的 GitHub 账户。

  3. 进入你 GitHub 账户中的 Fork 后的仓库页面。

### 步骤 2：在 Cloudflare 中连接 GitHub 项目

  1. 登录你的 Cloudflare 账户。

  2. 在仪表盘中，点击左侧菜单中的 **Pages** 。

  3. 点击 **Create a project**  按钮。

  4. 选择 **Connect to GitHub** ，并确保你已经授予 Cloudflare 访问你 GitHub 仓库的权限。

  5. 在仓库列表中找到你 Fork 的 `BPB-Worker-Panel` 仓库并选择它。

  6. 点击 **Begin setup** ，然后根据提示配置 Cloudflare Pages 的项目设置：

     * **项目名称** ：可以选择自定义，或者使用默认的仓库名称。

     * **构建设置** ：保持默认设置，除非你有特定要求。

     * **分支选择** ：通常选择 `main` 分支。

  7. 配置完成后，点击 **Save and Deploy** ，开始部署。

### 步骤 3：创建 KV 并绑定到 Cloudflare 项目

  1. 在 Cloudflare 仪表盘中，点击左侧菜单中的 **Workers** 。

  2. 选择 **KV** （Key-Value）存储选项，然后点击 **Create a Namespace** 。

  3. 在弹出框中，为你的 Namespace 命名为 `bpb`。这个名称必须与项目代码中的 KV 命名匹配。

  4. 创建完成后，返回到你的 `BPB-Worker-Panel` Pages 项目设置。

  5. 找到 **KV Bindings**  部分，点击 **Add Binding** 。

  6. 在 **Variable name**  中填写 `bpb`，在 **Namespace**  中选择刚刚创建的 `bpb` KV。

  7. 保存你的更改。

### 步骤 4：重新部署项目

  1. 当所有设置完成后，返回到 Cloudflare Pages 项目的仪表盘。

  2. 点击 **Deploy**  或 **Redeploy** ，重新部署项目。

此步骤会触发 Cloudflare 的构建和部署流程，将你的项目部署到 Pages 上，同时连接了 KV 存储。

### 验证项目是否正常运行

  1. 部署完成后，你会获得一个 URL，访问该 URL 查看项目是否正常工作。

  2. 确保页面正常加载，并且能够与 KV 存储交互。
