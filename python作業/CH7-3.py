import random

numbers = random.sample(range(1, 50), 7)

print("大樂透開獎號碼：")

for num in numbers:
    print(num, end=" ")