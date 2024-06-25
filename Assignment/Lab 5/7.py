# iman code
def harmonicseries(n):
    sumharmonic = 0
    for i in range(1, n + 1):
        sumharmonic = sumharmonic + 1/i
    return sumharmonic

n = int(input("Please enter any integer:"))
print(f"the sum of first {n} of harmonic series is {harmonicseries(n):.2f}")
    