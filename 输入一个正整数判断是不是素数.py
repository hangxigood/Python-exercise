"""
输入一个正整数判断是不是素数。

Version : 0.1
Date : 2020.2.8
Author : Frank.Xiang

"""
num = int(input('请输入一个正整数：'))
is_prime = 1
for i in range(2,num):
	if num % i == 0 :
		is_prime = 0
		break
if is_prime == 1 and num != 1:
	print('该正整数是素数。')
else:
	print('该正整数不是素数。')