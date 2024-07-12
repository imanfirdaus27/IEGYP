from Employee import Employee
class Manager(Employee):

    def __init__(self, name, pay, employees=None):
        super().__init__(name,pay)
        if employees is None:
            employees = []
        self._employees = employees
        

    def add_employee(self, emp):
        self._employees.append(emp)

    def remove_employee(self, emp):
        self.employees.remove(emp)

    def __str__(self):
        return f"Manager(Name: {self._name}, Pay: {self._pay}, Employees: {[emp.name for emp in self._employees]})"