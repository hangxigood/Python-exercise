"""
找出所有水仙花数

Version: 0.1
Author: Frank.Xiang
"""
i = 0
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			if a**3 + b**3 + c**3 == 100*a + 10*b + c:
				i = i + 1
				print('The %dth number is %d'%(i,100*a + 10*b + c))

"""
别人的代码

for num in range(100, 1000):
   low = num % 10
   mid = num // 10 % 10
   high = num // 100
   if num == low ** 3 + mid ** 3 + high ** 3:
       print(num)

"""