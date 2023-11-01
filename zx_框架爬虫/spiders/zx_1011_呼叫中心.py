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
'''
未完成
'''

def selenium():
    num = 0
    url = 'http://116.62.32.158/'
    driver = uc.Chrome(driver_executable_path=r"D:\chromedriver\chromedriver.exe")
    driver.get(url)
    # time.sleep(10)
    driver.implicitly_wait(20)
    name = driver.find_element(by=By.XPATH,value="//*[@id='customerName']")
    name.clear()
    name.send_keys('小游神群呼')
    driver.implicitly_wait(20)
    admin = driver.find_element(by=By.XPATH,value="//*[@id='userName']")
    admin.clear()
    admin.send_keys('admin')
    driver.implicitly_wait(20)
    password = driver.find_element(by=By.XPATH,value="//*[@id='password']")
    password.clear()
    password.send_keys('yidanke@xiaoyoushen')
    driver.implicitly_wait(20)
    driver.find_element(by=By.XPATH, value="//span[contains(text(),'登 录')]").click()
    driver.implicitly_wait(20)
    print('登录成功')
    # time.sleep(5)
    # try:
    #     driver.find_element(by=By.XPATH, value="//span[contains(text(),'知道了')]").click()
    #     time.sleep(2)
    # except:
    #     pass
    # driver.find_element(by=By.XPATH, value="//span[contains(text(),'外呼任务')]").click()

    cookies = driver.get_cookies()

    s = requests.session()
    c = requests.cookies.RequestsCookieJar()
    for item in cookies:
        c.set(item["name"], item["value"])

    s.cookies.update(c)

    params = {
        'm': 'service',
        'c': 'calleeList',
        'f': 'uploadFile',
    }
    file_path = r'C:\Users\Administrator\Desktop\2020.txt'
    with open(file_path, 'rb') as f:
        files = {'file': f}
        headers = {'content-type': 'multipart/form-data'}
        response = s.request('POST', 'http://116.62.32.158/service/index.php',
                                    files=files,
                                    headers=headers,
                                    params = params,
                                     verify=False, )

    params = {
        'm': 'service',
        'c': 'callTask',
        'f': 'edit',
    }

    data = {
        'name': 'ceshi',
        'calleeList': '12652',
        'callType': '2',
        'CIDGroup': '410',
        'weekday1': '["1","2","3","4","5","6","0"]',
        'startTime1': '08:00:00',
        'endTime1': '18:00:00',
        'weekday2': '',
        'startTime2': '',
        'endTime2': '',
        'weekday3': '',
        'startTime3': '',
        'endTime3': '',
        'remark': '',
        'concurrenceMode': '0',
        'agentGroup': '447',
        'maxConcurrence': '0',
        'multiplier': '3',
        'id': '-1',
        'file': '',
    }
    response1 = s.post(
        'http://116.62.32.158/service/index.php',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    time.sleep(100)


if __name__ == '__main__':
    selenium()
