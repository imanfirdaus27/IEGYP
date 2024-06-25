# If we want to use any of the built in python module
# then we have to import them inside our program and use it
# command line argument is always of string type

import sys

print(sys.argv)

for value in sys.argv:
    print(value)

print(len(sys.argv) - 1)

# we want to perform and addition of all the arguments
total = 0
for value in sys.argv[1:]:
    total = total + int(value)

print("Total: ", total)

# Parsing
# Parsing in Python refers to the process of analyzing a string of symbols (such as code or data) according to the rules of a formal grammar. \ 
# This can involve converting data from one format to another, extracting meaningful information from a text, or interpreting and executing code. \ 
# Parsing is a fundamental operation in many programming tasks, \
# such as processing configuration files, interpreting user input, working with data formats like JSON or XML, and compiling code.