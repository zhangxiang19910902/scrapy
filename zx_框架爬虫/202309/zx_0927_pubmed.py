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







client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_0927_pubmed

def start_requests():
    aaa = pd.read_excel(r"C:\Users\Administrator\Desktop\zx.xls", header=0)
    url_list = []
    for i in aaa.itertuples():
        url = "https://pubmed.ncbi.nlm.nih.gov" + i[1]
        url_list.append(url)
    return url_list

def parse(urls):
    cookies = {
        'pm-csrf': '6bSC4VEXHxYhVFeNhocxn6kenof5FsItlJoggZkPVuYEdMJvCeFizg91ZveIF8AP',
        'pm-sessionid': '94m6zywixcyp67h8r8xuqqlg0911pi82',
        'ncbi_sid': 'C89F22D3513D1613_1997SID',
        '_gid': 'GA1.2.240366757.1695798369',
        'pm-sid': 'QzBHksP117i_KJ0IxEX9dA:13b38e89528232d218b02d7449cb0174',
        'pm-adjnav-sid': 'SKo9o2egcDDSSzYBJ_OKPQ:13b38e89528232d218b02d7449cb0174',
        '_ga_DP2X732JSX': 'GS1.1.1695798368.1.1.1695799583.0.0.0',
        '_ga': 'GA1.2.72034425.1695798369',
        'ncbi_pinger': 'N4IgDgTgpgbg+mAFgSwCYgFwgBwHZsAMRBAjAGwkCiZAIgELYCsxBATAJy6UDMljAggBY6IgHQlRAWziMQAGhABXAHYAbAPYBDVMqgAPAC6ZQrTOEUAjSVHQLuZsJeu2Qgs5osBnAxE0BjIwVZLHkQVgIzPEJicipaBmZiDi5eAWExCWlZBVYSBycbDEcrQo9vXwCMADkAeSrKUNZTLGLnUWU/C2R21Ul25ERRAHN1GEb2MxJ2cNDuCKwSAkJZvIXpiLtmkEXBDZBueywAM01VTyhZtywfRQu7bDNZiaxsEl2yUN3I1kFGNwVBIcQARRNx2KDPlclGotDp9IFXMFgaFGED2EQUVD2Nw8kEPlg9oxcGY9hRIgQPgoyPiQNAfMhYHcQGQHi9UexBII8gBfblAA',
    }

    headers = {
        'authority': 'pubmed.ncbi.nlm.nih.gov',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'pm-csrf=6bSC4VEXHxYhVFeNhocxn6kenof5FsItlJoggZkPVuYEdMJvCeFizg91ZveIF8AP; pm-sessionid=94m6zywixcyp67h8r8xuqqlg0911pi82; ncbi_sid=C89F22D3513D1613_1997SID; _gid=GA1.2.240366757.1695798369; pm-sid=QzBHksP117i_KJ0IxEX9dA:13b38e89528232d218b02d7449cb0174; pm-adjnav-sid=SKo9o2egcDDSSzYBJ_OKPQ:13b38e89528232d218b02d7449cb0174; _ga_DP2X732JSX=GS1.1.1695798368.1.1.1695799583.0.0.0; _ga=GA1.2.72034425.1695798369; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgBwHZsAMRBAjAGwkCiZAIgELYCsxBATAJy6UDMljAggBY6IgHQlRAWziMQAGhABXAHYAbAPYBDVMqgAPAC6ZQrTOEUAjSVHQLuZsJeu2Qgs5osBnAxE0BjIwVZLHkQVgIzPEJicipaBmZiDi5eAWExCWlZBVYSBycbDEcrQo9vXwCMADkAeSrKUNZTLGLnUWU/C2R21Ul25ERRAHN1GEb2MxJ2cNDuCKwSAkJZvIXpiLtmkEXBDZBueywAM01VTyhZtywfRQu7bDNZiaxsEl2yUN3I1kFGNwVBIcQARRNx2KDPlclGotDp9IFXMFgaFGED2EQUVD2Nw8kEPlg9oxcGY9hRIgQPgoyPiQNAfMhYHcQGQHi9UexBII8gBfblAA',
        'referer': 'https://pubmed.ncbi.nlm.nih.gov/?term=tang%20JT&page=10',
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


    num = 0

    for a in urls:
        time.sleep(2)


        db_dict = {}
        response = requests.get(a,
                                headers=headers,
                                cookies=cookies,
                                )
        response = Selector(text=response.text)
        auth = ''.join(response.xpath("//*[@name='citation_authors']/@content").getall()).strip()
        auth = re.sub(';$','',auth)
        db_dict['标题'] = ''.join(response.xpath("//*[@name='citation_title']/@content").getall()).strip()
        db_dict['期刊'] =''.join(response.xpath("//*[@name='citation_journal_title']/@content").getall()).strip()
        db_dict['时间'] =''.join(response.xpath("//*[@name='citation_date']/@content").getall()).strip()
        db_dict['作者'] = auth.rsplit(';',1)[0]
        db_dict['通讯作者'] =auth.rsplit(';',1)[-1]
        db_dict['url'] =a
        db2.insert_one(db_dict)
        num +=1
        print(f'添加{num}条成功')

if __name__ == '__main__':
    urls = start_requests()
    parse(urls)