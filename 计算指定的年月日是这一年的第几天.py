"""
计算指定的年月日是这一年的第几天
ver:0.1
author:Frank.Xiang
"""

def is_leapyear(year): #闰年返回True,平年返回False
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def howmuch_day(month,day,year):
	month_day = [[31,28,31,30,31,30,31,31,30,31,30,31],
	[31,29,31,30,31,30,31,31,30,31,30,31]][is_leapyear(year)] #这里有个列表后+ True/False 选择小技巧
	num_day = 0
	for i in range(0,month-1):
		num_day += month_day[i]
	return num_day+day

def main():
	print(howmuch_day(2,12,2020))

if __name__ == '__main__':
	main()