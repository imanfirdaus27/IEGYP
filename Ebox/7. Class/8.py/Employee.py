class Employee:

    def __init__(self, name, pay) :
        self._name = name
        self._pay = pay
        self._email = self._name+".@gmail.com"
        
    @property #The @property decorator is applied to a method to define a getter method. This allows you to access the value using the method name as if it were an attribute.
    def name(self) :
    	return self._name
    
    @name.setter
    def name(self, value) :
        self._name = value
	
    def __str__(self) : 
        return self._name