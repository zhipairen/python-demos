# -*- coding: utf-8 -*-
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# 格式化
print('Name: %s. Age: %2d-%02d' % ('guo', 3, 1))
print('%.2f,%x' % (3.1415926, 0xff))
s1 = 72
s2 = 85
r = s1 / s2
print('r:', r)
print('s1/s2: %.2f%%' % (r))
s = u'Python中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
