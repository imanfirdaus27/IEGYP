fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]

# to print all the fruits in the list
for fruit in fruits:
    print(fruit)

# print the fruit which is in the even position
for fruit in fruits[::2]:
    print(fruit)

# print the fruit that has 6 characters
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

multiplicants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplier = 5
for multiplicant in multiplicants:
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)

# range operator : will not generate list of numbers
# it is used to select from a list 
# however we have a function called range
# range function will help us to generate number 
# range function takes start_index, end_index
# start_index is included
# end_index is not included
multiplicants = range(1, 13)
multiplier = 6
for multiplicant in multiplicants:
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)

# products = ["cooking oil", "ginger", 'garlic', 'tomato', 'milk']
# go to the super market
# for product in products:
#    shelfno = search(product)
#    walkto(selfno)
#    if notsure():
#       callwife(question)
#       product = product + "10kg"
#    pick(product)
#    addtocart(product)
# checkout(mycart)
# total = 0
# for product in mycart:
#    price = getprice(product)
#    total = total + price
#    addtobasket(product)
# dopayment(total)

# Take a number as input print all the digits in the number
usernumber = int(input("Enter the number: "))
# mynumber = 12345
# do you have a list = no
# how many digits do we have = dont know
# you have to use while loop
mynumber = usernumber
print("-----------------------")
while(mynumber > 0):
    print(mynumber % 10)
    mynumber = mynumber // 10

mynumber = usernumber
print("-------------------------")
numberofdigits = len(str(mynumber)) - 1
while(mynumber > 0):
    print(mynumber // 10 ** numberofdigits)
    mynumber = mynumber % 10 ** numberofdigits
    numberofdigits = numberofdigits - 1

mynumber = str(usernumber)
print("-------------------------")
for number in mynumber:
    print(number)

# Hanafi Effect
num = str(usernumber)
i = 0
while i < len(num):
    print(int(num[i]))
    i += 1


fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]
# only for loops can have else part
# The code in the else part will get executed only when all fully