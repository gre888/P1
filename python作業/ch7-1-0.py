# 輸入第一個正整數 a：48
# 輸入第二個正整數 b：72
# a, b 兩整數的GCD為 24

a=int(input("輸入第一個正整數 a:"))
b=int(input("輸入第二個正整數 b:"))
while b != 0:
    r = a % b
    a = b
    b = r
print("a, b 兩整數的GCD為", a)
