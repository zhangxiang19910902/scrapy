# from pymongo import MongoClient
# import requests
#
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client['name']['motor1']
#
# headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#     }
#
# for a in db.find():
#     codes = a.get("name")
#     codes = codes.replace("/","_")
#     img_url = a.get("logo")
#     img_url = img_url.replace(' ','')
#     response = requests.get(img_url,stream=True, headers=headers)
#     # title = str(i[0]).replace(' ','_').replace(".",'')
#     with open(f'./logos1/{codes}.png', 'wb') as f:
#         f.write(response.content)
#     print(f"{codes}-----下载成功")