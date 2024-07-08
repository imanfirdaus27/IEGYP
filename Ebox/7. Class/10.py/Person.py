class Person:
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} is {self.__age} years old and her email id is {self.__first_name}.{self.__last_name}@gmail.com"

    def fullname(self):return f"{self.__first_name} {self.__last_name}"