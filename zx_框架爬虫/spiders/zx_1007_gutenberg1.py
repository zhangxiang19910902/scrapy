import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.gutenberg.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Sun, 01 Oct 2023 12:48:42 GMT',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'If-None-Natch':'',
    'If-Modified-Since':''
}




response = requests.get('https://www.gutenberg.org/cache/epub/1399/pg1399-images.html', headers=headers)

res = BeautifulSoup(response.text,'html.parser')

aaa = ''.join(res.findAll("div")).strip()


with open(f'./gutenberg.txt', mode='w',encoding='utf-8') as f:
    f.write(aaa)

