dict1 = {}

while True:
    print("\n===== 英漢字典 =====")
    print("1. 新增／修改")
    print("2. 刪除")
    print("3. 查詢")
    print("4. 離開")

    choice = input("請選擇功能：")

    if choice == '1':
        word = input("請輸入英文單字：")
        meaning = input("請輸入中文解釋：")

        if word in dict1:
            print("單字已存在，修改中文解釋")
        else:
            print("新增單字")

        dict1[word] = meaning

    elif choice == '2':
        word = input("請輸入要刪除的英文單字：")

        if word in dict1:
            del dict1[word]
            print("刪除成功")
        else:
            print("不存在字典中")

    elif choice == '3':
        word = input("請輸入要查詢的英文單字：")

        if word in dict1:
            print("中文解釋：", dict1[word])
        else:
            print("不存在字典中")

    elif choice == '4':
        print("程式結束")
        break

    else:
        print("選項錯誤，請重新輸入")