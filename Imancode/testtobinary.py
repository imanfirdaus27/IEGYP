# convert 25 to binary

x =25

a1 = x//2
b1 = x % 2
print ("Remainder:", b1)

a2 = a1 // 2
b2  = a1 % 2
print ("Remainder:", b2)

a3 = a2 // 2
b3  = a2 % 2
print ("Remainder:", b3)

a4 = a3 // 2
b4  = a3 % 2
print ("Remainder:", b4)

a5 = a4 // 2
b5  = a4 % 2
print ("Remainder:", b5)

print (b5, b4, b3, b2, b1)