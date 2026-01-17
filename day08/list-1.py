#创建列表

items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]

print(type(items2))  # [35, 12, 99, 68, 55, 35, 87]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]



items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']

#列表的运算
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
#使用+运算符实现两个列表的拼接
items6 += items7

#使用*运算符实现列表的重复运算
print(items6 * 3)
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6)

#使用in或not in运算符判断一个元素在不在列表中
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False

# 列表获取 元素 []
items8 = [35, 12, 99, 45, 66]
print(items8[0])
#长度
print(len(items8))

# 列表切片
#切片运算是形如[start:end:stride]的运算符，其中start代表访问列表元素的起始位置，end代表访问列表元素的终止位置（终止位置的元素无法访问），而stride则代表了跨度
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0:3])

#元素的遍历
languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])

languages = ['Python', 'Java', 'C++', 'Kotlin']
for a in languages:
    print(a)


counters = [0] * 6
import random

for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

