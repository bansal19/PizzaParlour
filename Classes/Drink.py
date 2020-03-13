from Classes.MenuItem import MenuItem
import json

class Drink(MenuItem):
	""" A drink for the Pizza Parlour
	"""
	with open('../Menu.json') as f:
		data = json.load(f)
	
	all_possible_drinks = data['all_drinks']
	
	def __init__(self, chosen_drink):
		self.drink = ""
		
		if chosen_drink in self.all_possible_drinks:
			self.drink = chosen_drink
	
	def add_drink(self, drink_name, drink_price):
		"""
		Add a Drink to our JSON
		
		:param drink_name:
		:type drink_name:
		:param drink_price:
		:type drink_price:
		:return:
		:rtype:
		"""
		pass
