count = 10
givennumber = 2

while (count > 0):
    for mynumber in range(2, 51):
        for i in range(2, mynumber):
            if (mynumber % i == 0):
                 break
    else:
        print(mynumber, end=' ')