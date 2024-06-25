# # naqib code
# c = 0
# total = 0
# while c < 11:
#     for i in range(1,10000):
#         total = 0
#         for j in range(1,10000):
#             if i % j == 0:
#                 total += j
#                 if i == j and total == (i * 2):
#                     print(i)
#                     c += 1

# write a program that generates 10 perfect numbers

# iman code

def sieveoferatosthenes(a):
    
    isprime = [False] * (a + 1) # It initializes is_prime with False for all indices.

    for mynumber in range(2, a + 1):
        for i in range(2, mynumber):
            if (mynumber % i == 0):
                break
        else:
            isprime[mynumber] = True
    
    return isprime


a = 10000
primenumbersflags = sieveoferatosthenes(a)

for i in range(2, a + 1):
    if primenumbersflags[i]:
        print(i, end=" ")


# yang betul

def is_perfect(n):
    # Initialize the sum of proper divisors
    divisors_sum = 0
    # Iterate through all numbers from 1 to n-1
    for i in range(1, n):
        # Check if i is a proper divisor of n
        if n % i == 0:
            # Add i to the sum of divisors
            divisors_sum += i
    # Check if the sum of proper divisors equals n
    return divisors_sum == n

def generate_perfect_numbers(count):
    perfect_numbers = []
    num = 1
    while len(perfect_numbers) < count:
        if is_perfect(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

# Generate the first 4 perfect numbers
perfect_numbers = generate_perfect_numbers(4)
print(perfect_numbers)

