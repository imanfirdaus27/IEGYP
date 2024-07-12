
try:
    x = input("Enter number 1\n")
    y = input("Enter number 2\n")
    
    result = int(x) / int(y)
    print(result)

except ZeroDivisionError:
    print("Divide By Zero Error")

except ValueError:
    print("Invalid Value")
   