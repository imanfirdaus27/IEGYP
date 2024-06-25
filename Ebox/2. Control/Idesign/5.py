hurl_factor, spin_factor, speed_factor = map(int, input().split())


condition1 = hurl_factor > 50
condition2 = spin_factor > 60
condition3 = speed_factor > 100


if condition1 and condition2 and condition3:
    grade = 10
elif condition1 and condition2:
    grade = 9
elif condition2 and condition3:
    grade = 8
elif condition1 and condition3:
    grade = 7
elif condition1 or condition2 or condition3:
    grade = 6
else:
    grade = 5

print(grade)