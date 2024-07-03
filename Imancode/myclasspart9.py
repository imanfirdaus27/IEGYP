# Method are nothing but functions inside the class
# Methods  take atleast 1 parameter (self)
# This parameter is used by python to pass the instance

class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

mycalculator = calculator(10, 20)
print(mycalculator.add())
print(mycalculator.subtract())


# There is a class
# this like a module # not very popular
# This is called class method
class Utility:

    def addition(x, y):
        return x + y
    
    def subtraction(x, y):
        return x - y
    
    def multiplication(x, y):
        return x * y
    
    def division(x, y):
        return x / y
    
print(Utility.addition(10,20))

#however this can be easily done just using module in python
# no need to create class


class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    
    def getFullname(firstname, lastname):
        return firstname + lastname
    
    def __str__(self):
        return Customer.getFullname(self.firstname, self.lastname)
    
myCustomer = Customer("John", "David")
print(myCustomer)

    