---
title: 【Hexo博客系列】No.1 搭建Hexo博客，快速简洁高效，零成本搭建个人博客：Hexo + GitHub Pages +
date: '2025-04-07 12:00:00'
tags:
- 建站
categories:
- 建站
description: 搭建Hexo博客，快速简洁高效，零成本搭建个人博客：Hexo + GitHub Pages + Cloudflare Pages 完整指南 本文详细介绍了如何使用Hexo框架搭建一个个人博客，并将其部署到GitHub Pages和Cloudflare Pages上。主要内容包括：
---
# [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#%E6%90%AD%E5%BB%BAHexo%E5%8D%9A%E5%AE%A2%EF%BC%8C%E5%BF%AB%E9%80%9F%E7%AE%80%E6%B4%81%E9%AB%98%E6%95%88%EF%BC%8C%E9%9B%B6%E6%88%90%E6%9C%AC%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%EF%BC%9AHexo-GitHub-Pages-Cloudflare-Pages-%E5%AE%8C%E6%95%B4%E6%8C%87%E5%8D%97 "搭建Hexo博客，快速简洁高效，零成本搭建个人博客：Hexo + GitHub Pages + Cloudflare Pages 完整指南")搭建Hexo博客，快速简洁高效，零成本搭建个人博客：Hexo + GitHub Pages + Cloudflare Pages 完整指南

本文详细介绍了如何使用Hexo框架搭建一个个人博客，并将其部署到GitHub Pages和Cloudflare Pages上。主要内容包括：

  * 环境准备：安装Node.js和Git
  * 配置Git和GitHub：设置SSH密钥，创建GitHub仓库
  * 初始化Hexo项目：安装Hexo，创建新博客
  * 部署到GitHub Pages：配置部署设置，推送静态文件
  * 部署到Cloudflare Pages：连接GitHub仓库，自动部署
  * 基本使用方法：创建新文章，本地预览，发布更新

这个教程适合那些想要快速搭建个人博客，但又不想花费太多成本的人。通过使用Hexo、GitHub和Cloudflare的免费服务，您可以轻松创建一个高效、简洁的博客网站。

