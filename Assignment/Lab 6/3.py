def primefactors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Get user input and calculate prime factors
number = int(input("Please enter any number: "))
result = primefactors(number)
print(f"Prime factors of {number}: {result}")

# chatgpt
# def prime_factors(n):
#     factors = []
#     divisor = 2

#     while n > 1:
#         while n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#         divisor += 1

#     return factors

# Example usage:
# number = 84
# print(f"Prime factors of {number}: {prime_factors(number)}")