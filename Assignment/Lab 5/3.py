# iman code
def calculateeuclidean(a,b):
    if a<b:
        a,b = b,a
    
    while b != 0:
        a, b = b, a % b     
    return a

a = int(input("Please enter any first integer:"))
b = int(input("Please enter any second integer:"))
print(calculateeuclidean(a,b))

# chatgpt code

# def calculateeuclidean(a, b):
#     if a < b:
#         a, b = b, a
    
#     while b != 0:
#         a, b = b, a % b
    
#     return a

# # Input from the user
# a = int(input("Please enter the first integer: "))
# b = int(input("Please enter the second integer: "))

# # Calculate GCD using the function and print the result
# gcd_result = calculateeuclidean(a, b)
# print(f"The GCD of {a} and {b} is: {gcd_result}")