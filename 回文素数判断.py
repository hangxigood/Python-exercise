"""
判断一个数字是否是回文素数

Version: 0.1
Author: Frank.Xiang
"""

from is_palindromes import is_palindromes
from is_Prime_number import is_Prime_number

if __name__ == '__main__':
	Num = int(input('Please input the number :'))
	if is_palindromes(Num) and is_Prime_number(Num) == True:
		print('%d is Palindrome prime'%Num)
	else:
		print('%d is not Palindrome prime'%Num)