from MenuItem import MenuItem
import json


class Pizza(MenuItem):
	"""
	Pizza Class
	"""
	try:
		with open('../Menu.json', "r") as f:
			data = json.load(f)
			f.close()
	except IOError:
		print("Could not load JSON file")
	
	# The prices of each pizza
	all_pizza_types = data["all_pizza_types"]
	
	# All possible toppings offered. Each topping costs 50 cents
	all_pizza_toppings = data["all_pizza_toppings"]
	
	# Pizza size
	all_pizza_sizes = data["all_pizza_sizes"]
	
	def __init__(self, pizza_type, size, toppings=None):
		
		# Initialise to empty list
		if toppings is None:
			toppings = {}
		self.pizza_toppings = {}
		self.size = "medium"
		
		if pizza_type in self.all_pizza_types:
			self.pizza_type = pizza_type
		else:
			# Default Pizza Type
			self.pizza_type = 'Margherita'
		
		for topping in toppings:
			if topping in self.all_pizza_toppings:
				self.pizza_toppings[topping] = self.all_pizza_toppings[topping]
		
		if size in self.all_pizza_sizes:
			self.size = size
		
		self.price = float(self.all_pizza_types[self.pizza_type]) + sum(self.pizza_toppings.values()) + \
		             float(self.all_pizza_sizes[self.size])
	
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
		return float(self.all_pizza_types[self.pizza_type]) + sum(self.pizza_toppings.values()) + \
		       float(self.all_pizza_sizes[self.size])
	
	"""
	The below functions are for modifying the Menu json file.
	"""
	
	def create_pizza_type(self, new_type, price):
		"""
		Given a new_type and a price, create a new Pizza type.
		:param new_type: New type of pizza to add
		:type new_type: string
		:param price: price of the new type
		:type price: float
		:return: void
		:rtype: void
		"""
		try:
			if new_type not in self.all_pizza_types:
				with open('../Menu.json', "r+") as f:
					data = json.load(f)
					data["all_pizza_types"].update({new_type: price})
					f.seek(0)
					json.dump(data, f, indent=4)
					f.truncate()  # Removes the remaining part of the JSON
					f.close()
		except IOError:
			print("Could not add pizza type {} to Menu!".format(new_type))
	
	def remove_pizza_type(self, remove_type):
		"""
		Given a particular type of pizza, remove it to show that the Pizza Parlour is no longer serving this type of pizza.
		:param remove_type: remove this type of pizza
		:type remove_type: string
		:return: void
		:rtype: void
		"""
		try:
			if self.all_pizza_types.pop(remove_type, None) is not None:
				with open('../Menu.json', "r+") as f:
					data = json.load(f)
					data["all_pizza_types"] = self.all_pizza_types
					f.seek(0)
					json.dump(data, f, indent=4)
					f.truncate()  # Removes the remaining part of the JSON
					f.close()
		except IOError:
			print("Could not remove the pizza type: {}".format(remove_type))
	
	def create_pizza_topping(self, new_topping, new_topping_price):
		"""
		Create a new pizza topping with the name of the new_topping
		
		:param new_topping: New topping name
		:type new_topping: string
		:param new_topping_price: new topping price
		:type new_topping_price: float
		:return: void
		:rtype: void
		"""
		try:
			if new_topping not in self.all_pizza_toppings:
				with open('../Menu.json', "r+") as f:
					data = json.load(f)
					data["all_pizza_toppings"].update({new_topping: new_topping_price})
					f.seek(0)
					json.dump(data, f, indent=4)
					f.truncate()  # Removes the remaining part of the JSON
					f.close()
		except IOError:
			print("Could not add pizza topping {} to Menu!".format(new_topping))
		
	def remove_pizza_topping_from_menu(self, remove_topping):
		"""
		Given remove_topping, remove this topping from the Pizza Parlour's menu
		:param remove_topping: topping that needs to be removed.
		:type remove_topping: string
		:return: void
		:rtype: void
		"""
		try:
			if self.all_pizza_toppings.pop(remove_topping, None) is not None:
				with open('../Menu.json', "r+") as f:
					data = json.load(f)
					data["all_pizza_toppings"] = self.all_pizza_toppings
					f.seek(0)
					json.dump(data, f, indent=4)
					f.truncate()  # Removes the remaining part of the JSON
					f.close()
		except IOError:
			print("Could not remove the pizza type: {}".format(remove_topping))


if __name__ == "__main__":
	newZa = Pizza("Pepperoni", "small")
	print(newZa.get_type())
	print(newZa.remove_pizza_topping_from_menu("Corona deez nuts"))
	print(newZa.remove_pizza_topping_from_menu("Corona Virus"))
