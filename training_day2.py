# wap to create a class bank accounts with deposite and withdraw methods

class bankAccounts:
    def __init__(self, amount):
        self.balance = amount
    def deposite(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def checkBalance(self):
        print(self.balance)
        
Account1 = bankAccounts(1000)
Account1.checkBalance()
Account1.deposite(5000)
Account1.checkBalance()
Account1.withdraw(3000)
Account1.checkBalance()
        
# wap to create a class car with brand and speed attributes and add a method to display the details

class car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def display(self):
        print("brand = ",self.brand,"\nspeed = ",self.speed)
        
WagonR = car("Maruti_Sezuki", 160)
WagonR.display()
Asta = car("hyundai", 140)
Asta.display()

        
# create classes vehicles, cars and electric cars in a multi level manner add one methode in which class calls all te methods using electric cars

class vehicles:
    def __init__(self, noOfTtires, fuelType):
        self.noOfTires = noOfTtires
        self.fuelType = fuelType
    def display(self):
        print("no. of tires = ",self.noOfTires,"\nfuel type = ",self.fuelType)
        
class cars(vehicles):
    def __init__(self, noOfTtires, fuelType, color, model, brand, milage):
        super().__init__(noOfTtires, fuelType)
        self.color = color
        self.model = model
        self.brand = brand
        self.milage = milage
        
    def display(self):
        super().display()
        print("color = ",self.color,"\nmodel = ",self.model,"\nbrand = ",self.brand,"\nmilage = ",self.milage,)

class electricCars(cars):
    def __init__(self, noOfTtires, fuelType, color, model, brand, milage, softwareVersion):
        super().__init__(noOfTtires, fuelType, color, model, brand, milage)
        self.softwareVersion = softwareVersion
    
    def display(self):
        super().display()
        print("software version = ",self.softwareVersion)
     
     
Vehicle1 = vehicles(3, "petrol")   
car1 = cars(4, "petrol", "red", "wagonR", "Maruti Sizuki", 100)
electricCar1 = electricCars(4, "electric", "blue", "BE6", "Mahendra", 80, 10.77)

print("details of vehicle 1")
Vehicle1.display()
print("---------------------------")
print("details of car 1")
car1.display()
print("---------------------------")
print("details of electric car 1")
electricCar1.display()

# wap to add an element to a set 
s = {"hello", 5, 8, 10, "world"}
n = input("write element to add : ")
s.add(n)
print(s)

# wap to remove an element to a set 
n = input("enter the element to remove : ")
s.remove(n)
print(s)

# wap to find union of 2 sets
l = {"hello", 4, 7, 9, "why"}
print(s|l)
print(s.union(l))

# wap to find intersection of 2 sets 
print(s&l)
print(s.intersection(l))

# wap  to find difference of 2 sets
print(s-l)
print(s.difference(l))

# wap to access a value by key
dict = {"green":"go","yellow":"ready","red":"stop"}
n = input("enter the key : ")
print(dict[n])

# wap to print dictionary keys and values using loop
print("full dictionary = ",dict.items())
print("values = ",dict.values())
print("keys = ",dict.keys())

# wap to count how many times an element appears in tuple
tup = ("hello", 5, 8, 11, "archit", 11, 5, 8, 11, 11, 11)
print("number of 11's = ",tup.count(11))
print("number of 5's = ",tup.count(5))

# wap to find the length of the tuple
a = ("hello", 5, 8, 10, "world")
print(len(a))

# wap to check if a number is even or odd using function
def iseven(n):
    print("even") if n%2==0 else print("odd")
    
iseven(5)
iseven(4)
iseven(2)
iseven(7)

# wap to function to return the multiplication table
def table(n):
    for i in range(1,11):
        print(n," X ",i," = ",n*i)
        
table(5)
table(10)
