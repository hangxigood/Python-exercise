"""
各类排序算法
Version: 0.1
Author: Frank.Xiang
"""



from random import randint

#选择排序法

def select_sort(original_list):
	sort_list = original_list
	for i in range(len(sort_list)-1):
		for j in range(i+1,len(sort_list)):
			if sort_list[i] > sort_list[j]:
				sort_list[i],sort_list[j] = sort_list[j],sort_list[i]

	return sort_list

#冒泡排序法
'''
1.两两排序，循环比较 n-1 次，
2.每次循环缩减一次比较。
3.如果有一次循环无交换，则停止，出结果。
'''

def bubble_sort(original_list):
	sort_list = original_list
	original_len = len(original_list)

	while original_len:
		flag = True
		for i in range(original_len-1):
			if sort_list[i] > sort_list[i+1]:
				sort_list[i],sort_list[i+1] = sort_list[i+1],sort_list[i]
				flag = False

		if flag == True:
			break

		original_len -= 1

	return sort_list

#归并排序法
'''
两列数组比较合并
1.从第一个数开始比，谁小则移至temp数组，同时移动下标。
2.直至其中一列下标到顶结束，把剩下一列剩余数值加上
'''

def merge(divide_list1,divide_list2):
	temp = []
	len_list1 = len(divide_list1)
	len_list2 = len(divide_list2)
	i = j = 0

	while ((len_list1-i) * (len_list2-j)):
		if divide_list1[i] <= divide_list2[j]:
			temp.append(divide_list1[i])
			i += 1
		else:
			temp.append(divide_list2[j])
			j += 1

	temp += divide_list1[i:]
	temp += divide_list2[j:]

	return temp

'''
拆分递归
1.长数组，持续从中拆分，直至无法拆分
2.从最小单位开始合并，合并结果作为上一层的参数继续合并，直至最初数列。
'''

def merge_sort(original):
	if len(original) < 2:
		return original
	mid = len(original)//2
	left = merge_sort(original[:mid])
	right = merge_sort(original[mid:])

	return merge(left,right)

#快速排序Python 高速版本
def quick_sort(list):
	if len(list) < 2:
		return list
	pivot = list[randint(0,len(list)-1)]
	left = [x for x in list if x < pivot]
	mid = [x for x in list if x == pivot]
	right = [x for x in list if x > pivot]

	return quick_sort(left) + mid + quick_sort(right)

#快速排序 实在版本

def quick_sort(list):
	item = list[:]
	_quick_sort(item,0,len(item)-1)
	return item

def _quick_sort(list,start,end):
	if start < end:
		pos = _partition(list,start,end)
		_quick_sort(list,pos+1,end)
		_quick_sort(list,start,pos-1)

def _partition(list,start,end):
	pivot = list[end]
	i = start - 1

	for j in range(start,end):
		if list[j] < pivot:
			i += 1 
			list[j],list[i] = list[i],list[j]

	list[end],list[i+1] = list[i+1],list[end]
	return i+1

	


 
#随机数列排序

def main():
	a_list = []
	for _ in range(8):
		a_list.append(randint(0,100))
	print(quick_sort(a_list))

if __name__ == '__main__':
	main()




