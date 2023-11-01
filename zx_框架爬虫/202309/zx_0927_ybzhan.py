import time

import requests
from pymongo import MongoClient
from scrapy import Selector
client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_0927_ybzhan

cookies = {
    'ASP.NET_SessionId': 'udrkhw3synriyndosg2pezjj',
    'mtcached_mtsession_udrkhw3synriyndosg2pezjj': '10.115.3.131:9715',
    'Hm_lvt_fe76d250fc45bcdfc9267a4f6348f8d8': '1695779190',
    'XWTVisitorID': '2093319',
    'ybzhancompanyidstat77791ip12312517399': '1',
    'ybzhancompanyidstat115692ip12312517399': '1',
    'Hm_lpvt_fe76d250fc45bcdfc9267a4f6348f8d8': '1695796149',
}

headers = {
    'authority': 'www.ybzhan.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'ASP.NET_SessionId=udrkhw3synriyndosg2pezjj; mtcached_mtsession_udrkhw3synriyndosg2pezjj=10.115.3.131:9715; Hm_lvt_fe76d250fc45bcdfc9267a4f6348f8d8=1695779190; XWTVisitorID=2093319; ybzhancompanyidstat77791ip12312517399=1; ybzhancompanyidstat115692ip12312517399=1; Hm_lpvt_fe76d250fc45bcdfc9267a4f6348f8d8=1695796149',
    'referer': 'https://www.ybzhan.cn/brands/list_p100.html',
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


num = 1

for a in range(1,101):
    while True:
        try:
            response = requests.get(f'https://www.ybzhan.cn/brands/list_p{a}.html', cookies=cookies, headers=headers)
            if response.status_code ==200:
                break
            else:
                print(response.status_code)
        except:
            print("程序报错")
    res = Selector(text=response.text)
    urls = res.xpath("//dt/a/@href").getall()
    for b in urls:
        time.sleep(1.5)
        url1 = 'https:' + b
        while True:
            try:
                response1 = requests.get(url1, cookies=cookies,
                                        headers=headers)
                if response.status_code == 200:
                    break
                else:
                    print(response.status_code)
            except:
                print("程序报错")

        res1 = Selector(text=response1.text)
        db_dict = {}
        db_dict['品牌名称'] = ''.join(res1.xpath("//b[contains(text(),'品牌名称')]//text()").getall()).replace('品牌名称：','').strip()
        db_dict['英文名称'] = ''.join(res1.xpath("//b[contains(text(),'英文名称')]//text()").getall()).replace('英文名称：','').strip()
        db_dict['品牌所属企业'] = ''.join(res1.xpath("//*[contains(text(),'品牌所属企业')]//a//text()").getall()).strip()
        db_dict['品牌介绍'] = ''.join(res1.xpath("//div[@id='introduce']//p//text()").getall()).strip()
        db_dict['企业档案'] = '\n'.join(res1.xpath("//div[@id='archives']//p//text()").getall()).strip()
        db_dict['品牌产品'] = '\n'.join(res1.xpath("//div[@id='product']//p//text()").getall()).strip()
        db_dict['url'] = url1

        logo = res1.xpath("//div[@class='brandCenter clearfix']/a//img/@src").get()
        logo_join = 'https:' + logo
        db_dict['logo'] = logo_join
        code_logo = f"2020_{num}"
        db_dict['code_logo'] = code_logo
        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')
