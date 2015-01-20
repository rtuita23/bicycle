import bicycle as bp

def main():
    # Instatiating the Bicycle objects
    
    bmx = bp.Bicycle('BMX', 50, 400)
    downhill = bp.Bicycle('Downhill', 50, 100)
    freeride = bp.Bicycle('Free Ride', 60, 300)
    allmountain = bp.Bicycle('All Mountain', 70, 350)
    hardtail = bp.Bicycle('Hard Tail', 76, 400)
    dirtjump = bp.Bicycle('Dirt Jump', 85, 500)
    
    bikes = [bmx.bike(), downhill.bike(), freeride.bike(), allmountain.bike(), hardtail.bike(), dirtjump.bike()]
                    
    ''' Instantiating one Bike Shop '''
    
    shop = (bp.Bike_Shop('First Bicycle Store', bikes))
    print str(shop)
    
    
    """
    # Instantiating 3 customers with budgets
    
    cust1 = bp.Customer("Bob Jones", 300)
    cust2 = bp.Customer("David Smith", 450)
    cust3 = bp.Customer("Peter Duke", 500)
    
    print str(cust1) + '\n' + str(cust2) + '\n' + str(cust3) + '\n'
    """ 
if __name__ =="__main__":
    main()
   