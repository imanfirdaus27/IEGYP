# Find whether the given number is positive, negative or zero
# Find whether my business is making profit, loss or breakeven

expenses = 1000
sales = 1100

# Objective 1: please print only when we have profit
if (sales > expenses):
    # this is called block of code
    # "block" means one or more than one statement to be executed
    print("You are making profit")


# Objective 2: Please print when we have profit and loss
if (sales > expenses):
    print("You are making Profit")
else:
    print("You are making losses")


# Objective 3: Please print when we have profit, loss and breakeven
if (sales > expenses):
    print("You are making Profit")
else:
    if (sales == expenses):
        print("You are at Breakeven")
    else:
        print("You are making losses")

if (sales > expenses):
    print("You are making Profit")
elif (sales == expenses):
    print("You are at Breakeven")
else:
    print("You are making losses")

print("The END")