numlist = [2,3,1,5,6,7,1]
print(numlist)

#fill your code
try:
    x = int(input("Enter n"))

    sum = 0
    for i in range(x):
        sum = sum + numlist[i]
    print("Sum=",sum)
    
except IndexError:
    print("Index Value out of range")