n = int(input("n:"))
flag = 1
count = 1
list = []
for i in range(n):
    list.append(0)
num = n
while flag:
    for i in range(num):
        tmp = str(count)
        if list[i] == -1:
            continue
        if '3' in tmp:
            list[i] = -1
            n -= 1
            count += 1
        else:
            list[i] = count
            count += 1
        if n == 1:
            flag = 0
            break
        print(list)

for i in range(num):
    if list[i]!= -1:
        print(i)

