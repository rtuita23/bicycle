class Bicycle:    # Create Bicycle class 
    def __init__(self, modelName, weight, cost):    # Constructor w/ 3 parameters
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
        
    def __str__(self):    # Return the parameters for print
        return self.modelName + ' ' + self.weight + ' ' + str(self.cost)
    
class Shop(Bicycle):    # Create a Bicycle Shop class which derives from Bicycle Class
    def __init__(self, name, modelName, weight, cost):    # Constructor w/ 4 parameters
        Bicycle.__init__(self, modelName, weight, cost)    # Inherit inventory from Bicycle Class
        self.name = name
        
    def __str__(self):    # Return the parameters for print
        return self.name + ' ' + self.modelName + ' ' + self.weight + ' ' + self.cost
    
    def price(self):    # Compute sales price per bike
        selling_price = 0
        self.selling_price = self.cost + (self.cost*.20)
        return self.selling_price 
    
    def profit(self):    # Compute profit margin for all sales
        return price() - self.cost
    
class Customer:    # Create a Customer class
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    
    def __str__(self):
        return self.name + ' ' + str(self.fund)
    

cus1 = Customer('Paul', 200)
cus2 = Customer('Peter', 500)
cus3 = Customer('Jane', 1000)

print str(cus1) + '\n' + str(cus2) + '\n' + str(cus3)

        