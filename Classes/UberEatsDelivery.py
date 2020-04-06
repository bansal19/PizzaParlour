from OrderDistribution import OrderDistribution
import json


class UberEatsDelivery(OrderDistribution):
    """
    Implements the abstract class that is Order Distribution.

    Defines the Uber Eats delivery of Pizza Parlour. Assuming all input is from JSON and not CSV
    The JSON input should look like:

    {
        "address": 5 Hoskin Avenue, Toronto",
        "order": ["medium Margherita", "onions", "tomatoes", "water"]
        "order number": 19
    }
    """

    def __init__(self, json_filename):
        """
        Initialise values here based on the json_filename
        """
        try:
            with open(json_filename, "r") as f:
                data = json.load(f)
                self.jsonFile = json_filename
                self.address = data["address"]
                self.orderDetails = data["order"]
                self.orderNum = data["order number"]
            self.delivered = False
        except IOError:
            print("IOError, could not read the UberEats file")

    def set_address(self, new_address):
        """
        Change the address of the order to new_address
        """
        self.address = new_address

    def get_address(self):
        """
        Obtain the address from the file that we just read
        """
        try:
            with open(self.jsonFilem, "r") as f:
                data = json.load(f)
                self.address = data["address"]
                return self.address

        except IOError:
            print("Could not open UberEats JSON file")

    def is_delivered(self):
        """
        Allows us to know if the order has been delivered or not
        """
        self.delivered = True

