# -*- coding:utf-8 -*-

import requests
from scrapy import Selector

num = 0
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'If-Modified-Since': 'Thu, 15 Sep 2022 03:24:31 GMT',
    'If-None-Match': 'W/"63229aef-50f8"',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.greek.people.cn/517546/index68.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
url_list = []
for aaa in range(57,69):
    url_ = f'http://www.greek.people.cn/517546/index{aaa}.html'
    url_list.append(url_)
for bbb in url_list:
    response = requests.get(bbb, headers=headers)
    res = Selector(text=response.text)
    urls = res.xpath("//b/a/@href").getall()
    for url in urls:
        url = 'http://www.greek.people.cn' + url
        while True:
            try:
                response1 = requests.get(url, headers=headers)
                if response1.status_code == 200:
                    break
                else:
                    pass
            except:
                print("程序报错")
        response1.encoding='utf-8'
        res1 = Selector(text=response1.text)
        title = ''.join(res1.xpath("//h1//text()").getall()).strip()
        time1 = ''.join(res1.xpath("//*[@class='origin cf']//text()").getall()).strip()
        content = ''.join(res1.xpath("//div[@class='w1000 d2txtCon cf']/p//text()").getall()).strip()
        content_all = title + '\n' + time1 + '\n' + content + '\n' + url
        try:
            with open(f'./data_txt/{title}.txt', mode='w', encoding='utf-8') as f:
                f.write(content_all)
        except:
            with open(f'./data_txt/{num}.txt', mode='w', encoding='utf-8') as f:
                f.write(content_all)
        num+=1
        print(f'爬取{num}条成功')