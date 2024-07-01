# principle
# period
# rate
# calculatesimpleinterest
# calculatetotalamounttobeprinted

# result = calculatesimpleinterest(principal, period, rate)
# newresult = calculatesimpleinterest(principal, result)

# Class is a blueprint
# which contains variable and functions inside the class
# however the variable in class is property
# functions in class is methods
class Student:

    def __init__(self, firstname, lastname, icnumber):
        # below is the properties
        # properties = parameter
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""

    # this is our first method/function inside the class student
    # remember methods must have atleast 1 parameter

    def attendClass(self):
        print(f"{self.firstname}{self.lastname} started attending class")

    def doProject(self, projectname):
        print("Object started doing the project", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam:{exam} and obtained the score {grade}"
    
    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("IC Number:", self.icnumber)
        for program in self.program:
            print("Program:", program)
        print("Address:")
        print("Street:", self.address["street"])
        print("City:", self.address["city"])
        print("State:", self.address["state"])
        print("Country:", self.address["country"])
        print("Zipcode:", self.address["zipcode"])


    #there is also another special method
    # which returns string value
    #this method will be called whenever you tray to print the object

    def __str__(self):
        return f"""print("First Name:", {self.firstname}
        print("Last Name:", {self.lastname}
        print("IC Number:", {self.icnumber}"""
        

    

# how to set value for the properties
# 1) using constructor (__init__method)

#create first object for class
zul = Student("Ahmad", "Zul", "01002121234")
# how to invoke/call the method
zul.attendClass()
# pass value to 2nd parameter
zul.doProject("Pokemon")
# return something
print(zul.attendExam("python 102"))
 # print info

# how can i access the property of an object

# 2) you can set values to the property directly using the dot operator
zul.program = ["Python", "Data Sciences", "Machine Learning"]
zul.address = {
        "street": "Jalan 1",
        "city": "Kuala Lumpur",
        "state": "Wilayah Persekutuan Kuala Lumpur",
        "country": "Malaysia",
        "zipcode": "50450"
}

zul.info()
# Default behaviour is to print the address location where the object is
# however if we want to override that behaviour we can do that by
# creating a special method __str__
print(zul)
# when we try to print teh object using print function
# if that class has __str__ method it will be executed automatically

# The __str__(self) method in Python is a special method that 
# is used to define a human-readable string representation of 
# an object. When you implement the __str__(self) method in a 
# class, you are essentially telling Python how you want instances 
# of that class to be represented as strings. This can be particularly useful 
# for debugging, logging, or presenting object information in a readable format.