def maximumMinimum(n):
    numbers = list(map(int, n.split(',')))
    
    if not numbers:  # Handle case where input is empty
        return None, None
    
    max_value = numbers[0]
    min_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value

# Get user input
user_input = input("Please enter any numbers separated by commas: ")

# Call the function and get the result
max_num, min_num = maximumMinimum(user_input)

# Print the result
if max_num is not None and min_num is not None:
    print("Maximum value:", max_num)
    print("Minimum value:", min_num)
else:
    print("No numbers entered or invalid input.")


