---
title: https://github.com/wenfxl/openai-cpa/tree/v8.9.1项目升级教程
date: '2026-04-09 12:00:00'
cover: /img/covers/httpsgithubcomwenfxlopenai-cpatreev891.jpg
tags:
- GPT
categories:
- GPT
description: 把升级的文件拉进去之后执行这些命令都可以了 1.项目有 requirements.txt ，必须装： pip3 install -r requirements.txt 统一用这个： python3 -m pip install -r requirements.txt python
---
把升级的文件拉进去之后执行这些命令都可以了

  

1.项目有 `requirements.txt`，必须装：

```
 
    pip3 install -r requirements.txt

```

统一用这个：

```
 
    python3 -m pip install -r requirements.txt  
    python3 wfxl_openai_regst.py

```

  

## 八、最短解决路径（只做这3步）

直接执行：

```
 
    cd /home/ubuntu/gpt  
    python3 -m pip install -r requirements.txt  
    python3 wfxl_openai_regst.py

```

  

长期后台运行命令，现测试能不能运行，然后再运行这个

nohup python3 wfxl_openai_regst.py > run.log 2>&1 &

  

  

更新无法运行都运行依赖安装

#### 如果没用虚拟环境

```
 
    pip3 install pymysql

```

  

### 直接执行（最简单）

cd /home/ubuntu/gpt

```

    unzip Wenfxl-Codex-Manager-v12.0.2.zip

```

→ 会解压到当前目录（gpt文件夹） 

* * *

### 推荐方式（避免文件混乱）

```

    mkdir codex  
    unzip Wenfxl-Codex-Manager-v9.0.1.zip -d codex

```

→ 解压到 `codex` 文件夹，不污染当前目录 

  

  

  

  

  

 结论：**用`nohup` 或 `screen`，不要再用前台运行**。你现在已经能启动，下一步只是“守护运行”。

* * *

## 一、最直接方案（推荐）

```
 
    nohup python3 wfxl_openai_regst.py > log.txt 2>&1 &
    
      
    
    
      
    
    
      
    
    
      
    
    
      
    
    
      
    
    
      
    
    
      
    
    
      
    
    
      
    
    
    # **二：docker项目部署教程**
    
    **  
    **
    
    **  
    **
    
    **  
    **
    
    **  
    **
    
    **  
    **
    
    **  
    **
    
    ## **更新  
    ** 方法 2：手动更新 Docker 镜像
    
    
    
    
    
        1. 
         
    
    
        1. 停止容器：
    
    docker compose down
      
        2. 拉取最新镜像：
    
    docker pull wenfxl/wenfxl-codex-manager:latest
    
    ## 3：
    
    ## 需要cd /home/ubuntu/gpt，才能执行下面命令成功
    
    ## 
    
    
    
    
    ## 
      
        3. 启动容器：
    
    docker compose up -d
      
        * 如果你改过本地 
    
    
        * 如果你改过本地 Dockerfile 或配置文件，需要先 docker build -t wenfxl-codex-manager:latest . 再 up -d。
    
    
    
    
    
    [![](https://blogger.googleusercontent.com/img/a/AVvXsEjGWs0sOPasUw68V7ez7BWat2kqMZ4Rn3k2-4vCrLi-2Rj5B3Zs6Bko_7efkmR3HwEZu0aGlXVYIPsL7ikYDBg5ofBx9ca_qoUj1NGfU2XgsVsqwoiBjOLALz8woOzLnQz51P373auN5UoIgO6X5CsD2l9SazcuyYKf-W6j-DNOp77_neV90DijBgAoYTLw=w689-h240)](https://blogger.googleusercontent.com/img/a/AVvXsEjGWs0sOPasUw68V7ez7BWat2kqMZ4Rn3k2-4vCrLi-2Rj5B3Zs6Bko_7efkmR3HwEZu0aGlXVYIPsL7ikYDBg5ofBx9ca_qoUj1NGfU2XgsVsqwoiBjOLALz8woOzLnQz51P373auN5UoIgO6X5CsD2l9SazcuyYKf-W6j-DNOp77_neV90DijBgAoYTLw)
    
      
    access_token----Cookie
      
    这个网站是获取token的:https://chatgpt.com/api/auth/session
    
    ## 这个网站是获取cook的:https://admin.openai.com/  
      
    
    
    [![](https://blogger.googleusercontent.com/img/a/AVvXsEgmnak6N_lapSw8IpgkyDne1W5abmSR-dKJAoG2Xb7zBJnxlZRiz5fJnZjy-__5Z2jhYEfMi9ogOPCHMFPE4RtXwyGR1VgH-rdNsB2e9pmf0ncMOVLZWLfU0jXEsrUYXl3nrAouDR_ftzpQ5FuJiZryD69LMJ1-zPHFPTUyONsjPKCWJWhg-l1eqfRt-0fL=w785-h266)](https://blogger.googleusercontent.com/img/a/AVvXsEgmnak6N_lapSw8IpgkyDne1W5abmSR-dKJAoG2Xb7zBJnxlZRiz5fJnZjy-__5Z2jhYEfMi9ogOPCHMFPE4RtXwyGR1VgH-rdNsB2e9pmf0ncMOVLZWLfU0jXEsrUYXl3nrAouDR_ftzpQ5FuJiZryD69LMJ1-zPHFPTUyONsjPKCWJWhg-l1eqfRt-0fL)
    
      
      
      
    

```

```

  

```

