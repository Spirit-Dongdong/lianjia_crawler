# -*- coding: UTF-8 -*-

import requests
import time
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

# url = 'https://bj.lianjia.com/ershoufang/pg9l2p3'
# r = requests.get(url)
#
# print(r.text)

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "zh-CN,zh;q=0.8",
}

proxies = {"http": "http://112.20.127.211:9999"}

def get_list():
    for i in range(1, 29):
        url = "https://bj.lianjia.com/ershoufang/pg%dl2p3" % i
        r = requests.get(url, headers = headers)
        r.encoding = r.apparent_encoding
        output = open('../list/p%d.html' % i, mode='w')
        output.write(r.text)
        output.close()
        time.sleep(3)
        print(i)

def test():
    url = "http://ip.chinaz.com/"
    r = requests.get(url, headers = headers, proxies = proxies)
    print(r.text)

    #
    # area_list = ['shunyi', 'changping', 'daxing', 'chaoyang', 'haidian']
    # for area in area_list:
    #     pass

if __name__ == '__main__':
    test()