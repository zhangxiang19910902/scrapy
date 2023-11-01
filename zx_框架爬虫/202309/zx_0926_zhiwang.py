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





base_url = 'https://kns.cnki.net'




def start_requests():
    aaa = pd.read_excel(r"C:\Users\Administrator\Desktop\zx.xls", header=0)
    url_list = []
    for i in aaa.itertuples():
        url = "https://kns.cnki.net" + i[1]

        url_list.append(url)
    return url_list

def parse(urls):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': 'cangjieStatus_NZKPT2=true; cangjieConfig_NZKPT2=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222022-10-20%22%2C%22endTime%22%3A%222030-12-31%22%2C%22orginHosts%22%3A%22kns.cnki.net%22%2C%22type%22%3A%22mix%22%2C%22poolSize%22%3A%2210%22%2C%22intervalTime%22%3A10000%2C%22persist%22%3Afalse%7D; UM_distinctid=18acb5fa106b08-078584fb32919f-26031e51-1fa400-18acb5fa107aac; Ecp_ClientId=4230925160500377582; Ecp_IpLoginFail=230925123.125.173.99; SID_sug=128007; SID_kns_new=kns25128005; ASP.NET_SessionId=qq5ltduiqbqy04rl0ziele3s; SID_kns8=123148; dblang=all; knsLeftGroupSelectItem=1%3B2%3B; CurrSortField=%e7%9b%b8%e5%85%b3%e5%ba%a6%2frelevant%2c(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27time%27)+desc; CurrSortFieldType=desc; Ecp_ClientIp=123.125.173.99',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_0926_zhiwang

    num = 0

    for a in urls:
        time.sleep(2)


        db_dict = {}
        response = requests.get(a,
                                headers=headers)
        response = Selector(text=response.text)
        auth = ';'.join(response.xpath("//h3[@class='author']//span//a/text()").getall()).strip()
        if not auth:
            auth = ''.join(response.xpath("//h3[@class='author']//span//text()").getall()).strip()
            auth = auth.replace(',',';')
        db_dict['标题'] = ''.join(response.xpath("//h1//text()").getall()).strip()
        db_dict['期刊'] =''.join(response.xpath("//div[@class='top-tip']/span/a[1]//text()").getall()).strip()
        db_dict['时间'] =''.join(response.xpath("//div[@class='top-tip']/span/a[2]//text()").getall()).strip()
        db_dict['作者'] = auth.rsplit(';',1)[0]
        db_dict['通讯作者'] =auth.rsplit(';',1)[-1]
        db_dict['url'] =a
        db2.insert_one(db_dict)
        num +=1
        print(f'添加{num}条成功')

if __name__ == '__main__':
    urls = start_requests()
    parse(urls)