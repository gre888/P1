T=[]
for i in range(1,10):
    R=[]
    for j in range(1,10):
        R.append(i*j)
    T.append(R)

for R in T:
    for num in R:
        print(num,end="\t")
    print()
    