* * *

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#1-%E4%BA%8B%E5%89%8D%E5%87%86%E5%A4%87 "1.事前准备")1.事前准备

  1. 域名（非必须，你也可以使用免费域名，或者`GitHub.io`或`Pages.dev`分配的域名也可以）
  2. [GitHub](https://github.com/)（必须，你需要注册一个GitHub帐号）
  3. [Cloudflare](https://dash.cloudflare.com/)（非必须，你需要注册一个Cloudflare帐号，这样你就可以将博客部署在CF的CDN里加速，但是你也可以直接使用`GitHub.io`分配的域名）

* * *

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#2-%E8%BD%AF%E4%BB%B6%E6%94%AF%E6%8C%81 "2.软件支持")2.软件支持

  1. [Node](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#2-1-%E5%AE%89%E8%A3%85-Node)（必须）
  2. [Git](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#2-2-%E5%AE%89%E8%A3%85-Git)（必须）
  3. [VSCode](https://code.visualstudio.com/)（非必须，这是一款轻量型的代码编辑器，可以帮助你养成一个很好的编程习惯）

### [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#2-1-%E5%AE%89%E8%A3%85-Node "2.1.安装 Node")2.1.安装 Node

  1. 打开Node官网，下载和自己系统相配的Node的安装程序，否则会出现安装问题。下载地址：<https://nodejs.org/en>
  2. 下载后安装，安装的目录可以使用默认目录`C:/Program Files/nodejs/`
  3. 安装完成后，检查是否安装成功。在键盘按下win + R键，输入CMD，然后回车，打开CMD窗口，执行`node -v`命令，看到版本信息，则说明安装成功。  
[![2.1.3.安装 Node](https://img.090227.xyz/file/5ca2f549a4489064d3444.jpg)](https://img.090227.xyz/file/5ca2f549a4489064d3444.jpg)
  4. 修改npm源。npm下载各种模块，默认是从国处服务器下载，速度较慢，建议配置成华为云镜像源。打开CMD窗口，运行如下命令:

CMD
[code]1  
         
[/code]

| 
[code]npm config set registry https://mirrors.huaweicloud.com/repository/npm/  
         
[/code]  
  
---|---  

### [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#2-2-%E5%AE%89%E8%A3%85-Git "2.2.安装 Git")2.2.安装 Git

  1. 进入官网下载适合你当前系统的 Git：<https://git-scm.com/downloads>  
[![2.2.1.安装 Git](https://img.090227.xyz/file/14b9fdf14c49320e531fb.jpg)](https://img.090227.xyz/file/14b9fdf14c49320e531fb.jpg)
  2. 下载后傻瓜式安装Git即可，安装的目录最好使用默认目录`C:/Program Files/Git`
  3. 点击电脑左下角开始即可看见`Git CMD`、`Git Bash`、`Git GUI`。
     * `Git CMD` 是windows 命令行的指令风格
     * `Git Bash` 是linux系统的指令风格（建议使用）
     * `Git GUI`是图形化界面（新手学习不建议使用）

* * *

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#3-%E9%85%8D%E7%BD%AE-Git-%E5%AF%86%E9%92%A5%E5%B9%B6%E8%BF%9E%E6%8E%A5%E8%87%B3-Github "3.配置 Git 密钥并连接至 Github")3.配置 Git 密钥并连接至 Github

常用 Git 命令

SHELL
[code]
    1  
    2  
    3  
    
[/code]

| 
[code]
    git config -l  //查看所有配置  
    git config --system --list //查看系统配置  
    git config --global --list //查看用户（全局）配置  
    
[/code]  
  
---|---  
  
[![启动Git](https://img.090227.xyz/file/f403664b22ad3488a5fb4.jpg)](https://img.090227.xyz/file/f403664b22ad3488a5fb4.jpg)

### [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#3-1-%E9%85%8D%E7%BD%AE%E7%94%A8%E6%88%B7%E5%90%8D%E5%92%8C%E9%82%AE%E7%AE%B1 "3.1. 配置用户名和邮箱")3.1. 配置用户名和邮箱

SHELL
[code]
    1  
    2  
    
[/code]

| 
[code]
    git config --global user.name "你的用户名"  
    git config --global user.email "你的邮箱"  
    
[/code]  
  
---|---  
  
通过`git config -l` 检查是否配置成功。  
[![3.1. 配置用户名和邮箱](https://img.090227.xyz/file/67dca39142021e2214e2b.jpg)](https://img.090227.xyz/file/67dca39142021e2214e2b.jpg)

### [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#3-2-%E9%85%8D%E7%BD%AE%E5%85%AC%E9%92%A5%E8%BF%9E%E6%8E%A5Github "3.2. 配置公钥连接Github")3.2. 配置公钥连接Github

  1. 执行以下命令生成ssh公钥，此公钥用于你的计算机连接Github

SHELL
[code]1  
         
[/code]

| 
[code]ssh-keygen -t rsa -C "你的邮箱"  
         
[/code]  
  
---|---  
提示`Enter file in which to save the key`直接一路回车即可，新手小白不推荐设置密钥  
[![3.2.1.1](https://img.090227.xyz/file/45d70737c64caeb4393ad.jpg)](https://img.090227.xyz/file/45d70737c64caeb4393ad.jpg)  
之后打开C盘下用户文件夹下的.ssh的文件夹，会看到以下文件
     * `id_rsa`私钥
     * `id_rsa.pub`公钥  
[![3.2.1.2](https://img.090227.xyz/file/40bd636f749347666f9f7.jpg)](https://img.090227.xyz/file/40bd636f749347666f9f7.jpg)  
用记事本打开上述图片中的公钥`id_rsa.pub`，复制里面的内容，然后开始在github中配置ssh密钥。  
[![3.2.1.3](https://img.090227.xyz/file/0086246f3ccc703b9035e.jpg)](https://img.090227.xyz/file/0086246f3ccc703b9035e.jpg)
  2. 将 SSH KEY 配置到 GitHub  
进入github，点击右上角头像 选择`settings`，进入设置页后选择 `SSH and GPG keys`，名字随便起，公钥填到`Key`那一栏。  
[![3.2.2.1](https://img.090227.xyz/file/75fc281237bfc6751a295.jpg)](https://img.090227.xyz/file/75fc281237bfc6751a295.jpg)  
[![3.2.2.2](https://img.090227.xyz/file/993edae3bbca9489dc156.jpg)](https://img.090227.xyz/file/993edae3bbca9489dc156.jpg)  
[![3.2.2.3](https://img.090227.xyz/file/fa8a7628c285e6be5c0a4.png)](https://img.090227.xyz/file/fa8a7628c285e6be5c0a4.png)  
[![3.2.2.4](https://img.090227.xyz/file/f3fa79cf3d639ef2d5bcb.png)](https://img.090227.xyz/file/f3fa79cf3d639ef2d5bcb.png)
  3. 测试连接，输入以下命令

SHELL
[code]1  
         
[/code]

| 
[code]ssh -T git@github.com  
         
[/code]  
  
---|---  
第一次连接会提示`Are you sure you want to continue connecting (yes/no/[fingerprint])?`，输入`yes`即可  
[![3.2.3.1](https://img.090227.xyz/file/faa0077eeab8c82f1de9e.png)](https://img.090227.xyz/file/faa0077eeab8c82f1de9e.png)  
出现连接到账户的信息，说明已经大功告成，至此完成了环境准备工作。  
[![3.2.3.2](https://img.090227.xyz/file/faa0077eeab8c82f1de9e.png)](https://img.090227.xyz/file/faa0077eeab8c82f1de9e.png)

### [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#3-3-%E5%88%9B%E5%BB%BAGitHub-io%E4%BB%93%E5%BA%93 "3.3. 创建GitHub.io仓库")3.3. 创建GitHub.io仓库

  1. 点击右上角的`+`按钮，选择New repository，创建一个`<用户名>.github.io`的仓库。
  2. 仓库名字的格式必须为：`<用户名>.github.io` (注意：前缀必须为用户名，此为预览博客需要，后期可修改仓库名)
  3. 可见性必须选择 `Public` 方便第一次部署检查问题，点击 Creat repository 进行创建即可  
[![3.3. 创建GitHub.io仓库](https://img.090227.xyz/file/3d9274644460cd1ffeb26.png)](https://img.090227.xyz/file/3d9274644460cd1ffeb26.png)

* * *

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#4-%E5%88%9D%E5%A7%8B%E5%8C%96-Hexo-%E5%8D%9A%E5%AE%A2 "4.初始化 Hexo 博客")4.初始化 Hexo 博客

  1. 创建一个文件夹来保存博客源码（我这里选的路径为`D:/Hexo-Blog`），在文件夹内右键鼠标，选择`Open Git Bash here`  
[![4.1](https://img.090227.xyz/file/f78e04406dc803d610538.png)](https://img.090227.xyz/file/f78e04406dc803d610538.png)
  2. 在`Git BASH`输入如下命令安装 Hexo

SHELL
[code]1  
         
[/code]

| 
[code]npm install -g hexo-cli && hexo -v  
         
[/code]  
  
---|---  
[![4.2](https://img.090227.xyz/file/808bff9b7ab5b13fcd200.png)](https://img.090227.xyz/file/808bff9b7ab5b13fcd200.png)
  3. 安装完后输入`hexo -v`验证是否安装成功。  
[![4.3](https://img.090227.xyz/file/17349517f78516f7ac8ff.png)](https://img.090227.xyz/file/17349517f78516f7ac8ff.png)
  4. 初始化 Hexo 项目安装相关依赖。

SHELL
[code]1  
         2  
         3  
         
[/code]

| 
[code]hexo init blog-demo  
         cd blog-demo  
         npm i  
         
[/code]  
  
---|---  
[![4.4](https://img.090227.xyz/file/1c130d7beed537111d448.png)](https://img.090227.xyz/file/1c130d7beed537111d448.png)
  5. 初始化项目后，`blog-demo`有如下结构：  
[![4.5](https://img.090227.xyz/file/74128294708705e22e188.png)](https://img.090227.xyz/file/74128294708705e22e188.png)

  * node_modules：依赖包
  * scaffolds：生成文章的一些模板
  * source：用来存放你的文章
  * themes：主题
  * .npmignore：发布时忽略的文件（可忽略）
  * _config.landscape.yml：主题的配置文件
  * config.yml：博客的配置文件
  * package.json：项目名称、描述、版本、运行和开发等信

  6. 输入`hexo cl && hexo s`启动项目  
[![4.6](https://img.090227.xyz/file/e8c930919bb49270bde5a.png)](https://img.090227.xyz/file/e8c930919bb49270bde5a.png)
  7. 打开浏览器，输入地址：<http://localhost:4000/> ，看到下面的效果，说明你的博客已经构建成功了。  
[![4.7](https://img.090227.xyz/file/e285037815104f68f4514.jpg)](https://img.090227.xyz/file/e285037815104f68f4514.jpg)

* * *

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#5-%E5%B0%86%E9%9D%99%E6%80%81%E5%8D%9A%E5%AE%A2%E6%8C%82%E8%BD%BD%E5%88%B0-GitHub-Pages "5.将静态博客挂载到 GitHub Pages")5.将静态博客挂载到 GitHub Pages

  1. 安装 hexo-deployer-git

SHELL
[code]1  
         
[/code]

| 
[code]npm install hexo-deployer-git --save  
         
[/code]  
  
---|---  
  2. 修改 `_config.yml` 文件  
在blog-demo目录下的_config.yml，就是整个Hexo框架的配置文件了。可以在里面修改大部分的配置。详细可参考官方的[配置描述](https://hexo.io/zh-cn/docs/configuration)。  
修改最后一行的配置，将repository修改为你自己的github项目地址即可，还有分支要改为`main`代表主分支（注意缩进）。

YAML
[code]1  
         2  
         3  
         4  
         
[/code]

| 
[code]deploy:  
           type: git  
           repository: git@github.com:cmliussss2024/cmliussss2024.github.io.git  
           branch: main  
         
[/code]  
  
---|---  
  3. 修改好配置后，运行如下命令，将代码部署到 GitHub（Hexo三连）。

SHELL
[code]1  
         2  
         3  
         4  
         5  
         6  
         7  
         
[/code]

| 
[code]// Git BASH终端  
         hexo clean && hexo generate && hexo deploy    
           
         // 或者  
           
         // VSCODE终端  
         hexo cl; hexo g; hexo d  
         
[/code]  
  
---|---  

  * hexo clean：删除之前生成的文件，可以用`hexo cl`缩写。
  * hexo generate：生成静态文章，可以用`hexo g`缩写
  * hexo deploy：部署文章，可以用`hexo d`缩写  
[![5.3.1](https://img.090227.xyz/file/18b052b831896bf00cfc4.jpg)](https://img.090227.xyz/file/18b052b831896bf00cfc4.jpg)  
 _注意：deploy时可能要你输入 username 和 password。_

如果出现Deploy done，则说明部署成功了。  
[![5.3.2](https://img.090227.xyz/file/93a5d61648491a5278556.jpg)](https://img.090227.xyz/file/93a5d61648491a5278556.jpg)  
稍等两分钟，打开浏览器访问：[https://cmliussss2024.github.io](https://cmliussss2024.github.io/) ，这时候我们就可以看到博客内容了。  
[![5.3.3](https://img.090227.xyz/file/1239b1270fcdc8bd896a6.jpg)](https://img.090227.xyz/file/1239b1270fcdc8bd896a6.jpg)

* * *

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#6-%E5%B0%86%E9%9D%99%E6%80%81%E5%8D%9A%E5%AE%A2%E6%8C%82%E8%BD%BD%E5%88%B0-Cloudflare-Pages "6.将静态博客挂载到 Cloudflare Pages")6.将静态博客挂载到 Cloudflare Pages

  1. 在 `Workers 和 Pages` 中选择 `Pages` 的 `连接到 Git`  
[![6.1.1](https://img.090227.xyz/file/b3eae4e84c4c7c31af665.jpg)](https://img.090227.xyz/file/b3eae4e84c4c7c31af665.jpg)  
[![6.1.2](https://img.090227.xyz/file/440581264cb313ed77e75.jpg)](https://img.090227.xyz/file/440581264cb313ed77e75.jpg)

  2. 然后登录你Blog仓库对应的GitHub帐号  
[![6.2.1](https://img.090227.xyz/file/733c0a673bb66670b7ca1.jpg)](https://img.090227.xyz/file/733c0a673bb66670b7ca1.jpg)  
[![6.2.2](https://img.090227.xyz/file/8fb282e32991167a98f57.jpg)](https://img.090227.xyz/file/8fb282e32991167a98f57.jpg)

  3. 点击`保存并部署`后等待部署完成即可。  
[![6.3](https://img.090227.xyz/file/60cca5e2200e260327227.jpg)](https://img.090227.xyz/file/60cca5e2200e260327227.jpg)

  4. 提示`成功！您的项目已部署到以下区域：全球`后，浏览器访问：[https://cmliussss2024-github-io.pages.dev](https://cmliussss2024-github-io.pages.dev/) ，这时候我们就可以看到博客内容了。  
[![6.4](https://img.090227.xyz/file/0f2a697243725c6fa2ab8.jpg)](https://img.090227.xyz/file/0f2a697243725c6fa2ab8.jpg)  
 _这时你也就可以将你的`<用户名>.github.io`的仓库设置为`Private`私库了_

  5. 如果你有自己的域名，你可以在这里绑定你自己的自定义域，即可  
[![6.5](https://img.090227.xyz/file/2c9ce4b9b67c09376bb91.jpg)](https://img.090227.xyz/file/2c9ce4b9b67c09376bb91.jpg)

* * *

# [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8 "如何使用")如何使用

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#%E6%96%B0%E5%BB%BA%E4%B8%80%E7%AF%87%E5%8D%9A%E6%96%87 "新建一篇博文")新建一篇博文

SHELL
[code]
    1  
    
[/code]

| 
[code]
    hexo new 这是一篇新的博文  
    
[/code]  
  
---|---  
  
然后用文本编辑器去编辑`_posts/这是一篇新的博文.md`里的内容即可，注意要使用Markdown格式书写。  
详细使用方法可以查阅 <https://hexo.io/zh-cn/docs/writing>

## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#%E7%BC%96%E8%BE%91%E5%AE%8C%E6%96%87%E7%AB%A0%E4%BF%9D%E5%AD%98%E5%90%8E%E5%8F%AF%E4%BB%A5%E4%BD%BF%E7%94%A8%E5%A6%82%E4%B8%8B%E5%91%BD%E4%BB%A4%EF%BC%8C%E7%94%9F%E6%88%90%E6%9C%AC%E5%9C%B0%E9%A1%B5%E9%9D%A2-http-localhost-4000-%EF%BC%8C%E8%BF%9B%E8%A1%8C%E9%A2%84%E8%A7%88 "编辑完文章保存后可以使用如下命令，生成本地页面 http://localhost:4000/ ，进行预览")编辑完文章保存后可以使用如下命令，生成本地页面 <http://localhost:4000/> ，进行预览

SHELL
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
    // Git BASH终端  
    hexo cl && hexo s  
      
    // 或者  
      
    // VSCODE终端  
    hexo cl; hexo s  
    
[/code]  
  
---|---  
  
## [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#%E7%A1%AE%E8%AE%A4%E6%97%A0%E8%AF%AF%E5%90%8E%E4%BD%BF%E7%94%A8%E4%BB%A5%E4%B8%8B%E5%91%BD%E4%BB%A4%EF%BC%8C%E5%B0%86%E6%9C%AC%E5%9C%B0%E6%96%87%E7%AB%A0%E6%8E%A8%E9%80%81%E8%87%B3GitHub%E4%BB%93%E5%BA%93%E5%8D%B3%E5%8F%AF "确认无误后使用以下命令，将本地文章推送至GitHub仓库即可")确认无误后使用以下命令，将本地文章推送至GitHub仓库即可

SHELL
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
    // Git BASH终端  
    hexo cl && hexo g && hexo d  
      
    // 或者  
      
    // VSCODE终端  
    hexo cl; hexo g; hexo d  
    
[/code]  
  
---|---  
  
下一期会讲讲进阶的使用方法，主题美化

* * *

# [](https://vercel.blog.cmliussss.com/p/HexoBlogNo1/#VSCODE-%E7%BB%88%E7%AB%AF%E9%A6%96%E6%AC%A1%E6%89%A7%E8%A1%8C%E6%8A%A5%E9%94%99 "VSCODE 终端首次执行报错")VSCODE 终端首次执行报错

使用管理员身份打开 powershell ,输入以下命令

POWERSHELL
[code]
    1  
    
[/code]

| 
[code]
    Set-ExecutionPolicy RemoteSigned
[/code]  
  
---|---
