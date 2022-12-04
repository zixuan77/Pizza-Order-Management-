from SpecialtyPizza import SpecialtyPizza
from CustomPizza import CustomPizza
from Pizza import Pizza
class PizzaOrder:
    def __init__(self, time):
        self.pizzalist = []
        self.time = time
    
    def setTime(self, time):
        self.time = time
    
    def getTime(self):
        return self.time
    
    def addPizza(self, pizza):
        self.pizzalist.append(pizza)
    
    def getOrderDescription(self):
        orderprice = 0.0
        count = 0
        while count < len(self.pizzalist):
            orderprice += self.pizzalist[count].getPrice()
            count += 1

        output = "******\nOrder Time: {}\n".format(self.time)
        npizza = 0
        while npizza < len(self.pizzalist):
            output += self.pizzalist[npizza].getPizzaDetails()
            output += "\n----\n"
            npizza += 1
        
        output += "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(orderprice)
        return output




