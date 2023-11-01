import requests
import time
import re
from scrapy import Selector




num = 1

cookies = {
    'mm_v8': '80',
    'mm_v8': '20',
    'affinity': '"cee875c3597c01a3"',
    'country_code': 'in',
    'lang': 'en',
    'notice_behavior': 'implied|eu',
    '_mkto_trk': 'id:483-DRZ-814&token:_mch-kyndryl.com-1697507521704-49658',
    '_gcl_au': '1.1.378605285.1697507522',
    'AMCVS_CB2D53C960AC271C0A495E19%40AdobeOrg': '1',
    'at_check': 'true',
    '_rdt_uuid': '1697507522005.24648623-ff80-4655-b2ce-290e1ccd2b2f',
    '__pdst': 'e3557c3d7d444ff681bca79646b71c81',
    's_ecid': 'MCMID%7C32660101027481237212805852114510755205',
    's_cc': 'true',
    'AMCV_CB2D53C960AC271C0A495E19%40AdobeOrg': '-1124106680%7CMCIDTS%7C19648%7CMCMID%7C32660101027481237212805852114510755205%7CMCAAMLH-1698112321%7C11%7CMCAAMB-1698112321%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1697514722s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0',
    'mdLogger': 'false',
    'kampyle_userid': '90c5-f306-05dc-9d9e-6e90-6d72-ffa8-724b',
    'kampyleUserSession': '1697507522879',
    'kampyleUserSessionsCount': '1',
    '_uetsid': 'c3faaa806c8f11eeac87b5f385a5d658',
    '_uetvid': 'c3fad7406c8f11ee9760ed602e8b7705',
    'mbox': 'session#8a021e1b8cde4606849b801d0c1d1de7#1697509430|PC#8a021e1b8cde4606849b801d0c1d1de7.32_0#1760752370',
    '_hjSessionUser_2730899': 'eyJpZCI6IjA2MzdkMThjLWY3MWUtNTAxOC04Mjc1LTJhMWI1YjYwMGU3NiIsImNyZWF0ZWQiOjE2OTc1MDc1MjI3MDUsImV4aXN0aW5nIjp0cnVlfQ==',
    'utag_main': 'v_id:018b3b5532e7002211bb77d2786e0506f002e06700bd0$_sn:1$_se:10$_ss:0$_st:1697509391209$ses_id:1697507521256%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:kyndryl.com$dc_visit:1$dc_event:10%3Bexp-session$dc_region:ap-east-1%3Bexp-session$_aa:32660101027481237212805852114510755205%3B%20s_cc%3Dtrue%3B%20AMCV_CB2D53C960AC271C0A495E19%40AdobeOrg%3D-1124106680',
    'kampyleSessionPageCounter': '8',
    '__cf_bm': 'U.7955s9_XKPMoybMz67P3L3KZzvJZ81b7.qDVL7li8-1697511732-0-AW0YeAGafXc51mI3b89xJ+iLeeJnhHS270Dii/opyIFePzX7Yk1s3oJeE5HhcGVl0x63Vg16/RKB6csfjDgEDz8=',
    '_cfuvid': 'lnacPODcBWjzEfRNAyQC32cTVtUxTik7dPHgd8MbA8k-1697511732526-0-604800000',
}

