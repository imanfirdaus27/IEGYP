N = input()

if N.isdigit() and int(N) >= 10: #isdigit
    first_digit = int(N[0])
    last_digit = int(N[-1])
    difference = abs(first_digit - last_digit)
    print(difference)
else:
    print("Invalid Input")

# The isdigit() method in Python is used to check if all characters in a string are digits. \ 
# If the string contains only digit characters (0-9) and is not empty, isdigit() \ 
# returns True. Otherwise, it returns False.