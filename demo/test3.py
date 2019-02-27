# -*- coding: utf-8 -*-
import math
def _abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else: 
        return -x
print(_abs(-2))

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny # tuple类型
x, y = move(100, 100, 60, math.pi / 6)
print('x:', x, 'y:', y)

# 一元二次方程： ax^2 + bx + c = 0
def quadratic(a, b , c):
    t = pow(b, 2) - 4 * a * c
    s = math.sqrt(t)
    if t > 0:
        return (-b + s) / (2 * a), (-b - s) / (2 * a)
    elif t == 0:
        return (-b + s) / (2 * a)
    else:
        print('无解')
        return None
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print('%2d^%2d=%d' % (2,5, power(2, 5)))  
# 可变参数
def calc(*args):
    sum = 0 
    for a in args:
        sum = sum + a * a
    print('more args:', sum)
    return sum
calc(1,2,3)
nums = [1, 2, 3, 4]
calc(*nums)
# 关键字参数
def person(name, age, **rest):
    print('name:', name, 'age:', age, 'other:', rest)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('terry', 34, **extra)

# def p1(name, *, city, job, age):
#     print(name, city, job, age)

# p1('terry',city='shanghai',job='iT', age='23')

def _iter(num, pro):
    if num == 1:
        return pro
    return _iter(num - 1, num * pro)
print('尾递归', _iter(5, 1))