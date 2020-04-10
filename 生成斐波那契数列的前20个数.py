"""
生成斐波那契数列的前20个数

Version: 0.1
Author: Frank.Xiang
"""
a = 1
b = 1
print(a)
print(b)
for i in range(18):
	c = a + b
	print(c)
	a = b
	b = c
