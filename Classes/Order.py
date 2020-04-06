from enum import Enum
from Classes.Pizza import Pizza
from Classes.Drink import Drink
from Classes.MenuItem import MenuItem
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
		self.order_address = None
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

	def add_order_item(self, menu_item):
		"""

		Adds an item to this order

		:param menu_item: Item to add to this order
		:return: void
		"""
		self.order_items.append(menu_item)

	def remove_order_item(self, menu_item):
		"""
		Remove this menu item from this current order.
		"""

		breakpoint()

		for item in self.order_items:
			if isinstance(menu_item, Drink) and isinstance(item, Drink):
				if item.get_drink() == menu_item.get_drink():
					self.order_items.remove(item)
					return
			elif isinstance(menu_item, Pizza) and isinstance(item, Pizza):
				if item.get_type() == menu_item.get_type():
					self.order_items.remove(item)
					return
		print("WARNING!", menu_item, "could not be deleted.")

	def cancel_order(self):
		"""
		Cancel current order
		:return: void
		:rtype: void
		"""
		self.order_status = OrderStatus.CANCELED

	def set_order_distribution(self, distribution, order_address=None):
		"""
		Set the order distribution from a list of "pickup", "in-house", "uber",
		"foodora"
		Order address cannot be none if using in-house, uber or foodora
		"""
		if distribution in ["pickup", "in-house", 'uber', "foodora"]:
			self.distribution = distribution
			self.set_order_address(order_address)
		else:
			self.distribution = "pickup"

	def set_order_address(self, order_address):
		"""Set the address of the order if it is not a pickup"""
		self.order_address = order_address

	def order_ready_for_pickup(self):
		""" Set an order to be ready for pickup"""
		self.order_status = OrderStatus.OUT_FOR_PICKUP

	def order_picked_up(self):
		""" Set an order to complete, it has been picked up"""
		self.order_status = OrderStatus.PICKED_UP

	def order_out_for_delivery(self):
		""" Set an order's status to be out for delivery"""
		self.order_status = OrderStatus.OUT_FOR_DELIVERY

	def order_delivered(self):
		""" Set an order's status to delivered"""
		self.order_status = OrderStatus.DELIVERED

	def to_dict(self):
		"""
		Return to later once we know what we want out of this
		:return:
		"""
		order_details = {"orderID": self.order_number, "order status": str(self.order_status),
						 "order items": [], "order distribution": self.distribution, "order price": self.get_price(),
						 "order address": self.order_address}

		for item in self.get_order_items():
			order_details["order items"].append(item.to_dict())

		return order_details


class OrderStatus(Enum):
	""" Each order has a status"""
	STARTED = 0
	OUT_FOR_DELIVERY = 1
	DELIVERED = 2
	OUT_FOR_PICKUP = 3
	PICKED_UP = 4
	CANCELED = 9

