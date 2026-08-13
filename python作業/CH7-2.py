text = input("請輸入一段中文文章：")

count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print("字元出現次數：")

for ch, num in count.items():
    print(ch, "：", num)