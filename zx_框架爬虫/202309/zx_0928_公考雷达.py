import time

import requests
from pymongo import MongoClient
from scrapy import Selector
client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_0927_ybzhan
def gongkao(keyword,page):
    cookies = {
        'Hm_lvt_f721d958b1ffbdd95625a927f9bbe719': '1695694037',
        'Hm_lvt_a85566772a4d8c7093230e45128ffa8f': '1695694037',
        'XSRF-TOKEN': 'eyJpdiI6IlZ3cnFoSGF0RXRHZEs5U0FnM04wQmc9PSIsInZhbHVlIjoibjNqVGJEbVFSazE0TjlTdWNaZ2RUdjJOMFR5Q0RGUHlCemp6eExhT2dtREx0cFFZTzFJZXc3UW5oMVwvMndUYXQiLCJtYWMiOiIxY2M5YjIwZGE1ZDkyMzk4ODU2MGNmM2YxYzIxOWEwMWEyMDkyMzQzNjliYWE4NWQzMTQ3MmFiYTcyZDI4Nzc5In0%3D',
        'gkld_session': 'eyJpdiI6IjFLSVgwY3hsb1A5VmtHZzhpSDR3WWc9PSIsInZhbHVlIjoiXC9nMFA0VzI2ZEtLN3k4eGYrQWNIbjFLaTZoOFE1T3Z5NUNpQmQ3b0tNdHVtZklQQTdOeHVHM3Y4WXpweGcxeTlyVlZqUVdtTUN3M01UcGJLajFFR2lhemZtZ2JCRUNwaFM1WU1uejMwcm9Nb0lRMDN2ZlwvRXExZzA0WU9ueHZsUyIsIm1hYyI6IjM4ODNmODQzYWFlMTRhOTIyNmEwZDY3ZmRiNWEwY2NhNTRhYmI1YTI5ZTZiNzk0MGJiNmE4OGE3MGJhNmE0YmIifQ%3D%3D',
        'Hm_lpvt_f721d958b1ffbdd95625a927f9bbe719': '1695867381',
        'Hm_lpvt_a85566772a4d8c7093230e45128ffa8f': '1695867381',
        'acw_tc': '2760823116958786433945742e74eb853cf6ed9921d896f5db6bb686ec14e4',
        'acw_sc__v2': '65150e02acb6a64fe51bd2a7e04c72e1bc2c8bf7',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_f721d958b1ffbdd95625a927f9bbe719=1695694037; Hm_lvt_a85566772a4d8c7093230e45128ffa8f=1695694037; acw_tc=2760821616958670977094722e40a0fadfbf9b3eeb363cbd722f47a5f19179; acw_sc__v2=6514e0d936582f75ddde229c9667a81262ee2e81; XSRF-TOKEN=eyJpdiI6Im9MTTNMK2ZHSTNuZ3NJdUE1NEdIbmc9PSIsInZhbHVlIjoiVkNWc1doeEtiU0hpWVRRZFNHNFZhOUR2Nk01cGNsaUJTdVgrM09VQjBCT3BiMUlBOHRzazZUQ3pKWFcxalZYOCIsIm1hYyI6IjY1Y2YyNjFiNDg0NzI4M2JiMTA0NGFiZGFlMTNhYTY1Njk2ZDc3Y2Y3ZTJhZDU1Mjk0N2Q4NjhkZTI3N2U5YWMifQ%3D%3D; gkld_session=eyJpdiI6Ik9kUkRyd1dsQXg0WitmMkQrTlpIeFE9PSIsInZhbHVlIjoid2FyVWwzcm9WNDZhR3pEeEREZjhZZWRjMVZaM0paMzl2UnJxZjNKS1RKMDZteVR5SndjREdXVmJENjRtcldkUUJEVkIzVno3VzNOOVJ4RXBkYk5pNjA2VGhEY1FrM2dobDFCZml6MDRNZjFGQmZJaGpzR0JwM29sTlZ2bEdcL2dNIiwibWFjIjoiZDk5NGVjZGIxNjVjZmE5ZjQxNmE5YzQ0MzgwODVkMWI2MTljYjBhOTI2ODc3MGNmZDg0NDBhZjE0NDk5ZDg5YiJ9; Hm_lpvt_f721d958b1ffbdd95625a927f9bbe719=1695867098; Hm_lpvt_a85566772a4d8c7093230e45128ffa8f=1695867098',
        'Referer': 'https://www.gongkaoleida.com/search?searchType=2&keyword=%E8%BE%85%E5%AF%BC%E5%91%98&sortType=2&enrollFilter=0&page=1',
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
    for a in range(1,page+1):
        params = {
            'searchType': '2',
            'keyword': keyword,
            'sortType': '2',
            'enrollFilter': '0',
            'page': a,
        }

        while True:
            try:
                response = requests.get('https://www.gongkaoleida.com/search', params=params, cookies=cookies, headers=headers)
                if response.status_code == 200:
                    break
                else:
                    print(response.status_code)
            except:
                print("没有访问到页面！")

        res = Selector(text=response.text)

        url_list = res.xpath("//ul[@class='search-list']/li//a/@href").getall()



        for b in url_list:
            cookies1 = {
                'Hm_lvt_f721d958b1ffbdd95625a927f9bbe719': '1695694037',
                'Hm_lvt_a85566772a4d8c7093230e45128ffa8f': '1695694037',
                'acw_tc': '2760821616958670977094722e40a0fadfbf9b3eeb363cbd722f47a5f19179',
                'acw_sc__v2': '6514e0d936582f75ddde229c9667a81262ee2e81',
                'XSRF-TOKEN': 'eyJpdiI6InZEV2t2bFQ1OTBpekk5UlBGem5vZ2c9PSIsInZhbHVlIjoiUFFFdHhWZUl5S1Z5OGhsK1RYSXIwR1pnU0VcL3hoTVFyTTRqT0dmMnhRamt1U0VXY1Q2RWlcLzQzTDZlWHB2TnNVIiwibWFjIjoiNDEyYzg4YzIwOTEyMTlmOTI4ZDkwZGM1NGRmZWVjZThhYzkwZWE5OWE2MjVlNDRmMWI5YTk1MDRlZGZkMGNlMSJ9',
                'gkld_session': 'eyJpdiI6IndvTXdTVTdUQTdLZEZuM1VScCtSdGc9PSIsInZhbHVlIjoicHhYdEpOeEdCazNNdzhyb3d3MWx5XC8rUlFNMDdiTTNWbHFvXC9IRzdUeGFCZlg5TlBERzlcL3dJdjBiV2lmWE5STFMycXVyelFHa085ckJuXC8ySU1qNWFpQ2lcL1ZJVUE1UjAzbUx2RkpidkZ1RFlydVJLY242WEVoajJRQnh1blowQiIsIm1hYyI6ImFmMDQ5MDE2Y2M3OTA2ZmJlYmQ4MzUwZDNiYWJiNmVlY2UzMjI5NTY3OTM1ODMwOGNlZTQ5ZTQ1OGNkMWE1MGEifQ%3D%3D',
                'Hm_lpvt_f721d958b1ffbdd95625a927f9bbe719': '1695867377',
                'Hm_lpvt_a85566772a4d8c7093230e45128ffa8f': '1695867377',
            }

            headers1 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                # 'Cookie': 'Hm_lvt_f721d958b1ffbdd95625a927f9bbe719=1695694037; Hm_lvt_a85566772a4d8c7093230e45128ffa8f=1695694037; acw_tc=2760821616958670977094722e40a0fadfbf9b3eeb363cbd722f47a5f19179; acw_sc__v2=6514e0d936582f75ddde229c9667a81262ee2e81; XSRF-TOKEN=eyJpdiI6InZEV2t2bFQ1OTBpekk5UlBGem5vZ2c9PSIsInZhbHVlIjoiUFFFdHhWZUl5S1Z5OGhsK1RYSXIwR1pnU0VcL3hoTVFyTTRqT0dmMnhRamt1U0VXY1Q2RWlcLzQzTDZlWHB2TnNVIiwibWFjIjoiNDEyYzg4YzIwOTEyMTlmOTI4ZDkwZGM1NGRmZWVjZThhYzkwZWE5OWE2MjVlNDRmMWI5YTk1MDRlZGZkMGNlMSJ9; gkld_session=eyJpdiI6IndvTXdTVTdUQTdLZEZuM1VScCtSdGc9PSIsInZhbHVlIjoicHhYdEpOeEdCazNNdzhyb3d3MWx5XC8rUlFNMDdiTTNWbHFvXC9IRzdUeGFCZlg5TlBERzlcL3dJdjBiV2lmWE5STFMycXVyelFHa085ckJuXC8ySU1qNWFpQ2lcL1ZJVUE1UjAzbUx2RkpidkZ1RFlydVJLY242WEVoajJRQnh1blowQiIsIm1hYyI6ImFmMDQ5MDE2Y2M3OTA2ZmJlYmQ4MzUwZDNiYWJiNmVlY2UzMjI5NTY3OTM1ODMwOGNlZTQ5ZTQ1OGNkMWE1MGEifQ%3D%3D; Hm_lpvt_f721d958b1ffbdd95625a927f9bbe719=1695867377; Hm_lpvt_a85566772a4d8c7093230e45128ffa8f=1695867377',
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

            while True:
                try:
                    response1 = requests.get(b, headers=headers1, cookies=cookies1)
                    if response1.status_code == 200:
                        break
                    else:
                        print(response1.status_code)
                except:
                    print("没有访问到页面！")
            res1 = Selector(text=response1.text)

            zhiwei_name = ''.join(res1.xpath("//th[contains(text(),'职位名称')]/following-sibling::td[1]//text()").getall()).strip()
            baokao_diqu = ''.join(res1.xpath("//th[contains(text(),'职位名称')]/following-sibling::td[1]//text()").getall()).strip()




if __name__ == '__main__':
    keyword = '辅导员'
    page = 500
    gongkao(keyword,page)