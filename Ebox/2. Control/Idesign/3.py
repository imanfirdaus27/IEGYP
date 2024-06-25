x = int(input())
y = int(input())

if y < 50:
    discount = 0
elif 50 <= y <= 100:
    discount = 10
elif 101 <= y <= 200:
    discount = 20
elif 201 <= y <= 400:
    discount = 30
elif 401 <= y <= 500:
    discount = 40
else:  # y > 500
    discount = 50

totalprice = float(x * y)
discountamount = float(totalprice * (discount / 100))
finalprice = float(totalprice - discountamount)

print(f'{finalprice:.2f}')