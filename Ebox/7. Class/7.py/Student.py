class Student:
    def __init__(self,__id,__username,__password,__name,__address,__city,__pincode,__contact_number,__email):
        self.__id = __id
        self.__username = __username
        self.__password = __password
        self.__name = __name
        self.__address = __address
        self.__city = __city
        self.__pincode = __pincode
        self.__contact_number = __contact_number
        self.__email = __email

    def __str__(self):
        return f"Id:{self.__id}\nUser Name : {self.__username}\nPassword : {self.__password}\nName : {self.__name}\nAddress : {self.__address}\ncity : {self.__city}\nPincode : {self.__pincode}\nContact Number : {self.__contact_number}\nemail : {self.__email}"