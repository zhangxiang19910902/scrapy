import re
import time

import requests
from pymongo import MongoClient
from scrapy import Selector

def get_year(datas):
    years = re.findall('[12]\d{3}', datas)
    if years:
        year = int(years[0])
    return year

client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_1010_pharmacodia

cookies = {
    'sensorsdata2015jssdkcross': '%7B%22%24device_id%22%3A%2218b134b762b726-0db7c6ddc44e2d-26031e51-2073600-18b134b762c102e%22%7D',
    'sajssdk_2015_new_user_data_pharmacodia_com': '1',
    '__snaker__id': 'yXJhoMsKVhkN1Xfh',
    'gdxidpyhxdE': 'PX5iJEOkZ7zzYqx2%5CaY3oEucRtu%5CR0TPu6mc0qVNLzYnS7Okq1y4ID8hzIMJmOoHpIipuBHm773f4n3HGCo7cs79YtAXERmq7uDWl2HcR1wmM%2BE6%2FEtzxQKLAbxxXLx7jy%2F9SnNW%2BkDe8A6WVQDw428mPwCHgW4tro6TV0sRTdOfMidx%3A1696836714145',
    'YD00751428505743%3AWM_NI': 'IFz1x45ZsY0Y6w4O%2Bpz5jasZ6N7mNkQA9jNJO82CpChulivExNXsdLNyVFDg%2FUna0qyOiGvmZVbQ%2BIPiclj0q0rbmETL1zXUqf53VXoikihaTFaVeXi4YdU38uoUzPEFMmU%3D',
    'YD00751428505743%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eeb8f26e98e88e90f43ab5e78eb7c15e978f8f86d563ac87ababc97bf2be85a3d62af0fea7c3b92a8b9ab6d2fb40f786bdbab353f6a9fcb0aa7cbaeba682f252f692f98ecd61939ff78bcd428de8fea4f349acaba48af54fbc929894e7488ea79aa7c76ded8ba282b37bbb91a7a8f5679a8aaeb2aa4394b7ad8de93cb3f0be83f04f9894ff9bdb5fb3bafbd4d554adb7a58aeb6b989aafb7e854abec9785d839fcaba1b6f95c879a838ed837e2a3',
    'YD00751428505743%3AWM_TID': '8eZVg9Ra5fxBQREAVFbBzlYeNdu3KfAW',
    'sceneStr': 'perFei.ec0552bb73684f308773a3c75e09ae91_1',
    'qrCodeType': '2',
    'sa_jssdk_2015_data_pharmacodia_com': '%7B%22distinct_id%22%3A%22591b4f91-9048-4465-bab0-0a73b19e72ca%22%2C%22first_id%22%3A%2218b134b762b726-0db7c6ddc44e2d-26031e51-2073600-18b134b762c102e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D',
    'time': 'long',
    'mobile': '18500945556',
    'email': '',
    'username': 'yd_44356533',
    'realName': '%E5%BC%A0%E7%BF%94',
    'authorities': '[]',
    'pmcucookie': '5257b31d856f4b7abdf7e2e33bced1bb',
    'activeAlert': 'false',
    'JSESSIONID': '694A3B4234EFB942DB014609CEAE0EE1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2218b134b762b726-0db7c6ddc44e2d-26031e51-2073600-18b134b762c102e%22%7D; sajssdk_2015_new_user_data_pharmacodia_com=1; __snaker__id=yXJhoMsKVhkN1Xfh; gdxidpyhxdE=PX5iJEOkZ7zzYqx2%5CaY3oEucRtu%5CR0TPu6mc0qVNLzYnS7Okq1y4ID8hzIMJmOoHpIipuBHm773f4n3HGCo7cs79YtAXERmq7uDWl2HcR1wmM%2BE6%2FEtzxQKLAbxxXLx7jy%2F9SnNW%2BkDe8A6WVQDw428mPwCHgW4tro6TV0sRTdOfMidx%3A1696836714145; YD00751428505743%3AWM_NI=IFz1x45ZsY0Y6w4O%2Bpz5jasZ6N7mNkQA9jNJO82CpChulivExNXsdLNyVFDg%2FUna0qyOiGvmZVbQ%2BIPiclj0q0rbmETL1zXUqf53VXoikihaTFaVeXi4YdU38uoUzPEFMmU%3D; YD00751428505743%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb8f26e98e88e90f43ab5e78eb7c15e978f8f86d563ac87ababc97bf2be85a3d62af0fea7c3b92a8b9ab6d2fb40f786bdbab353f6a9fcb0aa7cbaeba682f252f692f98ecd61939ff78bcd428de8fea4f349acaba48af54fbc929894e7488ea79aa7c76ded8ba282b37bbb91a7a8f5679a8aaeb2aa4394b7ad8de93cb3f0be83f04f9894ff9bdb5fb3bafbd4d554adb7a58aeb6b989aafb7e854abec9785d839fcaba1b6f95c879a838ed837e2a3; YD00751428505743%3AWM_TID=8eZVg9Ra5fxBQREAVFbBzlYeNdu3KfAW; sceneStr=perFei.ec0552bb73684f308773a3c75e09ae91_1; qrCodeType=2; sa_jssdk_2015_data_pharmacodia_com=%7B%22distinct_id%22%3A%22591b4f91-9048-4465-bab0-0a73b19e72ca%22%2C%22first_id%22%3A%2218b134b762b726-0db7c6ddc44e2d-26031e51-2073600-18b134b762c102e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; time=long; mobile=18500945556; email=; username=yd_44356533; realName=%E5%BC%A0%E7%BF%94; authorities=[]; pmcucookie=5257b31d856f4b7abdf7e2e33bced1bb; activeAlert=false; JSESSIONID=694A3B4234EFB942DB014609CEAE0EE1',
    'Origin': 'https://data.pharmacodia.com',
    'Referer': 'https://data.pharmacodia.com/cro/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'pmcucookie': '5257b31d856f4b7abdf7e2e33bced1bb',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}






num = 0

for a in range(1,12):
    json_data = {
        'dimension': '',
        'page': a,
        'searchId': 'ff13dd13-9f06-4346-ba81-530ccdef2c6c',
        'size': 10,
        'sortBy': 'pageView',
        'sortOrder': 'DESC',
    }
    while True:
        time.sleep(2)
        try:
            response = requests.post('https://data.pharmacodia.com/api/cro/query/list', cookies=cookies, headers=headers, json=json_data)
            if response.status_code ==200:
                break
            else:
                print(response.status_code)
        except:
            print("程序报错")
    res_json = response.json()
    for b in res_json['data']['records']:
        db_dict = {}
        db_dict['title'] = b['cnShortName']
        db_dict['website'] = b['website']
        db_dict['phone'] = b['phone']
        db_dict['serviceType'] = '; '.join(b['serviceType'])
        db_dict['province'] = b['province']
        db_dict['id'] = b['id']

        db2.insert_one(db_dict)
        num += 1
        print(f'添加{num}条成功')

