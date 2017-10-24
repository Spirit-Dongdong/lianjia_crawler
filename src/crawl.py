# -*- coding: UTF-8 -*-

import requests
import time
import os
from bs4 import BeautifulSoup
import sys
import random
reload(sys)

sys.setdefaultencoding('UTF8')

url_list = set()

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "zh-CN,zh;q=0.8",
}


def crawl_single(id):
    url = 'https://bj.lianjia.com/ershoufang/%s.html' % id
    r = requests.get(url, headers = headers)
    r.encoding = r.apparent_encoding
    output = open('../detail/%s.html' % id, mode='w')
    output.write(r.text)
    output.close()
    print(id)
    time.sleep(random.uniform(10, 25))

def get_list():
    for f in os.listdir('../list'):
        s = BeautifulSoup(open('../list/%s' % f), 'html.parser')
        # ll = s.find_all('ul', {'class':'sellListContent'})
        aa = s.find_all('a', {'data-housecode': True})
        for l in aa:
            url_list.add(l.attrs['data-housecode'])


if __name__ == '__main__':
    crawled_items = os.listdir('../detail')
    for l in open('../ids.txt'):
        id = l.strip()
        f = '%s.html' % id
        # print(f in crawled_items)
        if f not in crawled_items:
            crawl_single(id)


