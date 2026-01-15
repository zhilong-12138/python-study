#运算符	描述
#[]、[:]	索引、切片
#**	幂
#~、+、-	按位取反、正号、负号
#*、/、%、//	乘、除、模、整除
#+、-	加、减
#>>、<<	右移、左移
#&	按位与
#^、`	`
#<=、<、>、>=	小于等于、小于、大于、大于等于
#==、!=	等于、不等于
#is、is not	身份运算符
#in、not in	成员运算符
#not、or、and	逻辑运算符
#=、+=、-=、*=、/=、%=、//=、**=、&=、|=、^=、>>=、<<=	赋值运算符


#算术运算符
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

print(321 / 12)     # 除法运算，输出26.75
print(round(321 / 12, 1))   # 四舍五入保留一位小数，输出 26.8 round(值, 位数)
print(f"{321 / 12:.1f}")    # 四舍五入保留一位小数，输出 26.8
# :.1f 表示按浮点数格式输出，并保留 1 位小数（四舍五入）。
""""
- 外面是 f"..." ：说明这是 f-string
- 里面 {321 / 12:.1f} ：
- 321 / 12 是表达式
- :.1f 是格式说明：保留 1 位小数

print("{name} 已经 {age} 岁了")
# 会原样输出 {name} 和 {age}，不会替换成变量值
"""
name = "张三"
age = 18
print("{name} 已经 {age} 岁了")


#算术运算的优先级 如果还有求幂运算，求幂运算的优先级是高于乘除法的

print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625
""""
原始：((2 + 3) * 5) ** 2
      └─┬─┘
步骤1：  5
        (5 * 5) ** 2
         └─┬─┘
步骤2：   25
          25 ** 2
          └──┬──┘
步骤3：     625
"""


#赋值运算符和复合赋值运算符
a = 10
b = 3
a += b        # 相当于：a = a + b 13
a *= a + 2    # 相当于：a = a * (a + 2) 13*15=195
print(a)      # 大家算一下这里会输出什么 195


#海象运算符
# SyntaxError: invalid syntax
#print((a = 10)) 报错：SyntaxError: invalid syntax
# 海象运算符
print((a := 10))  # 10
print(a)          # 10

"""
逻辑运算符有三个，分别是and、or和not。and字面意思是“而且”，所以
and运算符会连接两个布尔值或者产生布尔值的表达式，如果两边的布尔值都是True，那么运算的结果就是True；左右两边的布尔值有一个是False，最终的运算结果就是False。当然，如果and运算符左边的布尔值是False，不管右边的布尔值是什么，最终的结果都是False，这时运算符右边的布尔值会被跳过（专业的说法叫短路处理，如果and右边是一个表达式，那么这个表达式不会执行）。
or字面意思是“或者”，所以or运算符也会连接两个布尔值或产生布尔值的表达式，如果两边的布尔值有任意一个是True，那么最终的结果就是True。当然，or运算符也是有短路功能的，当它左边的布尔值为True的情况下，右边的布尔值会被短路（如果or右边是一个表达式，那么这个表达式不会执行）。
not运算符的后面可以跟一个布尔值，如果not后面的布尔值或表达式是True，那么运算的结果就是False；如果not后面的布尔值或表达式是False，那么运算的结果就是True。
"""


#比较运算符和逻辑运算符的使用

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False

#将华氏温度转换为摄氏温度
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))


#输入半径计算圆的周长和面积

radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)