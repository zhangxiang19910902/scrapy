# -*- coding: utf-8 -*-

import requests
import execjs


cookies = {
    'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f': '1695626212',
    'mobile_iindex_uuid': '510a0845-7c9e-56b8-9480-6d262db845d8',
    'Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f': '1695626319',
}

headers = {
    'authority': 'www.chinaindex.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f=1695626212; mobile_iindex_uuid=510a0845-7c9e-56b8-9480-6d262db845d8; Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f=1695626319',
    'funcid': 'undefined',
    'incognitomode': '0',
    'referer': 'https://www.chinaindex.net/ranklist/4',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'uuid': '510a0845-7c9e-56b8-9480-6d262db845d8',
}

params = {
    'channel': 'movielist',
    'sign': '5f3cce6a40c09a221b21104cc98436a3',
}
#
# response = requests.get(
#     'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# ).json()
#
# data = response['data']
# lastFetchTime = response['lastFetchTime']
#
#
# aaa = open("zx_0925_aesjs.js",'r',encoding='utf-8').read()
#
# ctx = execjs.compile(aaa)
#
# ctxx = ctx.call('aaabbb',data, lastFetchTime)
# print(ctxx)


