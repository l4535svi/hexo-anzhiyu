---
title: Codex Proxy 您的本地 Codex 编程助手中转站 将 Codex Desktop 的能力以 OpenAI 标准协议对外暴露，无缝接入任意 AI 客户端。
date: '2026-03-14 12:00:00'
cover: https://picsum.photos/seed/codex-proxy-codex-codex-desktop-openai/800/450
tags:
- OpenClaw
categories:
- OpenClaw
description: docker与领一个中转冲突需要改端口的命令 cd /root/codex-proxy sed -i 's/"1455:1455"/"18080:1455"/g' docker-compose.yml docker compose down docker compose up -
---
docker与领一个中转冲突需要改端口的命令

 cd /root/codex-proxy

sed -i 's/"1455:1455"/"18080:1455"/g' docker-compose.yml

docker compose down

docker compose up -d --build

  

全自动一件脚本

cd /root/codex-proxy && TS=$(date +%F-%H%M%S) && cp -r data data.bak.$TS 2>/dev/null; cp .env .env.bak.$TS 2>/dev/null; git stash -u; git checkout master && git pull origin master && sed -i 's/"1455:1455"/"18080:1455"/g' docker-compose.yml && docker compose down && docker compose up -d --build
