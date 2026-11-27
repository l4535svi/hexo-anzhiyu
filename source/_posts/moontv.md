---
title: MoonTv 一键搭建数据接口
date: '2026-11-19 12:00:00'
cover: /img/covers/moontv.jpg
tags:
- MoonTv 资源
categories:
- MoonTv 资源
description: 使用方法： https://moontv.gyx.workers.dev/?url=https://raw.githubusercontent.com/666zmy/MoonTV/refs/heads/main/config.json&pretty=true addEventLi
---
使用方法：  https://moontv.gyx.workers.dev/?url=https://raw.githubusercontent.com/666zmy/MoonTV/refs/heads/main/config.json&pretty=true

  

addEventListener('fetch', event => {

  event.respondWith(handleRequest(event.request))

})

  

async function handleRequest(request) {

  try {

    // 解析 URL 参数

    const url = new URL(request.url)

    const targetUrl = url.searchParams.get('url')

   

    if (!targetUrl) {

      return new Response('Missing url parameter', { status: 400 })

    }

   

    // 验证 URL 格式

    try {

      new URL(targetUrl)

    } catch {

      return new Response('Invalid URL format', { status: 400 })

    }

   

    // 从远程获取 JSON

    const response = await fetch(targetUrl)

   

    if (!response.ok) {

      return new Response(`Failed to fetch: ${response.status}`, { status: response.status })

    }

   

    const jsonData = await response.json()

   

    // 对 JSON 做 base58 编码

    const jsonString = JSON.stringify(jsonData)

    const encoded = base58Encode(jsonString)

   

    return new Response(encoded, {

      headers: {

        'Content-Type': 'text/plain',

        'Access-Control-Allow-Origin': '*'

      }

    })

   

  } catch (error) {

    return new Response(`Error: ${error.message}`, { status: 500 })

  }

}

  

// Base58 编码实现

function base58Encode(str) {

  const ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

  const bytes = new TextEncoder().encode(str)

 

  if (bytes.length === 0) return ''

 

  let num = BigInt('0x' + Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join(''))

 

  if (num === 0n) return ALPHABET[0]

 

  let result = ''

  while (num > 0n) {

    result = ALPHABET[Number(num % 58n)] + result

    num = num / 58n

  }

 

  // 处理前导零

  for (let i = 0; i < bytes.length && bytes[i] === 0; i++) {

    result = ALPHABET[0] + result

  }

 

  return result

}
