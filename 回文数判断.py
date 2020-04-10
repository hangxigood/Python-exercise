"""
练习2：实现判断一个数是不是回文数的函数。

Version: 0.1
Author: Frank.Xiang
"""
def is_palindromes(num):
	re_num = 0
	ce_num = num
	while ce_num > 0:
		re_num = re_num * 10 + ce_num % 10
		ce_num = ce_num // 10
	if num == re_num:#这里可以直接 return total == num
		return True
	else:
		return False