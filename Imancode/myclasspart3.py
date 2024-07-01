# Encapsulation (membungkus)
# Encapsulate the properties inside the class
# in other languageswe have keywords public, private, protected
# to protect the properties

class circle:

    def __init__(self, radius):
        # change the property with single underscore
        # will makes the property private
        self.__radius = 0
        if (isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")

    # getter method and setter method
    # to protect the property with security(to people talk to boss through the security)
    def getRadius(self):
        return self.__radius # to talk to security (tugasnya adalah untuk get the value from yang nak cakap tu)
    
    def setRadius(self, radius): # to talk to security (tugasnya adalah untuk set)
        if (isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")
    
    # property is a class
    # We are calling/invoking the class by passing the method as argument
    # Please notice after getRadius there is no ()
    # the property class returns the property object which is assigned to a variable radius
    # in other words radius is an instance of property class
    
    radius = property(getRadius, setRadius) # property() is actually the class # created new property called radius


    def area(self):
        return self.__radius * self.__radius * 3.14
    
    def circumference(self):
        return self.__radius * 2 * 3.14
    
    def __str__(self): #tengok balik why we use this str
        return f"Radius of this circle is {self.__radius}"
    

mycircle = circle(20)
print(mycircle)

# mycircle.__radius = 30
# please dont use __ in this section
# you are indirectly passing the value 30 to setter method
mycircle.radius = 30
# mycircle._radius will still changed the property so not really private
# doubleunderscore (real private)
print(mycircle)
print(mycircle.area())


# you are indirectly passing the value abc to setter method
mycircle = circle("abc")
print(mycircle)









