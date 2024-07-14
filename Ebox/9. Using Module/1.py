import math

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return ''.join(map(str, fib_series[:n]))

n = int(input())
print(fibonacci(n))