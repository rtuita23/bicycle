class Bicycle:    # Create Bicycle class 
    def __init__(self, modelName, weight, cost):    # Constructor w/ 3 parameters
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
        
    def __str__(self):    # Return the parameters for print
        return self.modelName + ' ' + self.weight + ' ' + str(self.cost)
    
class Shop(Bicycle):    # Create a Bicycle Shop class which derives from Bicycle Class
    stock = []
    def __init__(self, modelName, weight, cost, name):    # Constructor w/ 4 parameters
        Bicycle.__init__(self, modelName, weight, cost)    # Inherit inventory from Bicycle Class
        self.name = name
    
    def __str__(self):    # Return the parameters for print
        retStr = 'Name of store is ' + self.name + '\n'
        retStr += 'Inventory is ' + str(self.inventory())
        return retStr
    
    def inventory(self):
        self.stock.append([self.modelName, self.weight, self.cost])
        return self.stock
        
    def price(self):    # Compute sales price per bike
        selling_price = 0
        self.selling_price = self.cost + (self.cost*.20)
        return self.selling_price 
    
    def profit(self):    # Compute profit margin for all sales
        return self.price() - self.cost
    
class Customer:    # Create a Customer class
    def __init__(self, name, fund): # Get name and fund of customers
        self.name = name
        self.fund = fund
    
    def __str__(self):
        return self.name + ' ' + str(self.fund)      
    
