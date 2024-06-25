x,y = input().split()
a,b = input().split()
z,c = input().split()

y = int(y)
b = int(b)
c = int(c)

if (x == a == z) and (y == b == c) :
    print("Double Bonanza")
elif (x==a==z) or  (y ==b ==c):
     print("Bonanza")
else:
    print("No Bonanza")