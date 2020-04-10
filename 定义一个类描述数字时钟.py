'''
定义一个类描述数字时钟
ver：0.1
author: Frank.Xiang
'''
from time import sleep

class Clock(object): # 这里是objcet ? 为什么？
	"""docstring for Clock"""
	def __init__(self,hour=0,minute=0,second=0): #这里是 self.hour 还是直接 hour ?
		self._hour = hour
		self._minute = minute #
		self._second = second

	def run(self): #这里要加self 为什么
		self._second += 1
		if self._second == 60:
			self._minute += 1
			self._second = 0
			if self._minute == 60:
				self._hour += 1
				self._minute = 0
				if self._hour == 24:
					self._hour = 0

	def show_time(self):
		return '%02d:%02d:%02d'%(self._hour,self._minute,self._second) #返回不用 print 

def main():
	clock = Clock(23,59,0)
	while True:
		print(clock.show_time()) #这里是 clock 还是 Clock ? return 回来也要 print
		sleep(1)
		clock.run()

if __name__ == '__main__':
	main()