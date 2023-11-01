#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import csv
import time


def jd_crawl_comment(item_id, pagenum):
    list_ = []
    start_page = 0
    end_page = pagenum
    for p in range(start_page, end_page + 1):
        print(p)
        # productid = 100034710010
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10084545717055&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'
        url = url.format(p)
        print(url)
        # 仿造请求头，骗过浏览器
        headers = {
            'cookie': 'shshshfpa=af8ec6bc-c6d9-745f-cf2d-7e9f230f9ebb-1690252978; shshshfpx=af8ec6bc-c6d9-745f-cf2d-7e9f230f9ebb-1690252978; __jdu=16903525330592021116275; pinId=y5mzaVmQqBCcpnNLAZ-FXrV9-x-f3wj7; pin=jd_50c266c981af8; unick=jd_139110yiq; _tp=1sO%2FQrO9UHCbvniUoOC6wwG2i7b7x24Hw48sqrmCkyg%3D; _pst=jd_50c266c981af8; b_dw=1210; b_dh=609; b_dpr=1.5; b_webp=1; b_avif=0; autoOpenApp_downCloseDate_auto=1694683681749_1800000; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1694683697407_1; areaId=1; TrackID=1M_--_qcTw3oqWwXXp36sWoM3RfZa75-MN0kkJHd2c1qzMk87FGs6EjFpGYRwCPAx6al8_ZDLdG45W_bJtbzAWZrBWMAuGatJcduB0Gb4j55GqMd8V-Rf4J6TqbfFUq40; thor=90EFD0BDA212BAB390B9CD15B49F09FEC441955B7D886D0957770AD05DAC6A9E6EB41C5CBB3288F8F6D8F0DE66838368CEA5E3715C2D0A0B2059E6A7075DD7D8F7FE41BD67BAA0F03EA0EE8021432D255DBE6AC6054825C550413C7D273DA046C74F03B6FE678262DB628687EEE87D11C1D6C500C5C2998FC5FAD84E7EEA9CECC84575848F6284A32920E794C24C8B3599923C4BA295F8275956CCBC9E875A59; flash=2_WBSugSg-ZniAjmYnmZTdgHHixCOAZGrFrG820KQJfDERYnEU4KABHhIMbtDxtGMOxw1X9k5z-rVU1cAsBRUbRMa9k9cpqqFp9kqQ11IeS7s*; user-key=b8cb8a2f-2fa4-48c2-9ac4-f1943ef0690d; ipLoc-djd=1-2802-54745-0; PCSYCityID=CN_110000_110100_0; unpl=JF8EAKlnNSttWUhRUhsAE0AUG1UEW19cQ0dQa2QEV1RYGVADGAJPFRZ7XlVdXxRLFh9vYRRVVFNPXQ4ZASsVEUtcVVZtC0oVAmlgA1JYXntkNRgCKxMgS1pcX18MSBMBbWYBXF5ZSFQFGwUYFBR7XGReVQ97JzNqZwRUXF9KVAcdMhoiEktcVVxcDE8TAl8sa1UQWExcBBkGGBYSSVxQVl4JSBcDb2AGUlloSmQG; __jdv=76161171|ntp.msn.cn|t_2030767747_|jingfen|024f139c5a9a43e9ab520281c5721e67|1697504313055; 3AB9D23F7A4B3CSS=jdd03O4JXPSFFTWUV46JJRJFPNVZR2L5O3QBS4GN5DA2NMYPYAOMUFXV2E35WWFSX2MMSJVHMDO2GMDZMUUHGPHRL3Q4EAMAAAAMLHMSEDYIAAAAACTH62IVVMN2IS4X; _gia_d=1; jsavif=0; __jda=122270672.16903525330592021116275.1690352533.1697443179.1697504313.58; __jdc=122270672; 3AB9D23F7A4B3C9B=O4JXPSFFTWUV46JJRJFPNVZR2L5O3QBS4GN5DA2NMYPYAOMUFXV2E35WWFSX2MMSJVHMDO2GMDZMUUHGPHRL3Q4EAM; token=4104aa0dae1b52ab2df72c1c42a8d4e2,3,943057; __tk=9f91c1a0d1a6d4d2b8ec94218d57b35c,3,943057; shshshsID=3a90a967908f0d52e69623b30551e8a5_3_1697504330526; __jdb=122270672.3.16903525330592021116275|58.1697504313; shshshfpb=AAoaDJDuLEo7GvMbZdF_PLX6fIw-euxaQJSl4fwAAAAA',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
            'Referer': 'https://item.jd.com/'
        }
        # 发起请求
        # request = urllib.request.Request(url=url, headers=headers)
        # 得到响应
        content = requests.get(url=url, headers=headers).content.decode('utf-8')
        # 去掉多余得到json格式
        content = content.strip('fetchJSON_comment98vv995();')
        print(content)
        obj = json.loads(content)

        comments = obj['comments']
        print(comments)
        productCommentSummary = obj['productCommentSummary']
        print(productCommentSummary)
        fp = open('Mate 60-1.txt', 'a', encoding='gbk')
        for comment in comments:
            # print(comment)

            product_color = comment['productColor']

            product_size = comment['productSize']

            comment_id = comment['id']

            content = comment['content']

            if_plus_vip = comment['plusAvailable']

            post_time = comment['creationTime']

            reply_count = comment['replyCount']

            score = comment['score']

            user_name = comment['nickname']

            product_id = productCommentSummary['skuId']

            goodrate = productCommentSummary['goodRate']

            sku_id = comment['referenceId']

            item = {
                'product_color': product_color,
                'product_size': product_size,
                'comment_id': comment_id,
                'content': content,
                'if_plus_vip': if_plus_vip,
                'post_time': post_time,
                'reply_count': reply_count,
                'score': score,
                'user_name': user_name,
                'product_id': product_id,
                'goodrate': goodrate,
                'sku_id': sku_id,
            }
            string = str(item)

            print(product_color, product_size, comment_id, content, if_plus_vip, post_time, reply_count, score,
                  user_name, product_id, sku_id)
            list_.append(
                ['华为', 'Mate 60', product_color, product_size, product_id, content, post_time, 5999, '', user_name,
                 'jd', comment_id, reply_count, score, if_plus_vip, goodrate, sku_id])
            fp.write(string + '\n')

        fp.close()
        print('%s-page---finish' % p)
        # print(list_)
        time.sleep(5)
    return list_


def write_to_csv(list_, header, outputfile):
    with open(outputfile, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for l in list_:
            writer.writerow(l)
    f.close()


if __name__ == "__main__":
    list_ = jd_crawl_comment(100009464799, pagenum=99)
    outputfile = 'Mate 60-1.csv'
    header = ['brand', 'category', 'product_color', 'product_size', 'product_id', 'content', 'post_time',
              'product_price', 'product_label', 'user_name', 'platform', 'comment_id', 'reply_count', 'score',
              'if_plus_vip', 'goodrate', 'sku_id']
    write_to_csv(list_, header, outputfile)

# In[ ]:




