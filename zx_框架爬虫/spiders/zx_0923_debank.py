# -*- coding: utf-8 -*-
import re
import scrapy
import time
import json
from scrapy import Request as req
from scrapy import Selector
from pymongo import MongoClient



class ZgpSciepubSpider(scrapy.Spider):
    num = 0

    name = 'zx_0923_debank'

    handle_httpstatus_list = [302,304]

    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOADER_MIDDLEWARES': {
            'zx_框架爬虫.middlewares.ProxyMiddleware': 543,
        },
    }



    base_url = 'https://www.faz.net/suche/s4.html?ct=article&ct=audio&ct=blog&ct=gallery&ct=infografik&ct=storytelling&ct=video&&query=china&from=01.02.2020&to=01.03.2020#listPagination'




    def start_requests(self):
        headers = {
            'authority': 'api.debank.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'account': '{"random_at":1694582370,"random_id":"94bfa2b852914a0b93d15b91704d260c","user_addr":null}',
            'origin': 'https://debank.com',
            'referer': 'https://debank.com/',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'source': 'web',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'x-api-nonce': 'n_XdypSQLfoQ4D85kmKoWmHGXnceMy9BHiToABAUMI',
            'x-api-sign': 'afcd95822d78888b01232fd5e83a98fedb741376160eae37f93fb68245a32171',
            'x-api-ts': '1695459383',
            'x-api-ver': 'v2',
        }

        for a in range(100):
            number = a * 50
            url  =f"https://api.debank.com/user/rank_list?start={number}&limit=50"
            yield scrapy.Request(url=url, headers=headers, callback=self.parse,dont_filter=True)



    def parse(self, response, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db2 = client.name.zx_0923_debank

        res_josn = response.json()
        for i in res_josn['data']['rank_list']:
            db_dict = {}
            db_dict['id'] = i['id']
            db2.insert_one(db_dict)
            self.num += 1
            print(f'添加{self.num}条成功')



if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(["scrapy", "crawl", 'zx_0923_debank'])

