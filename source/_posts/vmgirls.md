---
title: vmgirls爬取经验
date: '2021-03-17 12:00:00'
tags:
- 免费图库
categories:
- 免费图库
description: 导入模块 首先我们要导入此次需要用到的模块 requests是使用Apache2 licensed 许可证的HTTP库。比urllib2模块更简洁。 Request支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动响应内容的编码，支持国际化的URL
---
导入模块  
首先我们要导入此次需要用到的模块

requests是使用Apache2 licensed 许可证的HTTP库。比urllib2模块更简洁。

Request支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动响应内容的编码，支持国际化的URL和POST数据自动编码。

在python内置模块的基础上进行了高度的封装，从而使得python进行网络请求时，变得人性化，使用Requests可以轻而易举的完成浏览器可有的任何操作。

现代，国际化，友好。

requests会自动实现持久连接keep-alive

parsel主要用来将请求后的字符串格式解析成re,xpath,css进行内容的匹配

os模块提供了非常丰富的方法用来处理文件和目录。

time时间模块，用于设定延时，避免网站崩溃

urllib.parse 模块提供了很多解析和组建 URL 的函数。由于网页中所有的图片都采用相对路径，所以需要用到urljoin函数将网址进行整合。

相关代码：

Python  
1  
2  
3  
4  
5  
6

# 导入模块

import requests  
import parsel  
import os  
import time  
from urllib import parse  
请求头与网址  
由于网站采取了一定的反爬机制，我们要用user-agent进行伪装。

相关代码：

Python  
1  
2  
3  
4  
5

# 请求头

headers ={  
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'  
}  
url = 'https://www.vmgirls.com/13344.html'  
请求网页  
使用requests模块中的get（）函数来模拟访问并将得到的内容保存在变量response中，并将获得的网页内容用文本形式显示出来。

相关代码：

Python  
1  
2  
3

# 请求网页

response = requests.get(url=url, headers=headers)  
html = response.text  
解析网页  
利用 XPath 进行 HTML 的解析，获取想要得到的图片地址列表data_list与文件夹名dir_name

相关代码：

Python  
1  
2  
3  
4  
5  
6  
7

# 解析网页

pars = parsel.Selector(html)  
data_list = pars.xpath('//div[@class="nc-light-gallery"]/p/a/@href').getall()

# 获取文件夹名

dir_name = pars.xpath('//div[@class="nc-light-gallery"]/p/a/img/@alt').get()  
if not os.path.exists(dir_name):  
os.mkdir(dir_name)  
保存图片  
保存图片数据到本地

加一秒延迟，防止网站崩溃。  
将获取到的相对路径转为绝对路径  
将数据以二进制形式保存  
设置文件夹名文件名  
相关代码：

Python  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
for img in data_list:  
# 加一秒延迟  
time.sleep(1)  
# 相对路径转为绝对路径  
img_url = parse.urljoin('http://www.vmgirls.com/', img)  
data = requests.get(url=img_url, headers=headers).content  
# 获取图片名  
file_name = img_url.split('/')[-1]  
with open(dir_name + '/' + file_name, mode='wb') as f:  
f.write(data)  
print('正在保存', file_name)  
完整代码  
Python  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  
31  
32  
import requests  
import parsel  
import os  
import time  
from urllib import parse

# 请求头与网址

headers ={  
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'  
}  
url = 'https://www.vmgirls.com/13344.html'

# 请求网页

response = requests.get(url=url, headers=headers)  
html = response.text

# 解析网页

pars = parsel.Selector(html)  
data_list = pars.xpath('//div[@class="nc-light-gallery"]/p/a/@href').getall()

# 获取文件夹名

dir_name = pars.xpath('//div[@class="nc-light-gallery"]/p/a/img/@alt').get()  
if not os.path.exists(dir_name):  
os.mkdir(dir_name)

# 保存图片

for img in data_list:  
# 加一秒延迟  
time.sleep(1)  
# 相对路径转为绝对路径  
img_url = parse.urljoin('http://www.vmgirls.com/', img)  
data = requests.get(url=img_url, headers=headers).content  
# 获取图片名  
file_name = img_url.split('/')[-1]  
with open(dir_name + '/' + file_name, mode='wb') as f:  
f.write(data)  
print('正在保存', file_name)  
爬取成功

其他方法  
Python  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  
31  
32  
import time  
from urllib import parse  
import requests  
import re  
import os

# 请求头

headers ={  
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'  
}  
url_ = 'https://www.vmgirls.com/13344.html'  
response = requests.get(url=url_, headers=headers)  
html = response.text

# 获取文件夹名

dir_name = re.findall('

# (.*?)

', html)[-1]  
if not os.path.exists(dir_name):  
os.mkdir(dir_name)

# 解析网页

urls = re.findall('[', html)](\(.*?\))

# 保存图片

for url in urls:  
# 加一秒延迟  
time.sleep(1)  
# 把相对路径转为绝对路径  
url = parse.urljoin('http://www.vmgirls.com/', url)  
print(url)  
# 文件名  
file_name = url.split('/')[-1]  
response = requests.get(url=url, headers=headers)  
# 以二进制形式存储  
with open(dir_name + '/' + file_name, mode='wb') as f:  
f.write(response.content)  
print('正在保存', file_name)  
文章作者: 王小二  
文章链接: https://www.wangxe.top/2020/08/23/vmgirls/  
版权声明: 本博客所有文章除特别声明外，均采用 CC BY-NC-SA 4.0 许可协议。转载请注明来自 王小二！
