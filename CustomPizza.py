from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        if self.size == "S":
            self.setPrice(8.00)
        elif self.size == "M":
            self.setPrice(10.00)
        else:
            self.setPrice(12.00)
        self.alist = []

    def addTopping(self, topping):
        self.alist.append(topping)

        tprice = 0.0
        if self.size == "S":
            tprice = 0.5

        elif self.size == "M":
            tprice = 0.75

        else:
            tprice = 1.00

        
        self.price += tprice
        
    
        
    def getPizzaDetails(self):
        
        output = ""
        if len(self.alist) == 0:
            output += "CUSTOM PIZZA\nSize: {}\nToppings:\nPrice: ${:.2f}\n".format(self.size, self.price)
        else:
            output += "CUSTOM PIZZA\nSize: {}\nToppings:\n".format(self.size)
            ntop = 0
            while ntop < len(self.alist):
                output += "\t+ {}\n".format(self.alist[ntop])
                ntop += 1
            
            output += "Price: ${:.2f}\n".format(self.price)

        return output
