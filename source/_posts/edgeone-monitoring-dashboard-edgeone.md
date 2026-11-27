---
title: EdgeOne Monitoring Dashboard (EdgeOne 监控大屏)
date: '2025-12-30 12:00:00'
cover: /img/covers/edgeone-monitoring-dashboard-edgeone.jpg
tags:
- EdgeOne监控大屏
categories:
- EdgeOne监控大屏
description: ✨ 主要功能 实时概览 ：展示站点总请求数、总流量、总带宽等关键指标。 多维度分析 ： 国家/地区排行 ：支持中英文显示，直观展示流量来源。 省份/状态码/域名/URL/资源类型 ：全方位的 Top N 分析。 回源分析 ：监控回源流量、带宽及请求数，掌握源站负载。 灵活查询 ：
---
## ✨ 主要功能

[](https://github.com/wangai14/eo_monitor#-%E4%B8%BB%E8%A6%81%E5%8A%9F%E8%83%BD)

  * 实时概览：展示站点总请求数、总流量、总带宽等关键指标。
  * 多维度分析：
    * 国家/地区排行：支持中英文显示，直观展示流量来源。
    * 省份/状态码/域名/URL/资源类型：全方位的 Top N 分析。
  * 回源分析：监控回源流量、带宽及请求数，掌握源站负载。
  * 灵活查询：
    * 支持自定义时间段（近1小时 - 近31天）。
    * 支持切换数据粒度（分钟/小时/天/自动）。
  * 个性化配置：支持自定义站点名称。

## 🚀 快速部署

[](https://github.com/wangai14/eo_monitor#-%E5%BF%AB%E9%80%9F%E9%83%A8%E7%BD%B2)

### 方式一：EdgeOne Pages (推荐)

[](https://github.com/wangai14/eo_monitor#%E6%96%B9%E5%BC%8F%E4%B8%80edgeone-pages-%E6%8E%A8%E8%8D%90)

  1. Fork 本仓库到您的 GitHub 账号。
  2. 前往 [腾讯云 EdgeOne 控制台](https://console.cloud.tencent.com/edgeone) 创建 Pages 项目。
  3. 连接您的 GitHub 仓库。
  4. 在 环境变量 (Environment Variables) 中添加以下配置：
     * `SECRET_ID`: 您的腾讯云 SecretId
     * `SECRET_KEY`: 您的腾讯云 SecretKey
     * `SITE_NAME`: (可选) 自定义大屏标题，默认为 "AcoFork 的 EdgeOne 监控大屏"
     * `SITE_ICON`: (可选) 自定义网页图标，默认为 "[https://q2.qlogo.cn/headimg_dl?dst_uin=2726730791&spec=0](https://q2.qlogo.cn/headimg_dl?dst_uin=2726730791&spec=0)"
  5. 部署项目。

### 方式二：本地运行 / Node.js 环境

[](https://github.com/wangai14/eo_monitor#%E6%96%B9%E5%BC%8F%E4%BA%8C%E6%9C%AC%E5%9C%B0%E8%BF%90%E8%A1%8C--nodejs-%E7%8E%AF%E5%A2%83)

  1. 克隆仓库：
[code]git clone https://github.com/afoim/eo_monitior
         cd eo_monitior
[/code]

  2. 安装依赖：
[code]npm install -g edgeone
         edgeone login
[/code]

  3. 配置密钥：

     * 方法 A (环境变量)：创建 `.env` 文件或直接导出环境变量 `SECRET_ID` 和 `SECRET_KEY`。
     * 方法 B (文件配置)：在项目根目录创建 `key.txt` 文件，内容格式如下（注意使用中文冒号）：
[code]SecretId：您的SecretId
           SecretKey：您的SecretKey
           
[/code]

  4. 启动服务：
[code]edgeone pages dev
[/code]

  5. 访问 `http://localhost:8088`。

## 🔑 权限说明

[](https://github.com/wangai14/eo_monitor#-%E6%9D%83%E9%99%90%E8%AF%B4%E6%98%8E)

使用的腾讯云访问密钥必须拥有 EdgeOne 只读访问权限 (`QcloudTEOReadOnlyaccess`)。 请前往访问管理控制台创建和管理密钥（只需要 编程访问）：

  * 国内版 (China Station): <https://console.cloud.tencent.com/cam/user/userType>
  * 海外版 (International Station): <https://console.tencentcloud.com/cam/user/userType>

## 🛠️ 技术栈

[](https://github.com/wangai14/eo_monitor#%EF%B8%8F-%E6%8A%80%E6%9C%AF%E6%A0%88)

  * 后端：Node.js, Express, Tencent Cloud SDK
  * 前端：HTML5, Tailwind CSS, ECharts
  * 部署：Tencent Cloud EdgeOne Pages
