# -*- coding: utf-8 -*-
from pymongo import MongoClient
import re
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db2 = client.name.zx_0921_qccsj
def r_excel():
    num  = 0

    aaa = pd.read_excel(r"C:\Users\Administrator\Desktop\aaa.xlsx", header=0)
    url_list = []
    for i in aaa.itertuples():
        url_list.append(i[1])
        url_list.append(i[2])

    for a in url_list:
        a = str(a)
        ccc = re.findall(r"1\d{10}",a)
        if ccc:
            for b in ccc:
                db_dict = {}
                db_dict['phone'] = b
                db2.insert_one(db_dict)
                num += 1
                print(f'添加{num}条成功')
if __name__ == '__main__':
    r_excel()