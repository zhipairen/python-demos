# -*- coding:utf-8 -*-
from collections import Iterable
from collections import Iterator
list = range(100)
print('list 10', list[:10])
print('list -10',list[-10:])
print('list 10:2',list[:10:2])
print(isinstance('abc', Iterable))
print('list and dict is not iterator:', isinstance([], Iterator), isinstance({}, Iterator))
print('generator is iterator:', isinstance((x for x in range(10)), Iterator))
print('iter set list dict str:', isinstance(iter([]), Iterator))
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
for i, value in enumerate(['A','B','C']):
    print(i, value)
for x, y in [(1, 2),(3, 6)]:
    print(x, y)
# 列表生成式
list1 = [x * x for x in range(1, 11) if x % 2 == 0]
print('list1:', list1)

list2 = [ m + n for m in 'abs' for n in 'fds']
print('list2:', list2)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
list3 = [k + '=' + v for k, v in d.items()]
print('list3:', list3)

# 生成器： 边循环边计算
g = (x * x for x in range(10))
for n in g:
    print('generator:', n)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# f = fib(6)
# while True:
#     try:
#         x = next(f)
#         print('fib:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
   
    