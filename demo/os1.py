# -*- coding: utf-8 -*-
import os
import pickle
import json

# 当前目录绝对路径
path = os.path.abspath('.')
# 拼接路径: os.path.join('p1','p2')
# 拆分路径： os.path.split('path')
def files():
    dirs = [x for x in os.listdir('.') if os.path.isdir(x)] # 当前目录下的所有目录
    pys = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
    print('dirs:', dirs)
    print('py files:', pys)
files()

# pickling: 把变量从内存中变成可存储或传输的过程称之为序列化
# unpickling: 把变量内容从序列化的对象重新读到内存里称之为反序列化
d = dict(name='Bob', age=20, score=90)
byt = pickle.dumps(d)
print('pickling bytes:', byt)
unbyt = pickle.loads(byt)
print('unpick:', unbyt)
jsons =json.dumps(d)
print('json:', jsons)
unjson = json.loads(jsons)
print('load json:', unjson)
