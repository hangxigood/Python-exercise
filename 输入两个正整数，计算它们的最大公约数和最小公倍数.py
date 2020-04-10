"""
输入两个正整数，计算它们的最大公约数和最小公倍数。

一个数字能同时被两个数整除，找出这组数值中的最大值和最小值。

Version : 0.1
Date : 2020.2.8
Author : Frank.Xiang

"""

a = int(input('Please enter the first positive integers:'))
b = int(input('Please enter the second positive integers:'))
c = min(a,b)
e = 0
f = 0
if a == 1 and b == 1:
	print('The greatest common divisor and the least common multiple is 1')
elif a == 1 or b == 1:
	print('The greatest common divisor is 1')
	print('The least common multiple is %d'%max(a,b))
else:
	for d in range(2,c):
		if a % d == 0 and b % d == 0: #原来的写法是 if a % d and b % d == 0，有错
			e = max(e,d)
			f = 1
	for g in range(max(a,b),a*b+1):
		if g % a == 0 and g % b == 0:
			print('The least common multiple is %d'%g)
			break
	if f == 0:
		print('The greatest common divisor is 1')
	else:
		print('The greatest common divisor is %d'%e)

"""
别人的代码

x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
        
"""