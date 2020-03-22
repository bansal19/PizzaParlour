from OrderDistribution import OrderDistribution


class InHouseDelivery(OrderDistribution):
    """
    Class represents the InHouseDelivery system of the Pizza Parlour.
    """
    def __init__(self, delivery_address):
        self.delivery_address = delivery_address
        self.delivered = False

    def set_adrress(self, new_address):
        """
        param: new_address - The new address that this order needs to be sent to
        return: void
        """
        self.delivery_address = new_address

    def get_address(self):
        """
        Return the address of the delivery of the Pizza Parlour
        """
        return self.delivery_address

    def is_delivered(self):
        """
        The order has been delivered, so set the delivered to true
        """
        self.delivered = True