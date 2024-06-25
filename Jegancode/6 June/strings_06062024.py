firstname = "Khairi"
lastname = "Abu Bakar"
# + is arithmatic operator used for addition
# to perform addition both side of + must be integer or float

# however if both sides are string then python performs
# string concatenation
fullname = firstname + " " + lastname #Khairi Abu Bakar
fullname1 = firstname + lastname #KhairiAbu Bakar
print(fullname1)

carplate = "JCG"
number = 9876
# in this case one is string (JCG) another one is number (9876)
# python does not know whether to perform addition or 
# string concatenation

# I can only concatenate str (not "int") to str
# JCG cannot be converted to number 
# 9876 can be converted to string
# we use the buit in function str to convert
carplatenumber = carplate + str(number)
print(carplatenumber)

# we also know * means multiplication
# how can we use * over string data
product = "book"
# when you multiply string with integer then the * becomes times operator
print(product * 5)
print("=" * 50)