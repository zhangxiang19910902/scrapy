# -*- coding:utf-8 -*-
import time
import pandas as pd
from scrapy import Selector
import undetected_chromedriver as uc


def start_requests():
    aaa = pd.read_excel(r"./aaa.xls", header=0)
    url_list = []
    for i in aaa.itertuples():
        url_list.append(i[1])
    return url_list

def selenium(key_list):
    num = 0
    url = 'https://www.baidu.com/s?wd=%E5%8A%9E%E7%90%86%E6%88%BF%E5%B1%8B%E6%8A%B5%E6%8A%BC'
    driver = uc.Chrome(driver_executable_path=r"D:\chromedriver\chromedriver.exe")
    driver.get(url)
    # time.sleep(10)
    driver.implicitly_wait(20)
    time.sleep(5)
    list2  = []
    for i in key_list:
        driver.get(f'https://www.baidu.com/s?wd={i}')
        driver.implicitly_wait(20)
        time.sleep(1.5)
        content = driver.page_source
        response = Selector(text=content)
        contetn_list = '\n'.join(response.xpath("//div[@class='_3te7bpt f13 c-gap-top-xsmall']//text()").getall())
        if not contetn_list:
            print("弹出验证---等待10秒手动解除验证")
            time.sleep(10)
        list2.append([i, contetn_list])
        num += 1
        shijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(f"获取{num}条数据成功-----{shijian}")
    return list2

def to_execel(list2):
    shijian = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    df = pd.DataFrame(list2,columns=['url', 'company'])
    df.to_excel(f".//baidu_{shijian}.xlsx", index=False)

if __name__ == '__main__':
    key_list = start_requests()
    list2 = selenium(key_list)
    to_execel(list2)
