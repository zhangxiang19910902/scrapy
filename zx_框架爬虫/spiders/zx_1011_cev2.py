import re
import time
import datetime
import requests
from pymongo import MongoClient
from scrapy import Selector
from fake_useragent import UserAgent


client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_1011_cev2


cookies = {
    '_gid': 'GA1.3.477849048.1697001355',
    '_ga_28DDD4N8WD': 'GS1.1.1697001354.1.1.1697003476.52.0.0',
    '_ga': 'GA1.1.1172834826.1697001355',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': '_gid=GA1.3.477849048.1697001355; _ga_28DDD4N8WD=GS1.1.1697001354.1.1.1697003476.52.0.0; _ga=GA1.1.1172834826.1697001355',
    'Referer': 'https://www.cev-pc.or.jp/tokei/koufu.html',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


num = 0


while True:
    time.sleep(2)
    try:
        response = requests.get('https://www.cev-pc.or.jp/tokei/hanbaidaisu.html', cookies=cookies, headers=headers)
        if response.status_code ==200:
            break
        else:
            print(response.status_code)
    except:
        print("程序报错")
res = Selector(text=response.text)

name = ''.join(res.xpath("//tr[@class='nendo']//text()").getall()).strip()
name_list = name.split('\n')


lists = res.xpath("//tr[@class='nendo']/following-sibling::tr")

for b in lists:
    aaa = b.xpath("./*")
    if len(aaa) ==8:
        db_dict = {}
        db_dict[name_list[0].strip()] = ''.join(b.xpath("./th//text()").getall()).strip()
        db_dict['年度2'] = ''.join(b.xpath("./td[1]//text()").getall()).strip()
        db_dict[name_list[1].strip()] = ''.join(b.xpath("./td[2]//text()").getall()).strip()
        db_dict[name_list[2].strip()] = ''.join(b.xpath("./td[3]//text()").getall()).strip()
        db_dict[name_list[3].strip()] = ''.join(b.xpath("./td[4]//text()").getall()).strip()
        db_dict[name_list[4].strip()] = ''.join(b.xpath("./td[5]//text()").getall()).strip()
        db_dict[name_list[5].strip()] = ''.join(b.xpath("./td[6]//text()").getall()).strip()
        db_dict[name_list[6].strip()] = ''.join(b.xpath("./td[7]//text()").getall()).strip()
        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')
    else:
        db_dict = {}
        db_dict['年度2'] = ''.join(b.xpath("./td[1]//text()").getall()).strip()
        db_dict[name_list[1].strip()] = ''.join(b.xpath("./td[2]//text()").getall()).strip()
        db_dict[name_list[2].strip()] = ''.join(b.xpath("./td[3]//text()").getall()).strip()
        db_dict[name_list[3].strip()] = ''.join(b.xpath("./td[4]//text()").getall()).strip()
        db_dict[name_list[4].strip()] = ''.join(b.xpath("./td[5]//text()").getall()).strip()
        db_dict[name_list[5].strip()] = ''.join(b.xpath("./td[6]//text()").getall()).strip()
        db_dict[name_list[6].strip()] = ''.join(b.xpath("./td[7]//text()").getall()).strip()
        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')

lists2 = res.xpath("//div[@class='hanbai_box_in']/*[2]//tr")
for c in lists2:
    bbb = c.xpath("./*")
    if len(bbb) == 8:
        db_dict = {}
        db_dict[name_list[0].strip()] = ''.join(c.xpath("./th//text()").getall()).strip()
        db_dict['年度2'] = ''.join(c.xpath("./td[1]//text()").getall()).strip()
        db_dict[name_list[1].strip()] = ''.join(c.xpath("./td[2]//text()").getall()).strip()
        db_dict[name_list[2].strip()] = ''.join(c.xpath("./td[3]//text()").getall()).strip()
        db_dict[name_list[3].strip()] = ''.join(c.xpath("./td[4]//text()").getall()).strip()
        db_dict[name_list[4].strip()] = ''.join(c.xpath("./td[5]//text()").getall()).strip()
        db_dict[name_list[5].strip()] = ''.join(c.xpath("./td[6]//text()").getall()).strip()
        db_dict[name_list[6].strip()] = ''.join(c.xpath("./td[7]//text()").getall()).strip()
        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')
    else:
        db_dict = {}
        db_dict['年度2'] = ''.join(c.xpath("./td[1]//text()").getall()).strip()
        db_dict[name_list[1].strip()] = ''.join(c.xpath("./td[2]//text()").getall()).strip()
        db_dict[name_list[2].strip()] = ''.join(c.xpath("./td[3]//text()").getall()).strip()
        db_dict[name_list[3].strip()] = ''.join(c.xpath("./td[4]//text()").getall()).strip()
        db_dict[name_list[4].strip()] = ''.join(c.xpath("./td[5]//text()").getall()).strip()
        db_dict[name_list[5].strip()] = ''.join(c.xpath("./td[6]//text()").getall()).strip()
        db_dict[name_list[6].strip()] = ''.join(c.xpath("./td[7]//text()").getall()).strip()
        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')