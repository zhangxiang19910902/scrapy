# import re
# import time
#
# import requests
# from pymongo import MongoClient
# from scrapy import Selector
#
# def get_year(datas):
#     years = re.findall('[12]\d{3}', datas)
#     if years:
#         year = int(years[0])
#     return year
#
# client = MongoClient('mongodb://localhost:27017/')
# db2 = client.name.zx_1009_pubmed
#
# cookies = {
#     'pm-csrf': '6bSC4VEXHxYhVFeNhocxn6kenof5FsItlJoggZkPVuYEdMJvCeFizg91ZveIF8AP',
#     'ncbi_sid': 'C89F22D3513D1613_1997SID',
#     'pm-sessionid': '66nyqvompnmefnjvuacakmdf48bu6wgo',
#     '_gid': 'GA1.2.1890171152.1696835413',
#     'pm-sid': 'Xgsxt25Kovuaje8ZTEKRDQ:a4342a0ab619c1c41a99625c7d653732',
#     'pm-adjnav-sid': 'fm3Xub0vmbdo76QfJ7FpwA:a4342a0ab619c1c41a99625c7d653732',
#     '_ga': 'GA1.1.72034425.1695798369',
#     'pm-iosp': '',
#     '_ga_DP2X732JSX': 'GS1.1.1696837922.3.0.1696837922.0.0.0',
#     '_gat_ncbiSg': '1',
#     'pm-sfs': '',
#     'ncbi_pinger': 'N4IgDgTgpgbg+mAFgSwCYgFwgMwEEDsAYgAykCMATABxWFXb4Cspp2VALGYdYWQKIVcAOjJCAtnHYgANCACuAOwA2AewCGqBVAAeAF0ygKmcHIBGYqOlnZjYMxasgpWAM5Q1EAMaJoLuUv1ZRmMZEDIyYwjZCmJjPCIWSho6BmYWNk5uWn5BEXFJUIoIrDtzSwxShww3D29ff10MADkAeSa+QqMS+0shBU9TZD6lMT7kRCEAcxUYQoBOSLmY0OxYrDJiKljrYrCl7ZwusOJ2A+wbLAAzNSU3FecQXQg5KBWqEOsFrAp2JfwyfChU7GH5zTjYKSydgXEDEITYObwoEPRSqDRaPRA4LrUKMGFzABsCyCDzm2CiIEYBOMB0YgKwBwJuy2NlkBOprncXkQIAAvrygA==',
# }
#
# headers = {
#     'authority': 'pubmed.ncbi.nlm.nih.gov',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     # 'cookie': 'pm-csrf=6bSC4VEXHxYhVFeNhocxn6kenof5FsItlJoggZkPVuYEdMJvCeFizg91ZveIF8AP; ncbi_sid=C89F22D3513D1613_1997SID; pm-sessionid=66nyqvompnmefnjvuacakmdf48bu6wgo; _gid=GA1.2.1890171152.1696835413; pm-sid=Xgsxt25Kovuaje8ZTEKRDQ:a4342a0ab619c1c41a99625c7d653732; pm-adjnav-sid=fm3Xub0vmbdo76QfJ7FpwA:a4342a0ab619c1c41a99625c7d653732; _ga=GA1.1.72034425.1695798369; pm-iosp=; _ga_DP2X732JSX=GS1.1.1696837922.3.0.1696837922.0.0.0; _gat_ncbiSg=1; pm-sfs=; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgMwEEDsAYgAykCMATABxWFXb4Cspp2VALGYdYWQKIVcAOjJCAtnHYgANCACuAOwA2AewCGqBVAAeAF0ygKmcHIBGYqOlnZjYMxasgpWAM5Q1EAMaJoLuUv1ZRmMZEDIyYwjZCmJjPCIWSho6BmYWNk5uWn5BEXFJUIoIrDtzSwxShww3D29ff10MADkAeSa+QqMS+0shBU9TZD6lMT7kRCEAcxUYQoBOSLmY0OxYrDJiKljrYrCl7ZwusOJ2A+wbLAAzNSU3FecQXQg5KBWqEOsFrAp2JfwyfChU7GH5zTjYKSydgXEDEITYObwoEPRSqDRaPRA4LrUKMGFzABsCyCDzm2CiIEYBOMB0YgKwBwJuy2NlkBOprncXkQIAAvrygA==',
#     'referer': 'https://pubmed.ncbi.nlm.nih.gov/?term=Tang+JT&cauthor_id=24137187',
#     'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
# }
#
#
#
# num = 0
#
# for a in range(1,16):
#     params = {
#         'term': 'Tang JT',
#         'cauthor_id': '24137187',
#         'page': a,
#     }
#     while True:
#         try:
#             response = requests.get('https://pubmed.ncbi.nlm.nih.gov/', params=params, cookies=cookies, headers=headers)
#             if response.status_code ==200:
#                 break
#             else:
#                 print(response.status_code)
#         except:
#             print("程序报错")
#     res = Selector(text=response.text)
#     urls = res.xpath("//a[@class='docsum-title']")
#     for b in urls:
#         db_dict = {}
#         db_dict['title'] = ''.join(b.xpath(".//text()").getall()).strip()
#         db_dict['auth'] = ''.join(b.xpath("./following-sibling::div[@class='docsum-citation full-citation']/span[@class='docsum-authors full-authors']//text()").getall()).strip()
#
#         infor = ''.join(b.xpath("./following-sibling::div[@class='docsum-citation full-citation']/span[@class='docsum-journal-citation full-journal-citation']//text()").getall()).strip()
#         db_dict['journals_name'] = infor.split('.',1)[0]
#         db_dict['year'] = get_year(infor)
#
#         db2.insert_one(db_dict)
#         num += 1
#         print(f'添加{num}条成功')
#
