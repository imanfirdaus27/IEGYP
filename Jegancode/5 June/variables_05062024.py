# product is the variable 
# "Television" is the string value/literal
# to differentiate the variables from values we use double quote ""
# or single quote ''
# product = 'Television'
product = "Television" # string
quantity = 2 # integer
price = 1455.25 # float
available = True # True / False (boolean value/literal)
print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", available)

# type is another built in function that tell us what is the
# data type of the variables (dynamically assigned by python)
# ((a + b) * c)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price
print("Total:", total)

# In real world use cases the 10 will not be hard coded
# the 10 is coming from an input device (keyboard)
# So the input value can be a string which needs to be converted
quantity = "10"
print(type(quantity))
price = "1455.55"
# print(quantity * price)

# type casting
# convert one data type to another
# to convert string to integer we have a built in function int
# to convert string to float we have a built in function float
total = int(quantity) *  float(price)
print(total)

