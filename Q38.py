a = []
list = []
for j in range(0,3):
    for i in range(0,3):
        num = int(input())
        list.append(num)
    tmp = list.copy()
    a.append(tmp)
    list.clear()
res = 0
res = sum(a[i][i] for i in range(0,3))

print(a)
print(res)