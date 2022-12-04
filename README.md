# Pizza-Order-Management-


The goal for this lab is to write a program that will manage incoming pizza orders. All pizza orders have an associated time representing when the customer expects to have their pizza ready (it’s possible for a customer to call ahead and schedule a later pickup time). All pizza orders will be managed by a MinHeap where the next order to prepare is the one that is the earliest compared to the other orders.

In order to manage pizza orders for this lab, you will design various Pizza classes (Pizza, CustomPizza, and SpecialtyPizza that utilizes inheritance / polymorphism), a PizzaOrder class representing a collection of Pizzas a customer wants to place in a single order, and an OrderQueue class that organizes the Pizza orders in a MinHeap data structure.


Pizza.py - Defines a Pizza class representing commonality for all Pizzas. For simplicity, this class will assume all Pizzas have a size and price

CustomPizza.py - Defines a child class of Pizza. This class should inherit all fields / methods from the Pizza class, but also introduces the concepts of toppings a customer can order(represented as a list of strings)

SpecialtyPizza.py - Defines a child class of Pizza. This class should inherit all fields / methods from the Pizza class. Specialty pizzas are defined by a name attribute and all have a set price depending on the pizza size

PizzaOrder.py - Defines a class that is a collection of pizza objects the customer wants to order. The total price for the order can be derived from each individual pizza price. This class will also have an expected time of when the customer would like their pizzas ready for pickup. More details on this later in the writeup

OrderQueue.py - Defines a MinHeap to organize and process Pizza Orders according to their expected time of pickup. You can adapt the Heap implementation shown in the textbook supporting the specifications in this lab.

testFile.py - This file will contain your pytest functions that tests the overall correctness of your class definitions
