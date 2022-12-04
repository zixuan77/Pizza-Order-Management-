# test Pizza
from PizzaOrder import PizzaOrder
from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException

def testpizzaconstruction():
    pizza1 = Pizza("S")
    assert pizza1.getSize() == "S"
    assert pizza1.getPrice() == 0.0


def testpizzaset():
    pizza1 = Pizza("S")
    pizza1.setPrice(8.50)
    pizza1.setSize("M")
    assert pizza1.getPrice() == 8.50
    assert pizza1.getSize() == "M"

    pizza2 = Pizza("M")
    pizza2.setPrice(10.00)
    pizza2.setSize("L")
    assert pizza2.getPrice() == 10.00
    assert pizza2.getSize() == "L"

# test custompizza
def test_cpaddtopping():
    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    assert cp2.getPrice() == 13.00
    cp2.addTopping("bacon")
    assert cp2.getPrice() == 14.00
    assert cp2.getSize() == "L"


def test_custompizzaconstruction():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n"
    
    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    cp2.addTopping("bacon")
    assert cp2.getPizzaDetails() == \
        "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ bacon\nPrice: $14.00\n"

# test specialtypizza

def test_spgetdetails():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n"
    
    sp2 = SpecialtyPizza("M", "Best-one")
    assert sp2.getPizzaDetails() == "SPECIALTY PIZZA\nSize: M\nName: Best-one\nPrice: $14.00\n"

# test pizzaorder

def test_pizzaorder():

    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    sp2 = SpecialtyPizza("M", "Best-one")
    order1 = PizzaOrder(123000)
    order1.addPizza(cp1)
    order1.addPizza(sp1)

    order2 = PizzaOrder(113000)
    order2.addPizza(sp2)

    assert order1.getTime() == 123000
    assert order2.getTime() == 113000
    

    assert order1.getOrderDescription() == \
    "******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\n\
SPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n"

    assert order2.getOrderDescription() == "******\nOrder Time: 113000\nSPECIALTY PIZZA\nSize: M\nName: Best-one\nPrice: $14.00\n\n----\nTOTAL ORDER PRICE: $14.00\n******\n"


# test orderqueue
def test_orderqueue():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    sp2 = SpecialtyPizza("M", "Best-one")
    order1 = PizzaOrder(123000) #12:30:00PM
    order1.addPizza(cp1)
    order1.addPizza(sp1)

    order2 = PizzaOrder(90500)
    order2.addPizza(sp1)
    order2.addPizza(sp2)

    order3 = PizzaOrder(100000)
    order3.addPizza(cp1)
    order3.addPizza(sp2)

    oq = OrderQueue()
    oq.addOrder(order1)
    oq.addOrder(order2)
    oq.addOrder(order3)

    assert oq.processNextOrder() == \
        "******\n\
Order Time: 90500\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Best-one\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.00\n\
******\n"
    assert oq.processNextOrder() == \
        "******\n\
Order Time: 100000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Best-one\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $23.00\n\
******\n"

 


