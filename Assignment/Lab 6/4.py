def product(n):
    product = 1
    for digit in str(n):
        product = product * int(digit)
    return product

n = product(int(input("Please enter any integer:")))
print(n)