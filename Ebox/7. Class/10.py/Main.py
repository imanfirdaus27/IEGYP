from Person import Person

person_first_name = input("Enter first name\n")
person_last_name = input("Enter last name\n")
person_age = input("Enter age\n")
person = Person(person_first_name, person_last_name, person_age)
print("Full name of the person is",person.fullname())
print("Person Details")
print(person)
	