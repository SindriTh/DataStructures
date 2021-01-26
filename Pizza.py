#   
#   
class Pizza(object):
    identifier = 0 
    def __init__(self,topping1= None, topping2 = None, topping3 = None):
        self.id = Pizza.identifier
        Pizza.identifier += 1
        self.served = False
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3

    def __str__(self):
        return str(self.id)

class PizzaOrders(object):
    identifier = 0 
    def __init__(self):
        self.listi = []
    
    def addpizza(self,topping1= None, topping2 = None, topping3 = None):
        self.listi.append(Pizza(topping1, topping2, topping3))
    
    def markserved(self,number):
        for pizza in self.listi:
            if pizza.id == number:
                pizza.served = True

    def removeserved(self):
        for pizza in self.listi:
            if pizza.served == True:
                self.listi.remove(pizza)
    def getids(self):
        return self.listi

    def getza(self):
        print(f"Pizza ID  Served?  Topping 1    Topping 2    Topping 3")
        print("-------------------------------------------------------")
        for pizza in self.listi:
            print(f"{pizza.id:3}       {self.isserved(pizza):5}    {pizza.topping1:10}   {pizza.topping2:10}   {pizza.topping3:10}")
        #return outstring

    def isserved(self,pizza):
        if pizza.served == 0:
            return "No"
        return "Yes"


orders = PizzaOrders()
for i in range(0,150):
     orders.addpizza("banani","avacaidi",f"Tomati{i}")

orders.markserved(3)
orders.removeserved()
orders.markserved(5)
print(orders.getza())

