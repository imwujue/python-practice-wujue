list = [1,3,5,7,9,2,4,6,8,0]
#bubble sort
for i in range(0,10):
    for j in range(i+1,10):
        if list[i]>list[j]:
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
    print(list)
print()