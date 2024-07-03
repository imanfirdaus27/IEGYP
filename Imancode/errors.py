x = 10

# if (x% 2 == 0):
# print("x is even")

# logical error
# if (x % 2 == 0):
#     print(f"Given Number is {x}")
# print("Even Number")

# runtime error

# we know the following line is taking user input

try:
    principle = int(input("Principle: "))

except ValueError:
    # when that error occur what we must do
    print("Principle amount must be an Integer")

except Exception as e:
    print("Something went wrong:", e)
else:
    # if there is no error then this block will execute
    print("All is well")
finally:
    # The code inside this block will always executed
    print("Thank You")


period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * period * rate) / 100
print("Interest Amount:", interest)






