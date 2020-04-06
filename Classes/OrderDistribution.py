from abc import ABC, abstractmethod


class OrderDistribution(ABC):
    """
	An OrderDistribution class

	Abstract class that defines the interface of an order delivery service
	"""
    def __init__(self):
        pass

    @abstractmethod
    def set_address(self):
        pass

<<<<<<< HEAD
	@abstractmethod
	def get_address(self):
		pass

	@abstractmethod
	def is_delivered(self):
		pass

	def __str__(self):
		"""
=======
    def get_address(self):
        pass

    def __str__(self):
        """
>>>>>>> 889fe4bd206af28f549bd34423df5cf546887947
		Return to later once we know what we want out of this
		:return:
		"""
        pass
