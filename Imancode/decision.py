# find whether the given number is positive, negative or zero
# find whether my business is making profit, loss or breakeven

expenses = 1000
sales = 1100

# Objective: please print only when we have profit
if (sales > expenses):
    # this is called block
    # "block" means one or more than one statements to be executed
    print("You are making profit")

print("The END")


# Objective 2: Please print when we have profit or loss
if (sales > expenses):
    print("You are making profit")
else:
    print("You are making loss")
print("The END")

# Objective 3: Please print when we have profit or loss or breakeven
if (sales > expenses):
    print("You are making profit")
else:
    if (sales == expenses):
        print("You are at breakeven")
    else:
         print("You are making losses")

print("The END")

#elif method
if (sales > expenses):
    print("You are making profit")
elif (sales == expenses):
    print("You are at breakeven")
else:
    print("You are making losses")

print("The END")