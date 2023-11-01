# -*- coding:utf-8 -*-
import re
import time
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.chrome.options import Options
import jsonpath
from pymongo import MongoClient
import requests
import json

import time
import pandas as pd
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


def selenium():
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_0921_gugexueshu_Customer
    num = 0
    url = 'https://scholar.google.com/scholar?start=10&q=Employee+Experience&hl=en&as_sdt=0,5'
    driver = uc.Chrome(driver_executable_path=r"D:\chromedriver\chromedriver.exe")
    driver.get(url)
    # time.sleep(10)
    driver.implicitly_wait(20)
    time.sleep(20)
    for i in range(100):
        page = i*10
        driver.get(f'https://scholar.google.com/scholar?start={page}&q=Customer+Experience&hl=en&as_sdt=0,5')
        driver.implicitly_wait(20)
        time.sleep(1.5)
        content = driver.page_source
        response = Selector(text=content)

        contetn_list = response.xpath("//div[@class='gs_r gs_or gs_scl']")
        for a in contetn_list:
            db_dict1 = {}
            title = ' '.join(a.xpath(".//h3//a//text()").getall()).strip()
            if not title:
                title = ' '.join(a.xpath(".//h3//text()").getall()).strip()
            db_dict1['标题'] = title
            db_dict1['信息'] = ' '.join(a.xpath(".//div[@class='gs_a']//text()").getall()).strip()
            db_dict1['摘要'] = ' '.join(a.xpath(".//div[@class='gs_rs']//text()").getall()).strip()
            num += 1
            db2.insert_one(db_dict1)
            print(f"获取{num}条链接成功----")
if __name__ == '__main__':
    selenium()
