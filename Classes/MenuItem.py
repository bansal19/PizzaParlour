from Menu import Menu


class MenuItem(Menu):
    """
	Menu Item
	"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        """
		Gets the price of the current item
		
		:return: price of item
		:rtype: int
		"""
        return self.price

    def set_price(self, new_price):
        """
		
		:param self:
		:type self:
		:param new_price: New price of curent MenuItem
		:type new_price: int
		:return: void
		:rtype: void
		"""
        self.price = new_price

    def get_name(self):
        """
		Get the name of the current item
		
		:return: the name of the current item
		:rtype: string
		"""
        return self.name

    def set_name(self, new_name):
        """
		Sets the name of the current MenuItem
		
		:param new_name: New Name of the item
		:type new_name: string
		:return: void
		:rtype: void
		"""
        self.name = new_name
