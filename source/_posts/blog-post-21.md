---
title: 哪吒探针搭建教程
date: '2025-07-16 12:00:00'
cover: /img/covers/blog-post-21.jpg
tags:
- 哪吒探针
categories:
- 哪吒探针
description: 演示站（随着时间推移，有可能会关闭演示站）： 演示站你点击登录可以看到后端的美化效果，但是看不到服务器信息，也会出现报错，这是权限不足引起的。不是程序或者搭建的问题。 vps.1keji.net 哪吒监控 Nezha Monitoring 1.解析两个域名，一个是面板域名，另一个
---
演示站（随着时间推移，有可能会关闭演示站）：

演示站你点击登录可以看到后端的美化效果，但是看不到服务器信息，也会出现报错，这是权限不足引起的。不是程序或者搭建的问题。

![](https://vps.1keji.net/apple-touch-icon.png)[vps.1keji.net](https://vps.1keji.net/)

### [哪吒监控 Nezha Monitoring](https://vps.1keji.net/)

1.解析两个域名，一个是面板域名，另一个是通讯域名。

2.安装nginx和docker，并进行反代。

```

    wget -O 1keji.sh "https://www.1keji.net" && chmod +x 1keji.sh && ./1keji.sh
    

```

3.安装哪吒探针程序。

```

    curl -L https://raw.githubusercontent.com/nezhahq/scripts/refs/heads/main/install.sh -o nezha.sh && chmod +x nezha.sh && sudo ./nezha.sh
    

```

大陆地区使用以下镜像：

```

    curl -L https://gitee.com/naibahq/scripts/raw/main/install.sh -o nezha.sh && chmod +x nezha.sh && sudo CN=true ./nezha.sh
    

```

4.美化：

前端自定义代码

```

    <script>
      // 禁用系统默认的小人（哪吒）动画
      window.DisableAnimatedMan = true;
    
      // 背景图、移动背景图、
      window.CustomBackgroundImage = "电脑端背景图链接";
      window.CustomMobileBackgroundImage = "手机端背景图链接";
      window.ShowNetTransfer = true;
      window.FixedTopServerName = true;
    
      // 将所有 HTTP 链接改为 HTTPS，避免混合内容警告
      const AVIF_URL = "右上角小人";
    
      // 在 <head> 中注入 CSS，隐藏默认小人，定义自定义小人样式
      const style = document.createElement('style');
      style.innerHTML = `
        /* 隐藏任何通过 dicebear API 加载的默认头像 */
        .transition-opacity img[src*="dicebear"] {
          display: none !important;
        }
        /* 自定义小人样式 */
        .custom-avatar {
          position: absolute !important;
          right: -40px !important;
          top: -155px !important;
          z-index: 10 !important;
          width: 160px !important;
          height: auto !important;
        }
      `;
      document.head.appendChild(style);
    
      // 监听 DOM 变化，自动移除系统头像并插入自定义小人
      const observer = new MutationObserver(() => {
        // 抓取小人容器
        const xpath = "/html/body/div/div/main/div[2]/section[1]/div[4]/div";
        const container = document.evaluate(
          xpath, document, null,
          XPathResult.FIRST_ORDERED_NODE_TYPE, null
        ).singleNodeValue;
    
        if (!container) return;
    
        // 移除任何残留的默认头像
        container.querySelectorAll('img[src*="dicebear"]').forEach(el => el.remove());
    
        // 如果还没插入自定义小人，则插入
        if (!container.querySelector('img.custom-avatar')) {
          const img = document.createElement('img');
          img.src = AVIF_URL;
          img.className = 'custom-avatar';
          container.appendChild(img);
        }
      });
    
      // 从页面一加载就开始观察，保持一直生效
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    </script>
    

```

仪表板自定义代码：

```

    <script>
      // 禁用默认小人图（哪吒官方保留变量）
      window.DisableAnimatedMan = true;
    
      // 引入自定义字体（MiSans 字体，可替换为你喜欢的字体）
      const fontLink = document.createElement('link');
      fontLink.rel = 'stylesheet';
      fontLink.href = 'https://font.sec.miui.com/font/css?family=MiSans:400,700:MiSans';
      document.head.appendChild(fontLink);
    
      // 修改左上角标题文本 “哪吒监控” -> “哪吒探针”
      const observerAdminTitle = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
          mutation.addedNodes.forEach(node => {
            if (node.nodeType === 1) {
              const links = node.matches('.transition-opacity') ? [node] : node.querySelectorAll('.transition-opacity');
              links.forEach(link => {
                const textNode = Array.from(link.childNodes).find(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim() === '哪吒监控');
                if (textNode) {
                  textNode.textContent = '哪吒探针';
                  observerAdminTitle.disconnect();
                }
              });
            }
          });
        });
      });
      observerAdminTitle.observe(document.body, { childList: true, subtree: true });
    </script>
    
    <style>
      /* 自定义字体并添加白色阴影 */
      * {
        font-family: 'HarmonyOS Sans', sans-serif !important;
        font-size: 16px;
        text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.9);
     /* 使用白色阴影增强对比度 */
      }
    
      /* 仪表板背景图全覆盖 */
      html, body {
        height: 100% !important;
        background: url("https://img.003666.xyz/2025/05/24/141a91d4cba94b49001.webp") no-repeat center center fixed !important;
        background-size: cover !important;
      }
    
      /* 顶部导航背景透明 + 模糊 */
      .el-header {
        background-color: transparent !important;
        backdrop-filter: blur(4px);
        box-shadow: none !important;
      }
    
      /* 替换默认头像图（avatar） */
      img[src*="https://api.dicebear.com/7.x/notionists/svg"] {
        content: url("https://img.003666.xyz/2025/05/24/e6c54e4c9202c540001.avif") !important;
        width: 100px !important;
        height: auto !important;
        margin-top: -0px;
      }
    
      /* 替换左上角 logo 图标 */
      img[src*="/dashboard/logo.svg"] {
        content: url("https://img.003666.xyz/2025/05/24/0eb4169981a13265001.webp") !important;
      }
    
      /* 去掉页脚 */
      footer {
        display: none !important;
      }
    
      /* 为主容器添加半透明背景 */
      .el-container {
        background-color: rgba(255, 255, 255, 0.7) !important; /* 半透明白色背景 */
      }
    
      /* 为卡片等组件设置更高透明度的背景 */
      .el-card, .el-message-box, .el-dialog {
        background-color: rgba(255, 255, 255, 0.9) !important;
      }
    
      /* 针对黑色文字，添加白色阴影以增强对比度 */
      .el-text, .el-button, .el-table, .el-form-item__label, .el-form-item__content, .el-menu-item, .el-submenu__title {
        color: #333 !important; /* 确保文字颜色为深色 */
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8); /* 白色阴影 */
      }
    
      /* 针对可能存在的浅色文字，添加黑色阴影 */
      .el-text-light, .el-button--text, .el-link {
        color: #fff !important; /* 假设某些文字是浅色的 */
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* 黑色阴影 */
      }
    </style>
    

```

视频教程：

![](https://img.youtube.com/vi/TU5bqzBiU0w/maxresdefault.jpg)

[哪吒探针V1版，最新稳定简单安装教程。前后端高级美化：背景更换、小人定制、头像替换全搞定！](https://www.youtube.com/watch?v=TU5bqzBiU0w "哪吒探针V1版，最新稳定简单安装教程。前后端高级美化：背景更换、小人定制、头像替换全搞定！")

前端添加ip显示

```

    <script>
        // 插入 IP 图片
    const observerImg = new MutationObserver(() => {
      if (!document.querySelector('img[src*="ping0.cc"]')) {
        const img = document.createElement('img');
        img.src = 'https://ping0.cc/img1';
        img.alt = 'Your IP';
        img.className = 'ip-img';
    
        // 添加样式
        const style = document.createElement('style');
        style.innerHTML = `
          /* 通用样式 */
          .ip-img {
            width: 400px;
            max-width: 90%;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.25);
            opacity: 0.7;
            z-index: 1000;
          }
    
          /* 桌面端固定在右下角 */
          @media (min-width: 768px) {
            .ip-img {
              position: fixed;
              bottom: 10px;
              right: 10px;
            }
          }
    
          /* 移动端放在页面内容最下方，不悬浮 */
          @media (max-width: 767px) {
            .ip-img {
              position: static;
              display: block;
              margin: 20px auto 10px auto;
            }
          }
        `;
        document.head.appendChild(style);
    
        document.body.appendChild(img);
      }
    });
    observerImg.observe(document.body, { childList: true, subtree: true });
    
      // 禁用系统默认的小人（哪吒）动画
      window.DisableAnimatedMan = true;
    
      // 背景图、移动背景图、
      window.CustomBackgroundImage = "电脑端背景图链接";
      window.CustomMobileBackgroundImage = "手机端背景图链接";
      window.ShowNetTransfer = true;
      window.FixedTopServerName = true;
    
      // 将所有 HTTP 链接改为 HTTPS，避免混合内容警告
      const AVIF_URL = "右上角小人";
    
      // 在 <head> 中注入 CSS，隐藏默认小人，定义自定义小人样式
      const style = document.createElement('style');
      style.innerHTML = `
        /* 隐藏任何通过 dicebear API 加载的默认头像 */
        .transition-opacity img[src*="dicebear"] {
          display: none !important;
        }
        /* 自定义小人样式 */
        .custom-avatar {
          position: absolute !important;
          right: -40px !important;
          top: -155px !important;
          z-index: 10 !important;
          width: 160px !important;
          height: auto !important;
        }
      `;
      document.head.appendChild(style);
    
      // 监听 DOM 变化，自动移除系统头像并插入自定义小人
      const observer = new MutationObserver(() => {
        // 抓取小人容器
        const xpath = "/html/body/div/div/main/div[2]/section[1]/div[4]/div";
        const container = document.evaluate(
          xpath, document, null,
          XPathResult.FIRST_ORDERED_NODE_TYPE, null
        ).singleNodeValue;
    
        if (!container) return;
    
        // 移除任何残留的默认头像
        container.querySelectorAll('img[src*="dicebear"]').forEach(el => el.remove());
    
        // 如果还没插入自定义小人，则插入
        if (!container.querySelector('img.custom-avatar')) {
          const img = document.createElement('img');
          img.src = AVIF_URL;
          img.className = 'custom-avatar';
          container.appendChild(img);
        }
      });
    
      // 从页面一加载就开始观察，保持一直生效
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    </script>
    

```

显示位置：

位置| 设置方式  
---|---  
右上角| `top: 10px; right: 10px;`  
右下角| `bottom: 10px; right: 10px;`  
左上角| `top: 10px; left: 10px;`  
左下角| `bottom: 10px; left: 10px;`  
页面中间| `top: 50%; left: 50%; transform: translate(-50%, -50%);`  
居中下方| `bottom: 10px; left: 50%; transform: translateX(-50%);`
