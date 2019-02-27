# -*- coding: utf-8 -*-
# StringIO在内存中读写str
from io import StringIO
# from io import BytesIO 操作二进制数据
# 模式： r, w, rw, a(追加)
BASIC_FILE = '/Users/terry/Desktop/2018/terry/python/'
with open('%sdemo/data.txt' % BASIC_FILE, 'r') as f:
    print('file:', f.read())
with open('%sdemo/data1.txt'% BASIC_FILE, 'w') as f:
    f.write('数据2 1111')
# StringIO
fI = StringIO(u'Hello!\nIO!\nGoodbye!')
def output():
    while True:
        s = fI.readline()
        if s == '':
            break
        print(s.strip())
output()