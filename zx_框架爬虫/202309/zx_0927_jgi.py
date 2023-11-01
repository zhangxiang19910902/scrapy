import requests
from scrapy import  Selector
import urllib.request
def get_download(url):
    headers = {
        'authority': 'genome.jgi.doe.gov',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'sso_url=https%3A%2F%2Fsignon.jgi.doe.gov%2Fsignon; referring_url=https%3A%2F%2Fgenome.jgi.doe.gov%2Fportal%2Fext-api%2Fdownloads%2Fbulk%2F260245-7%2Fstatus%3Fhtml%3Dtrue; JSESSIONID=4E1983D1C5DD608F58E3CF51744B17F1; HA_LB_SERV=lb_s2; _ga=GA1.1.29798752.1695783989; _ga_XCXPZ4EQ28=GS1.1.1695783989.1.1.1695784443.0.0.0; jgi_session=%2Fapi%2Fsessions%2F3a2cf8484491289a9284077cf21268f0; _ga_YBLMHYR3C2=GS1.1.1695784444.1.1.1695784463.0.0.0',
        'referer': 'https://signon.jgi.doe.gov/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }


    response = requests.get(
        url,
        headers=headers,
    )

    res = Selector(text=response.text)

    dow_url = res.xpath("//*[contains(text(),'Download')]/@href").get()

    dow_join = 'https://genome.jgi.doe.gov' + dow_url
    return dow_join

def download_url(url,dow_path):
    headers1 = {
        'authority': 'genome.jgi.doe.gov',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'sso_url=https%3A%2F%2Fsignon.jgi.doe.gov%2Fsignon; referring_url=https%3A%2F%2Fgenome.jgi.doe.gov%2Fportal%2Fext-api%2Fdownloads%2Fbulk%2F260245-7%2Fstatus%3Fhtml%3Dtrue; JSESSIONID=4E1983D1C5DD608F58E3CF51744B17F1; HA_LB_SERV=lb_s2; _ga=GA1.1.29798752.1695783989; _ga_XCXPZ4EQ28=GS1.1.1695783989.1.1.1695784443.0.0.0; jgi_session=%2Fapi%2Fsessions%2F3a2cf8484491289a9284077cf21268f0; _ga_YBLMHYR3C2=GS1.1.1695784444.1.1.1695784463.0.0.0',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        # 'content-length':"24",
    }

    response = requests.get(
        url,
        headers=headers1,
        stream=True
    )
    with open(dow_path, 'wb') as f:
        f.write(response.content)

    print('\nDownload finished!')


    # total_size = int(response.headers['content-length'])
    # block_size = 1024
    # progress = 0
    #
    # with open(dow_path, 'wb') as file:
    #     for data in response.iter_content(block_size):
    #         progress += len(data)
    #         file.write(data)
    #         done = int(50 * progress / total_size)
    #         print('\r[{}{}] {:.2f}%'.format('=' * done, ' ' * (50 - done), 100 * progress / total_size), end='')
    #


if __name__ == '__main__':
    url = 'https://genome.jgi.doe.gov/portal/ext-api/downloads/bulk/260245-8/status?html=true'
    dow_path = '../spiders/download/444.zip'
    dow_url = get_download(url)
    download_url(dow_url,dow_path)