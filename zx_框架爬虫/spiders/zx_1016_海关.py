# -*- coding:utf-8 -*-
import jsonpath
from pymongo import MongoClient
import json
import time
from scrapy import Selector
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import requests
from PIL import Image
import pytesseract
import  base64
'''
linsan3666@gmail.com
Aa112211
'''

num = 0
def content_text(response_content):
    global num
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.zx_1016_海关2
    for a in response_content:
        db_dict1 = {}
        db_dict1['number'] = ' '.join(a.xpath("./td[1]//text()").getall()).strip()
        db_dict1['id'] = ' '.join(a.xpath("./td[2]//text()").getall()).strip()
        if not db_dict1['id']:
            id = a.xpath("./td[2]//img/@src").get()
            id = id.replace('data:image/png;base64,' , '')
            img_data = base64.b64decode(id)
            img_name = f'{num}tupian_id'
            with open(f'./imgs/{img_name}.png', 'wb') as fp:
                fp.write(img_data)
                print(f'{img_name}下载成功')
                time.sleep(1.5)
            img = Image.open(f'./imgs/{img_name}.png')
            text = pytesseract.image_to_string(img)
            db_dict1['id'] = text
        db_dict1['企业名称'] = ' '.join(a.xpath("./td[3]//text()").getall()).strip()
        if not db_dict1['企业名称']:
            id = a.xpath("./td[3]//img/@src").get()
            id = id.replace('data:image/png;base64,', '')
            img_data = base64.b64decode(id)
            img_name = f'{num}tupian_name'
            with open(f'./imgs/{img_name}.png','wb') as fp:
                fp.write(img_data)
                print(f'下载成功')
                time.sleep(1.5)
            img = Image.open(f'./imgs/{img_name}.png')
            text = pytesseract.image_to_string(img,lang='chi_sim')
            db_dict1['企业名称'] = text
        db_dict1['信用等级'] = ' '.join(a.xpath("./td[4]//text()").getall()).strip()
        db_dict1['所在地海关'] = ' '.join(a.xpath("./td[5]//text()").getall()).strip()
        if not db_dict1['所在地海关']:
            id = a.xpath("./td[5]//img/@src").get()
            id = id.replace('data:image/png;base64,', '')
            img_data = base64.b64decode(id)
            img_name = f'{num}tupian_xinyong'
            with open(f'./imgs/{img_name}.png', 'wb') as fp:
                fp.write(img_data)
                print(f'{img_name}下载成功')
                time.sleep(1.5)
            img = Image.open(f'./imgs/{img_name}.png')
            text = pytesseract.image_to_string(img,lang='chi_sim')
            db_dict1['所在地海关'] = text
        db_dict1['时间'] = ' '.join(a.xpath("./td[6]//text()").getall()).strip()
        if not db_dict1['时间']:
            id = a.xpath("./td[6]//img/@src").get()
            id = id.replace('data:image/png;base64,', '')
            img_data = base64.b64decode(id)
            img_name = f'{num}tupian_time'
            with open(f'./imgs/{img_name}.png', 'wb') as fp:
                fp.write(img_data)
                print(f'{img_name}下载成功')
                time.sleep(1.5)
            img = Image.open(f'./imgs/{img_name}.png')
            text = pytesseract.image_to_string(img)
            db_dict1['时间'] = text
        num += 1
        db2.insert_one(db_dict1)
        print(f"获取{num}条链接成功----")
def selenium():
    url = 'http://credit.customs.gov.cn/ccppwebserver/pages/ccpp/html/directory.html'
    driver = uc.Chrome(driver_executable_path=r"D:\chromedriver\chromedriver.exe")
    driver.get(url)
    time.sleep(10)

    content = driver.page_source
    response = Selector(text=content)
    response_content = response.xpath("//*[@id='tableDate']//tr[@ondblclick]")
    content_text(response_content)

    while True:
        try:
            time.sleep(5)
            driver.find_element(by=By.XPATH, value="//a[@id='hasNextHref']").click()
            driver.implicitly_wait(10)
            time.sleep(2)
            content1 = driver.page_source
            response1 = Selector(text=content1)
            response1_content = response1.xpath("//*[@id='tableDate']//tr[@ondblclick]")
            content_text(response1_content)
        except:
            print("失败")
if __name__ == '__main__':
    selenium()
