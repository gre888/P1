#1公尺=3.28英尺、1公斤=2.2英磅，請寫出一個可讓使用者選擇要轉換哪一單位的程式。 
s=int(input("要轉換 1.公尺->英尺    或者2. 公斤->英磅"))
print(s)
num=float(input("請輸入要轉換的數值:"))
print(num)
if s==1:
    print(f"{num}公尺={num*3.28:.6f}英尺")  
if s==2:
    print(f"{num}公斤={num*2.2:.6f}英磅")    
else:
    print("無此選項")
