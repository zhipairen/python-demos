list = ['one', 'two', 'three', [1, '2']]
len = len(list)
list.append('four')
list.insert(1, 'five')
list[3] = 'set'
print('list2:', list[4][1])
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
# dict
d = {'name': 'terry', 'age': 20, 'sex': 1}
print('name:', d['name'])
print('excent:', 'power' in d)
print(d.get('age'))
print(d.get('age', 22))
d.pop('sex')
d['age'] = 23
print('now d:', d)
s = set([1, 3, 4, 1, 2, 3, 5, 4])
s.add(7)
print('set:', s)
s2 = set([2, 6, 4, 5, 2])
s2.remove(4)
print('s & s2:', s & s2)
print('s | s2:', s | s2)
# 不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回