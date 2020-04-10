'''
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
ver:0.1
author:Frank.Xiang
'''
def Joseph_ring():
	persons = [True] * 30
	index,count,number = 0,0,0 
	#index 代表列表中的具体位置
	#count 对True 是否到达9的计数
	#number 对扔人次数的计算
	while number < 15: #作15次这个行为,扔15个人就停止
		if persons[index] :
			count += 1
			if count == 9:
				persons[index] = False
				count = 0
				number += 1
		index += 1 #无论数的是是活还是死，index需要如实累加，方便下一次循环开启
		index %= 30 #使列表变成一个循环
	return(persons)
		


def main():
	print(Joseph_ring())

if __name__ == '__main__':
	main()