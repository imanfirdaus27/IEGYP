a = int(input())

even = 0
odd = 0

for i in range(a):# tak payah guna range because dia a dah in the list but in string type
        x =  int(input()) # to convert the string type in the list to integer type
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

print(even,odd)