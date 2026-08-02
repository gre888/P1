
lst=[[87,64,88],[93,72,86],[80,88,89],[79,91,90]]

for i in range(4):
    sumh=0
    for j in range(3):
            sumh+=lst[i][j]
    print(f"Sum of row {i}: {sumh}",end="     ")
    print()
print("水平loop結束")


for j in range(3):
    sumv=0
    for i in range(4):
        sumv+=lst[i][j]
    print(f"Sum of column{j}平均: {sumv/4}",end="     ")
    print()    
print("垂直loop結束")