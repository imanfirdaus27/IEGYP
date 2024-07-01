# Has-a relathionship
# Customer has-a passport
class Passport:

    def __init__(self, country, passportnumber):
       self.country = country
       self.passportnumber = passportnumber

    def __str__ (self):
        return f"Country:{self.country} \nPassport NUmber: {self.passportnumber}"
           
class Customer:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        # Customes has a passport
        # When you have relathionship with another class then that
        # becomes a property to this class
        self.passport = None # it is no brain ... tengok balik yang no brain and empty brain
    
    def __str__ (self):
        message = f"First Name: {self.firstname}\n"
        message = message + f"Last Name: {self.lastname}\n"
        message = message + f"IC Number: {self.icnumber}\n"
        if(self.passport != None):
            message = message + self.passport.__str__()
        return message

peter = Customer("Parker", "Peter")
passport = Passport("UK", "E0202932")
peter.passport = passport
print(peter)
# now we know how to convert an python object to a dictionary
print(peter.__dict__)

#{'firstname': 'Parker', 'lastname': 'Peter', 'icnumber': '', 'passport': <__main__.Passport object at 0x00000203A31C6F90>}
# json format is like above