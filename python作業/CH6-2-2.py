name = ['老張','發叔','李董','豪哥','小何']
age = [54,46,50,40,38]
choice = int(input("1.由小到大排序\n2.由大到小排序 : "))

data = list(zip(age,name))
if choice == 1:
    data.sort()
    print("由小到大排序:")
else:
    data.sort(reverse=True)
    print("由大到小排序:")

for a,n in data:
    print(n, ":", a)