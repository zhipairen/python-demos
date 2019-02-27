#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module'

import sys

def test():
    args = sys.argv
    print('sys args:', args) 

if __name__ == '__main__': # 命令行把特殊变量置为main
    test()

# class 类： 私有变量以 __ 开头，外部不可访问,内部私有变量被自动改成类似 _Person__name
# 特殊变量：类似__var__, 可直接访问
class Person(object): # 继承 object
    name = 'Person' # 类属性
    __slots__ = ('__name', '__score', 'sex') # 限制该类实例能添加的属性
    def __init__(self, name, score): # self 不用传递
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Person('Terry', 23)
bart.print_score()

class Student(Person):
    # __slots__ = ('age','en') # 子类需要定义才能对子类实例起作用(+父类的属性限制)
    def run(self):
        print('I am Student...')
    def __len__(self):
        return 100
    @property # getter
    def birth(self):
        return self._birth
    @birth.setter # setter
    def birth(self, value):
        if value > 2000:
            self._birth = '00'
        else:
            self._birth = '90'
    @property
    def age(self):
        return 2018
    @age.setter
    def age(self, value):
        self._age = value

stu = Student('student', 18)
stu.print_score() # 继承Person类
# 多态： 子类方法覆盖父类方法
print('new data type:', isinstance(stu, Student))
# isinstance(obj,Type): 判断类型； dir(obj): 获得一个对象的所有属性和方法
print('all prop and method:', dir(stu)) 
print('len:', len(stu)) # len()函数内部调用对象的__len__
# getattr()、 setattr()、 hasattr()
print('hasattr:', hasattr(stu, 'run'))
print('setattr:', setattr(stu, 'age', 18))
print('getattr:', getattr(stu, 'age'))
stu.sex = 1
stu.birth = 2012
print('setter prop:', stu.birth)
# 多重继承 class A(P1, P2,...)
class MyT(Person, object):
    def __init__(self):
        pass
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
print('fib:', Fib()[5])
# callable(obj): 可以判断一个对象是否是“可调用”对象
# 枚举: Enum
# 元类： metaclass




