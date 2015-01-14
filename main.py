import bicycle as bp

def main():
    # Intianting the bicycle objects
    bic1 = bp.Bicycle('bmx', '50kg', 150)
    bic2 = bp.Bicycle('dmx', '50kg', 250)
    bic3 = bp.Bicycle('vmx', '50kg', 450)
    
    bike_inventory = [bic1, bic2, bic3]
    
    for i in bike_inventory:
        print i

    
    #print str(bic1) + '\n' + str(bic2) + '\n' + str(bic3) + '\n'
    
    # Intianting the shop objects
    bshop = Shop(bike_inventory)

    cus1 = bp.Customer('Paul', 200)
    cus2 = bp.Customer('Peter', 500)
    cus3 = bp.Customer('Jane', 1000)

    print str(cus1) + '\n' + str(cus2) + '\n' + str(cus3)

if __name__ =="__main__":
    main()
 