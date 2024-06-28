def properdivisorofthenumber(n):
    
    properdivisor = []
    for i in range(1, n):
        if n % i == 0:
            properdivisor.append(i)
    return properdivisor

n = properdivisorofthenumber(int(input("Please enter any integer:")))
print(n)