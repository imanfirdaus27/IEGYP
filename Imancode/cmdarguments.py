# if we want to use any of the built in python module
# then we have to import them inside our program and use it

import sys

print (sys.argv) #variable length 

for value in sys.argv:
    print(value)

print(len(sys.argv) - 1)

# we want to perform and addition of all the arguments
total = 0
for value in sys.argv[1:]:
    total = total + int(value)

print("Total: ", total)

# Parsing

