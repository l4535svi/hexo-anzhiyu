---
title: KatelyaTV各种tv搭建教程
date: '2025-09-18 12:00:00'
tags:
- 影视大全
categories:
- 影视大全
description: 'KatelyaTV version: "3.9" services: ktv: image: ghcr.io/wangai14/ktv:latest container_name: ktv restart: unless-stopped ports: - "3000:3000"'
---
[KatelyaTV](https://github.com/katelya77/KatelyaTV)

version: "3.9"

services:

  ktv:

    image: ghcr.io/wangai14/ktv:latest

    container_name: ktv

    restart: unless-stopped

    ports:

      \- "3000:3000"   # 宿主机:容器

    environment:

      \- TZ=Asia/Shanghai

已经做docker镜像了    

可以直接使用镜像仓库部署
