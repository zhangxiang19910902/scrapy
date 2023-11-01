import time

from scrapy import Selector
from pymongo import MongoClient
import requests


def get_key_by_value(value):
    dict_data = {
        'AUS': 'Australia',
        'AFG': 'Afghanistan',
        'BEL': 'Belgium',
        'BHS': 'Bahamas',
        'BGD': 'Bangladesh',
        'CAN': 'Canada',
        'CHN': 'China',
        'COL': 'Colombia',
        'DEU': 'Germany',
        'DZA': 'Algeria',
        'EGY': 'Egypt',
        'ESP': 'Spain',
        'FRA': 'France',
        'GBR': 'United Kingdom',
        'GEO': 'Georgia',
        'IND': 'Indonesia',
        'ITA': 'Italy',
        'JPN': 'Japan',
        'KAZ': 'Kazakhstan',
        'KOR': 'Korea',
        'LVA': 'Latvia',
        'MAR': 'Morocco',
        'MEX': 'Mexico',
        'MNG': 'Mongolia',
        'MYS': 'Malaysia',
        'NGA': 'Nigeria',
        'NLD': 'Netherlands',
        'NZL': 'New Zealand',
        'OAS': 'Other Asia',
        'PER': 'Peru',
        'PHL': 'Philippines',
        'RUS': 'Russian Federation',
        'SUD': 'Sudan',
        'THA': 'Thailand',
        'TUR': 'Turkey',
        'USA': 'United States',
        'VNM': 'Vietnam',
        # 'GBR': 'united kindom',
        'KGZ': 'Kyrgyz Republic',
        'AZE': 'Azerbaijan',
        'ARM': 'Armenia',
        'UZB': 'Uzbekistan',
        'BLR': 'Belarus',
        'ARE': 'United Arab Emirates',
        'AGO': 'Angola',

    }
    for key, val in dict_data.items():
        if val == value:
            return key
def get_url():
    years = [str(x) for x in range(1990, 2022)]
    products = [
                '100110',
                '100190',
                '110100',
                '110900',
                '110311',
                '110811',
                '190211',
                '190219',
                '190220',
                '190230',
                '190240',
                '190510',
                '190520',
                '190530',
                '190540',
                '190590',
                '190120',
                '230230']
    urls = []
    for year in years:
        for product in products:
            url = f'https://wits.worldbank.org/trade/comtrade/en/country/AUS/year/{year}/tradeflow/Exports/partner/WLD/product/{product}'
            urls.append([url,year,product])
    return urls


def get_content(urls):
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_1101_worldbank澳洲对世界_Quantity
    num = 0


    cookies = {
        'ASP.NET_SessionId': 'q0ovhmwweqykp3pfpeumanjt',
        'AMCVS_1E7B833554B8360D0A4C98A5%40AdobeOrg': '1',
        'at_check': 'true',
        's_cc': 'true',
        '_gcl_au': '1.1.1031868594.1698289214',
        'AMCV_1E7B833554B8360D0A4C98A5%40AdobeOrg': '179643557%7CMCIDTS%7C19657%7CMCMID%7C27869230437505577593246658815043084275%7CMCAAMLH-1698894014%7C9%7CMCAAMB-1698894014%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698296414s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0%7CMCCIDH%7C0',
        's_vnc365': '1729825215238%26vn%3D1',
        '_fbp': 'fb.1.1698289215408.1227672134',
        's_ips': '931',
        's_sq': '',
        'mbox': 'PC#7f3fbe965a9b4eb28a076c20c31ac207.35_0#1761536685|session#852067d3a6164b7190b55fbc413bddad#1698293745',
        's_tp': '996',
        's_ppv': 'en%253Awb%253Awits%253A%252Ftrade%252Fcomtrade%252Fen%252Fcountry%252Faus%252Fyear%252F2000%252Ftradeflow%252Fexports%252Fpartner%252Fall%252Fproduct%252F110100%2C93%2C93%2C93%2C931%2C1%2C1',
        's_nr730': '1698292337320-New',
        's_tslv': '1698292337321',
    }

    headers = {
        'authority': 'wits.worldbank.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'ASP.NET_SessionId=q0ovhmwweqykp3pfpeumanjt; AMCVS_1E7B833554B8360D0A4C98A5%40AdobeOrg=1; at_check=true; s_cc=true; _gcl_au=1.1.1031868594.1698289214; AMCV_1E7B833554B8360D0A4C98A5%40AdobeOrg=179643557%7CMCIDTS%7C19657%7CMCMID%7C27869230437505577593246658815043084275%7CMCAAMLH-1698894014%7C9%7CMCAAMB-1698894014%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698296414s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0%7CMCCIDH%7C0; s_vnc365=1729825215238%26vn%3D1; _fbp=fb.1.1698289215408.1227672134; s_ips=931; s_sq=; mbox=PC#7f3fbe965a9b4eb28a076c20c31ac207.35_0#1761536685|session#852067d3a6164b7190b55fbc413bddad#1698293745; s_tp=996; s_ppv=en%253Awb%253Awits%253A%252Ftrade%252Fcomtrade%252Fen%252Fcountry%252Faus%252Fyear%252F2000%252Ftradeflow%252Fexports%252Fpartner%252Fall%252Fproduct%252F110100%2C93%2C93%2C93%2C931%2C1%2C1; s_nr730=1698292337320-New; s_tslv=1698292337321',
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

    for a in urls:

        while True:
            try:
                response = requests.get(
                    a[0],
                    cookies=cookies,
                    headers=headers,
                )
                if response.status_code == 200:
                    break
                else:
                    pass
            except:
                print("程序报错")
            # time.sleep(2)

        res = Selector(text=response.text)
        aozhou_single = ''.join(res.xpath(f"//*[@class='metadataTable']/tbody/tr[1]/following-sibling::tr/td[8]//text()").getall()).replace(",", '').strip()
        # time.sleep(2)

        db_dict = {}

        db_dict['year'] = a[1]
        db_dict['word'] = aozhou_single
        db_dict['code'] = a[2]
        db2.insert_one(db_dict)
        num += 1
        print(f"添加{num}条成功---{a[1]}---{db_dict['word']}")

if __name__ == '__main__':
    urls = get_url()
    get_content(urls)