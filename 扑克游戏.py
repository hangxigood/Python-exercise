import random

class Card(object):

	def __init__(self,suite,face):
		self._suite = suite
		self._face = face

	@property
	def suite(self):
		return self._suite
	
	@property
	def face(self):
		return self._face

	def __str__(self):
		if self._face == 1:
			self._str = 'A'
		elif self._face == 11:
			self._str = 'J'
		elif self._face == 12:
			self._str = 'Q'
		elif self._face == 13:
			self._str = 'K'
		else:
			self._str = self._face

		return '%s,%s'%(self._suite,self._str)
	__repr__ = __str__
'''
也可以用这种列表解析式的方式实现，更简单更不容易错
class Poker(object):
	def __init__(self):
		self._cards = [Card(suite,face) for suite in '♠♥♣♦' for face in range(1,14)]  
		#这个列表里是52张 Card
'''

class Poker(object):
	def __init__(self):
		self._cards = []
		self._current = 0
		for suite in '♠♥♣♦' :
			for face in range(1,14):
				self._cards.append(Card(suite,face)) #这里的self._cards 是一个由 Card 类 组成的列表。

	@property
	def cards(self):
		return self._cards

	def shuffle(self):
		self._current = 0 #每次洗牌，发牌计数归零
		random.shuffle(self._cards)

	@property #装饰器，将方法变成属性，如果没有它的话，p.next 就只是一个方法，p.next() 才是属性
	def next(self):#发牌
		card = self._cards[self._current]
		self._current += 1
		return card

	def has_next(self):
		return self._current < len(self._cards) # 发牌数和总牌数作比较，若小于，则还有牌。

class Player(object):
	def __init__(self,name):
		self._name = name
		self._cards_on_hand = []

	@property
	def name(self):
		return self._name
	
	def get(self,card):
		self._cards_on_hand.append(card)

	'''
	def arrange(self):
		self._cards_on_hand.sort(key = lambda x:(x.suite,x.face))
		#lambda 是匿名函数，常用于快速便捷定义函数，x 代表 list 中的元素（即对象）
		#在sort 中，根据对象的suite 和face 属性进行排序
	'''

	def arrange(self, card_key):
		self._cards_on_hand.sort(key=card_key) #这里的key 调用的card_key 是一个函数
		#该函数用于提取列表中每个元素的比较值，在这里提取的是对象的.suite\.face 属性

	@property
	def cards_on_hand(self):
		return self._cards_on_hand

def get_key(card):
    return (card.suite, card.face)
	

def main():
	p = Poker()
	p.shuffle() #洗牌
	players = [Player('张三'),Player('李四'),Player('王五'),Player('赵六')]
	for _ in range(13):
		for player in players:
			player.get(p.next)
	for player in players:
		#player.arrange() #如果用上一种写法，这里不需要参数。
		player.arrange(get_key)
		print(player.cards_on_hand)
	


if __name__ == '__main__':
	main()



	

	
