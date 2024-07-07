def Attendance():
    
    c = int(input("Enter total Number of sheets:"))

    x = []

    for i in range(c):
        element = tuple(map(int,input().split()))
        x.append(element)

    y = tuple(x)
    z = set()

    for sheet in y:
        z.update(sheet)

    return x,z

k,l = Attendance()
print(f"Attendance Sheets with Register Number:{tuple(k)}", end = "")
print(f"\nFinal sheet:{tuple(l)}", end = "")