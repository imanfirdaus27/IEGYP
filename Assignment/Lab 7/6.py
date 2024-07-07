# Write a Python class that has two methods: 
# getString and printString , The getString accept 
# a string from the user and printString prints 
# the string in upper case.

class String():

    def __init__(self):
        self.userinput = ""
    
    def getString(self):
        self.userinput = input("Please provide your input:")

    def printString(self):
        print(f"The user input is:{self.userinput.upper()}")

s = String() #create an instance
s.getString()
s.printString()



    

