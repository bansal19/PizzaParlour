from enum import Enum

class Order:
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

	def addOrderItem(self, MenuItem):
		"""
		Adds an item to this order

		:param MenuItem: Item to add to this order
		:return: void
		"""
		self.order_items.append(MenuItem)

	def cancelOrder(self):
		self.order_status = OrderStatus.CANCELED

	def __str__(self):
		"""
		Return to later once we know what we want out of this
		:return:
		"""
		return self.price

class OrderStatus(Enum):
	STARTED = 0
	PLACED = 1
	OUT_FOR_DELIVERY = 2
	DELIVERED = 3
	OUT_FOR_PICKUP = 4
	PICKED_UP = 5
	CANCELED = 9



if __name__ == "__main__":
	order1 = Order()
	print(order1.getOrderNumber())
	order2= Order()
	print(order2.getOrderNumber())
	order2 = Order()
	print(order2.getOrderNumber())
	order3 = Order()
	print(order3.getOrderNumber())

