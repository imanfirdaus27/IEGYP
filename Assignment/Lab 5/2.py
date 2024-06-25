# #iman code

# n = int(input("Please enter any integer:"))

# print(n, end = " ")

# while n != 1:
#     if n % 2 == 0:
#         n = n/2
#         n = int(n)
#         print(n, end = " ")
#     else:
#         n = (3*n) + 1
#         n = int(n)
#         print(n, end = " ")
    
# #chatgpt code
# n = int(input("Please enter any integer: "))

# # Print the initial number before starting the sequence
# print(n, end=" ")

# while n != 1:
#     if n % 2 == 0:
#         n = n // 2  # Use integer division to ensure n remains an integer
#     else:
#         n = 3 * n + 1
#     print(n, end=" ")


# use iman code but use function approach
def collatz(n):
    print(n, end = " ")

    while n != 1:
        if n % 2 == 0:
            n = n/2
            n = int(n)
            print(n, end = " ")
        else:
            n = (3*n) + 1
            n = int(n)
            print(n, end = " ")

n = collatz(int(input("Please enter any integer:")))