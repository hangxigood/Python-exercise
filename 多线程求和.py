"""
1~100000000求和的计算
Version: 0.1
Author: Frank.Xiang
"""
"""单进程，out: The sum is 5000000050000000, using 8.89s
from time import time

def main():
	num = [ x for x in range(1,100000001)]
	sum = 0
	start = time()
	for x in num:
		sum += x
	end = time()
	print('The sum is %d, took %.2fs'%(sum,end-start))

if __name__ == '__main__':
	main()

8进程，The sum of numbers is :5000000050000000, took 1.13s

from time import time
from multiprocessing import Process,Queue

def sum_4_num(num_list,q):
	Sum_temp = 0
	for num in num_list:
		Sum_temp += num
	q.put(Sum_temp)

def main():
	num_process = 8
	num_slice = int(100000000/num_process)
	number_list = [x for x in range(1,100000001)]
	index = 0
	Sum = 0
	q = Queue()
	p_list = []

	for _ in range(num_process):
		p = Process(target = sum_4_num, args = (number_list[index:index + num_slice],q))
		p_list.append(p)
		index += num_slice
		p.start()

	start = time()

	for p in p_list:
		p.join()

	while not q.empty():
		Sum += q.get()

	end = time()

	print('The sum of numbers is :%d, took %.2fs'%(Sum,end - start))

if __name__ == '__main__':
	main()
"""

