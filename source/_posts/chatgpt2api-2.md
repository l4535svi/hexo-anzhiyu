---
title: ChatGPT2API最新版本可以聊天的
date: '2026-07-29 12:00:00'
tags:
- GPT
categories:
- GPT
description: 更新命令 如果你当初是用它官方的一键脚本 / Docker 安装的，默认安装目录是： /opt/chatgpt2api 最常见的更新方式 SSH 登录服务器后执行： cd /opt/chatgpt2api docker compose pull docker compose up
---
更新命令 

### 

如果你当初是用它官方的一键脚本 / Docker 安装的，默认安装目录是：
[code] 
    /opt/chatgpt2api  
    
[/code]
[/code]

### 最常见的更新方式

### 
[code]
    
    
    SSH 登录服务器后执行：
    
    
    
[code]
    cd /opt/chatgpt2api
    
    docker compose pull
    docker compose up -d
[/code]
[/code]

`
[/code]
[/code]

###   

### Docker 一键部署的修改方法

一键脚本默认安装目录是 `/opt/chatgpt2api`：
[code] 
    cd /opt/chatgpt2api
    nano .env
[/code]
[/code]

找到：
[code] 
    CHATGPT2API_AUTH_KEY=原来的密码
[/code]
[/code]

修改为新的密码，例如：
[code] 
    CHATGPT2API_AUTH_KEY=MyNewKey_2026_xxxxxxxxx
[/code]
[/code]

保存退出：
[code] 
    Ctrl + O
    回车
    Ctrl + X
[/code]
[/code]

然后重新创建容器：
[code] 
    docker compose up -d --force-recreate
[/code]
[/code]

必须重新创建容器，单纯执行 `docker restart chatgpt2api` 不会加载修改后的环境变量。

## 快速开始

[](https://github.com/yukkcat/chatgpt2api#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)

### 一键安装

[](https://github.com/yukkcat/chatgpt2api#%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85)
[code]
    curl -fsSL https://raw.githubusercontent.com/yukkcat/chatgpt2api/main/deploy/install.sh | sudo bash
[/code]

固定安装当前稳定版：
[code]
    curl -fsSL https://raw.githubusercontent.com/yukkcat/chatgpt2api/v2.7.0/deploy/install.sh | sudo bash -s -- --branch v2.7.0
[/code]

### Docker 运行

[](https://github.com/yukkcat/chatgpt2api#docker-%E8%BF%90%E8%A1%8C)
[code]
    git clone https://github.com/yukkcat/chatgpt2api.git
    cd chatgpt2api
    cp .env.example .env
    printf '{ "auth-key": "your_secret_key_here" }\n' > config.json
    docker compose up -d
[/code]

启动前请先在 `.env` 中设置 `CHATGPT2API_AUTH_KEY`，也可以继续在 `config.json` 中填写 `auth-key`。 仓库只保留 `config.example.yaml` 作为配置示例，运行时真实配置文件仍是本地 `config.json`，不要把本地配置提交到仓库。

  * Web 面板：`http://localhost:3000`
  * API 地址：`http://localhost:3000/v1`
  * 数据目录：`./data`

### WARP / FlareSolverr 稳定代理部署

