"""
设计一个函数返回传入的列表中最大和第二大的元素的值。
ver:0.1
author:Frank.Xiang
"""
def get_max_and_secondlargest(list):
	resorted_list = sorted(list,reverse=True)
	max_num = resorted_list[0]
	sec_num = resorted_list[1]
	return max_num,sec_num

"""
也可以整体作排序对比
"""
def max2(list):
	m1,m2 = (list[0],list[1]) if list[0]>list[1] else (list[1],list[0])#两个赋值，要加括号
	for index in range(2,len(list)):
		if list[index]>m1: #同时寻找最大值和次大值，只需轮询的数字只有更大、更小、在中间的情况，分析后转化为代码即可
			m2 = m1
			m1 = list[index]
		elif list[index]>m2:
			m2 = list[index]
	return m1,m2
