N = int(input())

# Initialize variables
count = 0
num = 2

# Loop to find and print the first N prime numbers
while count < N:
    is_prime = True
    
    # Check if num is prime
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    # If num is prime, print it and increment count
    if is_prime:
        print(num, end=' ')
        count += 1
    
    # Move to the next number
    num += 1
    