[](https://github.com/yukkcat/chatgpt2api#warp--flaresolverr-%E7%A8%B3%E5%AE%9A%E4%BB%A3%E7%90%86%E9%83%A8%E7%BD%B2)

如果注册或图片链路经常遇到 Cloudflare 拦截，可以启用附带的 WARP + Privoxy + FlareSolverr 方案：
[code]
    cp .env.example .env
    printf '{ "auth-key": "your_secret_key_here" }\n' > config.json
    docker compose -f docker-compose.warp.yml up -d
[/code]

该 compose 会启动：

  * `warp-proxy`：提供 WARP SOCKS5 出口。
  * `privoxy`：把 WARP SOCKS5 转成 HTTP 代理。
  * `flaresolverr`：刷新 Cloudflare clearance。
  * `init-config`：幂等写入 `proxy_runtime` 默认配置。
  * `app`：启动 ChatGPT2API 主服务。

默认只让上游 OpenAI / ChatGPT 请求走稳定代理，账号邮箱、CPA 等辅助链路不会被强制接管。账号自身配置的代理优先级最高，其次是稳定代理运行时，再其次是显式代理和旧版全局代理。

可在 `.env` 中调整端口和代理运行时参数，也可在后台设置页的「稳定代理运行时」面板手动保存、测试代理和测试 clearance。

### 本地开发

[](https://github.com/yukkcat/chatgpt2api#%E6%9C%AC%E5%9C%B0%E5%BC%80%E5%8F%91)

启动后端：
[code]
    git clone https://github.com/yukkcat/chatgpt2api.git
    cd chatgpt2api
    uv sync
    uv run main.py
[/code]

启动前端：
[code]
    cd chatgpt2api/web-vue
    npm install
    npm run dev
[/code]

后续更新新版本：
[code]
    git pull
    docker compose up -d
[/code]

### 账号存储后端配置

[](https://github.com/yukkcat/chatgpt2api#%E8%B4%A6%E5%8F%B7%E5%AD%98%E5%82%A8%E5%90%8E%E7%AB%AF%E9%85%8D%E7%BD%AE)

支持通过环境变量 `STORAGE_BACKEND` 切换账号池和管理 Key 的存储方式：

  * `json` \- 本地 JSON 文件（默认）
  * `sqlite` \- 本地 SQLite 数据库
  * `postgres` \- 外部 PostgreSQL（需配置 `DATABASE_URL`）
  * `git` \- Git 私有仓库（需配置 `GIT_REPO_URL` 和 `GIT_TOKEN`）

说明：该配置只影响账号池和管理 Key。系统设置、调用日志、概览统计、图片索引、注册机配置仍按各自模块独立保存，其中概览统计默认写入 `data/dashboard_metrics.json` 并滚动保留最近 30 天。

示例：使用 PostgreSQL
[code]
    environment:
      - STORAGE_BACKEND=postgres
      - DATABASE_URL=postgresql://user:password@host:5432/dbname
[/code]

## 功能详情

[](https://github.com/yukkcat/chatgpt2api#%E5%8A%9F%E8%83%BD%E8%AF%A6%E6%83%85)

### API 兼容能力

[](https://github.com/yukkcat/chatgpt2api#api-%E5%85%BC%E5%AE%B9%E8%83%BD%E5%8A%9B)

> 兼容的是本项目已实现的 ChatGPT Web 逆向场景，不等同于官方 OpenAI 全量 API 代理。

  * `GET /v1/models`：合并本地模型目录和上游实时模型，返回当前可暴露模型。
  * `POST /v1/chat/completions`：支持文本、搜索和图片场景，支持 `stream`、`tools`、`web_search_options`、`reasoning_effort` / `thinking_effort`。
  * `POST /v1/responses`：支持文本、搜索和图片工具调用，支持 `image_generation` 与 `web_search*` 工具。
  * `POST /v1/messages`：Anthropic Messages 兼容入口，走同一账号池和调用日志。
  * `POST /v1/search`：ChatGPT 搜索兼容入口，返回文本、引用来源和搜索结果信息。
  * `POST /v1/images/generations`：图片生成，支持 `n=1..4`。
  * `POST /v1/images/edits`：图片编辑，支持 multipart、远程 URL、base64、data URL 和多参考图。
  * `POST /v1/editable-file-tasks`、`GET /v1/editable-file-tasks`：统一 PPT / PSD 可编辑文件任务。
  * `POST /v1/ppt/generations`、`POST /v1/psd/generations`：PPT / PSD 生成快捷入口。
  * `GET /files/{path}`：下载 PPT / PSD / 可编辑文件任务产物。

### 对话画图工作台

[](https://github.com/yukkcat/chatgpt2api#%E5%AF%B9%E8%AF%9D%E7%94%BB%E5%9B%BE%E5%B7%A5%E4%BD%9C%E5%8F%B0)

  * 侧边栏会话 + 底部输入框布局，支持普通文本对话、搜索模式、文生图、图生图和多图参考。
  * 支持 `gpt-image-2`、`codex-gpt-image-2`、`auto` 以及模型目录返回的文本/搜索模型。
  * 支持推理强度：低 / 中 / 高 / 超高，透传为 `reasoning_effort`。
  * 支持 Markdown 渲染、代码块、搜索引用来源、官网式 `cite` / `image_group` 占位解析和图片建议展示。
  * 图片任务内联展示生成中、成功和失败状态；切换会话后仍保留任务状态提示。
  * 支持全屏偏好持久化、历史删除、清空、滚动定位和大量消息下的渲染性能优化。
  * 可在系统设置中开启“图片成功后删除官网会话”，成功保存图片后尝试隐藏上游 ChatGPT conversation；默认关闭，便于保留恢复和排查现场。

### 图片链路和诊断

[](https://github.com/yukkcat/chatgpt2api#%E5%9B%BE%E7%89%87%E9%93%BE%E8%B7%AF%E5%92%8C%E8%AF%8A%E6%96%AD)

  * 图片请求会记录 `call_id`、账号邮箱、模型、endpoint、conversation id、代理来源、代理组/节点和关键阶段耗时。
  * 上游断流、SSE 超时、轮询超时、策略拒绝、文本回复但无图、图片解析/下载失败会尽量保留原始上游错误。
  * `image_stream_timeout_secs` 控制上游 SSE/HTTP 流硬截止；`image_poll_timeout_secs` 控制结果解析和轮询总等待。
  * 可通过实时监控查看活跃请求、入口排队、账号等待、出口等待、上游生成和慢请求分布。
  * 可通过调用日志查看请求详情、错误码、上游原始诊断、图片结果和账号信息。

### 账号、导入和注册

[](https://github.com/yukkcat/chatgpt2api#%E8%B4%A6%E5%8F%B7%E5%AF%BC%E5%85%A5%E5%92%8C%E6%B3%A8%E5%86%8C)

  * 账号管理支持搜索、筛选、批量刷新、导出、编辑、分组、代理设置和异常账号处理。
  * 异常账号不再走自动/手动重登；鉴权失效按“自动移除异常账号”开关决定删除或保留异常状态。
  * 支持本地 CPA JSON、远程 CPA、Sub2API、access token 导入。
  * 远程 CPA / Sub2API 连接可在设置页维护，也可在账号管理里打开统一导入弹窗。
  * Sub2API 导入支持读取远程分组，按分组折叠、全组选中、单账号选择、按组导入和去重保存。
  * 注册账号支持临时邮箱、GPTMail、Outlook Token 邮箱池、Microsoft passwordless 验证和 plus alias 分裂。

### 代理、存储和运维

[](https://github.com/yukkcat/chatgpt2api#%E4%BB%A3%E7%90%86%E5%AD%98%E5%82%A8%E5%92%8C%E8%BF%90%E7%BB%B4)

  * 代理优先级：账号个人代理 > 账号组代理/代理组 > 显式任务代理 > 默认代理 > 稳定代理运行时 > 直连。
  * 代理组支持多出口节点、节点图片并发、轮换间隔、健康展示和测试。
  * 备用出口可用于图片早期 TLS / 连接超时失败后的重试，默认关闭。
  * 支持本地图片存储、WebDAV、双写、图片索引、标签、下载、压缩和清理。
  * R2 备份可覆盖配置、账号、日志、图片索引、概览统计等关键数据。
  * 概览中心的调用趋势、成功率和模型统计独立滚动保留最近 30 天。

### 关键配置项

[](https://github.com/yukkcat/chatgpt2api#%E5%85%B3%E9%94%AE%E9%85%8D%E7%BD%AE%E9%A1%B9)

配置项| 默认值| 说明  
---|---|---  
`image_stream_timeout_secs`| `80`| 图片上游 SSE / HTTP 流最长等待时间。  
`image_poll_timeout_secs`| `60`| 图片结果解析和轮询最长等待时间。  
`image_parallel_generation`| `true`| 多图请求是否并行生成。  
`image_account_concurrency`| `1`| 单账号图片并发上限，可设置为 1–3。  
`image_remove_conversation_after_result`| `false`| 图片成功保存后尝试隐藏上游 ChatGPT 官网会话。  
`auto_remove_invalid_accounts`| `true`| 鉴权失效账号是否自动移除。  
`auto_remove_rate_limited_accounts`| `false`| 远程确认图片额度耗尽后是否自动移除账号。  
`log_retention_days`| `30`| 调用日志自动清理天数。  
`proxy_runtime`| 关闭| 稳定代理运行时和 Cloudflare clearance 配置。  
  
### 状态说明

[](https://github.com/yukkcat/chatgpt2api#%E7%8A%B6%E6%80%81%E8%AF%B4%E6%98%8E)

  * 发布变更以 [CHANGELOG.md](https://github.com/yukkcat/chatgpt2api/blob/main/CHANGELOG.md) 为准。
  * 仓库只保留发布必要文件和长期维护文档；被忽略的本地草稿、测试记录和运行产物不作为发布内容。

## 效果展示

[](https://github.com/yukkcat/chatgpt2api#%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA)

[![screenshot 1](https://github.com/yukkcat/chatgpt2api/raw/main/docs/images/1.png)](https://github.com/yukkcat/chatgpt2api/blob/main/docs/images/1.png)| [![screenshot 2](https://github.com/yukkcat/chatgpt2api/raw/main/docs/images/2.png)](https://github.com/yukkcat/chatgpt2api/blob/main/docs/images/2.png)  
---|---  
[![screenshot 3](https://github.com/yukkcat/chatgpt2api/raw/main/docs/images/3.png)](https://github.com/yukkcat/chatgpt2api/blob/main/docs/images/3.png)| [![screenshot 4](https://github.com/yukkcat/chatgpt2api/raw/main/docs/images/4.png)](https://github.com/yukkcat/chatgpt2api/blob/main/docs/images/4.png)  
[![screenshot 5](https://github.com/yukkcat/chatgpt2api/raw/main/docs/images/5.png)](https://github.com/yukkcat/chatgpt2api/blob/main/docs/images/5.png)| [![screenshot 6](https://github.com/yukkcat/chatgpt2api/raw/main/docs/images/6.png)](https://github.com/yukkcat/chatgpt2api/blob/main/docs/images/6.png)
