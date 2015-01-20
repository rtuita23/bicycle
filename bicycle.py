"""
    BICYCLE CLASS
    TODO - A bicycle has a model name
    TODO - A bicycle has a weight
    TODO - A bicycle has a cost
    TODO - Return as dictionary ()

"""
class Bicycle:
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
    
    def bike(self):
        return {'Model': self.modelName, 'Weight': self.weight, 'Cost': self.cost}
    
"""
    BIKE SHOP CLASS
    TODO - has a name
    TODO - has an inventory of different bicycles
    TODO - can sell bicycles with a margin over their cost
    TODO - Can see how much profit they have made from selling bikes

"""
class Bike_Shop():    
    def __init__(self, name, inventory):    
        self.name = name
        self.inventory = inventory
        
    def __str__(self):
        models = ''
        for bikes in self.inventory:
            for key in bikes.keys():
                if key == 'Model':
                    models += bikes[key] + '\n'       
        return 'Models are: ' + '\n' + str(models)
                    
    
    def price(self):     
        for bikes in self.inventory:
            for key in bikes.keys():
                if key == "Cost":
                    bikes[key] = bikes[key] + bikes[key] * self.margin
        return 'New Pricing: ' + self.inventory
                    
"""

class Customer:    # Create a Customer class
    def __init__(self, name, fund): # Get name and fund of customers
        self.name = name
        self.fund = fund
    
    def __str__(self):
        return 'Customer Name: '+ self.name + '\n' + \
               'Fund Amount: ' + str(self.fund)
"""