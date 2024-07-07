# x = int(input())

# l = ['/']*x
# m = ["\\"]*x #This means you use \\ to represent a single backslash in the string.
# string1 = ''.join(l)
# string2 = ''.join(m)

# n = string1 + string2

# print(n)

# lines = 4

# if x==5:
#     for i in range(lines - 1):
#         print(n+n)
# elif x==10:
#     for i in range(lines - 1):
#         print(n+n)

def print_pattern(n):
    # Create the pattern strings
    pattern1 = '/' * n + '\\' * n
    pattern2 = '/' * n + '\\' * n
    
    # Print the pattern 6 times
    for _ in range(4):
        print(pattern1 + pattern2)

# Example usage:
input_value = int(input("Enter the number of '/' and '\\' to print: "))
print_pattern(input_value)


        

