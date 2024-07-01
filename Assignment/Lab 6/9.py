# chatgpt code
# Print Pascal's Triangle in Python

# input n
# n = 8

# for i in range(1, n+1): # berapa baris nak buat
#     for j in range(0, n-i+1): # berapa kotak kosong or space
#         print(' ', end='')

#     # first element is always 1
#     C = 1
#     for j in range(1, i+1): # perulangan dalam setiap baris yang mengira dan mencetak nombor dalam baris tersebut

#         # first value in a line is always 1
#         print(' ', C, sep='', end='')

#         # using Binomial Coefficient
#         C = C * (i - j) // j
#     print()

# imancode

# Print Pascal's Triangle in Python
def pascal_triangle(n):
# iterate up to n
  for i in range(n):
    # adjust space
    print(' '*(n-i), end='')

    # compute each value in the row
    coef = 1
    for j in range(0, i + 1):
        print(coef, end=' ')
        coef = coef * (i - j) // (j + 1)
    print()
    # Print Pascal's Triangle in Python

n = 8
result = pascal_triangle(n)