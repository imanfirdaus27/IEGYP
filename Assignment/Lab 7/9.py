# Write a Python class BankAccount with attributes 
# like accountNumber, openingBalance, currentBalance dateOfOpening and customerName. 
# Add methods like deposit, withdraw, and checkBalance.


class BankAccount():

    def __init__(self, accountNumber, openingBalance, currentBalance, dateOfOpening, customerName): #initialize
        self.accountNumber = accountNumber
        self.openingBalance = openingBalance
        self.currentBalance = currentBalance
        self.dateOfOpening = dateOfOpening
        self.customerName = customerName

    def deposit(self, amount):
        self.currentBalance = self.currentBalance + amount
        print(f"Your Deposit:{amount}")
        print(f"Your Current Balance:{self.currentBalance}")

    def withdraw(self, amount):
        self.currentBalance = self.currentBalance - amount
        print(f"Your Withdraw:{amount}")
        print(f"Your Current Balance:{self.currentBalance}")

    def checkBalance(self):
        print(f"Your Current Balance:{self.currentBalance}")

    def __str__(self):
        return (f"Account Number: {self.accountNumber}\n"
                f"Opening Balance: RM {self.openingBalance}\n"
                f"Current Balance: {self.currentBalance}\n"
                f"Date of Opening: {self.dateOfOpening}\n"
                f"Customer Name: {self.customerName}")


    
a =  map(int, input("Enter your account number:").split())
b =  float(input("Enter your opening balance:"))     
c =  float(input("Enter your current balance:"))
d =  map(int, input("Enter date of opening of your account:").split('-'))
e =  input("Enter your name:")

p1 = BankAccount(a, b, c, d, e)

p1.deposit(1000) # access the deposit method
p1.withdraw(500) # access the withdraw method
p1.checkBalance() # access the checkBalance method
print(p1)

# # chatgpt code

class BankAccount:

    def __init__(self, accountNumber, openingBalance, currentBalance, dateOfOpening, customerName):
        self.accountNumber = accountNumber
        self.openingBalance = openingBalance
        self.currentBalance = currentBalance
        self.dateOfOpening = dateOfOpening
        self.customerName = customerName

    def deposit(self, amount):
        self.currentBalance += amount
        print(f"Your Deposit: {amount}")
        print(f"Your Current Balance: {self.currentBalance}")

    def withdraw(self, amount):
        self.currentBalance -= amount
        print(f"Your Withdraw: {amount}")
        print(f"Your Current Balance: {self.currentBalance}")

    def checkBalance(self):
        print(f"Your Current Balance: {self.currentBalance}")

    def __str__(self):
        return (f"Account Number: {self.accountNumber}\n"
                f"Opening Balance: RM {self.openingBalance}\n"
                f"Current Balance: {self.currentBalance}\n"
                f"Date of Opening: {self.dateOfOpening}\n"
                f"Customer Name: {self.customerName}")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid float.")

def get_date_input(prompt):
    while True:
        date = input(prompt)
        try:
            # Check if date is in the format dd-mm-yyyy
            day, month, year = map(int, date.split('-'))
            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                return date
            else:
                print("Invalid date. Please enter a date in the format dd-mm-yyyy.")
        except ValueError:
            print("Invalid date format. Please enter a date in the format dd-mm-yyyy.")

def get_string_input(prompt):
    return input(prompt)

# Get user input
account_number = get_int_input("Enter your account number: ")
opening_balance = get_float_input("Enter your opening balance: ")
current_balance = get_float_input("Enter your current balance: ")
date_of_opening = get_date_input("Enter date of opening of your account (dd-mm-yyyy): ")
customer_name = get_string_input("Enter your name: ")

# Create BankAccount object
p1 = BankAccount(account_number, opening_balance, current_balance, date_of_opening, customer_name)

# Access methods
p1.deposit(1000)
p1.withdraw(500)
p1.checkBalance()
print(p1)

# 
