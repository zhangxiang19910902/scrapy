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

def parse():
    cookies = {
        '_gcl_au': '1.1.1261486701.1697426157',
        '_gid': 'GA1.2.890059666.1697426159',
        '_hjSessionUser_3682842': 'eyJpZCI6IjNiYjUyMjgzLTExZGEtNWM1Ni1iYzYwLTI4ZWNmMzQ4NTVlYiIsImNyZWF0ZWQiOjE2OTc0MjYxNzU2MTYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_3682842': '1',
        '_hjSession_3682842': 'eyJpZCI6IjI4ZDFkZDQwLTM4Y2MtNDhkNy04Zjk4LTA0YzNlY2I3NjFhOSIsImNyZWF0ZWQiOjE2OTc1MjU0MjQyMzYsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_ga': 'GA1.1.348076745.1697426159',
        '__kla_id': 'eyJjaWQiOiJZek0wTW1ReFptWXRNREkxTlMwME5ERXdMVGxsT1dZdE16WTFaVEUyTm1FNFl6VTEiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTc0MjYxNzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYnJvYWR3YXlsaWNlbnNpbmcuY29tL2NyZWF0b3JzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5NzUyNTQ1MSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9icm9hZHdheWxpY2Vuc2luZy5jb20vc2hvd3MvbXVzaWNhbHMvIn19',
        '_ga_WR5QBCR2CC': 'GS1.1.1697525394.7.1.1697525517.60.0.0',
    }

    headers = {
        'authority': 'broadwaylicensing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_gcl_au=1.1.1261486701.1697426157; _gid=GA1.2.890059666.1697426159; _hjSessionUser_3682842=eyJpZCI6IjNiYjUyMjgzLTExZGEtNWM1Ni1iYzYwLTI4ZWNmMzQ4NTVlYiIsImNyZWF0ZWQiOjE2OTc0MjYxNzU2MTYsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_3682842=1; _hjSession_3682842=eyJpZCI6IjI4ZDFkZDQwLTM4Y2MtNDhkNy04Zjk4LTA0YzNlY2I3NjFhOSIsImNyZWF0ZWQiOjE2OTc1MjU0MjQyMzYsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _ga=GA1.1.348076745.1697426159; __kla_id=eyJjaWQiOiJZek0wTW1ReFptWXRNREkxTlMwME5ERXdMVGxsT1dZdE16WTFaVEUyTm1FNFl6VTEiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTc0MjYxNzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vYnJvYWR3YXlsaWNlbnNpbmcuY29tL2NyZWF0b3JzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5NzUyNTQ1MSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9icm9hZHdheWxpY2Vuc2luZy5jb20vc2hvd3MvbXVzaWNhbHMvIn19; _ga_WR5QBCR2CC=GS1.1.1697525394.7.1.1697525517.60.0.0',
        'if-modified-since': 'Tue, 17 Oct 2023 06:33:46 GMT',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'If-None-Natch':'',
        'If-Modified-Since':'',
    }




    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_1019_broadwaylicensing

    num = 0


    while True:
        time.sleep(2)
        try:
            response = requests.get('https://broadwaylicensing.com/shows/musicals/', cookies=cookies,
                                    headers=headers)
            if response.status_code == 200:
                break
            else:
                print(response.status_code)
        except:
            print("程序报错")

    res = Selector(text=response.text)

    content_list = res.xpath("//div[@id='scroll-point']/div")
    for a in content_list:
        ids = a.xpath("./@id").get()
        urls = a.xpath(".//div[@class='x-column x-1-3']//a/@href").getall()
        for b in urls:
            while True:
                time.sleep(2)
                try:
                    response1 = requests.get(b, cookies=cookies,
                                            headers=headers)
                    if response.status_code == 200:
                        break
                    else:
                        print(response.status_code)
                except:
                    print("程序报错")
            res1 = Selector(text=response1.text)

            db_dict = {}
            db_dict['License_name'] = ids
            db_dict['production_name'] = ''.join(res1.xpath("//div[@class='x-main full']//h1//text()").getall()).strip()
            db_dict['url'] = b
            db_dict['Play_description'] = ''.join(res1.xpath("//div[@id='lexisynopsis']//text()").getall()).strip()
            if not db_dict['Play_description']:
                db_dict['Play_description'] = ''.join(res1.xpath("//td[@class='poster-image']/following-sibling::td//p//text()").getall()).strip()

            Rights = res1.xpath("//*[@class='streaming-rights desktop']")
            if Rights:
                db_dict['Rights'] = 'Archival Video Rights'
            else:
                db_dict['Rights'] = ''

            db_dict['Orchestrations'] = '\n'.join(res1.xpath("//*[@id='orchestrations']/following-sibling::p[1]//text()").getall()).strip()
            db_dict['Creators'] = '\n'.join(res1.xpath("//div[@class='creator clearfix']//div[@class='x-column x-2-3 last']//h3//text()").getall()).strip()
            db_dict['contribution'] = '\n'.join(res1.xpath("//div[@class='creator clearfix']//div[@class='x-column x-2-3 last']//p//span[@class='role']//text()").getall()).strip()
            db_dict['role_description'] = '\n'.join(res1.xpath("//div[@class='creator clearfix']//div[@class='x-column x-2-3 last']//p//span[@class='desktop']//text()").getall()).strip()
            db_dict['Credits'] = ''.join(res1.xpath("//div[@id='credits']/following-sibling::p[1]//text()").getall()).strip()
            db_dict['Roles'] = ''.join(res1.xpath("//div[@class='x-main full']//div[@class='table show-details']/div[1]//strong//text()").getall()).strip()
            db_dict['Musicians'] = ''.join(res1.xpath("//div[@class='x-main full']//div[@class='table show-details']/div[2]//strong//text()").getall()).strip()
            db_dict['Acts'] = ''.join(res1.xpath("//div[@class='x-main full']//div[@class='table show-details']/div[3]//strong//text()").getall()).strip()
            db_dict['Duration'] = ''.join(res1.xpath("//div[@class='x-main full']//div[@class='table show-details']/div[4]//strong//text()").getall()).strip()

            db_dict['Casting'] = '\n'.join(res1.xpath("//div[@class='clearfix']//p/strong//text()").getall()).strip()
            db_dict['Casting_role'] = '\n'.join(res1.xpath("//div[@class='clearfix']//p/text()[1]").getall()).strip()
            db_dict['role_description'] = '\n'.join(res1.xpath("//div[@class='clearfix']//p/text()[2]").getall()).strip()

            db2.insert_one(db_dict)
            num +=1
            print(f'添加{num}条成功')

if __name__ == '__main__':
    parse()