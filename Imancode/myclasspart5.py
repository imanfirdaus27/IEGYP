# Is- A Relationship
# Alumni is a student
class Student:

    def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
            self.icnumber = ""

# Alumni extends Student class
class Alumni(Student): 
      
      def __init__(self, firstname, lastname, alumninumber):
        # Static calling
        # Student.__init__(self, firstname, lastname) # another teknik #create the parent inside the object
        # to create the parent object inside the child object
        # you can use super class
        # which will return the object of parent class
        # another method, you can use the keyword super
        super().__init__(firstname, lastname)
        self.alumninumber = alumninumber
      
      def __str__(self):
           return f"First Name: {self.firstname} \
                \nLast Name: {self.lastname} \
                \nIC Number: {self.icnumber} \
                \nAlumni Number: {self.alumninumber}"


# we have create and object of Alumni class
alumni = Alumni("Parker", "Peter", 97409) # child object
print(alumni)

