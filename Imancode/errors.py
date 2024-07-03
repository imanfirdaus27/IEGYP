x = 10

# if (x% 2 == 0):
# print("x is even")

# logical error
# if (x % 2 ==0):
#     print(f"Given Number is {x}")
# print("Even Number")

# runtime error

# we know the following line is taking user input

try:
    principle = int(input("Principle: "))
    period = int(input("Period: "))
    rate = int(input("Rate: "))
    interest = (principle * period * rate) / 100
    print("Interest Amount:", interest)
except:
    # when that error occur what we must do
    print("Principle amount must be an Integer")






