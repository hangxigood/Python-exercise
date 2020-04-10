"""
100个线程向同一个银行账户转账（转入1元钱）的场景
Version: 0.1
Author: Frank.Xiang
"""
from threading import Thread,Lock
from time import sleep

class account(object):
	"""docstring for account"""
	def __init__(self, balance=0):
		super(account, self).__init__()
		self._balance = balance
		self._lock = Lock()
	
	def deposit(self,money):
		self._lock.acquire()
		try:
			new_balance = self._balance + money
			sleep(0.01)
			self._balance = new_balance
		finally:
			self._lock.release()

	@property
	def balance(self):
		return self._balance
	
class deposit_thread(Thread):
	"""docstring for deposit_thread"""
	def __init__(self, account):
		super(deposit_thread, self).__init__()
		self._account = account
		
	def run(self):
		self._account.deposit(1)

def main():
	Account = account()
	people = []
	for _ in range(100):
		p = deposit_thread(Account)
		people.append(p)
		p.start()
	for p in people:
		p.join()
	print('The account balance is %d.'%Account.balance)

if __name__ == '__main__':
	main()