# A prime number is a number that can only be divided by itself and 1 without remainders
# use for loop when have the list

for mynumber in range(2, 51):
    for i in range(2, mynumber):
        if (mynumber % i == 0):
            break
    else:
        print(mynumber, end=' ')