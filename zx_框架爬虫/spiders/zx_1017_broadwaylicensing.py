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





base_url = ''




def start_requests():
    aaa = pd.read_excel(r"./data_exl/aaa.xls", header=0)
    url_list = []
    for i in aaa.itertuples():


        url_list.append(i[1])
    return url_list

def parse(urls):
    cookies = {
        '_gcl_au': '1.1.1261486701.1697426157',
        '_gid': 'GA1.2.890059666.1697426159',
        '_hjSessionUser_3682842': 'eyJpZCI6IjNiYjUyMjgzLTExZGEtNWM1Ni1iYzYwLTI4ZWNmMzQ4NTVlYiIsImNyZWF0ZWQiOjE2OTc0MjYxNzU2MTYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_3682842': '0',
        '_hjSession_3682842': 'eyJpZCI6IjRmZjU5NjMzLTViZTgtNDA1YS1iNGE5LTM3MDI5NjAzMmEzNiIsImNyZWF0ZWQiOjE2OTc1MDEzNjI0NDAsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
        '_hjAbsoluteSessionInProgress': '1',
        '_gat_UA-274065-5': '1',
        '_ga': 'GA1.1.348076745.1697426159',
        '__kla_id': 'eyJjaWQiOiJZek0wTW1ReFptWXRNREkxTlMwME5ERXdMVGxsT1dZdE16WTFaVEUyTm1FNFl6VTEiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTc0MjYxNzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYnJvYWR3YXlsaWNlbnNpbmcuY29tL2NyZWF0b3JzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5NzUwMTYwMywidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9icm9hZHdheWxpY2Vuc2luZy5jb20vY3JlYXRvcnMvIn19',
        '_ga_WR5QBCR2CC': 'GS1.1.1697501361.5.1.1697501612.50.0.0',
    }

    headers = {
        'authority': 'broadwaylicensing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'cookie': '_gcl_au=1.1.1261486701.1697426157; _gid=GA1.2.890059666.1697426159; _hjSessionUser_3682842=eyJpZCI6IjNiYjUyMjgzLTExZGEtNWM1Ni1iYzYwLTI4ZWNmMzQ4NTVlYiIsImNyZWF0ZWQiOjE2OTc0MjYxNzU2MTYsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_3682842=0; _hjSession_3682842=eyJpZCI6IjRmZjU5NjMzLTViZTgtNDA1YS1iNGE5LTM3MDI5NjAzMmEzNiIsImNyZWF0ZWQiOjE2OTc1MDEzNjI0NDAsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=1; _gat_UA-274065-5=1; _ga=GA1.1.348076745.1697426159; __kla_id=eyJjaWQiOiJZek0wTW1ReFptWXRNREkxTlMwME5ERXdMVGxsT1dZdE16WTFaVEUyTm1FNFl6VTEiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTc0MjYxNzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYnJvYWR3YXlsaWNlbnNpbmcuY29tL2NyZWF0b3JzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5NzUwMTYwMywidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9icm9hZHdheWxpY2Vuc2luZy5jb20vY3JlYXRvcnMvIn19; _ga_WR5QBCR2CC=GS1.1.1697501361.5.1.1697501612.50.0.0',
        'referer': 'https://broadwaylicensing.com/creators/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }


    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_1017_broadwaylicensing

    num = 0

    for a in urls:
        time.sleep(2)
        response = requests.get(a, cookies=cookies, headers=headers)
        response = Selector(text=response.text)
        db_dict = {}
        db_dict['title'] = ''.join(response.xpath("//div[@class='desktop']//h3//text()").getall()).strip()
        db_dict['type'] =''.join(response.xpath("//div[@class='desktop']//p//text()").getall()).strip()
        db_dict['content_url'] =response.xpath("//div[@class='x-main full']//div[@class='x-column x-2-3 x-sm last']/*[2]//a/@href").get()
        db_dict['auth'] = ''.join(response.xpath("//div[@class='x-column x-2-3 x-sm last']//h1//text()").getall()).strip()
        db_dict['content'] = ''.join(response.xpath("//div[@class='x-main full']//div[@class='x-column x-2-3 x-sm last']/*[2]//text()").getall()).strip()
        db_dict['url'] =a
        db2.insert_one(db_dict)
        num +=1
        print(f'添加{num}条成功')

if __name__ == '__main__':
    urls = start_requests()
    parse(urls)