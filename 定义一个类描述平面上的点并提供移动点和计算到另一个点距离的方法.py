'''
定义一个类
描述平面上的点
并提供移动点和计算到另一个点距离的方法
ver：0.1
author: Frank.Xiang
'''
from math import sqrt

class Point(object):
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
	def move_to(self,x,y):
		self.x = x
		self.y = y
	def move_by(self,dx,dy):
		self.x += dx
		self.y += dy 
	def get_distance(self,other): # other 可以在类中定义另一个对象
		dx = other.x - self.x
		dy = other.y - self.y
		return sqrt(dx**2 + dy**2)

def main():
	point1 = Point(5,3)
	print(point1.x,point1.y)
	point1.move_to(4,2)
	print(point1.x,point1.y)
	point1.move_by(1,1)
	print(point1.x,point1.y)
	point2 = Point(6,4)
	print('The distance is %.3d'%point1.get_distance(point2))

if __name__ == '__main__':
	main()
