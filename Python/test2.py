list=[8 for x in range(5)]
for i in range(5):
    s=int(input("Enter a number: "))
    list[i]=s
print(list)

max=list[0]
for j in list:
    if j>max:
        max=j
