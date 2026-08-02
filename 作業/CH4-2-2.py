income = float(input("請輸入您的綜合所得淨額："))
if income <= 540000:
    tax = 0
elif income <= 1210000:
    tax = income * 0.12
elif income <= 2420000:
    tax = income * 0.20
elif income <= 4530000:
    tax = income * 0.30
elif income <= 10310000:
    tax = income * 0.40
else:
    tax = income * 0.45
print("您所要繳交的所得稅額是：", tax)