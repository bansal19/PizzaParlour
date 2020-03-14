from MenuItem import MenuItem
import json


class Drink(MenuItem):
	""" A drink for the Pizza Parlour
	"""
	with open('../Menu.json', "r") as f:
		data = json.load(f)
	
	all_possible_drinks = data["all_drinks"]
	
	def __init__(self, chosen_drink):
		self.drink = ""
		
		if chosen_drink in self.all_possible_drinks:
			self.drink = chosen_drink

	def get_drink(self):
		"""
		Gets the current drink
		
		:return: drink
		:rtype: string
		"""
		return self.drink
	
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


if __name__ == '__main__':
	this_drink = Drink("Coke")
	print(this_drink.add_drink("Diet Yeet Shalom", 0.69))
