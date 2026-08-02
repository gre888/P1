
print("====== 主功能表 ======")
print("1. 新增作業")
print("2. 修改作業")
print("3. 刪除作業")
print("0. 結束程式")
while 1:
    c= int(input("請輸入選項："))
    if c==1:
        print("新增作業...")
    elif c==2:
        print("修改作業...")
    elif c== 3:
        print("刪除作業...")
    elif c==0:
        print("結束程式！")
        break
    else:
        print("輸入值不正確")