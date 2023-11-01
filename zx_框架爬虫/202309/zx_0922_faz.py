# -*- coding: utf-8 -*-
import re
import scrapy
import json
from scrapy import Request as req
from scrapy import Selector
from pymongo import MongoClient



class ZgpSciepubSpider(scrapy.Spider):
    num = 0

    name = 'zx_0922_faz'

    handle_httpstatus_list = [302,304]

    custom_settings = {
        # 'CONCURRENT_REQUESTS': 8,
        # 'DOWNLOAD_DELAY': 2,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'zx_框架爬虫.middlewares.ProxyMiddleware': 543,
        # },
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'f_gdpr=1; at_check=true; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKpg8jD8QwqI3ViVFKBTHzSnNygOwSsILq2lEJTAmlWAASvAbfpgEAAA%3D%3D; _sp_v1_p=297; _sp_v1_data=646292; _sp_su=false; adobe_isPurAbo=false; consentUUID=245cf12d-ab9f-43a4-929e-7a304f91dc84_23; consentDate=2023-09-21T06:02:31.834Z; affiliate_id=PIOFAZ; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Afalse%2C%22aa%22%3Atrue%2C%22campaign%22%3Afalse%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Afalse%2C%22target%22%3Atrue%2C%22mediaaa%22%3Afalse%7D; Affiliate ID=PIOFAZ; AMCVS_C6211D085C4EFDF30A495CFC%40AdobeOrg=1; AMCVS_41833DF75A550B4B0A495DA6%40AdobeOrg=1; iqaa_cc=true; s_ecid=MCMID%7C33454446628423628180143156059033626306; _gcl_au=1.1.892896302.1695276154; awin_comissiongroup=DEFAULT; s_cc=true; AAMC_iqdigital_0=REGION%7C3; aam_uuid=27647091569747093360707003345489471320; _pin_unauth=dWlkPU56bGpOelF6T0dJdFpXWmpaUzAwTlRKakxXRTVObU10TVRFME9XTTBORGxrTmpFeg; _fbp=fb.1.1695276155236.1546843431; _cb=DuDDQiCGagN7DSKZk5; tmpPersistentuserId=18704d7fce4452f489f0605d15824e7a; trc_cookie_storage=taboola%2520global%253Auser-id%3D3ae30100-ff73-493d-bc39-2001e7568333-tuctbd076b2; iqaa_sq=%5B%5BB%5D%5D; s_sq=%5B%5BB%5D%5D; adobe_DAI-2=2:D; adbprevpage=/aktuell/wirtschaft/markt-fuer-schweinefleisch-warum-der-preis-steigt-16651326; _gid=GA1.2.1182847248.1695368528; srvid=bb395a13b39656152115c1c3cdba904e; JSESSIONID=46EC04F255A21107793614FCA58F098F; AMCV_41833DF75A550B4B0A495DA6%40AdobeOrg=-2121179033%7CMCMID%7C27755755385254043860654478387955831266%7CMCAAMLH-1695973331%7C3%7CMCAAMB-1695973331%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1695375731s%7CNONE%7CvVersion%7C5.3.0; emqsegs=e0,e2ax,e1p,e8e,e3m,e1l,e6a,e2aw,e3f,e3v,e7j,e6b,e3n,e1u,e37,eky,e1r,e69,el0,e2h0,e2jg,e1yo,e1hf,e2h6,ekx,e2gy,e63,e1q,e1,e64,e7k,e39,e1hh,e1o,e8b,e1h,e2gz,e1ii,e3l,e3o,e2h7,e8k,e1j,e2uz; adp_segs=e0,e2ax,e1p,e8e,e3m,e6a,e2aw,e3f,e3v,e7j,e6b,e3n,e1u,e37,eky,e1r,e69,el0,e2h0,e2jg,e1yo,e2h6,ekx,e2gy,e63,e1q,e1,e64,e7k,e39,e1o,e8b,e1h,e2gz,e3l,e3o,e2h7,e8k,e1j; dypagr=; AMCV_C6211D085C4EFDF30A495CFC%40AdobeOrg=-2121179033%7CMCMID%7C33454446628423628180143156059033626306%7CMCAAMLH-1695973333%7C3%7CMCAAMB-1695973333%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1695375733s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.3.0; _cb_svref=null; ln_or=eyI3NDg1ODUiOiJkIn0%3D; outbrain_cid_fetch=true; adobe_pageViewCount=NaN; adobe_DAI-1=A:0-0-4-0-0-0-0|B:0-0-4-0-0-0-0|C:0-0-0-0-0-0-0|D:0-0-0-0-0-0-0|E:0-0-0-0-0-0-0|F:0-0-0-0-0-0-0|G:7-2-21-0-0-0-0|I:0-0-0-0-0-0-0|J:1-1-1-0-0-0-0|K:0-0-0-0-0-0-0|_V:0.2|_vC:3|_tS:51|_lUt:13386718372|_vSt:13386222029; mbox=PC#196d0e268aa04389a7f0691a9162d319.38_0#1758613825|session#d21911afef624024aa2ea04ce93ed109#1695370885; ioam2018=001f745a6477a276d650bdc78%3A1722319352881%3A1695276152881%3A.faz.net%3A31%3Afaz%3AFaz_Suche%3Anoevent%3A1695369024830%3Ahf0xzr; adb_dslv=1695369024842; _ga=GA1.1.115870537.1695276153; _ga_CXZVB3PCZ6=GS1.1.1695368538.4.1.1695369025.0.0.0; _chartbeat2=.1695276155251.1695369026025.11.TGjUAD5XKHFDjLwE2BoLAT_DRaDi5.7',
        'If-Modified-Since': 'Fri, 22 Sep 2023 07:50:20 GMT',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    base_url = 'https://www.faz.net/suche/s4.html?ct=article&ct=audio&ct=blog&ct=gallery&ct=infografik&ct=storytelling&ct=video&&query=china&from=01.02.2020&to=01.03.2020#listPagination'




    def start_requests(self):
        date_list_2019 = [
            '01.01.2019',
            '01.02.2019',
            '01.03.2019',
            '01.04.2019',
            '01.05.2019',
            '01.06.2019',
            '01.07.2019',
            '01.08.2019',
            '01.09.2019',
            '01.10.2019',
            '01.11.2019',
            '01.12.2019',
            '01.01.2020',
        ]

        date_list_2020 = [
            '01.01.2020',
            '01.02.2020',
            '01.03.2020',
            '01.04.2020',
            '01.05.2020',
            '01.06.2020',
            '01.07.2020',
            '01.08.2020',
            '01.09.2020',
            '01.10.2020',
            '01.11.2020',
            '01.12.2020',
            '01.01.2021',
        ]

        date_list_2021 = [
            '01.01.2021',
            '01.02.2021',
            '01.03.2021',
            '01.04.2021',
            '01.05.2021',
            '01.06.2021',
            '01.07.2021',
            '01.08.2021',
            '01.09.2021',
            '01.10.2021',
            '01.11.2021',
            '01.12.2021',
            '01.01.2022',
        ]

        date_list_2022 = [
            '01.01.2022',
            '01.02.2022',
            '01.03.2022',
            '01.04.2022',
            '01.05.2022',
            '01.06.2022',
            '01.07.2022',
            '01.08.2022',
            '01.09.2022',
            '01.10.2022',
            '01.11.2022',
            '01.12.2022',
            '01.01.2023',
        ]

        for b in range(12):
            for c in range(1,21):
                url = f'https://www.faz.net/suche/s{c}.html?ct=article&ct=audio&ct=blog&ct=gallery&ct=infografik&ct=storytelling&ct=video&&query=china&from={date_list_2022[b]}&to={date_list_2022[b+1]}#listPagination'
                yield scrapy.Request(url=url, headers=self.headers, callback=self.parse,dont_filter=True)



    def parse(self, response, **kwargs):
        journal_url_list = response.xpath("//a[@class='js-hlp-LinkSwap js-tsr-Base_ContentLink tsr-Base_ContentLink']//span[@class='ico-Base ico-Base-is-in-teaser-headline']/../../../../@href").getall()
        if journal_url_list:
            for i in journal_url_list:
                new_url = i if 'http' in i else response.urljoin(i)
                yield req(url=new_url.strip(), headers=self.headers, callback=self.pro_data,
                           dont_filter=True)




    def pro_data(self, response, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db2 = client.name.zx_0922_faz

        db_dict = {}
        db_dict['标题'] = ''.join(response.xpath("//*[@class='atc-IntroText']//text()").getall()).strip()
        db_dict['摘要'] =''.join(response.xpath("//*[@id='pageIndex_1']//text()").getall()).strip()
        db_dict['正文'] =''.join(response.xpath("//*[@class='atc-TextParagraph']//text()").getall()).strip()
        db_dict['日期'] =''.join(response.xpath("//*[@class='atc-MetaTime']//text()").getall()).strip()
        db_dict['url'] =response.url
        db2.insert_one(db_dict)
        self.num +=1
        print(f'添加{self.num}条成功')

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(["scrapy", "crawl", 'zx_0922_faz'])

