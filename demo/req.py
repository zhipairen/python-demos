# -*- coding: utf-8 -*-
from __future__ import absolute_import

from bs4 import BeautifulSoup # 对html源码重新格式化
import requests
import chardet # 检查编码

if __name__ == "__main__":
    r = requests.get('https://www.douban.com/')
    print('douban：', r.text)
# # get
# rg = requests.get(url, header={},params={'cat': '11'})
# # post 默认application/x-www-form-urlencoded
# rp = requests.post(url,data={'email':'11@qq.com'})
# # json 
# rj = requests.post(url, json = {'key': 'value'})
# # file
# rf = requests.post(url, files ={'file': open('data.txt', 'rb')})
# # cookies
# rc = requests.get(url,cookies={'token':'111'})
# 对 bytes检测编码
    data = '离离原上草，一岁一枯荣'.encode('gbk')
    encoding = chardet.detect(data)
    print('chardet:', encoding)