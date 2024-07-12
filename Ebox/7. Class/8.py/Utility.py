from Employee import Employee
from Developer import Developer
from Manager import Manager

class Utility :
	@staticmethod
	def print_employees_under_each_manager(manager_list):
		for i in manager_list:
			print(f"Manager Name:{i._name}")
			print("Employee List:")
			j = None
			for j in range(len(i._employees)):
				print(i._employees[j]._name,end=" ")
			if(j==None):
				print("None")
			print()
			print()
		
			