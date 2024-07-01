def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    
    # Check for factors from 3 up to the square root of num
    sqrt_num = int(num**0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

# Input
a = int(input().strip())
b = int(input().strip())

# Output prime numbers in the range [a, b]
result = []
for num in range(a, b + 1):
    if is_prime(num):
        result.append(str(num))

print(" ".join(result))