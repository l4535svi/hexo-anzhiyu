---
title: tg推送必须部署到work代码（不然无法使用）
date: '2025-01-11 12:00:00'
tags:
- 青龙全部
categories:
- 青龙全部
description: 代码 const whitelist = [ "/bot8106029732:" ] ; const tg_host = "api.telegram.org" ; addEventListener ( 'fetch' , event => { event . respondWit
---
代码

const whitelist = ["/bot8106029732:"];

const tg_host = "api.telegram.org";

 

addEventListener('fetch', event => {

    event.respondWith(handleRequest(event.request))

})

 

function validate(path) {

    for (var i = 0; i < whitelist.length; i++) {

        if (path.startsWith(whitelist[i]))

            return true;

    }

    return false;

}

 

async function handleRequest(request) {

    var u = new URL(request.url);

    u.host = tg_host;

    if (!validate(u.pathname))

        return new Response('Unauthorized', {

            status: 403

        });

    var req = new Request(u, {

        method: request.method,

        headers: request.headers,

        body: request.body

    });

    const result = await fetch(req);

    return result;

}
