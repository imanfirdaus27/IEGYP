def properdivisorofthenumber(n):
    
    properdivisor = []
    for i in range(1, n):
        if n % i == 0:
            properdivisor.append(i)
    return properdivisor

def isamicablenumbers(n, x):
    amicablepairs = []
    for a in range(n, x + 1):
        b = sum(properdivisorofthenumber(a))
        if b != a and sum(properdivisorofthenumber(b)) == a:
            amicablepairs.append((a, b))
    return amicablepairs

n = int(input("Please enter your lower range:"))
x = int(input("Please enter your upper range:"))

pairs = isamicablenumbers(n, x)
print(pairs)

# def properdivisorofthenumber(n):
#     properdivisors = []
#     for i in range(1, n):
#         if n % i == 0:
#             properdivisors.append(i)
#     return properdivisors

# def isamicablenumbers(n, x):
#     amicablepairs = []
#     for a in range(n, x + 1):
#         b = sum(properdivisorofthenumber(a))
#         if b > a:  # Ensuring we don't check the same pair twice
#             if sum(properdivisorofthenumber(b)) == a:
#                 amicablepairs.append((a, b))
#     return amicablepairs

# # Get user input for range
# lower_range = int(input("Please enter your lower range: "))
# upper_range = int(input("Please enter your upper range: "))

# # Find amicable numbers in the specified range
# pairs = isamicablenumbers(lower_range, upper_range)

# # Print the results
# if pairs:
#     print("Amicable pairs found:")
#     for pair in pairs:
#         print(pair)
# else:
#     print("No amicable pairs found in the specified range.")

