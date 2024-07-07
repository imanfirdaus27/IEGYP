def Strings(x,y):
    
    if x[0] == y[0]:
        c = x + " " + y
        print(c)
    else:
        print("Invalid Input")

x = input("Enter the first string:")   
y = input("Enter the second string:")

Strings(x,y)