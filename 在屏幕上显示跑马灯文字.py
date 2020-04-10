"""
ver : 0.1
author : Frank.Xiang
"""
import os
import time

def main():
	content = '我是一个大帅哥'
	while True:
		os.system('clear')
		print(content)
		content = content[1:] + content[0]
		time.sleep(0.2)

if __name__ == '__main__':
	main()
	