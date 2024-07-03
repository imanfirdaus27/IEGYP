# Multiple Inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card Class")
    
class AtmCard (Card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("Inside AtmCard Class")

class CreditCard (Card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("Inside CreditCard Class")

class DebitCard (Card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("Inside DebitCard Class")

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        # print("Inside BankCard Class")
        super().doSomething()

# we have created 5 classes
# and in all 5 classes we have doSomething method
# and it is implemented (got code inside which is "print")

# Let us create instance of last card
bankCard = BankCard()
bankCard.doSomething()
# now remove the print statement from bankcard.doSomething
# and call the super().dosomething
# this time you will see inside AtmCardClass (Which is first inherited class)

# now comment the dosomething method which is inside the AtmCard Class

# this time you will inside credit card class

# and so on

# Basically what we understand here is 
# pythin scan from left to right and identify the base classes
# and call the method accodingly
# This process is call method resolution order(MRO)
print(BankCard.__mro__)

# (<class '__main__.BankCard'>, 
# <class '__main__.AtmCard'>, 
# <class '__main__.CreditCard'>, 
# <class '__main__.DebitCard'>, 
# <class '__main__.Card'>, 
# <class 'object'>)

# BIGGEST CONCLUSISON:
# Every class we create in python is inherited from a class called object
# class object:
#    def __init__():
#       pass
#    def __str__():
#       print(memory address)


# Every class is extended from the object so means when looking at a class called object they will return the address location 
# object class is by default

# class object:
#   def __init__():
#       pass
#   def __str__():
#       return memory address

class Student(object): 
    pass
    # def __str__(self):
    #     return "Student"

class Alumni(Student):
    pass
    # def __str__(self):
    #     return "Alumni"

alumni = Alumni() # create object for Alumni
print(alumni) # print looking for __str #print will be looking

# Hope you guys still remember this
# Iterator object like enumerator, range, map, filter do not override
# the method __str__
# However those classes are inherited from the default python class
# claeed object which has the method __str__ which 
# returns the address location of the object
# Finally that gets printed using print function

class object:
    def __str__(self):
        return "Address"
class range(object):
    pass
myrange = range()
print(myrange) # print will be looking for __str__ method in range class

# What if i dont want my class to inherit from the base from the base called object
# Definitely you dont want to do this because
# you will loose all the default feature of a class

class myclass:
    pass

# myclass().will list more methods
# now we understad those methods are coming the base class called object

# no i insist i dont want my class to be inherited
class noObjectClass():
    pass

test = noObjectClass()
print(test)
