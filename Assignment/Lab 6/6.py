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