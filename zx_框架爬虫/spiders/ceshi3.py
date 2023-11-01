# -*- coding:utf-8 -*-
import jsonpath
from pymongo import MongoClient
import json
import time
from scrapy import Selector
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import requests
from selenium.webdriver.common.alert import Alert
import pandas as pd

def selenium(code_list):
    num = 0
    url = 'https://www.manomano.fr/recherche/8719883668338'
    driver = uc.Chrome(driver_executable_path=r"D:\chromedriver\chromedriver.exe")
    driver.get(url)
    # time.sleep(10)
    for a in code_list:
        join_url = 'https://www.manomano.fr/recherche/' + str(a[1])
        driver.get(join_url)
        driver.implicitly_wait(20)
        try:
            driver.find_element(by=By.XPATH, value="//div[@class='tG5dru JqwSfJ c5PGVKq']/a[1]").click()
        except:
            pass
        driver.implicitly_wait(20)
        time.sleep(2)
        print('登录成功')

def r_excel():
    num  = 0
    aaa = pd.read_excel(r"./data_exl/购物车.xlsx", header=0)
    url_list = []
    for i in aaa.itertuples():
        url_list.append([i[2],i[3]])
    return url_list

if __name__ == '__main__':
    code_list = r_excel()
    selenium(code_list)
