"""
打印星型三角形

Version: 0.1
Author: Frank.Xiang
Date: 2020-2-8
"""

for i in range(1,6): 
	for a in range(1,i+1): 
		print('*',end='')
	print(end='\n')

for i in range(1,6):
	for j in range(4,i-1,-1):
		print(' ',end='')
	for k in range(1,i+1):
		print('*',end='')
	print(end='\n')

for i in range(1,6):
	for j in range(4,i-1,-1):
		print(' ',end='')
	for k in range(1,2*i):
		print('*',end='')
	print()