total = []
for i in range(0,10):
    total.append([])
    for j in range(0,10):
        total[i].append(0)
for i in range(0,10):
    total[i][0] = 1
    total[i][i] = 1
for i in range(2,10):
    for j in range(1,i):
        total[i][j] = total[i-1][j-1]+total[i-1][j]
for i in range(10):
    for j in range(0,i+1):
        print(total[i][j], end=" ")
    print()