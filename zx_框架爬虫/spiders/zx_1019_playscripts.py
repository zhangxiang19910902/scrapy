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
        '_ga': 'GA1.1.645546069.1696991389',
        '_gcl_au': '1.1.1722564331.1696991389',
        'streamstats_anon_id_512709': '9df5e5a9-b227-4fa2-96df-619a8c388673',
        '_hjSessionUser_3682835': 'eyJpZCI6IjdhMDI5YjRkLTk2MTUtNTRjOS04Yzc0LTVmNjczMWY2N2RjNyIsImNyZWF0ZWQiOjE2OTY5OTE0MTAyNjUsImV4aXN0aW5nIjp0cnVlfQ==',
        'scrpop_data': '%7B%22global%22%3A%7B%22views%22%3A7%2C%22lastView%22%3A1697773340%2C%22lastViewElapse%22%3A65%2C%22sessionCount%22%3A1%2C%22lastPop%22%3A%7B%22ts%22%3A0%2C%22vc%22%3A0%2C%22timeSince%22%3A1697773340%2C%22viewsSince%22%3A7%7D%2C%22utm_source%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22(none)%22%7D%2C%22utm_campaign%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22(none)%22%7D%2C%22utm_medium%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22(none)%22%7D%2C%22referrer%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22https%3A%2F%2Fwww.playscripts.com%2Fplay%2F5629%22%7D%7D%2C%22campaigns%22%3A%7B%7D%2C%22exRefCounter%22%3A2%2C%22version%22%3A%5B1%5D%2C%22domain%22%3A%22playscripts.com%22%7D',
        '_uetsid': '8d1c58306ef911eeadeba357d5227c3f',
        '_uetvid': '197837e067de11eebbf29d990666e6b2',
        '_ga_FVN21GS0BD': 'GS1.1.1697784720.6.0.1697784720.60.0.0',
        '_gcl_aw': 'GCL.1697784721.CjwKCAjwp8OpBhAFEiwAG7NaElhbv-I6wOGONnfNMScBcjgJ74N5rteLeSK37lpFYJEOtsyGxVNDlBoCWo4QAvD_BwE',
        '_hjIncludedInSessionSample_3682835': '1',
        '_hjSession_3682835': 'eyJpZCI6IjEyZjFiN2E2LWU0YTYtNDczYy05ODVhLWYyZmEwOTgxMmFlZiIsImNyZWF0ZWQiOjE2OTc3ODQ3MjEzMjgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '__kla_id': 'eyJjaWQiOiJaVFF6T0dGak0yVXROR001WmkwME9XWXdMV0UwTjJJdFlXSmhaREZoWVdFeE4yTmsiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTY5OTEzOTIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBsYXlzY3JpcHRzLmNvbS9wcm9mZXNzaW9uYWwtdGhlYXRyZSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5Nzc4NDcyMiwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGxheXNjcmlwdHMuY29tLz9nYWRfc291cmNlPTEmZ2NsaWQ9Q2p3S0NBandwOE9wQmhBRkVpd0FHN05hRWxoYnYtSTZ3T0dPTm5mTk1TY0JjamdKNzRONXJ0ZUxlU0szN2xwRllKRU90c3lHeFZORGxCb0NXbzRRQXZEX0J3RSJ9fQ==',
        '_dd_s': 'logs=1&id=b48de6cb-be44-47c9-a744-5c806f0d5204&created=1697784724245&expire=1697785684095',
    }

    headers = {
        'authority': 'www.playscripts.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'cookie': '_ga=GA1.1.645546069.1696991389; _gcl_au=1.1.1722564331.1696991389; streamstats_anon_id_512709=9df5e5a9-b227-4fa2-96df-619a8c388673; _hjSessionUser_3682835=eyJpZCI6IjdhMDI5YjRkLTk2MTUtNTRjOS04Yzc0LTVmNjczMWY2N2RjNyIsImNyZWF0ZWQiOjE2OTY5OTE0MTAyNjUsImV4aXN0aW5nIjp0cnVlfQ==; scrpop_data=%7B%22global%22%3A%7B%22views%22%3A7%2C%22lastView%22%3A1697773340%2C%22lastViewElapse%22%3A65%2C%22sessionCount%22%3A1%2C%22lastPop%22%3A%7B%22ts%22%3A0%2C%22vc%22%3A0%2C%22timeSince%22%3A1697773340%2C%22viewsSince%22%3A7%7D%2C%22utm_source%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22(none)%22%7D%2C%22utm_campaign%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22(none)%22%7D%2C%22utm_medium%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22(none)%22%7D%2C%22referrer%22%3A%7B%22first%22%3A%22(none)%22%2C%22last%22%3A%22https%3A%2F%2Fwww.playscripts.com%2Fplay%2F5629%22%7D%7D%2C%22campaigns%22%3A%7B%7D%2C%22exRefCounter%22%3A2%2C%22version%22%3A%5B1%5D%2C%22domain%22%3A%22playscripts.com%22%7D; _uetsid=8d1c58306ef911eeadeba357d5227c3f; _uetvid=197837e067de11eebbf29d990666e6b2; _ga_FVN21GS0BD=GS1.1.1697784720.6.0.1697784720.60.0.0; _gcl_aw=GCL.1697784721.CjwKCAjwp8OpBhAFEiwAG7NaElhbv-I6wOGONnfNMScBcjgJ74N5rteLeSK37lpFYJEOtsyGxVNDlBoCWo4QAvD_BwE; _hjIncludedInSessionSample_3682835=1; _hjSession_3682835=eyJpZCI6IjEyZjFiN2E2LWU0YTYtNDczYy05ODVhLWYyZmEwOTgxMmFlZiIsImNyZWF0ZWQiOjE2OTc3ODQ3MjEzMjgsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __kla_id=eyJjaWQiOiJaVFF6T0dGak0yVXROR001WmkwME9XWXdMV0UwTjJJdFlXSmhaREZoWVdFeE4yTmsiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTY5OTEzOTIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBsYXlzY3JpcHRzLmNvbS9wcm9mZXNzaW9uYWwtdGhlYXRyZSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5Nzc4NDcyMiwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGxheXNjcmlwdHMuY29tLz9nYWRfc291cmNlPTEmZ2NsaWQ9Q2p3S0NBandwOE9wQmhBRkVpd0FHN05hRWxoYnYtSTZ3T0dPTm5mTk1TY0JjamdKNzRONXJ0ZUxlU0szN2xwRllKRU90c3lHeFZORGxCb0NXbzRRQXZEX0J3RSJ9fQ==; _dd_s=logs=1&id=b48de6cb-be44-47c9-a744-5c806f0d5204&created=1697784724245&expire=1697785684095',
        'referer': 'https://www.playscripts.com/?gad_source=1&gclid=CjwKCAjwp8OpBhAFEiwAG7NaElhbv-I6wOGONnfNMScBcjgJ74N5rteLeSK37lpFYJEOtsyGxVNDlBoCWo4QAvD_BwE',
        # 'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"',
        # 'sec-fetch-dest': 'document',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-user': '?1',
        # 'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_1031_playscripts
    num = 0

    aaa = [
        'https://www.playscripts.com/high-school',
        'https://www.playscripts.com/middle-school',
        'https://www.playscripts.com/college-theatre',
        'https://www.playscripts.com/professional-theatre',
        'https://www.playscripts.com/community-theatre',
        'https://www.playscripts.com/theatre-for-young-audiences'
    ]

    # for a in aaa:
    #     a = 'https://www.playscripts.com/middle-school'
    # while True:
    #     time.sleep(2)
    #     try:
    #         response = requests.get(a, cookies=cookies,headers=headers)
    #         if response.status_code == 200:
    #             break
    #         else:
    #             print(response.status_code)
    #     except:
    #         print("程序报错")

    # res = Selector(text=response.text)
    # dump1 = res.xpath("//*[@class='title-sections section-bg-dark']")
    # for b in dump1:
    #     title_b = ''.join(b.xpath(".//div[@class='tlt-title clearfix']/h3//text()").getall()).strip()
    #     url_b = b.xpath(".//*[@class='see-all-btn button-blue']/@href").get()
    #     if url_b:
    #         url_b = 'https://www.playscripts.com' + url_b
    #         while True:
    #             time.sleep(2)
    #             try:
    #                 response1 = requests.get(url_b, cookies=cookies, headers=headers)
    #                 if response1.status_code == 200:
    #                     break
    #                 else:
    #                     print(response1.status_code)
    #             except:
    #                 print("程序报错")
    #
    #         res1 = Selector(text=response1.text)
    #
    #         page = ''.join(res1.xpath("//div[@class='search-results following2']/div[@class='pagination'][1]//li[@class='last-page']//text()").getall()).strip()

    for c in range(116):
        url_c = f"https://www.playscripts.com/find-a-play?sort=popularity&page={c}"
        # url_c = f"https://www.playscripts.com/find-a-play?target_group%5B%5D=youth&subgenres%5B%5D=34&sort=popularity"
        while True:
            time.sleep(2)
            try:
                response2 = requests.get(url_c, cookies=cookies, headers=headers)
                if response2.status_code == 200:
                    break
                else:
                    print(response2.status_code)
            except:
                print("程序报错")
        res2 = Selector(text=response2.text)

        url_d = res2.xpath("//h3/a/@href").getall()

        for d in url_d:
            url_e = 'https://www.playscripts.com' + d

            while True:
                time.sleep(2)
                try:
                    response3 = requests.get(url_e, cookies=cookies, headers=headers)
                    if response3.status_code == 200:
                        break
                    else:
                        print(response3.status_code)
                except:
                    print("程序报错")

            res3 = Selector(text=response3.text)

            content_list = res3.xpath("//*[@id='all-prodhist']//tr")
            for ii in content_list:
                db_dict = {}
                # db_dict['Venue_type'] = 'theatre for young audiences'
                # db_dict['title'] = "HOLIDAY HITS"
                db_dict['Name'] = ''.join(res3.xpath("//span[@class='play_main']//text()").getall()).strip()
                db_dict['production_url'] = url_e
                db_dict['author_type'] = ''.join(
                    res3.xpath("//span[@class='playauthors']/text()").getall()).strip()
                db_dict['author'] = '; '.join(
                    res3.xpath("//span[@class='playauthors']//a//text()").getall()).strip()
                db_dict['category'] = ''.join(
                    res3.xpath("//*[@class='genre-duration-container']/div[1]//text()").getall()).strip()
                db_dict['times'] = ''.join(res3.xpath(
                    "//*[@class='genre-duration-container']/div[last()]//text()").getall()).strip()
                db_dict['casting'] = ' '.join(res3.xpath(
                    "//*[@class='movie-info']/div[1]/following-sibling::div//text()").getall()).strip()
                db_dict['play_description'] = ' '.join(res3.xpath("//*[@class='story-description']//text()").getall()).strip()

                db_dict['product_date'] = ''.join(ii.xpath("./td[1]//text()").getall()).strip()
                db_dict['production_name'] = ''.join(ii.xpath("./td[2]//text()").getall()).strip()
                db_dict['production_address'] = ''.join(ii.xpath("./td[3]//text()").getall()).strip()
                db2.insert_one(db_dict)
                num +=1
                print(f'添加{num}条成功----{c}---{db_dict["Name"]}')

if __name__ == '__main__':
    parse()