# Encapsulation (membungkus)
# Encapsulate the properties inside the class
# in other languageswe have keywords public, private, protected
# to protect the properties

class circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14
    
    def circumference(self):
        return self.radius * 2 * 3.14
    

mycircle = circle(20)





