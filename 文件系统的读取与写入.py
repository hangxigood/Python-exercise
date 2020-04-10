def main():

	#content = ('这里是第一行\n这里是第二行\n这里是第三行\n这里是第四行')
	try:
		with open('练习.txt','r') as f:
			while True:
				data = f.readline()
				if data:
					print(data,end='')
				else:
					break
	except FileNotFoundError:
		print('无法打开指定文件')
	except LookupError:
		print('指定了错误的编码')
	except UnicodeDecodeError:
		print('读取文件时解码错误')

if __name__ == '__main__':
	main()