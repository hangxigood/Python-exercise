
class Staff(object):
	"""docstring for ClassName"""
	def __init__(self,name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		self._name = name

	def get_salary(self):
		pass

class Manager(Staff):
	def __init__(self,name):
		super().__init__(name)

	def get_salary(self):
		return 15000
		
class Programmer(Staff):
	"""docstring for ClassName"""
	def __init__(self,name,operating_hours = 0):#必须给默认值，否则出错
		super().__init__(name) #继承父类的 name 属性
		self._operating_hours = operating_hours

	#@property
	def operating_hours(self):
		return self._operating_hours

	operating_hours = property(operating_hours)
	
	#@operating_hours.setter
	def operating_hours(self,operating_hours):
		self._operating_hours = operating_hours if operating_hours > 0 else 0
		#对输入属性进行判定

	operating_hours.setter()

	def get_salary(self):
		return self._operating_hours * 150

class Seller(Staff):
	"""docstring for Sales"""
	def __init__(self,name,sales = 0):
		super().__init__(name)
		self._sales = sales if sales > 0 else 0

	@property
	def sales(self):
		return self._sales
	
	@sales.setter #没有使用装饰器property 之前，无法使用修改器
	def sales(self,sales):
		self._sales = sales

	def get_salary(self):
		return self._sales * 0.05 + 1200

def main():
	staffs = [Manager('张三'),Programmer('李四'),Programmer('王五'),Seller('赵六')]
	for staff in staffs:
		if isinstance(staff,Programmer):
			staff.operating_hours = int(input('Please input the operating_hours of %s: '%staff.name))
			#为什么这里可以直接赋值？装饰器setter 的作用和原理是什么？
		elif isinstance(staff,Seller):
			staff.sales = int(input('Please input the sales of %s: '%staff.name))
		print('The salary of %s is %d'%(staff.name,staff.get_salary()))

if __name__ == '__main__':
	main()
		