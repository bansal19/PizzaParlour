class Pizza:
	"""
	Pizza Class
	"""
	
	# The prices of each pizza
	all_pizza_types = {'Pepperoni': 8.99, 'Margherita': 7.50, 'Vegetarian': 7.59, 'Neapolitan': 11.99}
	
	# All possible toppings offered. Each topping costs 50 cents
	all_pizza_toppings = ['onions', 'tomatoes', 'anchovies', 'extra cheese', 'garlic', 'salt', 'ham']
	
	def __init__(self, pizza_type, toppings):
		
		if pizza_type in self.all_pizza_types:
			self.pizza_type = pizza_type
			
		if all(topping in self.pizza_toppings for topping in toppings):
			self.pizza_toppings = toppings
		
		self.price = self.all_pizza_types[pizza_type] + (0.5 * len(toppings))

	def get_type(self):
		"""
		Return the current pizza type
		
		:return: pizza type
		:rtype: string
		"""
		return self.pizza_type

	def set_type(self, new_type):
		"""
		Upon modifying the order, a new pizza type can be set
		
		:param new_type: new type of the pizza
		:type new_type: string
		:return: void
		:rtype: void
		"""
		if new_type in self.all_pizza_types:
			self.pizza_type = new_type

	def get_toppings(self):
		"""
		Get all the pizza toppings

		:return: all the current toppings on the pizza
		:rtype: list
		"""
		return self.pizza_toppings
	
	def add_toppings(self, append_toppings):
		"""
		Add toppings to the pizza
		
		:param append_toppings: all the toppings that the customer wants appended
		:type append_toppings: list
		:return: void
		:rtype: void
		"""
		if all(topping in self.pizza_toppings for topping in append_toppings):
			for item in append_toppings:
				if item not in self.pizza_toppings:
					self.pizza_toppings.append(item)
	
	def remove_toppings(self, remove_toppings):
		"""
		Remove toppings that a customer has asked to be put on the pizza
		
		:param remove_toppings: all the toppings the client wants removed
		:type remove_toppings: list
		:return: void
		:rtype: void
		"""
		for item in remove_toppings:
			try:
				self.pizza_toppings.remove(item)
			except ValueError:
				print("Oops, that was already not on the pizza!")
	
	def get_price(self):
		"""
		Return the price of the pizza
		
		:return: price of pizza
		:rtype: float
		"""
		return self.all_pizza_types[self.pizza_type] + (0.5 * len(self.pizza_toppings))
