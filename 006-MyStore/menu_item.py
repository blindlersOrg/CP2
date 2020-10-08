class MenuItem:

	def __init__(self, name, cost = 0, qty = 0 ):
		self._name = name
		self._cost = cost
		self._qty = qty
		
	@property
	def cost(self):
		print("im in a property")
		return self._cost

	@cost.setter
	def cost(self, new_cost):
		print("im in the setter")
		if new_cost <= 0: print("price cannot be negative.  Price unchanged")
		else:
			self._cost = new_cost

	def __str__(self):
		return f'{self._name}: {self._qty} available at ${self._cost}'
		#return( '{}: {} available at ${}').format(self.name, #self.qty, self.cost)

	def __repr__(self):
		return f'{self._name}:{self._qty}:{self._cost}'


