a,b,c = (input().split())

a = int(a)
b = int(b)
c = int(c)

for i in range(1,c+1):    
        if i % 2 == 0:
            b *= 2
        else:
            a *=2

total = a + b

print(total)