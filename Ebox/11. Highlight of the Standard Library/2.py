import math

# Get the input list of numbers
numbers = list(map(float, input().split()))

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Calculate the floor, ceil, and round of the sum
floor_sum = math.floor(total_sum)
ceil_sum = math.ceil(total_sum)
round_sum = round(total_sum)

# Calculate the differences
diff1 = floor_sum - ceil_sum
diff2 = ceil_sum - round_sum
diff3 = floor_sum - round_sum

# Print the results
print(f"{diff1:.1f}")
print(f"{diff2:.1f}")
print(f"{diff3:.1f}")