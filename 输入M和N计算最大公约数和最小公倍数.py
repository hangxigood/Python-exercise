"""
输入M和N计算最大公约数和最小公倍数

Version: 0.1
Author: Frank.Xiang
"""

def GCD(Num1,Num2):
	for i in range(min(Num1,Num2),0,-1):
		if Num1 % i == 0 and Num2 % i == 0:
			break # 这里可以直接返回结果
	return i

def LCM(Num1,Num2):
	return(Num1 * Num2 / GCD(Num1,Num2))

print(GCD(12,8))
print(LCM(9,24))