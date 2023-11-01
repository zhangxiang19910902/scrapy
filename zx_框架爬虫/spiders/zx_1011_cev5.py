import re
import time
import datetime
import requests
from pymongo import MongoClient
from scrapy import Selector
from fake_useragent import UserAgent

'''

'''

client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_1011_cev5


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
        response = requests.get('https://www.cev-pc.or.jp/tokei/koufu3.html', cookies=cookies, headers=headers)
        if response.status_code ==200:
            break
        else:
            print(response.status_code)
    except:
        print("程序报错")
res = Selector(text=response.text)

fivelist = res.xpath("//table[@class='normalTable p-scroll-table blnone']")

fivelist1 = ['合计','急速','普通']


heng_list =res.xpath("//div[@class='normalTable-content']/div[1]//table[@class='normalTable p-scroll-table blnone']/tbody/tr[1]/th//text()").getall()
for index,a in enumerate(fivelist):

    lists = res.xpath(f"//div[@class='normalTable-content']/div[{index+1}]//table[@class='normalTable p-scroll-table blnone']/tbody/tr[1]/following-sibling::tr")


    for b in lists:
        db_dict = {}
        db_dict['type'] = fivelist1[index]
        db_dict[heng_list[0]] = ''.join(b.xpath("./td[1]//text()").getall()).strip()
        db_dict[heng_list[1]] = ''.join(b.xpath("./td[2]//text()").getall()).strip()
        db_dict[heng_list[2]] = ''.join(b.xpath("./td[3]//text()").getall()).strip()
        db_dict[heng_list[3]] = ''.join(b.xpath("./td[4]//text()").getall()).strip()
        db_dict[heng_list[4]] = ''.join(b.xpath("./td[5]//text()").getall()).strip()
        db_dict[heng_list[5]] = ''.join(b.xpath("./td[6]//text()").getall()).strip()
        db_dict[heng_list[6]] = ''.join(b.xpath("./td[7]//text()").getall()).strip()
        db_dict[heng_list[7]] = ''.join(b.xpath("./td[8]//text()").getall()).strip()
        db_dict[heng_list[8]] = ''.join(b.xpath("./td[9]//text()").getall()).strip()
        db_dict[heng_list[9]] = ''.join(b.xpath("./td[10]//text()").getall()).strip()
        db_dict[heng_list[10]] = ''.join(b.xpath("./td[11]//text()").getall()).strip()
        db_dict[heng_list[11]] = ''.join(b.xpath("./td[12]//text()").getall()).strip()
        db_dict[heng_list[12]] = ''.join(b.xpath("./td[13]//text()").getall()).strip()
        db_dict[heng_list[13]] = ''.join(b.xpath("./td[14]//text()").getall()).strip()
        db_dict[heng_list[14]] = ''.join(b.xpath("./td[15]//text()").getall()).strip()

        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')
