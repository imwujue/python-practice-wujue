a = [1,2,3,4,10,12]
num = int(input("num:"))
res = []
for i in range(len(a)):
    if num >= a[i]:
        res.append(a[i])
        if i == len(a)-1:
            res.append(num)
    else:
        res.append(num)
        for j in range(i,len(a)):
            res.append(a[j])
        break
print(res)