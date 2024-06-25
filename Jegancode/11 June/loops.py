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