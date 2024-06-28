def primenumbers(n):
    """Returns a list of prime numbers up to n."""
    primes = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def twinprimenumbers(primes):
    twinprimes = []
    for i in range(len(primes)-1):
        if primes[i+1] - primes[i] == 2:
            twinprimes.append((primes[i], primes[i+1]))
    return twinprimes
            
n = 1000
primethousand = primenumbers(n)
print(primethousand)

twin = twinprimenumbers(primethousand)
print(twin)

