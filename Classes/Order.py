from enum import Enum


class Order:
	"""
	An Order class
	"""
	total_orders = 0

	def __init__(self):
		self.order_items = []
		self.order_number = Order.total_orders
		self.order_status = OrderStatus.STARTED
		self.distribution = None
		Order.total_orders += 1

	@staticmethod
	def increase_total_orders(cls):
		"""
		Increases the number of total orders that have been created

		:param cls: Order
		:return: void
		"""
		cls.total_orders += 1

	@staticmethod
	def get_total_orders(cls):
		"""
		Gets the number of orders that have been created so far

		:param cls: Order
		:return: order number
		"""
		return cls.total_orders

	def get_order_number(self):
		"""
		Gets the unique number identifying this order
		The number is incremented with each order that gets created, starting from 0

		:return: this order number
		"""
		return self.order_number

	def get_price(self):
		"""
		Gets the total price of this order
		This number is calculated as the sum of the item prices in this order

		:return: total price of this order
		"""
		sum = 0

		for order in self.order_items:
			sum += order.get_price()

		return sum

	def get_order_items(self):
		"""
		Gets the items in this order

		:return: list of MenuItems in this order
		"""
		return self.order_items

	def add_order_item(self, MenuItem):
		"""
		Adds an item to this order

		:param MenuItem: Item to add to this order
		:return: void
		"""
		self.order_items.append(MenuItem)

	def cancel_order(self):
		"""
		Cancel current order
		:return: void
		:rtype: void
		"""
		self.order_status = OrderStatus.CANCELED

	def set_order_distribution(self, distribution):
		"""
		Set the order distribution from a list of "pickup", "in-house-delivery", "uber-delivery",
		"foodora-delivery"

		"""
		if distribution in ["pickup", "in-house-delivery", 'uber-delivery', "foodora-delivery"]:
			self.distribution = distribution
		else:
			self.distribution = "pickup"

	def __str__(self):
		"""
		Return to later once we know what we want out of this
		:return:
		"""
		order_details = {"orderID": self.order_number, "order status": str(self.order_status), "order items": [], "order distribution": self.distribution, "order price": self.get_price()}

		for item in self.get_order_items():
			order_details["order items"].append(str(item))

		return str(order_details)


class OrderStatus(Enum):
	""" Each order has a status"""
	STARTED = 0
	PLACED = 1
	OUT_FOR_DELIVERY = 2
	DELIVERED = 3
	OUT_FOR_PICKUP = 4
	PICKED_UP = 5
	CANCELED = 9

