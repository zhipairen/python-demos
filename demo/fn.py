# -*-coding: utf-8 -*-
# 高阶函数：让函数的参数能够接收别的函数
# map(f, Iterable) => Iterator(惰性序列)
# list(Iterator) => Iterable
'a test fn'
from functools import reduce
import functools
def f1(x):
    return pow(x, 2)
m = map(f1, range(5))
l = list(m)
print('list:', l)
# reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print("'123'=> 123:", str2int('123'))

# 计算素数算法：1. 2为素数，自然数序列筛除2的倍数 2. 取第一个3为素数，筛除3的倍数 3. 取序列第一个5为素数，筛除5的倍数，不断筛除，得到所有素数
# 生成奇数无限序列函数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0 # 关键字lambda表示匿名函数
# 不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 序列第一个数
        yield n
        it = filter(_not_divisible(n), it) # 新序列
# 1000以内的素数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
if __name__ == '__main__':
    # main()
    pass
# sorted
str1 = ['bob', 'about', 'Zoo', 'Credit']
def _sort(list, fn, reverse=False):
    result = sorted(list, key=fn, reverse=reverse)
    print('sorted result:', result)
_sort(str1, str.lower)
# 函数作为返回值(闭包)： 内部的局部变量还被新函数引用
# Decorator装饰器: 返回函数的高阶函数 
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw): 
        print('call %s():' % func.__name__)
        return func(*args, **kw) # 用函数逻辑再装饰
    return wrapper
@decorator # @语法糖 相当于执行了 func = decorator(func)
def now():
    print('2018-10-31')
now()
# 偏函数：
# functools.partial函数：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int, base=2) # int2('100') ==> kw = {'base': 2} int('100', **kw)
max2 = functools.partial(max, 10) # max2(2) ==> args = (10,2) max(*args)



