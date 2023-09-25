# -*- coding: utf-8 -*-
import re
import scrapy
import json
from scrapy import Request as req
from scrapy import Selector
from pymongo import MongoClient



class ZgpSciepubSpider(scrapy.Spider):
    num = 0

    name = 'zx_0920_zhyxzz'

    handle_httpstatus_list = [302]

    custom_settings = {
        # 'CONCURRENT_REQUESTS': 8,
        # 'DOWNLOAD_DELAY': 2,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        'DOWNLOADER_MIDDLEWARES': {
            'zx_框架爬虫.middlewares.ProxyMiddleware': 543,
        },
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", }

    base_url = 'https://zhyxzz.yiigle.com/channelIssue_select.jspx?year=2023'




    def start_requests(self):
        for i in range(2020,2024):
            url = f'https://zhyxzz.yiigle.com/channelIssue_select.jspx?year={i}'
            yield scrapy.Request(url=url, headers=self.headers, callback=self.page,dont_filter=True)



    def page(self, response, **kwargs):
        journal_url_list = json.loads(response.text)
        if journal_url_list:
            for i in journal_url_list:
                meta = response.meta
                year = i.get('issueYear')
                meta['year'] = year
                source = i.get('url')
                url = f'https://zhyxzz.yiigle.com{source}?tplReset=qikan'
                new_url = url if 'http' in url else response.urljoin(url)
                yield req(url=new_url.strip(), headers=self.headers, callback=self.parse,
                          meta=meta,dont_filter=True)


    def parse(self, response, **kwargs):
        meta = response.meta
        particulars = response.xpath("//p[@class='Current_Title']/a/@href").getall()
        for i in particulars:
            if '#' in i: continue
            new_url = i if 'http' in i else response.urljoin(i)
            yield req(url=new_url.strip(), headers=self.headers, callback=self.pro_data,
                      meta=meta,dont_filter=True)

    def pro_data(self, response, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db2 = client.name.zx_0920_aaa

        db_dict = {}
        auth = ''
        em  = ''
        title = ''.join(response.xpath("//title//text()").getall())

        data = json.loads(re.findall(r'xmlData:(.*?),toRouter', response.text)[0])
        res = Selector(text=data)
        auths = ''.join(res.xpath("//*[@id='cor1']//text()").getall()).strip()
        if auths:
            auth = ''.join(re.findall('通信作者：(.*?)，',auths))
            em = ''.join(re.findall('Email：(.*?)$',auths))

        db_dict['title'] =title
        db_dict['auth'] =auth
        db_dict['em'] =em
        db_dict['url'] =response.url
        db2.insert_one(db_dict)
        self.num +=1
        print(f'添加{self.num}条成功')

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(["scrapy", "crawl", 'zx_0920_zhyxzz'])

