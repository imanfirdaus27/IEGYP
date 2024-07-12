class InvalidAgeRangeException(Exception):
    pass

class Vote():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
    def checkage(self):
        if age >= 18:
            return name, age
        else:
            raise InvalidAgeRangeException("InvalidAgeRangeException")

try:
    name = (input("Enter the name\n"))
    age = int(input("Enter the age\n"))

    voter = Vote(name,age)
    isvalidAge = voter.checkage()

    if isvalidAge:
        print(f"Voter name:{name}\nVoter age:{age}")

except InvalidAgeRangeException as e:
    print("CustomException:",e)   

# Hanafi code
# class CustomError(Exception):
#     pass


# def vote(name, age):
#     print(f"Voter name: {name}")
#     print(f"Voter age: {age}")


# try:
#     name = input("Enter the Name\n")
#     age = int(input("Enter the age\n"))

#     if age < 18:
#         raise CustomError("CustomException: InvalidAgeRangeException")

#     vote(name, age)
# except CustomError as e:
#     error_message = str(e)
#     print(error_message)