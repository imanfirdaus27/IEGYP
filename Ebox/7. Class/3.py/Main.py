from Person import Person
from Address import Address

person_name = input("Enter name\n")
person_age = input("Enter age\n")
print("Enter address")
street = input("Enter street\n")
city = input("Enter city\n")
state = input("Enter state\n")
person_address = Address(street,city,state)
person = Person(person_name, person_age,person_address)
print("Person Details")
print(person)