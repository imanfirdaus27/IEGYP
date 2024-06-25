'''
firstname = "Khairi"
lastname = "Abu Bakar"
# + is aritmetic operator used for addition
# to perform addition both side of + must be integer or float

# however if both sides are string then python performs
# sting concatenation
fullname = firstname + " " + lastname
print(fullname)

carplate = "JCG"
number = 9876
# in this case one is string (JCG) another one is number (9876)
# python does not know whether to perform addition or
# string concatenation

# I can only concatenate str (not "int") to str
#JCG cannot be converted to number
# 9876 can be converted to a string
# we use the built in function str to convert
carplatenumber = carplate + str(number)
print(carplatenumber)


# we also know * means multiplication
# how can we use * over string data
product = "book"
# when you multiply string with integer then the * becomes times operator
print(product*5)
print("="*50)


# we already know strings in python are enclosed with
# either with double quote "" or single quote ''
# However in python you can use """...""" or '''...'''
# to handle multiline strings
'''
As I am not feeling well,
I am not able to attend th meeting, 
Please proceed without presence

'''
# \n # to escape sequence
# slash \ is also called escape sequence
# when the slash is followed by some letter it has meaning
# \n = new line chsracter
# \t = tab character
# \r = carriage return

filepath = "c:\newfolder\table\readme.txt" 
print(filepath)
filepath = input("Enter the path:")





# \n = new line character


product = "Television"
# product is variable
# to differentiate the literal and variable we use ""
# however in python you can use triple double quotes
# literal is a value (final answer)
# variable is something that always vary

# however in python you can use """...""" or '''...'''
# to handle mutltiline strings
# if we not assign to variable, it will become comment
# if we assign to the variable, it will become lateral/value that can be print


# relationship between strings and list
# strings are nothing but list of characters
'''

10
numbers = input("Enter the numbers (comma seperated):")
print(numbers)
print(type(numbers))
values = numbers.split(",") # split convert it to the list... from string to int
print(type(values))

total = 0
for value in values:
    total = total + int(value)

print(total)

