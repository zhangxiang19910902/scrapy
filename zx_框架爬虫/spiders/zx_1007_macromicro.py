import json
import jsonpath
from pymongo import MongoClient



# 读打开文件
with open('macromicro.json', encoding='utf-8') as a:
    # 读取文件
    result = json.load(a)
    # 获取姓名

client = MongoClient('mongodb://localhost:27017/')
collection_aaa = client.name.zx_1031_231_美国实际GDPSA_同比

res = jsonpath.jsonpath(result,"$..series")
for a in res[0][1]:
    db_dict = {}
    db_dict['日期'] = a[0]
    db_dict['数值'] = a[1]
    collection_aaa.insert_one(db_dict)