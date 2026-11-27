---
title: Cunlink短链接系统部署教程（2026）：Cloudflare Workers + D1，自建免费短链服务
date: '2026-07-26 12:00:00'
cover: /img/covers/cunlink2026cloudflare-workers-d1.jpg
tags:
- cloudflare项目
categories:
- cloudflare项目
description: 介绍 Cunlink 短链接系统的完整部署流程。基于 Cloudflare Workers + D1 构建，完全免费托管，支持自定义短码、点击数据分析、链接分组管理、二维码生成、API 接入、浏览器扩展等功能。 适合： - 需要自建短链接服务的个人开发者 - 不想被第三方短链平台
---
介绍 Cunlink 短链接系统的完整部署流程。基于 Cloudflare Workers + D1 构建，完全免费托管，支持自定义短码、点击数据分析、链接分组管理、二维码生成、API 接入、浏览器扩展等功能。 适合： - 需要自建短链接服务的个人开发者 - 不想被第三方短链平台限制的用户 - 想学习 Cloudflare Workers + D1 实战部署的人

![128.jpg](https://www.cunzhangblog.com/api/blob/images/80cf53ff7a4482183ab2e38f69ddd2d40f13eb6c.jpg)

## 核心结论

经过实际部署测试：

  * Cunlink 完全跑在 Cloudflare 免费额度上，不需要服务器，不需要月费
  * 部署不算复杂，但数据库初始化需要手动执行 22 条 SQL，是唯一容易卡住的地方
  * 功能完整度超出预期：点击分析、分组管理、API、浏览器扩展全都有

如果你需要一款自己能完全掌控的短链接系统，Cunlink 值得部署。尤其是已经有 Cloudflare 账号的用户，成本为零。

适合：

  * 个人站长和独立开发者
  * 需要短链点击数据分析的用户
  * 想跑在 Cloudflare 免费套餐上的项目

* * *

![cunlink](https://www.cunzhangblog.com/api/blob/images/dc67f553ece5caccaf8abdf522dc4bb723404f32.png)

## 什么是 Cunlink？

Cunlink 是一款基于 Cloudflare Workers + D1 的开源短链接系统。由 Web3村长在 shrtnr 基础上修改定制，使用 TypeScript + Hono 框架开发。

【[Github开源](https://github.com/cunzhangcrypto/cunlink)】

核心能力：

  1. 生成短链接（随机短码或自定义短码），支持 3 位短码
  2. 点击分析：追踪来源、国家、设备、浏览器、UTM 参数
  3. 链接分组管理：将相关短链接归组，查看组合数据
  4. 管理后台：图表分析、二维码生成、设置管理

## 为什么选择自建短链接系统？

市面上短链接服务很多，但自建有自己的优势：

方案| 费用| 数据掌控| 功能完整度| 可定制  
---|---|---|---|---  
Cunlink（自建）| 免费| 完全掌控| 高| 开源可改  
Bitly 免费版| 免费但有数量限制| 平台掌控| 中| ❌  
第三方短链平台| 按量计费| 数据在别人手里| 看平台| ❌  
  
自建的核心价值是数据完全在自己手里，不依赖第三方平台，也不怕服务涨价或关停。

## 技术架构

Cunlink 的技术栈：

层级| 技术  
---|---  
运行时| Cloudflare Workers  
数据库| Cloudflare D1（SQLite）  
缓存| Cloudflare KV  
框架| Hono + TypeScript  
SDK| Dart（Flutter 侧可用）  
  
数据库包含 7 张表：links（链接）、slugs（短码）、clicks（点击记录）、settings（设置）、api_keys（API 密钥）、bundles（分组）、bundle_links（分组关联），外加 14 个索引覆盖所有查询路径。

## 准备工作

开始部署之前，需要：

  * GitHub 账号
  * Cloudflare 账号（免费版即可）
  * Node.js 22+（可选，本地开发需要）

预计时间：20-30 分钟

难度：⭐⭐⭐

* * *

## Cunlink 部署教程

### 第一步：Fork 仓库

打开 [Cunlink](https://github.com/cunzhangcrypto/cunlink) 的 GitHub 页面，点击右上角的 Fork，把仓库复制到你自己的 GitHub 账号下。

### 第二步：在 Cloudflare Pages 创建项目

进入 Cloudflare Dashboard → Workers & Pages → 创建 → 连接到 Git，选择你刚 Fork 的仓库。

框架选择无，构建命令留空，点击开始部署。部署完成后 Cloudflare 会分配一个 workers.dev 域名。

### 第三步：创建 D1 数据库和 KV 命名空间

在 Cloudflare Dashboard 中：

  1. Workers & Pages → D1 → 创建数据库，取个名字（比如 cunlink）
  2. Workers & Pages → KV → 创建命名空间，取个名字（比如 cunlink）

### 第四步：绑定资源

回到刚才部署的 workers 项目 → 设置 → 绑定 → 添加绑定：

类型| 变量名| 选择  
---|---|---  
D1 数据库| `DB`| 你刚创建的 D1 数据库  
KV 命名空间| `SLUG_KV`| 你刚创建的 KV 命名空间  
  
### 第五步：初始化数据库（关键步骤）

进入 Workers & Pages → D1 → 点击你的数据库 → 控制台。

D1 Console 每次只能执行一条 SQL。以下每条代码单独复制，粘贴到 D1 Console 执行，成功后再执行下一条。

#### 如果是首次部署（全新数据库）

按以下顺序执行：

第 1 条 — 创建链接表

```

    CREATE TABLE IF NOT EXISTS links ( id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT NOT NULL, label TEXT, created_at INTEGER NOT NULL, expires_at INTEGER, created_via TEXT DEFAULT 'app', created_by TEXT DEFAULT 'anonymous' );

```

第 2 条 — 创建短码表

```

    CREATE TABLE IF NOT EXISTS slugs ( link_id INTEGER NOT NULL REFERENCES links(id) ON DELETE CASCADE, slug TEXT NOT NULL PRIMARY KEY, is_custom INTEGER NOT NULL DEFAULT 0, is_primary INTEGER NOT NULL DEFAULT 0, created_at INTEGER NOT NULL, disabled_at INTEGER );

```

第 3 条 — 创建点击记录表

```

    CREATE TABLE IF NOT EXISTS clicks ( id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT NOT NULL REFERENCES slugs(slug) ON DELETE CASCADE, clicked_at INTEGER NOT NULL, referrer TEXT, referrer_host TEXT, country TEXT, region TEXT, city TEXT, device_type TEXT, os TEXT, browser TEXT, language TEXT, link_mode TEXT DEFAULT 'link', channel TEXT, utm_source TEXT, utm_medium TEXT, utm_campaign TEXT, utm_term TEXT, utm_content TEXT, user_agent TEXT, is_bot INTEGER DEFAULT 0, visitor_fp TEXT, is_self_referrer INTEGER DEFAULT 0 );

```

第 4 条 — 创建设置表

```

    CREATE TABLE IF NOT EXISTS settings ( identity TEXT NOT NULL, key TEXT NOT NULL, value TEXT NOT NULL, PRIMARY KEY (identity, key) );

```

第 5 条 — 创建 API 密钥表

```

    CREATE TABLE IF NOT EXISTS api_keys ( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, key_prefix TEXT NOT NULL, key_hash TEXT NOT NULL UNIQUE, scope TEXT NOT NULL, created_at INTEGER NOT NULL, last_used_at INTEGER, identity TEXT NOT NULL DEFAULT 'anonymous' );

```

第 6 条 — 创建分组表

```

    CREATE TABLE IF NOT EXISTS bundles ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, icon TEXT, accent TEXT NOT NULL DEFAULT 'orange' CHECK (accent IN ('orange','red','green','blue','purple')), archived_at INTEGER, created_via TEXT DEFAULT 'app', created_by TEXT NOT NULL, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL );

```

第 7 条 — 创建分组-链接关联表

```

    CREATE TABLE IF NOT EXISTS bundle_links ( bundle_id INTEGER NOT NULL REFERENCES bundles(id) ON DELETE CASCADE, link_id INTEGER NOT NULL REFERENCES links(id) ON DELETE CASCADE, added_at INTEGER NOT NULL, PRIMARY KEY (bundle_id, link_id) );

```

第 8 条 — 插入默认设置

```

    IINSERT OR IGNORE INTO settings (identity, key, value) VALUES ('anonymous', 'slug_default_length', '3');

```

第 9 条 — 创建索引（第 1 个）

```

    CREATE INDEX IF NOT EXISTS idx_slugs_link_id ON slugs(link_id);

```

第 10 条 — 创建索引（第 2 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_slug ON clicks(slug);

```

第 11 条 — 创建索引（第 3 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_clicked_at ON clicks(clicked_at);

```

第 12 条 — 创建索引（第 4 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_country ON clicks(country);

```

第 13 条 — 创建索引（第 5 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_link_mode ON clicks(link_mode);

```

第 14 条 — 创建索引（第 6 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_referrer_host ON clicks(referrer_host);

```

第 15 条 — 创建索引（第 7 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_os ON clicks(os);

```

第 16 条 — 创建索引（第 8 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_visitor_fp ON clicks(visitor_fp);

```

第 17 条 — 创建索引（第 9 个）

```

    CREATE INDEX IF NOT EXISTS idx_clicks_is_self_referrer ON clicks(is_self_referrer);

```

第 18 条 — 创建索引（第 10 个）

```

    CREATE INDEX IF NOT EXISTS idx_api_keys_hash ON api_keys(key_hash);

```

第 19 条 — 创建索引（第 11 个）

```

    CREATE INDEX IF NOT EXISTS idx_api_keys_identity ON api_keys(identity);

```

第 20 条 — 创建索引（第 12 个）

```

    CREATE INDEX IF NOT EXISTS idx_bundles_created_by ON bundles(created_by);

```

第 21 条 — 创建索引（第 13 个）

```

    CREATE INDEX IF NOT EXISTS idx_bundles_archived_at ON bundles(archived_at);

```

第 22 条 — 创建索引（第 14 个）

```

    CREATE INDEX IF NOT EXISTS idx_bundle_links_link_id ON bundle_links(link_id);

```

#### 如果数据库已有旧数据，需要清空重建,新数据库则忽略以下7条代码的执行

先逐条执行以下 7 条 DROP 语句（同样每次一条）：

DROP 第 1 条

```

    DROP TABLE IF EXISTS bundle_links;

```

DROP 第 2 条

```

    DROP TABLE IF EXISTS bundles;

```

DROP 第 3 条

```

    DROP TABLE IF EXISTS api_keys;

```

DROP 第 4 条

```

    DROP TABLE IF EXISTS settings;

```

DROP 第 5 条

```

    DROP TABLE IF EXISTS clicks;

```

DROP 第 6 条

```

    DROP TABLE IF EXISTS slugs;

```

DROP 第 7 条

```

    DROP TABLE IF EXISTS links;

```

执行完 7 条 DROP 后，再按上面的 第 1-22 条 顺序执行建表和建索引。

### 第六步：完成部署

所有 SQL 执行成功后，刷新 workers 页面即可正常使用。管理后台路径为 `/_/admin/`。![image.png](https://www.cunzhangblog.com/api/blob/images/36a83970c77be0f0b80d63898e44167ada8426c4.png)

### 第七步：绑定自定义域名（推荐）

Cloudflare 分配的 workers.dev 域名在某些网络环境下可能访问不稳定，可以绑定自己的域名。

在 workers 项目的设置中找到域，点击添加域名。输入你的子域名（比如 cunlink.yourdomain.com），前提是这个域名已经托管在 Cloudflare 上。

添加完成后，即可通过自定义域名访问。

### 第八步：配置 Cloudflare Access 访问控制（重要）

Cunlink 默认不内置用户认证系统，也就是说任何人都可以通过 `/_/admin/` 路径进入你的管理后台。所以部署完成后必须加一道防护。

Cunlink 内置了对 Cloudflare Access（零信任）的支持，配置方法如下：

  1. 进入 Cloudflare 左侧最下方，点击 Zero Trust
  2. 如果是第一次使用，需要创建一个团队
  3. 找到左侧的 访问控制 → 应用程序，点击新建应用程序
  4. 选择 自托管和私有，点击继续
  5. 应用程序名称：填写名称（比如 cunlink）
  6. 策略名称：创建一个新策略
  7. 选择器：选择 电子邮件，输入你的邮箱地址（可以添加多个）
  8. 操作：允许
  9. 会话持续时间：建议设置为 24 小时（时间范围内只需认证一次）
  10. 保存策略并创建应用程序

配置完成后，再访问管理后台会自动跳转到 Cloudflare Access 的登录页面，输入邮箱接收验证码才能进入。非授权邮箱会被拦截。

如果你同时想限制 Cloudflare 分配的 workers.dev 域名的后台访问，也给它添加同样的策略即可。甚至可以直接在 workers 的域设置中把 workers.dev 域名关掉，只保留自定义域名访问。

### 本地开发（可选）

如果你的开发环境有 Node.js 22+ 和 Yarn：

```

    yarn install
    npx wrangler d1 migrations apply DB --local
    npx wrangler dev

```

在项目根目录创建 `.dev.vars` 文件可以免登录开发：

```

    DEV_IDENTITY=dev@local

```

## 我的部署体验

测试环境：

  * 平台：Cloudflare Workers + Pages（免费套餐）
  * 数据库：D1（免费额度内）
  * 缓存：KV（免费额度内）

部署结果：

✅ 顺利的地方：

  * workers 连接 Git 部署非常顺，Push 代码后自动构建
  * D1 Console 虽然每次只能执行一条 SQL，但操作路径清晰
  * 部署完成后页面响应很快，短链接跳转基本上是毫秒级

❌ 卡住的地方：

  * 22 条 SQL 手动执行确实有点繁琐，建议第一次部署时把这篇博客打开在旁边，逐条复制
  * D1 Console 偶尔会遇到执行超时的情况，刷新一下重试就行
  * 绑定 D1 和 KV 后需要重新部署一次才能生效

## 优点和不足

### 优点

  * 零成本部署，跑在 Cloudflare 免费套餐上
  * 点击分析维度多：国家、设备、浏览器、来源、UTM 参数全都有
  * 有 SDK 和 API，可以接入自己的系统
  * 支持自定义短码和随机短码

### 不足

  * D1 Console 执行 SQL 只能逐条操作，22 条建表步骤偏多
  * 管理后台默认没有用户认证，需要自己配 Cloudflare Access
  * 目前只有 workers 部署方式，没有一键部署按钮

## 常见问题 FAQ

### Cunlink 部署需要花钱吗？

不需要。全部跑在 Cloudflare 免费套餐上。D1 和 KV 都有免费额度，个人使用完全够用。

### 数据库初始化必须执行 22 次 SQL 吗？

是的。D1 Console 每次只能执行一条 SQL。本文第五步已经列好了全部 22 条代码和 7 条 DROP 语句，直接逐条复制执行即可。

### 管理后台怎么登录？

Cunlink 默认不内置用户认证。建议使用 Cloudflare Access 保护 `/_/admin/*` 路径，配置邮件验证码或 OAuth 登录。

### Cunlink 支持自定义短码吗？

支持。创建短链接时可以手动输入自定义短码，也可以让系统自动生成 3 位随机短码。

### 点击分析能看哪些数据？

可以查看来源域名、国家/地区、设备类型、操作系统、浏览器、语言、UTM 参数，以及是否为机器人访问。

## 总结

本文介绍了 Cunlink 短链接系统的完整部署流程。

通过实际部署测试：

  1. 基于 Cloudflare Workers + D1，零成本自建短链服务
  2. 部署的核心门槛在数据库初始化（22 条 SQL 需逐条执行）
  3. 功能完整度高：点击分析、分组管理、API、SDK、浏览器扩展全都有

如果你需要一款能自己掌控的短链接系统，而且已经有 Cloudflare 账号，Cunlink 值得花半小时部署。

## 相关资源

GitHub 仓库：<https://github.com/cunzhangcrypto/cunlink>

官网博客：<https://cunzhangblog.com/>

Cloudflare：<https://cloudflare.com/>

原项目 shrtnr：<https://github.com/oddbit/shrtnr>

❤️ 请村长
