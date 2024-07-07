def check():
    s1 = map(int, input().split(','))
    s1 = sorted(s1)
    s1 = set(s1)  # Convert to set

    s2 = map(int, input().split(','))
    s2 = sorted(s2)
    s2 = set(s2)  # Convert to set

    print(s1.issubset(s2))
    print(s2.issubset(s1))
    print(s1.issuperset(s2))
    print(s2.issuperset(s1))

x = check()