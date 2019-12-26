class Computer:

    def __init__(self):
        self.__maxprice = 900 # Declare private variable here
    
    def sell(self):
        print("Computer price is {} ".format(self.__maxprice))
    
    # Change private variable value here
    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

# Change private variable price here
c.setMaxPrice(1000)
c.sell()