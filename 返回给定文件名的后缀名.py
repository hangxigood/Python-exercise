"""
设计一个函数返回给定文件名的后缀名。
ver:0.1
author:Frank.Xiang
"""
def main():
	print(get_suffix_name('abc.happy',True))

def get_suffix_name(filename,has_dot = False):
	pos = filename.rfind('.') # find/rfind/index/rindex 返回的数值都是从正开始数的
	if 0 < pos < len(filename) - 1 :
		index = pos if has_dot else pos+1
		return filename[index:]
	else:
		return ' '

if __name__ == '__main__':
	main()