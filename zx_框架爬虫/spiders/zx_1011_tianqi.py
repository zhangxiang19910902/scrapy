import re
import time
import datetime
import requests
from pymongo import MongoClient
from scrapy import Selector
from fake_useragent import UserAgent


tunnel = "tps129.kdlapi.com:15818"
# 用户名密码方式
username = "t12987337781556"
password = "x0q6nsm5"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}

def getDatesByTimes():
    start_day = '202206'
    end_day = '202303'
    result = []
    date_start = datetime.datetime.strptime(start_day, '%Y%m')
    date_end = datetime.datetime.strptime(end_day, '%Y%m')
    result.append(date_start.strftime('%Y%m'))
    while date_start < date_end:
        date_start += datetime.timedelta(days=1)
        result.append(date_start.strftime('%Y%m'))
    result = list(dict.fromkeys(result))
    # result = list(set(result))
    return result


client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_1011_tianqi


cookies = {
    'Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2': '1696992314',
    'Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2': '1696992331',
}
ua = UserAgent()
headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1696992314; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1696992331',
    # 'Referer': 'https://lishi.tianqi.com/jinhua/202002.html',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua.chrome,
    # 'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

num = 0

year_list = getDatesByTimes()

for a in year_list:

    while True:
        time.sleep(2)
        try:
            response = requests.get(f'https://lishi.tianqi.com/jinhua/{a}.html', headers=headers,proxies=proxies)
            if response.status_code ==200:
                break
            else:
                print(response.status_code)
        except:
            print("程序报错")
    res = Selector(text=response.text)

    lists = res.xpath("//ul[@class='thrui']/li")
    for b in lists:
        db_dict = {}
        db_dict['date'] = ''.join(b.xpath("./div[1]//text()").getall()).strip()
        db_dict['temp_max'] = ''.join(b.xpath("./div[2]//text()").getall()).strip()
        db_dict['temp_min'] = ''.join(b.xpath("./div[3]//text()").getall()).strip()
        db_dict['weather'] = ''.join(b.xpath("./div[4]//text()").getall()).strip()
        db_dict['wind'] = ''.join(b.xpath("./div[5]//text()").getall()).strip()
        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功-----{a}')

