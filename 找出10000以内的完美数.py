"""
找出10000以内的完美数。
Version: 0.1
Author: Frank.Xiang
"""
a = 0
for Num in range(1,10001):
	for i in range(1,Num):
		if Num % i == 0:
			a = a + i
	if a == Num:
		print(Num)
	a = 0