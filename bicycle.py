class Bicycle:
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
        
    def __str__(self):
        return self.modelName + ' ' + self.weight + ' ' + str(self.cost)
    
class Shop:
    stock = ['a', 'b', 'c', 'd', 'e', 'f']
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def sell(self):
        selling_price = 0
        self.selling_price = self.cost + (self.cost*.20)
        return self.selling_price 
    
    def profit(self):
        return sell() - self.cost
    
class Customer:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    
    def __str__(self):
        return self.name + ' ' + str(self.fund)

cus1 = Customer('Paul', 200)
cus2 = Customer('Peter', 500)
cus3 = Customer('Jane', 1000)

print str(cus1) + '\n' + str(cus2) + '\n' + str(cus3)

        