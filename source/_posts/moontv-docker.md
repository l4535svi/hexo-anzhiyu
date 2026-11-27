---
title: MoonTV 的Docker 搭建
date: '2026-03-02 12:00:00'
cover: /img/covers/moontv-docker.jpg
tags:
- 影视大全
categories:
- 影视大全
description: 'Docker 部署 Kvrocks 存储（推荐） services: moontv-core: image: ghcr.io/mtvpls/moontvplus:latest container_name: moontv-core restart: on-failure port'
---
### Docker 部署

[](https://github.com/tao-t356/MoonTVPlus#docker-%E9%83%A8%E7%BD%B2)

#### Kvrocks 存储（推荐）

 ______
[code]
    services:  
    ---  
      moontv-core:  
        image: ghcr.io/mtvpls/moontvplus:latest  
        container_name: moontv-core  
        restart: on-failure  
        ports:  
          - '3000:3000'  
        environment:  
          - USERNAME=admin  
          - PASSWORD=admin_password  
          - NEXT_PUBLIC_STORAGE_TYPE=kvrocks  
          - KVROCKS_URL=redis://moontv-kvrocks:6666  
        networks:  
          - moontv-network  
        depends_on:  
          - moontv-kvrocks  
      moontv-kvrocks:  
        image: apache/kvrocks  
        container_name: moontv-kvrocks  
        restart: unless-stopped  
        volumes:  
          - kvrocks-data:/var/lib/kvrocks/data  
        networks:  
          - moontv-network  
    networks:  
      moontv-network:  
        driver: bridge  
    volumes:  
      kvrocks-data:
[/code]  
  
资源连接：

 ______
[code]
    https://raw.githubusercontent.com/hafrey1/LunaTV- config/refs/heads/main/LunaTV-config.txt
[/code]
