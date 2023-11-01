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
db2 = client.name.zx_1012_playscripts


cookies = {
    '_ga': 'GA1.1.645546069.1696991389',
    '_gcl_au': '1.1.1722564331.1696991389',
    'streamstats_anon_id_512709': '9df5e5a9-b227-4fa2-96df-619a8c388673',
    '_hjSessionUser_3682835': 'eyJpZCI6IjdhMDI5YjRkLTk2MTUtNTRjOS04Yzc0LTVmNjczMWY2N2RjNyIsImNyZWF0ZWQiOjE2OTY5OTE0MTAyNjUsImV4aXN0aW5nIjp0cnVlfQ==',
    '__kla_id': 'eyJjaWQiOiJaVFF6T0dGak0yVXROR001WmkwME9XWXdMV0UwTjJJdFlXSmhaREZoWVdFeE4yTmsiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTY5OTEzOTIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBsYXlzY3JpcHRzLmNvbS9wcm9mZXNzaW9uYWwtdGhlYXRyZSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5Njk5MzMwNywidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGxheXNjcmlwdHMuY29tL3Byb2Zlc3Npb25hbC10aGVhdHJlIn19',
    '_uetsid': '197824c067de11ee9f182fbd82bdc871',
    '_uetvid': '197837e067de11eebbf29d990666e6b2',
    '_ga_FVN21GS0BD': 'GS1.1.1696996876.2.0.1696996876.60.0.0',
    '_dd_s': 'logs=1&id=0d6e456d-bac7-4669-86ee-86ed677fbdd9&created=1697071818099&expire=1697072719103',
}

headers = {
    'authority': 'www.playscripts.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.1.645546069.1696991389; _gcl_au=1.1.1722564331.1696991389; streamstats_anon_id_512709=9df5e5a9-b227-4fa2-96df-619a8c388673; _hjSessionUser_3682835=eyJpZCI6IjdhMDI5YjRkLTk2MTUtNTRjOS04Yzc0LTVmNjczMWY2N2RjNyIsImNyZWF0ZWQiOjE2OTY5OTE0MTAyNjUsImV4aXN0aW5nIjp0cnVlfQ==; __kla_id=eyJjaWQiOiJaVFF6T0dGak0yVXROR001WmkwME9XWXdMV0UwTjJJdFlXSmhaREZoWVdFeE4yTmsiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTY5OTEzOTIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBsYXlzY3JpcHRzLmNvbS9wcm9mZXNzaW9uYWwtdGhlYXRyZSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5Njk5MzMwNywidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGxheXNjcmlwdHMuY29tL3Byb2Zlc3Npb25hbC10aGVhdHJlIn19; _uetsid=197824c067de11ee9f182fbd82bdc871; _uetvid=197837e067de11eebbf29d990666e6b2; _ga_FVN21GS0BD=GS1.1.1696996876.2.0.1696996876.60.0.0; _dd_s=logs=1&id=0d6e456d-bac7-4669-86ee-86ed677fbdd9&created=1697071818099&expire=1697072719103',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
num = 0
for a in range(1,34):
    params = {
        'target_group[0]': 'professional',
        'sort': 'date',
        'page': a,
    }

    while True:
        time.sleep(2)
        try:
            response = requests.get('https://www.playscripts.com/find-a-play', params=params, cookies=cookies, headers=headers)
            if response.status_code ==200:
                break
            else:
                print(response.status_code)
        except:
            print("程序报错")
    res = Selector(text=response.text)

    title_list = res.xpath("//div[@class='theater-story']")
    for b in title_list:

        Name = ''.join(b.xpath(".//h3//text()").getall()).strip()
        author_type = ''.join(b.xpath(".//h3/span/text()").getall()).strip()
        author = ''.join(b.xpath(".//h3/span//a//text()").getall()).strip()
        category = ''.join(b.xpath(".//div[@class='movie-info']/ul/li[1]//text()").getall()).strip()
        time_1 = ''.join(b.xpath(".//div[@class='movie-info']/ul/li[last()-1]//text()").getall()).strip()
        content = ''.join(b.xpath(".//div[@class='movie-info']/ul/li[last()]//text()").getall()).strip()


        xiangxingurl = b.xpath(".//h3//a/@href").get()
        url_join = 'https://www.playscripts.com' + xiangxingurl
        while True:
            time.sleep(2)
            try:
                response1 = requests.get(url_join, params=params, cookies=cookies,
                                        headers=headers)
                if response1.status_code == 200:
                    break
                else:
                    print(response1.status_code)
            except:
                print("程序报错")
        res1 = Selector(text=response1.text)
        xiangqing_list = res1.xpath("//*[@id='all-prodhist']//tr")
        for c in xiangqing_list:
            product_date = ''.join(c.xpath("./td[1]//text()").getall()).strip()
            production_name = ''.join(c.xpath("./td[2]//text()").getall()).strip()
            production_address = ''.join(c.xpath("./td[3]//text()").getall()).strip()

            db_dict = {}
            db_dict['Name'] = Name
            db_dict['author_type'] = author_type
            db_dict['author'] = author
            db_dict['category'] = category
            db_dict['time_1'] = time_1
            db_dict['content'] = content
            db_dict['product_date'] = product_date
            db_dict['production_name'] = production_name
            db_dict['production_address'] = production_address

            db2.insert_one(db_dict)
            num += 1
            print(f'添加{num}条成功')
