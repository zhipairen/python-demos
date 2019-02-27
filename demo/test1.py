# -*- coding: utf-8 -*-
# ASCII(一个字节) ===> unicode(2个字节) ===> UTF-8(可变长编码)
a = 123 #a是整数
print(a)
a = 'ABC' #a变为字符串
b = a
a = 'xyz'
print('a:', a)
print('b:', b)
print('10/3:', 10 / 3)
print('10//3:', 10 // 3)
print('10%3:', 10 % 3)
print('code:', ord('A'))