import json
import os


class Menu:
	""" Full menu of the Pizza Parlour"""

	__instance = None

	@staticmethod
	def get_instance():
		""" Static access method. """
		if Menu.__instance is None:
			Menu()
		return Menu.__instance
	
	def __init__(self, json_path):
		""" Virtually private constructor. """
		self.json_path = json_path
		data = None
		try:
			print(os.getcwd())
			with open(self.json_path, "r") as f:
				data = json.load(f)
				f.close()
		except IOError:
			print("Could not load JSON file")

		# The prices of each pizza
		self.all_pizza_types = data["all_pizza_types"]

		# All possible toppings offered. Each topping costs 50 cents
		self.all_pizza_toppings = data["all_pizza_toppings"]

		# Pizza size
		self.all_pizza_sizes = data["all_pizza_sizes"]

		# All pizza drinks in the Menu
		self.all_possible_drinks = data["all_drinks"]

		if Menu.__instance is not None:
			raise Exception("This class is a singleton!")
		else:
			Menu.__instance = self
	
	def get_menu(self):
		"""
		Get the full menu
		
		:return:
		:rtype:
		"""
		try:
			with open(self.json_path, "r") as f:
				data = json.load(f)
				return json.dumps(data, indent=4)
		except IOError:
			return "Could not get the menu! Had IOError opening and reading the Menu.json file"
	
	def get_item_price(self, name):
		"""

		Given a name, return the price of that item
		:param name: name of a MenuItem
		:type name: string
		:return: the price of the MenuItem
		:rtype: int
		"""
		try:
			with open(self.json_path, "r") as f:
				data = json.load(f)
				for categories in data:
					for item in data[categories]:
						if item == name:
							return data[categories][item]
				return "Menu item not found in menu!"
		except IOError:
			return "Could not get the menu! Had IOError opening and reading the Menu.json file"
	
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
				with open(self.json_path, "r+") as f:
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
				with open(self.json_path, "r+") as f:
					data = json.load(f)
					data["all_pizza_types"] = self.all_pizza_types
					f.seek(0)
					json.dump(data, f, indent=4)
					f.truncate()  # Removes the remaining part of the JSON
					f.close()
		except IOError:
			print("Could not remove the pizza type: {}".format(remove_type))