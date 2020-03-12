class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getPrice(self):
        return self.price
    
    def setPrice(self, new_price):
        self.price = new_price
    
    def getName(self):
        return self.name
    
    def setName(self, new_name):
        self.name = new_name

