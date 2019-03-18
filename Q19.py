
for i in range(2,1001):
    list = []
    list.append(1)
    # print("i:", i)
    num = i
    for j in range(2,i+1):
        while i%j == 0:
            list.append(j)
            i = i/j
    # print("list:",list)
    sum = 0
    for elem in list:
        sum += elem
    if sum == num:
        print("sum:",sum)