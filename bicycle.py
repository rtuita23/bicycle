class Bicycle:    # Create Bicycle class 
    def __init__(self, modelName, weight, cost):    # Constructor w/ 3 parameters
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
        
    def __str__(self):    # Return the parameters
        return {'model':self.modelName, 'weight': self.weight, 'cost':self.cost}
        
class Bike_Shop():    # Create a Bicycle Shop class which derives from Bicycle Class
    def __init__(self, name, inventory):    # Constructor w/ 2 parameters
        self.name = name
        self.inventory = inventory
    
    def __str__(self):    # Return the parameters for print
        return 'Name of store is: ' + self.name + '\n' + \
               'Inventory is: ' + str(self.inventory) + '\n'
                
    '''
    def price(self):    # Compute sales price per bike
        selling_price = 0
        for bike in self.inventory:
            for i in bike:
                if i == 'cost':
                    selling_price += int(self.inventory[i]) + int((self.inventory[i]))*.20
        return selling_price
    '''
    
    def profit(self):    # Compute profit margin for all sales
        return self.price() - self.cost
    
class Customer:    # Create a Customer class
    def __init__(self, name, fund): # Get name and fund of customers
        self.name = name
        self.fund = fund
    
    def __str__(self):
        return 'Customer Name: '+ self.name + '\n' + \
               'Fund Amount: ' + str(self.fund)
    
