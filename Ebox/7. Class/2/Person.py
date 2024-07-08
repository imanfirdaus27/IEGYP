class Person:
	def __init__(self,name, age):
		self.__name = name
		self.__age = age
		
	@classmethod
	def from_string(cls, person_str):
		name, age = map(str, person_str.split(','))
		return f"{name} is {age} years old"
		
	def __str__(self):
		return f"{self.__name}\n{self.__age}"