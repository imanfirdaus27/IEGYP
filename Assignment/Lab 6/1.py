def multiplicationtable(n):
    """Prints the multiplication table of a number n."""
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
    return n

n = multiplicationtable(int(input("Please enter any integer:")))