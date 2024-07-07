def Birthday():
    
    c = int(input())

    x = []

    for i in range(c):
        element = int(input())
        x.append(element)
    
    a = sum(x)

    b = int(input())

    c = a * b

    return a, c

k, l = Birthday()
print(f"Total number of books required:{k}")
print(f"Total cost:{l}")


