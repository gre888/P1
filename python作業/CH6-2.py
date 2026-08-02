name=['老張','發叔','李董','豪哥','小何']
age=[54,46,50,40,38]

data = list(zip(age,name))
s=int(input("請輸入排序方式(1.由小到大 2.由大到小):"))
if s==1:
    data.sort()
    print("由小到大排序結果：")
elif s==2:
    data.sort(reverse=True)
    print("由大到小排序結果：")
for a,n in data:
    print(n,a)    