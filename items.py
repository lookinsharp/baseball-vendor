class Item:
	#food or drink 
	isTossible = False
	price = -.1
	popularity = 0.0
	
	def __init__(self):
		#if item is x, y, or z, set item to b tossable? make new method for is it tossible
		self.isTossible = False
		self.price = -1
		self.poularity = -1

	def setToss(toss):
		if toss:
			isTossible = True
		else:
			isTossible = False
	def setPrice(p):
		if not p<0.01:
			price = p
		else:
			print("not an acceptible price")	
	def setPop(pop):
		if not pop < 1:
			popularity = pop
		else:
			print("not an acceptible popularity")