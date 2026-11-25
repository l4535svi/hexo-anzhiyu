---
title: CFnew 独立面板部署教程：Vercel 一键部署，面板与 Worker 分开运行
date: '2026-10-19 12:00:00'
tags:
- cloudflare项目
categories:
- cloudflare项目
description: 把 CFnew 面板搬出 Cloudflare，现在可以直接点按钮部署到 Vercel。每个人都能部署自己的面板，源码也单独放在了 cfnew-panel 仓库。 Worker 继续处理代理连接和保存配置；Vercel 负责控制台、优选操作和订阅生成。节点流量直接连接你的 Wor
---
把 CFnew 面板搬出 Cloudflare，现在可以直接点按钮部署到 Vercel。每个人都能部署自己的面板，源码也单独放在了 `cfnew-panel` 仓库。

Worker 继续处理代理连接和保存配置；Vercel 负责控制台、优选操作和订阅生成。节点流量直接连接你的 Worker，不绕面板服务器。这里分开的是面板运行位置，Worker 依然使用 Cloudflare。

## 部署入口

  * 面板源码：[byJoey/cfnew-panel](https://github.com/byJoey/cfnew-panel)
  * 配套精简内核：[cfnew / core-only](https://github.com/byJoey/cfnew/tree/core-only)
  * 一键部署：[部署到 Vercel](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FbyJoey%2Fcfnew-panel&project-name=cfnew-panel&repository-name=cfnew-panel)

[](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FbyJoey%2Fcfnew-panel&project-name=cfnew-panel&repository-name=cfnew-panel)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FbyJoey%2Fcfnew-panel&project-name=cfnew-panel&repository-name=cfnew-panel)

需要准备 GitHub、Vercel 和 Cloudflare 账号。面板不需要单独买服务器，也不需要给 Vercel 配数据库。想在线保存配置，需要给 Worker 绑定 Cloudflare KV。

“一键部署” 会替你带入仓库和项目设置。第一次仍要登录账号、授权 GitHub、创建项目，再点 Deploy；这些是平台自己的流程。

## 先部署精简 Worker 内核

已经在用 `core-only` 分支的用户，可以保留原来的 Worker、UUID 和 KV，直接往下部署面板。

原 `main` 是完整版本。这篇教程配套的是 `core-only` 精简内核，别拿错分支。

### 新建 Worker

  1. 打开 [core-only 分支](https://github.com/byJoey/cfnew/tree/core-only)，下载 `_worker.js`。
  2. 进入 Cloudflare 的 Workers & Pages，创建一个 Worker。可以先部署默认的 Hello World，再进入 Edit code。
  3. 用下载的 `_worker.js` 完整替换编辑器里的代码，点击 Deploy。
  4. 到 Worker 的 Settings → Variables and Secrets，新增变量 `u`，值填你自己的 UUID，保存并部署。大写 `U` 也支持。
  5. 在运行时设置里，将兼容日期设为 `2026-01-20`。
  6. 给 Worker 绑定一个自己能正常访问的域名。没有自定义域名时，也可以先用可访问的 `workers.dev` 地址。

UUID 要自己生成，不要照抄别人截图里的。macOS / Linux 可以运行：
[code]
    uuidgen  
    ---
[/code]  
  
Windows PowerShell：
[code]
    [guid]::NewGuid().ToString()  
    ---
[/code]  
  
如果你用 Cloudflare Pages，可以下载同一分支的 `pages.zip`，通过 Pages 直接上传，再设置 `u` 和 KV 绑定。

### 给 Worker 绑定自定义域名

如果第 6 步还没绑，可以这样做：

  1. 进入刚部署的 Worker，打开 Settings → Domains & Routes。
  2. 点击 Add → Custom Domain，填写例如 `worker.example.com`。
  3. 使用已在同一 Cloudflare 账号里正常托管的域名，确认后添加，等待域名和证书生效。
  4. 用 `https://worker.example.com` 打开，精简内核返回 `hello` 即可。

Cloudflare 会为 Worker 自定义域名创建对应的 DNS 记录和证书，不要再把这个域名 CNAME 到 Vercel。Vercel 面板另外用 `panel.example.com`，具体操作见后面的 “给 Vercel 面板绑定自己的域名”。

### 绑定 KV

到 Cloudflare 创建一个 KV 命名空间，再到刚才 Worker 的 Settings → Bindings 添加 KV 绑定，变量名填 `C` 或 `c`，选中这个命名空间，保存部署。

没有 KV 也能读取环境变量、生成订阅，但页面里的 “保存配置” 不能持久化。已有用户继续用原绑定，别为了换面板把 KV 删掉重建。

完成后打开 Worker 根域名，看到 `hello` 就是正常现象。精简内核的页面和订阅已经移到独立面板里，Worker 首页不会再显示控制台。

## 一键部署到 Vercel

点击文章上面的 Deploy 按钮。页面会先显示来源仓库 `byJoey/cfnew-panel`，确认是这个项目，再按提示登录。

![Vercel 一键部署页面，来源仓库为 byJoey/cfnew-panel](https://images.joeyblog.net/2026/10/17/cfnew-vercel-deploy-step.png)

  1. 登录 Vercel，按提示连接自己的 GitHub 账号。
  2. 选择保存代码的 GitHub 账号，创建仓库副本，名称可用 `cfnew-panel`。如果这个名称已经被占用，换一个即可。
  3. 项目使用仓库根目录。Application Preset（旧界面叫 Framework）选择 Other；如果自动识别成 Node，请手动改为 Other。不用自己填构建命令。
  4. 点击 Deploy，等待部署完成。
  5. 打开 Vercel 分配的 `你的项目.vercel.app` 地址。

下面是从零导入时的实际配置页。Root Directory 保持 `./`，Application Preset 选 `Other`；本次按这个配置成功部署。

![Vercel 新建项目配置：仓库根目录、项目名称和 Other 预设](https://images.joeyblog.net/2026/10/17/cfnew-vercel-create-config.png)

出现 Congratulations 就说明第一次部署已经完成，点击 Continue to Project 进入项目。

![Vercel 从零部署成功页面](https://images.joeyblog.net/2026/10/17/cfnew-vercel-deploy-success.png)

部署完成后，在项目 Overview 中确认 Status 为 Ready，Domains 下就是给用户访问的面板地址。截图来自这次从 GitHub 导入后重新创建的独立项目。Source 显示 `main` 和提交号，后续推送会自动触发部署。

![Vercel 项目总览中的正式部署状态 Ready 和面板域名](https://images.joeyblog.net/2026/10/17/cfnew-vercel-git-ready.png)

仓库列表为空时，先到 Vercel 账号的 Authentication → Sign-in Methods 连接 GitHub，再返回项目创建页。

如果 GitHub 中已经有自己的 `cfnew-panel` 仓库，可以在 New Project → Import Git Repository 直接选择现有仓库；已有源码保留，不需要再次创建同名副本。

第一次不设置任何变量，会进入公共模式：首页有 Worker 域名和 UUID / 自定义路径两个输入项。

![公共模式的 Worker 连接入口](https://images.joeyblog.net/2026/10/17/cfnew-panel-public-rebuilt.png)

填你的 Worker 域名，例如 `worker.example.com`，再填 Worker 变量 `u` 对应的 UUID，即可进入控制台。域名不要附带 UUID 或其他路径。

这里的 “公共” 指允许接入不同人的兼容 Worker，仍然需要对应的 UUID 或自定义入口路径。

## 给 Vercel 面板绑定自己的域名

不想用 `项目名.vercel.app`，可以换成自己的域名。下面用独立部署的 `cfnew-domain-demo` 演示，实际绑定 `cfnew-domain-demo.joeyblog.tech`。这一节的 8 张图都来自本次操作，已经走完 DNS 解析和 HTTPS 验证。截图用的演示环境已在教程完成后清理，请用自己的项目和域名操作。

先分清两个地址：

地址| 绑定到哪里| 用来做什么  
---|---|---  
`panel.example.com`| Vercel 面板项目| 打开控制台、更新订阅  
`worker.example.com`| Cloudflare Worker| 代理连接、读取和保存配置  
  
两者可以用同一个主域名下的不同子域名，不要把同一个完整域名同时绑到 Vercel 和 Worker。只换面板域名时，`w` 仍然填原来的 Worker 地址。

### 第一步：确认面板已经部署成功

按上面的部署步骤完成后，进入项目 Overview，确认 Production Deployment 是 Ready。已有可用项目直接用原项目，不需要像演示这样再建一份。

![独立演示项目已部署成功，正式部署状态为 Ready](https://images.joeyblog.net/2026/10/17/cfnew-domain-deployed.jpg)

### 第二步：在 Vercel 添加自己的域名

打开面板项目的 Domains。新版界面直接放在左侧；旧版通常在 Settings → Domains。点击 Add Existing，旧版按钮可能叫 Add。

![Vercel 项目 Domains 页面，右上角 Add Existing 用于添加已有域名](https://images.joeyblog.net/2026/10/17/cfnew-domain-settings.jpg)

输入准备给面板用的完整域名，例如 `panel.example.com`，不用写 `https://`，也不用带 UUID 或路径。选择 Connect to an environment → Production，然后点 Add Domain。这里是连接到正式部署，不要选成跳转到另一个域名。

![填写本次演示域名，连接 Production 环境后添加](https://images.joeyblog.net/2026/10/17/cfnew-domain-add.jpg)

### 第三步：复制 Vercel 给出的 DNS 记录

刚加完显示 Invalid Configuration 很正常，因为 DNS 还没有指过去。展开 View DNS configuration，查看它要求的 Type、Name、Value。

这次 Vercel 给的是一条 CNAME，Proxy 要求 Disabled。每个项目分到的目标可能不同，请复制自己页面的值，不要照抄截图里的目标，也不要只凭旧教程填写固定 IP。

![展开实际 DNS 配置，Vercel 给出 CNAME 名称、目标和关闭代理的要求](https://images.joeyblog.net/2026/10/17/cfnew-domain-dns-required.jpg)

### 第四步：到 Cloudflare 添加 CNAME

域名已经托管在 Cloudflare 的，进入对应主域名的 DNS → 记录 → 添加记录。以 `panel.example.com` 为例：

字段| 怎么填  
---|---  
类型| `CNAME`  
名称| `panel`  
目标| 粘贴自己 Vercel 页面给出的 Value，只填域名  
代理状态| 仅 DNS，灰云  
TTL| 自动  
  
下面是这次实际填写的记录。名称用了 `cfnew-domain-demo`，所以最终地址是 `cfnew-domain-demo.joeyblog.tech`。

![Cloudflare 新增 CNAME 的实际表单，目标取自 Vercel，代理状态为仅 DNS](https://images.joeyblog.net/2026/10/17/cfnew-domain-cloudflare-form.jpg)

点击保存，列表里应能看到这条 CNAME，代理状态仍是 仅 DNS。

![Cloudflare 已保存的演示 CNAME 记录，状态为仅 DNS，TTL 自动](https://images.joeyblog.net/2026/10/17/cfnew-domain-cloudflare-saved.jpg)

如果同一个名称已经有旧的 A、AAAA 或 CNAME，先确认旧记录服务的是谁，再处理冲突；别把正在用的博客或 Worker 记录直接覆盖掉。新增一个没用过的子域名最省事。

如果绑定的是根域名 `example.com`，按 Vercel 实际给出的 A 记录等要求填写，主机名通常是 `@`。域名在其他 DNS 服务商管理的，也到那家的解析页面添加；不必为了绑定这一个面板就迁移整个域名的 NS。

这里的灰云针对 Vercel 面板域名。Worker 的自定义域名由 Cloudflare 管理，不要把 Worker 记录也照着改成灰云。

### 第五步：等验证通过和 HTTPS 证书签好

回到 Vercel 的 Domains，点击这个域名旁边的 Refresh。DNS 生效后可能短暂显示 Generating SSL Certificate，等它完成。本次最终变为 Valid Configuration。

![演示自定义域名已通过 Vercel 验证，状态为 Valid Configuration，连接 Production](https://images.joeyblog.net/2026/10/17/cfnew-domain-valid.jpg)

Vercel 会自动签发和续期 HTTPS 证书，一般不用自己上传。然后直接用 `https://你的面板域名` 打开验证。

下面是本次自定义域名实际打开后的页面。演示没有设置 `w`，所以首页显示公共连接表单；设置了 `w` 的项目首页会显示 `hello`，需要在地址后面加 `/你的UUID` 进入。

![通过本次自定义域名 HTTPS 打开的 CFnew 面板，公共连接页正常显示](https://images.joeyblog.net/2026/10/17/cfnew-domain-live.jpg)

### 第六步：换成新域名的订阅

绑定完成后，重新用新域名打开面板，再复制订阅。客户端里以前保存的旧链接不会自己换域名，需要手动替换。
[code]
    控制台：https://panel.example.com/你的UUID  
    ---  
    订阅：  https://panel.example.com/你的UUID/sub?target=clash
[/code]  
  
公共模式仍然从首页填写 Worker 域名和 UUID。只绑定面板域名，不需要修改 Worker 的 `u` 或 KV，也不需要把 `w` 改成面板地址。

如果一直没成功，先对照这几项：

  * Invalid Configuration：检查名称、记录类型、目标是否和自己 Vercel 页面一致，代理是否为灰云，以及同名旧记录是否冲突。
  * 要求验证域名归属：按 Vercel 当场给出的名称和值补 TXT 记录，再验证；CNAME 负责解析，TXT 负责证明归属。
  * 证书一直签不下来：先确认 DNS 已生效，再检查域名的 CAA 限制，按 Vercel 提示处理。不要跳过浏览器证书警告。
  * 出现其他网站或跳转到旧地址：检查是否加到了错误项目、误选 Redirect，或者同名地址还命中了旧服务。
  * 浏览器能开，客户端更新失败：继续看下文的 Deployment Protection 排查。用新域名验证时，客户端也要换成新域名的订阅。

平台后续调整按钮位置时，可对照 [Vercel 官方域名配置说明](https://vercel.com/docs/domains/working-with-domains/add-a-domain)。

## 只管理自己的 Worker：设置 w

只想给自己的 Worker 用，就在 Vercel 面板项目里设置小写变量 `w`。

进入 Settings → Environment Variables：

项目| 填写内容  
---|---  
Name| `w`  
Value| `https://worker.example.com`，替换成自己的 Worker 根地址  
Environment| Production；要让预览部署也绑定时，再选 Preview  
  
保存后，Environment Variables 列表里应能看到 `w`，右侧显示它生效的环境。下面这张实测截图同时设置了 Production 和 Preview；变量值由 Vercel 默认遮盖。

![Vercel 环境变量页面中的 w，生效环境为 Production 和 Preview](https://images.joeyblog.net/2026/10/17/cfnew-vercel-w-rebuilt.png)

保存后，进入 Deployments，对正式部署执行 Redeploy。环境变量修改后，已经生成的旧部署不会自动变化。

`w` 只填 Worker 根地址，不要带 UUID、`/sub`、自定义路径或查询参数。它设置在 Vercel 面板项目，Worker 内核不用添加这个变量。

填写后，面板的行为变成：

  * 首页只返回 `hello`，没有连接表单，也没有 Worker 域名输入框。
  * 用 `https://面板域名/你的UUID` 直接打开原控制台。
  * 用 `https://面板域名/你的UUID/sub` 更新订阅。
  * 换查询参数也不能让这个面板连接其他 Worker。

例如，你的面板是 `panel.example.com`，Worker 是 `worker.example.com`。`w` 填后者，浏览器打开前者加 UUID。
[code]
    w=https://worker.example.com  
    ---  
       
    控制台：https://panel.example.com/你的UUID  
    订阅：  https://panel.example.com/你的UUID/sub
[/code]  
  
![绑定 Worker 后直接进入原控制台，截图中的访问凭据已遮盖](https://images.joeyblog.net/2026/10/17/cfnew-panel-bound-rebuilt.png)

如果 Worker 的 `d` 设置为 `/Admin/Panel`，也可以通过 `https://panel.example.com/Admin/Panel` 进入。路径区分大小写。登录后面板使用稳定的 UUID 地址，之后修改 `d`，已复制的订阅和当前面板重载仍能用。

`w` 留空或删掉后重新部署，就会恢复公共连接页。`w` 负责限制接入哪个 Worker，UUID / 自定义路径继续负责访问验证。

## 复制订阅到客户端

在面板里设置协议、优选地址，然后复制客户端对应的订阅链接。不要继续使用 Worker 上旧的 `/sub` 地址。

固定 Worker 的 Clash 订阅示例：
[code]
    https://panel.example.com/你的UUID/sub?target=clash  
    ---
[/code]  
  
公共模式示例：
[code]
    https://panel.example.com/sub?host=worker.example.com&uuid=你的UUID&target=clash  
    ---
[/code]  
  
也支持 `singbox`、`surge`、`loon`、`quanx`、`stash`、`base64` 和 `v2ray`。不指定时，按客户端请求头识别格式。各客户端对协议的支持不同，生成前先在面板启用客户端能使用的协议。

订阅地址里有访问凭据，别贴到公开群或截图里。换面板域名后，客户端也要换成新域名的订阅。

## 浏览器能打开，客户端却更新失败

先用未登录 Vercel 的浏览器打开你的面板域名。

如果出现 Vercel 登录页，到 Settings → Deployment Protection 调整 Vercel Authentication，让实际使用的面板域名允许公开访问。再用客户端更新一次。

浏览器里已经登录 Vercel，只能证明你有平台访问权；订阅客户端不会跟着拿到这份登录状态。不要把 Vercel 账号令牌塞进订阅地址。

如果加了自定义域名，用最终给客户端的那个域名验证。Preview 和 Production 的变量、域名与访问保护可能不同。

## 几个容易踩的坑

设置 w 后首页只剩 hello。 这是绑定模式的正常入口。请访问面板域名加 `/UUID` 或自定义路径。

出现 “读取配置失败”。 核对 Worker 域名是否能访问、UUID 是否一致，以及是否部署了 `core-only` 内核。面板不兼容只有静态网页、没有配置接口的 Worker。

修改 w 没变化。 确认环境选对了，并重新部署。之前发出的某个 Preview 链接仍可能保留旧变量，要打开新部署或正式域名。

优选检测的延迟和手机不一样。 在线检测由面板服务器发起，显示的是服务器视角。最终连通性和延迟以自己的客户端为准。

IPv6 在线检测失败。 这次 Vercel 环境实测 IPv4 检测可用，IPv6 在线检测遇到了平台出站错误。但 IPv6 节点生成和 Worker 实际代理连接已经验证，不能把在线检测失败直接理解成 IPv6 节点不能用。需要完整 IPv6 检测时，可将同一面板部署到支持 IPv6 出站的自有服务器。

GitHub Pages 能不能部署？ 这个面板需要服务端处理配置转发、订阅转换和在线检测，GitHub Pages 只能托管静态文件，所以不能直接替代 Vercel Functions。

## 后续更新与迁移

通过按钮创建的是你自己的仓库副本。面板更新时，需要把上游代码同步到自己的仓库并重新部署；连接了 Git 集成的 Vercel 项目，会按该项目的分支设置自动构建。

升级 Worker 时保留 `u`、KV 绑定和原配置；升级面板时保留 `w` 与域名设置。两边分开更新，别把 “面板升级” 当成 “重新建一个 Worker”。

也可以把这个仓库部署到自有服务器。安装 Node.js 22 后运行 `npm start`，或使用仓库中的 Docker Compose，再通过 HTTPS 反代访问。

源码和完整说明都放在 [cfnew-panel](https://github.com/byJoey/cfnew-panel)。有问题可以到 [TG 群](https://t.me/+ft-zI76oovgwNmRh) 交流。

## 修改和二次发布

允许合法修改、二次开发和 AI 辅助维护。基于本仓库源码改写相同逻辑后，仍须保留来源和版权说明，禁止把这类衍生实现冒充为与本项目无关的完全原创代码。自己新增的独立贡献可以单独说明。

本版本采用 [CFnew 源码使用与署名许可](https://github.com/byJoey/cfnew-panel/blob/main/LICENSE)，属于自定义许可；此前已按 MIT 发布的版本仍保留原授权。第三方代码和规则数据继续遵循各自许可。
