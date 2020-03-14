import json


class Menu:
	""" Full menu of the Pizza Parlour"""
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
	
	# All pizza drinks in the Menu
	all_possible_drinks = data["all_drinks"]
	
	__instance = None
	@staticmethod
	def get_instance():
		""" Static access method. """
		if Menu.__instance is None:
			Menu()
		return Menu.__instance
	
	def __init__(self):
		""" Virtually private constructor. """
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
			with open('../Menu.json', "r") as f:
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
		pass
	
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
	
	def add_drink_to_menu(self, drink_name, drink_price):
		"""
		Add a Drink to our JSON file

		:param drink_name: New drink to add
		:type drink_name: string
		:param drink_price: price of the new drink
		:type drink_price: float
		:return: void
		:rtype: void
		"""
		try:
			if drink_name not in self.all_possible_drinks:
				with open('../Menu.json', "r+") as f:
					data = json.load(f)
					data['all_drinks'].update({drink_name: drink_price})
					f.seek(0)
					json.dump(data, f, indent=4)
					f.close()
		except IOError:
			print("Could not add drink {} to Menu!".format(drink_name))
	
	def remove_drink_from_menu(self, drink):
		"""
		Given the drink (str), remove this from the Pizza Parlour menu (JSON file)

		:param drink: drink to be removed
		:type drink: string
		:return: void
		:rtype: void
		"""
		pass


if __name__ == "__main__":
	menu = Menu()
	print(menu.get_menu())
	
	print(menu.add_drink_to_menu("Diet Yeet Shalom", 0.69))
