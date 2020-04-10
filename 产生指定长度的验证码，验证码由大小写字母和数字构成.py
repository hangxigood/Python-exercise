"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
ver:0.1
author:Frank.Xiang
"""
import random
def generate_code(code_len = 4):
	all_chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	code = ''
	last_pos = len(all_chars) - 1
	for _ in range(code_len):
		code += all_chars[random.randint(0,last_pos)]
	return code
