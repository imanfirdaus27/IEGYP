def maximumMinimum(*args):
    return min(args), max(args)

print("Enter the values:")
input_values = input().split()
values = list(map(int, input_values))
min_val, max_val = maximumMinimum(*values)

print("The maximum value is :", max_val)
print("The minimum value is :", min_val)