# -*- coding: utf-8 -*-
import re
import time

import scrapy
import json
from scrapy import Request as req
from scrapy import Selector
from pymongo import MongoClient
import pandas as pd
from bs4 import BeautifulSoup
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
    db2 = client.name.zx_1025_twse2
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
                response = requests.post('https://mops.twse.com.tw/mops/web/ajax_t05st15',
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

        soup = BeautifulSoup(response.text, 'lxml')
        fixed_html = soup.prettify()
        res3 = Selector(text=fixed_html)
        content = res3.xpath("//*[@class='hasBorder']/tr[2]/following-sibling::tr")
        if not content:
            print(f"没有数据---{c}")
            continue
        if content:
            for aaa in content:
                db_dict = {}
                db_dict['code'] = c
                db_dict['大陸被投資公司名稱'] = ''.join(aaa.xpath("./td[1]//text()").getall()).strip()
                db_dict['主要營業項目'] = ''.join(aaa.xpath("./td[2]//text()").getall()).strip()
                db_dict['實收資本額'] = ''.join(aaa.xpath("./td[3]//text()").getall()).strip()
                db_dict['投資方式'] = ''.join(aaa.xpath("./td[4]//text()").getall()).strip()
                db_dict['本期期初自台灣匯出累計投資金額'] = ''.join(aaa.xpath("./td[5]//text()").getall()).strip()
                db_dict['本期匯出或收回投資金額_匯出'] = ''.join(aaa.xpath("./td[6]//text()").getall()).strip()
                db_dict['本期匯出或收回投資金額_收回'] = ''.join(aaa.xpath("./td[7]//text()").getall()).strip()
                db_dict['本期期末自台灣匯出累計投資金額'] = ''.join(aaa.xpath("./td[8]//text()").getall()).strip()
                db_dict['本公司直接或間接投資之持股比例'] = ''.join(aaa.xpath("./td[9]//text()").getall()).strip()
                db_dict['本期認列投資損益'] = ''.join(aaa.xpath("./td[10]//text()").getall()).strip()
                db_dict['期末投資帳面價值'] = ''.join(aaa.xpath("./td[11]//text()").getall()).strip()
                db_dict['截至本期止已匯回台灣之投資收益'] = ''.join(aaa.xpath("./td[12]//text()").getall()).strip()
                db2.insert_one(db_dict)
                num +=1
                print(f'添加{num}条成功----{c}---{db_dict["大陸被投資公司名稱"]}')
        content2 = res3.xpath("//*[@class='hasBorder']/tr[2]/following-sibling::td")
        if content2:
            num2 = int(len(content2)/12)
            for bbb in range(num2):
                index = bbb*12
                db_dict = {}
                db_dict['code'] = c
                db_dict['大陸被投資公司名稱'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+1}]//text()").getall()).strip()
                db_dict['主要營業項目'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+2}]//text()").getall()).strip()
                db_dict['實收資本額'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+3}]//text()").getall()).strip()
                db_dict['投資方式'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+4}]//text()").getall()).strip()
                db_dict['本期期初自台灣匯出累計投資金額'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+5}]//text()").getall()).strip()
                db_dict['本期匯出或收回投資金額_匯出'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+6}]//text()").getall()).strip()
                db_dict['本期匯出或收回投資金額_收回'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+7}]//text()").getall()).strip()
                db_dict['本期期末自台灣匯出累計投資金額'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+8}]//text()").getall()).strip()
                db_dict['本公司直接或間接投資之持股比例'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+9}]//text()").getall()).strip()
                db_dict['本期認列投資損益'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+10}]//text()").getall()).strip()
                db_dict['期末投資帳面價值'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+11}]//text()").getall()).strip()
                db_dict['截至本期止已匯回台灣之投資收益'] = ''.join(res3.xpath(f"//*[@class='hasBorder']/tr[2]/following-sibling::td[{index+12}]//text()").getall()).strip()
                db2.insert_one(db_dict)
                num += 1
                print(f'添加{num}条成功----{c}---{db_dict["大陸被投資公司名稱"]}')


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db3 = client.name.zx_1025_twse
    code_list = []
    for ids1 in db3.find():
        phoen1 = ids1['code']
        code_list.append(phoen1)
    parse(code_list)