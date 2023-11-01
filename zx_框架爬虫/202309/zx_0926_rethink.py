# -*- coding: utf-8 -*-
import re
import scrapy
import json
from scrapy import Request as req
from scrapy import Selector
from pymongo import MongoClient



class ZgpSciepubSpider(scrapy.Spider):
    num = 0

    name = 'zx_0926_rethink'

    # handle_httpstatus_list = [302,304]

    custom_settings = {
        # 'CONCURRENT_REQUESTS': 8,
        # 'DOWNLOAD_DELAY': 2,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'zx_框架爬虫.middlewares.ProxyMiddleware': 543,
        # },
    }

    headers = {
        'authority': 'rethink-event.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'cookie': '_fbp=fb.1.1695714294542.701081890; _gid=GA1.2.1552713917.1695714295; ln_or=eyI2NDk2OTkiOiJkIn0%3D; __hstc=18915879.647e1be5c73e729fea4694ae6737e126.1695714295764.1695714295764.1695714295764.1; hubspotutk=647e1be5c73e729fea4694ae6737e126; __hssrc=1; _ga_9X14YC115T=GS1.1.1695714294.1.1.1695714670.0.0.0; _ga=GA1.1.1821302404.1695714294',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }


    base_url = ''

    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_0926_rethink

    def start_requests(self):
        url = 'https://rethink-event.com/2023-sponsors-exhibitors/'
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse,dont_filter=True)




    def parse(self, response, **kwargs):
        # content_list = response.xpath("//div[@class='entry-content wp-block-post-content has-global-padding is-layout-constrained wp-block-post-content-is-layout-constrained']/div[@class='rt-logos-wrapper alignfull rt-logos-wrapper--no-margin-bottom'][5]/following-sibling::div[contains(@class,'rt-logos-wrapper')]//div[@class='rt-modal-logo-wrapper js-modal']")
        content_list = response.xpath("//div[@class='rt-modal-logo-wrapper js-modal']")
        for i in content_list:
            db_dict = {}
            db_dict['公司简称'] = ''.join(i.xpath(".//h3//text()").get()).strip()
            db_dict['简介'] =''.join(i.xpath(".//div[@class='rt-modal-logo__desc']/p//text()").getall()).strip()
            db_dict['Solution Showcase'] =';\n'.join(i.xpath(".//strong[contains(text(),'Solutions Showcase:')]/../following-sibling::ul[1]//li//text()").getall()).strip()
            db_dict['UN SDG Goals that we align with'] =';\n'.join(i.xpath(".//strong[contains(text(),'that we align with')]/../following-sibling::ul[1]//li//text()").getall()).strip()
            db_dict['Legal Name'] =''.join(i.xpath(".//strong[contains(text(),'Legal Name:')]/following-sibling::text()").getall()).strip()
            self.db2.insert_one(db_dict)
            self.num +=1
            print(f'添加{self.num}条成功')

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(["scrapy", "crawl", 'zx_0926_rethink'])

