from threading import Thread
from random import randint
from time import time,sleep
from os import getpid

class download_task(Thread):
	"""docstring for download_task"""
	def __init__(self, filename):
		super(download_task, self).__init__()
		self.filename = filename

	def run(self): # 进程执行的主程序
		print('%s下载任务开始.'%self.filename)
		time = randint(5,10)
		sleep(time)
		print('%s下载任务结束，耗时 %d 秒。'%(self.filename,time))

def main():
	start = time()
	p1 = download_task('Tokoy hot.avi')
	p2 = download_task('Beijing hot.avi')
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	end = time()
	print('所有任务下载结束，任务执行时间：%.4f 。'%(end - start))

if __name__ == '__main__':
	main()