headers = {
    'authority': 'www.kyndryl.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'mm_v8=80; mm_v8=20; affinity="cee875c3597c01a3"; country_code=in; lang=en; notice_behavior=implied|eu; _mkto_trk=id:483-DRZ-814&token:_mch-kyndryl.com-1697507521704-49658; _gcl_au=1.1.378605285.1697507522; AMCVS_CB2D53C960AC271C0A495E19%40AdobeOrg=1; at_check=true; _rdt_uuid=1697507522005.24648623-ff80-4655-b2ce-290e1ccd2b2f; __pdst=e3557c3d7d444ff681bca79646b71c81; s_ecid=MCMID%7C32660101027481237212805852114510755205; s_cc=true; AMCV_CB2D53C960AC271C0A495E19%40AdobeOrg=-1124106680%7CMCIDTS%7C19648%7CMCMID%7C32660101027481237212805852114510755205%7CMCAAMLH-1698112321%7C11%7CMCAAMB-1698112321%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1697514722s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; mdLogger=false; kampyle_userid=90c5-f306-05dc-9d9e-6e90-6d72-ffa8-724b; kampyleUserSession=1697507522879; kampyleUserSessionsCount=1; _uetsid=c3faaa806c8f11eeac87b5f385a5d658; _uetvid=c3fad7406c8f11ee9760ed602e8b7705; mbox=session#8a021e1b8cde4606849b801d0c1d1de7#1697509430|PC#8a021e1b8cde4606849b801d0c1d1de7.32_0#1760752370; _hjSessionUser_2730899=eyJpZCI6IjA2MzdkMThjLWY3MWUtNTAxOC04Mjc1LTJhMWI1YjYwMGU3NiIsImNyZWF0ZWQiOjE2OTc1MDc1MjI3MDUsImV4aXN0aW5nIjp0cnVlfQ==; utag_main=v_id:018b3b5532e7002211bb77d2786e0506f002e06700bd0$_sn:1$_se:10$_ss:0$_st:1697509391209$ses_id:1697507521256%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:kyndryl.com$dc_visit:1$dc_event:10%3Bexp-session$dc_region:ap-east-1%3Bexp-session$_aa:32660101027481237212805852114510755205%3B%20s_cc%3Dtrue%3B%20AMCV_CB2D53C960AC271C0A495E19%40AdobeOrg%3D-1124106680; kampyleSessionPageCounter=8; __cf_bm=U.7955s9_XKPMoybMz67P3L3KZzvJZ81b7.qDVL7li8-1697511732-0-AW0YeAGafXc51mI3b89xJ+iLeeJnhHS270Dii/opyIFePzX7Yk1s3oJeE5HhcGVl0x63Vg16/RKB6csfjDgEDz8=; _cfuvid=lnacPODcBWjzEfRNAyQC32cTVtUxTik7dPHgd8MbA8k-1697511732526-0-604800000',
    'if-modified-since': 'Tue, 17 Oct 2023 01:52:27 GMT',
    'referer': 'https://www.kyndryl.com/in/en/customer-stories',
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

response1 = requests.get('https://www.kyndryl.com/in/en/customer-stories', cookies=cookies, headers=headers)
res1  = Selector(text=response1.text)
aaa = res1.xpath("//a[@class='cmp-solution-card__action-link']/@href").getall()

for a in aaa:
    url = 'https://www.kyndryl.com' +a
    # url = 'https://www.kyndryl.com/in/en/customer-stories/bank-of-ayudhya-public-company-ltd'
    while True:
        time.sleep(2)
        try:
            response = requests.get(url, cookies=cookies, headers=headers)
            if response.status_code ==200:
                break
            else:
                print(response.status_code)
        except:
            print("程序报错")

    res = Selector(text=response.text)
    title = ''.join(res.xpath("//h1[@class='cmp-page-hero__title']//text()").getall()).strip()
    content1 = res.xpath("//div[@class='article aem-GridColumn aem-GridColumn--default--12']//text()").getall()
    content1 = [i.strip() for i in content1 if i.strip()]
    content1 = '\n'.join(content1)

    content2 = res.xpath("//div[@class='text aem-GridColumn aem-GridColumn--default--12']//text()").getall()
    if not content2:
        content2 = res.xpath("//div[@class='container responsivegrid aem-GridColumn aem-GridColumn--default--12']//text()").getall()
    content2 = [i.strip() for i in content2 if i.strip()]
    content2 = '\n'.join(content2)

    content3 = res.xpath("//div[@class='cmp-content-band-container__bottom']//text()").getall()
    content3 = [i.strip() for i in content3 if i.strip()]
    content3 = '\n'.join(content3)

    content_all = title + '\n'+ content1 + '\n'+ content2 +'\n'+ content3
    txt_title = title.replace(' ','_')
    with open(f'./data_txt/{num}_kyndryl.txt', mode='w',encoding='utf-8') as f:
        f.write(content_all)

    num +=1
    print(f'采集{num}条成功')


