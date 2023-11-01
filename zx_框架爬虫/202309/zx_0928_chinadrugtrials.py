# -*- coding:utf-8 -*-
import jsonpath
from pymongo import MongoClient
import json
import time
from scrapy import Selector
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
def deal_headers(response):
    html = jsonpath.jsonpath(json.loads(response.text), '$..response')[0]
    if not html:
        html = ''
    response2 = Selector(text=html) if html else None
    return response2


'''
linsan3666@gmail.com
Aa112211
'''

def selenium():
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client.name.ddd_1019
    num = 0
    # url = 'http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml'
    url = 'http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml'
    driver = uc.Chrome(driver_executable_path=r"D:\chromedriver\chromedriver.exe")
    driver.get(url)
    # time.sleep(10)
    driver.implicitly_wait(20)
    time.sleep(20)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    # driver.find_element(by=By.XPATH, value="//*[@class='cta-button cta-button--icon-pos-left cta-button--small cta-button--small-on-mobile cta-button--primary']").click()

    # driver.find_element(by=By.XPATH, value="//div[contains(text(),'Load More')]").click()
    # driver.implicitly_wait(10)
    # time.sleep(10)

    # target = driver.find_element_by_id("id_keypair")
    # driver.execute_script("arguments[0].scrollIntoView();", target)
    content = driver.page_source
    response = Selector(text=content)
    db_dict1 = {}
    db_dict1['number'] = ' '.join(response.xpath("//div[@id='toolbar_top']/div//text()").getall()).strip()
    db_dict1['登记号'] = ' '.join(response.xpath("//div[@id='collapseOne']//th[contains(text(),'登记号')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['申请人名称'] = ' '.join(response.xpath("//div[@id='collapseOne']//th[contains(text(),'申请人名称')]/following-sibling::td//text()").getall()).strip()
    db_dict1['联系人姓名'] = ' '.join(response.xpath("//div[@id='collapseTwo']//th[contains(text(),'联系人姓名')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['联系人Email'] = ' '.join(response.xpath("//div[@id='collapseTwo']//th[contains(text(),'联系人Email')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['联系人座机'] = ' '.join(response.xpath("//div[@id='collapseTwo']//th[contains(text(),'联系人座机')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['联系人手机号'] = ' '.join(response.xpath("//div[@id='collapseTwo']//th[contains(text(),'联系人手机号')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['主要研究者信息'] = ' '.join(response.xpath("//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'姓名')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['电话'] = ' '.join(response.xpath("//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'电话')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['Email'] = ' '.join(response.xpath("//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'Email')]/following-sibling::td[1]//text()").getall()).strip()
    db_dict1['单位名称'] = ' '.join(response.xpath("//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'单位名称')]/following-sibling::td[1]//text()").getall()).strip()
    num += 1
    db2.insert_one(db_dict1)
    print(f"获取{num}条链接成功----")

    while True:
        try:
            driver.find_element(by=By.XPATH, value="//div[@id='toolbar_bottom']//a[contains(text(),'下一个试验')]").click()
            driver.implicitly_wait(10)
            time.sleep(0.5)
            content = driver.page_source
            response = Selector(text=content)
            db_dict1 = {}
            db_dict1['申请人名称'] = ' '.join(response.xpath(
                "//div[@id='collapseOne']//th[contains(text(),'申请人名称')]/following-sibling::td//text()").getall()).strip()
            db_dict1['联系人姓名'] = ' '.join(response.xpath(
                "//div[@id='collapseTwo']//th[contains(text(),'联系人姓名')]/following-sibling::td[1]//text()").getall()).strip()
            db_dict1['联系人Email'] = ' '.join(response.xpath(
                "//div[@id='collapseTwo']//th[contains(text(),'联系人Email')]/following-sibling::td[1]//text()").getall()).strip()
            db_dict1['联系人座机'] = ' '.join(response.xpath(
                "//div[@id='collapseTwo']//th[contains(text(),'联系人座机')]/following-sibling::td[1]//text()").getall()).strip()
            db_dict1['联系人手机号'] = ' '.join(response.xpath(
                "//div[@id='collapseTwo']//th[contains(text(),'联系人手机号')]/following-sibling::td[1]//text()").getall()).strip()
            db_dict1['主要研究者信息'] = ' '.join(response.xpath(
                "//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'姓名')]/following-sibling::td[1]//text()").getall()).strip()
            db_dict1['电话'] = ' '.join(response.xpath(
                "//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'电话')]/following-sibling::td[1]//text()").getall()).strip()
            db_dict1['Email'] = ' '.join(response.xpath(
                "//*[@class='searchDetailTable marginBtm10']//th[contains(text(),'Email')]/following-sibling::td[1]//text()").getall()).strip()
            num += 1
            db2.insert_one(db_dict1)
            print(f"获取{num}条链接成功----")
        except:
            print("失败")
if __name__ == '__main__':
    selenium()
