from Employee import Employee

class Developer(Employee):
    
    def __init__(self, name, pay, prog_lang) :
        super().__init__(name, pay)
        self.prog_lang = prog_lang
        
    def __str__(self) :
        return self._name