# -*- coding:utf-8 -*
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
import os, argparse
# 任意二进制到文本字符串的编码方法,常用于在URL、Cookie、网页中传输少量二进制数据
# Base64编码会把3字节的二进制数据编码为4字节的文本数据  3*8= 4*6
import base64 

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('namedtuple: x is %s y is %s' % (p.x, p.y))
# list是线性存储，大数据下，插入和删除效率低(重新移动位置)
# deque 高效实现插入和删除的双向列表
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.pop()
print('deque: %s' % q)
# 默认值dict
dd = defaultdict(lambda: 'N/A')
# dict key按顺序输出
l = [('a', 1), ('b', 2), ('c', 3)]
d = dict(l)
od = OrderedDict(l)
print('dict: %s, order dict: %s' % (d, od))
# ChainMap: 按照顺序在内部的dict依次查找
defaults = {
    'color': 'red',
    'user': 'guest'
}
# 构造命令行参数
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parser_args()
# command_line_args = { k: v for k, v in vars(namespace).items() if v }
# # 组合成ChainMap:
# combined = ChainMap(command_line_args, os.environ, defaults)

# # 打印参数:
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])
# 计数器
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print('counter: %s' % c)
