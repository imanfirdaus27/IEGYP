x = int(input())  # Read the input integer

numbers = [30, 35]  # Initialize the series with the first two terms

odd_increment = 8
even_increment = 6
odd_multiplier = 2
even_multiplier = 2

while len(numbers) < x:
    if len(numbers) % 2 == 0:  # Even index (0-based, so the next index will be odd)
        next_number = numbers[-1] + odd_increment * odd_multiplier
        odd_multiplier += 1  # Increase the multiplier for the next odd increment
    else:  # Odd index
        next_number = numbers[-1] + even_increment * even_multiplier
        even_multiplier += 1  # Increase the multiplier for the next even increment
    
    # Append the new number to the list
    numbers.append(next_number)

# Print the series as a space-separated string
print(" ".join(map(str, numbers)))