from Classes.MenuItem import MenuItem


class Drink(MenuItem):
	""" A drink for the Pizza Parlour
	"""
	
	all_possible_drinks = {'Coke': 1.59, 'Diet Coke': 1.69, 'Coke Zero': 1.69, 'Pepsi': 1.69, 'Diet Pepsi': 1.29,
	                       'Dr Pepper': 1.29, 'Water': 0.99, 'Juice': 1.99}
	
	def __init__(self, chosen_drink):
		self.drink = ""
		
		if chosen_drink in self.all_possible_drinks:
			self.drink = chosen_drink
