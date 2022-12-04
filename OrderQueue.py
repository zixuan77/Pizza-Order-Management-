from PizzaOrder import PizzaOrder
from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class OrderQueue():
    def __init__(self):
        self.orderlist = [0]
        self.currentsize = 0
    
    def addOrder(self, pizzaOrder):
        self.orderlist.append(pizzaOrder)
        self.currentsize += 1
        self.perkUp(self.currentsize)
    
    def perkUp(self, i):
        while i//2 > 0:
            if self.orderlist[i].getTime() < self.orderlist[i // 2].getTime():
                temp = self.orderlist[i //2]
                self.orderlist[i//2] = self.orderlist[i]
                self.orderlist[i] = temp
            i = i//2
        
    def processNextOrder(self):
        if self.currentsize == 0:
            raise QueueEmptyException()
        orderremoved = self.orderlist[1]
        self.orderlist[1] = self.orderlist[self.currentsize]
        self.currentsize -= 1
        self.orderlist.pop()
        self.perkDown(1)
        return orderremoved.getOrderDescription()

    def perkDown(self, i):
        while i * 2 <= self.currentsize:
            minchild = self.minChild(i)
            if self.orderlist[i].getTime() > self.orderlist[minchild].getTime():
                temp = self.orderlist[minchild]
                self.orderlist[minchild] = self.orderlist[i]
                self.orderlist[i] = temp
            i = minchild
    
    def minChild(self,i):
        if i * 2 + 1 > self.currentsize:
            return i*2
        else:
            if self.orderlist[i*2].getTime() < self.orderlist[i*2+1].getTime():
                return i * 2
            else:
                return i *2 +1


    
class QueueEmptyException(Exception):
    pass
