


m = int(input("請輸入一個 1~12 之間的月份："))
if m in [3, 4, 5]:
    print(f"{m}月是春天")
elif m in [6, 7, 8]:
    print(f"{m}月是夏天")
elif m in [9, 10, 11]:
    print(f"{m}月是秋天")
elif m in [12, 1, 2]:
    print(f"{m}月是冬天")
else:
    print("輸入錯誤！")