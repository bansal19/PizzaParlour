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
	
	def set_drink(self, new_drink):
		"""
		Set a new drink
		
		:param new_drink: the new drink to set
		:type new_drink: string
		:return: void
		:rtype: void
		"""
		if new_drink in self.all_possible_drinks:
			self.drink = new_drink
	
	def get_price(self):
		"""
		Get the price of the current drink
		:return: the price of the drink
		:rtype: float
		"""
		return self.all_possible_drinks[self.get_drink()]


if __name__ == '__main__':
	print("Hey there.")
