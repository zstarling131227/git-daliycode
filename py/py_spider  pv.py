# !/usr/bin/python
import requests
from lxml import etree

url = "https://short.muqiacard.com/api/v1/short/link/mqfjg7?type=tendency&scope=30day&startDay=&endDay="
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
html = requests.get(url=url, headers=headers).text
dic1 = {
    "ip": 134577,
    "pv": 188835,
    "uv": 153324,
    "trend": {
        "today": {
            "pv": [3119, 2683, 2114, 2028, 2024, 2079, 1028, 3119, 2683, 2114, 2028, 2024, 2079, 1028],
            "uv": [2548, 2140, 1684, 1630, 1632, 1687, 818, 2548, 2140, 1684, 1630, 1632, 1687, 818],
            "ip": [],
            "time": ["2020-02-21", "2020-02-22", "2020-02-23", "2020-02-24", "2020-02-25", "2020-02-26", "2020-02-27"]
        }
    },
    "success": "true",
    "status": 200
}
print (dic1["trend"]["today"]["pv"])
from urllib import request, parse
import time

"""
首页：https://tieba.baidu.com/f?kw=华晨宇吧&pn=0
第二页：https://tieba.baidu.com/f?kw=华晨宇吧&pn=50
第三页：https://tieba.baidu.com/f?kw=华晨宇吧&pn=100
"""


class BaiduSpider(object):
    def __init__(self):
        # self.headers = {
        #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        # }
        self.headers = {
            'User-Agent': 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        }
        self.baseurl = 'https://tieba.baidu.com/f?{}'

    def get_page(self, url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def parse_page(self):
        pass

    def write_page(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    def main(self):
        name = input("输入贴吧名：")
        start = int(input("起始页："))
        end = int(input("终止页："))
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            query_string = {
                "kw": name,
                'pn': str(pn)
            }
            query_string = parse.urlencode(query_string)
            url = self.baseurl.format(query_string)
            html = self.get_page(url)
            filename = '{}-第{}页.html'.format(name, page)
            self.write_page(filename, html)
            print('第%d页爬取成功' % page)
            time.sleep(1)


if __name__ == "__main__":
    spider = BaiduSpider()
    spider.main()
