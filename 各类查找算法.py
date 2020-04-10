"""
各类查找算法
Version: 0.1
Author: Frank.Xiang
"""

from random import randint

#顺序查找
def seq_search(items,key):
	for index,item in enumerate(items):
		if item == key:
			return index
	return -1

#二分查找
#1.通过限制数组的左右限，取中间值，不断比较大小
#2.根据比较结果，改变左右限，使mid 趋近0
#3.必须用于顺序序列。
def bin_search(items,key):

	start = 0
	end = len(items)-1

	while start <= end:

		mid = (start + end)//2

		if items[mid] < key:
			start = mid + 1
		elif items[mid] > key:
			end = mid - 1
		else:	
			return mid

	return -1


def main():
	list1 = []
	for i in range(20):
		list1.append(i*2)
	print(list1)
	print('The index of 18 is: %d'%bin_search(list1,18))

if __name__ == '__main__':
	main()