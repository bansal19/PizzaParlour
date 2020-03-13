from Classes.MenuItem import MenuItem


class Pizza(MenuItem):
	"""
	Pizza Class
	"""
	
	# The prices of each pizza
	all_pizza_types = {'Pepperoni': 8.99, 'Margherita': 7.50, 'Vegetarian': 7.59, 'Neapolitan': 11.99}
	
	# All possible toppings offered. Each topping costs 50 cents
	all_pizza_toppings = ['onions', 'tomatoes', 'anchovies', 'extra cheese', 'garlic', 'salt', 'ham']
	TOPPINGS_PRICE = 0.50
	# Pizza size
	all_pizza_sizes = {'small': -2.00, 'medium': 0.00, 'large': 2.00, 'family size': 5.00}
	
	def __init__(self, pizza_type, toppings, size):
		
		# Initialise to empty list
		self.pizza_toppings = []
		
		if pizza_type in self.all_pizza_types:
			self.pizza_type = pizza_type
		else:
			# Default Pizza Type
			self.pizza_type = 'Margherita'

		for topping in toppings:
			if topping in self.all_pizza_toppings:
				self.pizza_toppings.append(topping)
		
		if size in self.all_pizza_sizes:
			self.size = size
		
		self.price = self.all_pizza_types[pizza_type] + (self.TOPPINGS_PRICE * len(toppings)) + size

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
		return self.all_pizza_types[self.pizza_type] + (self.TOPPINGS_PRICE * len(self.pizza_toppings)) + self.size
	
	def create_pizza_type(self, new_type, price):
		"""
		Given a new_type and a price, create a new Pizza type.
		:param new_type: New type of pizza to add
		:type new_type: string
		:param price: price of the new type
		:type price: int
		:return: void
		:rtype: void
		"""
		self.all_pizza_types[new_type] = price
	
	def remove_pizza_type(self, remove_type):
		"""
		Given a particular type of pizza, remove it to show that the Pizza Parlour is no longer serving this type of pizza.
		:param remove_type: remove this type of pizza
		:type remove_type: string
		:return: void
		:rtype: void
		"""
		if self.all_pizza_types.pop(remove_type, None) is None:
			print("The type specified, {}, does not exist in all pizza types!".format(remove_type))
	
	
	
""" Add the ability to add pizza types, remove pizza types, add possible pizza toppings, remove all possible pizza toppings
change price of certain items
"""
