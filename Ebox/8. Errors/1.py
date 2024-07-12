'''
x = int(input("Enter number 1\n"))
y = int(input("Enter number 2\n"))

z = x / y

if z == 0:
    print(f"Divide By Zero Error")

else:
    print(f"{z:.1f}")
'''

try:
    x = int(input("Enter number 1\n"))
    y = int(input("Enter number 2\n"))

    result = x / y
    print(f"{result:.1f}")

except ZeroDivisionError:
    print("Divide By Zero Error")

except ValueError:
    print("Invalid Value")

# Hanafi code

    
# try:
#     x = input("Enter number 1\n")
#     y = input("Enter number 2\n")
    
#     result = int(x) / int(y)
#     print(result)

# except ZeroDivisionError:
#     print("Divide by Zero Error")

# except ValueError:
#     print("Invalid Value")






