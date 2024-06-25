x = int(input())

if x < 15000:
        HRA = (15/100)*x
        DA = (90/100)*x
elif x >= 15000:
         HRA = 5000
         DA = (98/100) * x

gross = x + HRA + DA

print(f'{gross:.2f}')