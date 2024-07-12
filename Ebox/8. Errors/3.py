class NotEligibleException(Exception):
    pass

class Student():
    def __init__(self, marks):
        self.marks = marks

        
    def checkmarks(self):
        if marks>= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")

try:
    marks = int(input("Enter marks of student\n"))

    s = Student.checkmarks(marks)

    if s == True:
        print("Eligible")

except NotEligibleException as e:
    print(e)