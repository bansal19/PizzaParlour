from abc import ABC, abstractmethod


class OrderDistribution(ABC):
    """
	An OrderDistribution class

	Abstract class that defines the interface of a order delivery service
	"""
    def __init__(self):
        pass

    @abstractmethod
    def set_address(self):
        pass

    def get_address(self):
        pass

    def __str__(self):
        """
		Return to later once we know what we want out of this
		:return:
		"""
        pass
