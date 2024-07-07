def symmetric():  
    set1 = map(int,input().split(','))
    set1 = sorted(set1)

    set2 = map(int, input().split(','))
    set2 = sorted(set2)

    c = set(set1).symmetric_difference(set(set2))

    # print(set1)
    # print(set2)
    # print(c)

    if c:
        print(f"{{{','.join(map(str, sorted(c)))}}}")
    else:
        print("Invalid Input")

x = symmetric()