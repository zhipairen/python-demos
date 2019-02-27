# -*- coding: utf-8 -*-
import re

test = '010-1232'
# 正则匹配
def reg(str):
    res = r'^\d{3}\-\d{3,8}'
    if re.match(res, str):
        print( 'match ok')
    else:
        print('match failed')
reg(test)
# 分组（）
resg = r'^(\d+)(0*)$' # 默认采用贪婪匹配（尽可能多的匹配）
resg1 = r'^(\d+?)(0*)$' # 加？可以采用非贪婪匹配
groupT = re.match(resg, test).groups()
print('groups:', groupT)
# 1. 编译 2. 匹配字符串，可以预编译正则表达式
re_num = re.compile(r'^\d{3}\-\d{3,8}$')
reu = re_num.match(test).groups()
