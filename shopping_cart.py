class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        # creating the shopping cart class
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.totalPrice = 0.0
    
    def addItem(self, item):
        self.items.append(item)
        self.totalPrice += item.price
    
    def removeItem(self, item):
        self.items.remove(item)
        self.totalPrice -= item.price
    
    def getTotalPrice(self):
        return self.totalPrice
