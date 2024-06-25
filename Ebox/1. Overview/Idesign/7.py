import sys

print("Arguments:")

for argument in sys.argv[1:]:
         print(argument)

print(f"Number of arguments is {len(sys.argv)-1}")