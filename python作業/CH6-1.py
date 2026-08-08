T=[]
for i in range(1,10):
    R=[]
    for j in range(1,10):
        R.append(i*j)
    T.append(R)

for A in T:
    for num in A:
        print(num,end="\t")
    print()
    