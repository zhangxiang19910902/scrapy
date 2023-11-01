# -*- coding: utf-8 -*-
import re
import time

import scrapy
import json
from scrapy import Request as req
from scrapy import Selector
from pymongo import MongoClient
import pandas as pd

import requests
from fake_useragent import UserAgent

tunnel = "tps129.kdlapi.com:15818"
# 用户名密码方式
username = "t12987337781556"
password = "x0q6nsm5"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}
def parse(code_list):
    ua = UserAgent()
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'jcsession=jHttpSession@674c73dd; _ga=GA1.1.1803258226.1698126055; _ga_LTMT28749H=GS1.1.1698130982.2.1.1698130982.0.0.0',
        # 'Cookie': 'jcsession=jHttpSession@2d3e77f8; _ga=GA1.1.1803258226.1698126055; _ga_LTMT28749H=GS1.1.1698133020.3.1.1698133020.0.0.0',
        # 'Origin': 'https://mops.twse.com.tw',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        'User-Agent': ua.chrome,
        # 'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"',
    }




    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_1025_twse
    num = 0


    for c in code_list:
        data = {
            'encodeURIComponent': '1',
            'step': '1',
            'firstin': '1',
            'off': '1',
            'keyword4': '',
            'code1': '',
            'TYPEK2': '',
            'checkbtn': '',
            'queryName': 'co_id',
            'inpuType': 'co_id',
            'TYPEK': 'all',
            'isnew': 'true',
            'co_id': c,
            'year': '',
            'season': '',
        }

        while True:
            time.sleep(1.5)
            try:
                response = requests.post('https://mops.twse.com.tw/mops/web/ajax_t05st03',
                                         headers=headers, data=data,
                                         # proxies=proxies
                                         )
                if response.status_code == 200:
                    print(f'响应码：{response.status_code}')
                    break
                else:
                    print(response.status_code)
            except:
                print("程序报错")
        res3 = Selector(text=response.text)

        db_dict = {}
        db_dict['code'] = ''.join(res3.xpath("//*[@class='hasBorder']//tr//th[contains(text(),'股票代號')]/following-sibling::td[1]//text()").getall()).strip()
        if not db_dict['code']:
            print(f'没找到code:{c}')
            continue
        db_dict['name'] = ''.join(res3.xpath("//*[@class='hasBorder']//tr//th[text()='公司名稱']/following-sibling::td[1]//text()").getall()).strip()
        db_dict['industry_type'] = ''.join(res3.xpath("//*[@class='hasBorder']//tr//th[text()='產業類別']/following-sibling::td[1]//text()").getall()).strip()
        db_dict['adds'] = ''.join(res3.xpath("//*[@class='hasBorder']//tr//th[text()='地址']/following-sibling::td[1]//text()").getall()).strip()
        db_dict['phone'] = ''.join(res3.xpath("//*[@class='hasBorder']//tr//th[text()='總機']/following-sibling::td[1]//text()").getall()).strip()

        db2.insert_one(db_dict)
        num +=1
        print(f'添加{num}条成功----{c}---{db_dict["name"]}')

if __name__ == '__main__':
    code_list = []
    for a in range(7442,10000):
        b = str(a).zfill(4)
        code_list.append(b)
    parse(code_list)