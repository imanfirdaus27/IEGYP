class CustomError(Exception):
    def __init__(self,comment):
        self.comment = comment

username = input("Enter the username\n")
password = input("Enter the password\n")

low_case = 0
up_case = 0
num_case = 0

for i in password:
    if i.islower():
        low_case += 1
    elif i.isupper():
        up_case += 1
    elif i.isdigit():
        num_case += 1

try:
    if low_case >= 1 and up_case >= 1 and num_case >=1:
        print(f"Employee Username: {username}\nPassword: {password}")
    else:
        raise CustomError
except:
    print("CustomException: Invalid Password Exception")