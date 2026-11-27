---
title: workbuddy2api-hub部署教程
date: '2026-09-20 12:00:00'
cover: /img/covers/workbuddy2api-hub.jpg
description: 直接 Docker Compose 部署 如果你是在 Linux / Ubuntu / Debian / NAS / VPS 上： git clone https://github.com/ardeyouxipianyi/workbuddy2api-hub.git cd work
---
### 直接 Docker Compose 部署

如果你是在 Linux / Ubuntu / Debian / NAS / VPS 上：

```
 
    git clone https://github.com/ardeyouxipianyi/workbuddy2api-hub.git
    cd workbuddy2api-hub
    
    docker compose up -d --build  
      
    
    
    那升级非常简单，进入项目目录后执行：
    cd workbuddy2api-hub
    

```

git pull docker compose down docker compose up -d \--build  
  
  
  
  
最新脚本  

```

    curl -fsSL https://raw.githubusercontent.com/ardeyouxipianyi/workbuddy2api-hub/main/quick-deploy.sh | bash  
    
    

```

`

`

