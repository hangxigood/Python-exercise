"""
实现判断一个数是不是素数的函数

Version: 0.1
Author: Frank.Xiang
"""

def is_Prime_number(num):
	for i in range(2,num):
		if num % i == 0:
			return False
			break
	return True if num!=1 else False

"""
别人的做法

for i in range(2,num):
	if num % i == 0:
	return False # 我觉得可以加 break 节省计算资源，省去继续找因数
return True if num !=1 else False

"""
