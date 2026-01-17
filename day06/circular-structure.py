# 循环结构

import time

print('hello, world')
time.sleep(1)

"""
每隔1秒输出一次“hello, world”

Author: zhiLong
Version: 1.0

a = "30" 是一个字符串，包含两个字符：'3' 和 '0'
for i in a 循环会遍历字符串中的每个字符
因此循环会执行 2次（不是3次），分别对应字符 '3' 和 '0'

a = "30"
for i in a:
    print('hello, world')
    time.sleep(1)
    
    
    
range(30) 产生可迭代的数字序列
str(30) 将整数转换为可遍历的字符串
只有可迭代对象才能用于 for 循环

你遇到了 TypeError: 'int' object is not iterable 错误
import time

a1 = 30
for i in a1:
    print('hello, world')
    time.sleep(1)
"""

"""
从1到100的整数求和

Version: 1.0
Author: zhiLong
for-in循环

total = 0
for i in range(1, 101):
    total += i
print(total)
"""

"""
从1到100的整数求和

Version: 1.1
Author: zhiLong

while循环
"""
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# break和continue


total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

total = 0
for i in range(1, 101):
    if total == 1560:
        continue
    total += i
print(total)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()

"""
输入一个大于1的正整数判断它是不是素数

Version: 1.0
Author: zhiLong

num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
"""

"""
猜数字小游戏

Version: 1.0
Author: zhiLong
"""
import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print('猜对了.')
        break
print(f'你一共猜了{counter}次.')
