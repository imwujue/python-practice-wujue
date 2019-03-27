sum = 0
least = 200
flag = 1
while flag:
    for i in range(5):
        sum = least*5 +1
        if i == 4:
            flag = 0
            break
        if sum%4 == 0:
            least = sum/4
        else:
            least += 1
            break
print(sum)


