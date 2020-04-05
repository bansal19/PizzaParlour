from Classes.MenuItem import MenuItem
import json


class Pizza(MenuItem):
	"""
	Pizza Class
	"""
	try:
		with open('Classes/Menu.json', "r") as f:
			data = json.load(f)
			f.close()
	except IOError:
		print("Could not load JSON file")
	
	# The prices of each pizza
	all_pizza_types = data["all_pizza_types"]
	
	# All possible toppings offered.
	all_pizza_toppings = data["all_pizza_toppings"]
	
	# Pizza size
	all_pizza_sizes = data["all_pizza_sizes"]
	
	def __init__(self, pizza_type, size, toppings=None):

		self.price = 0

		# Initialise to empty list
		if toppings is None:
			toppings = []
		self.pizza_toppings = []
		self.size = "medium"
		
		if pizza_type in self.all_pizza_types:
			self.pizza_type = pizza_type
		else:
			# Default Pizza Type
			self.pizza_type = 'Margherita'
		
		for topping in toppings:
			if topping in self.all_pizza_toppings:
				self.pizza_toppings.append(topping)
				self.price += float(self.all_pizza_toppings[topping])
			else:
				print("Sorry, topping " + topping + " does not exist in the Menu")

		if size in self.all_pizza_sizes:
			self.size = size
		
		self.price += float(self.all_pizza_types[self.pizza_type]) + float(self.all_pizza_sizes[self.size])

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
		self.price = float(self.all_pizza_types[self.pizza_type]) + float(self.all_pizza_sizes[self.size])

		for topping in self.get_toppings():
			self.price += float(self.all_pizza_toppings[topping])

		return self.price

	def __str__(self):
		"""ToString function of the Pizza Class"""
		return {self.pizza_type: {"size": self.size, "toppings": self.get_toppings(), "price": self.get_price()}}
