"""
找出100以内的所有素数
说明：素数指的是只能被1和自身整除的正整数（不包括1）。

Version: 0.1
Author: Frank.Xiang
"""

for Num in range(2,100):
	a = 0
	for i in range(2,Num):
		if Num % i == 0:
			a = 1
			break
	if (a == 0):
		print(Num)