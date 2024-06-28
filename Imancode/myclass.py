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

    def __init__(self):
        print("Object is created")

    # this is our first method/function inside the class student
    # remember methods must have atleast 1 parameter

    def attendClass(self):
        print("Object started attending class")

    def doProject(self, projectname):
        print("Object started doing the project", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam: {exam} and obtained the score {grade}"


#create first object for class
zul = Student()
# how to invoke/call the method
zul.attendClass()
# pass value to 2nd parameter
zul.doProject("Pokemon")
# return something
print(zul.attendExam("python 102"))


