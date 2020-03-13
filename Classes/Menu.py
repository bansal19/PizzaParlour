class Menu:
	""" Full menu of the Pizza Parlour"""
	
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
		pass
	
	def get_item_price(self, name):
		"""
		Given a name, return the price of that item
		:param name: name of a MenuItem
		:type name: string
		:return: the price of the MenuItem
		:rtype: int
		"""
		pass
	
