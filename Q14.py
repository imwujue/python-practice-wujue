def reduceNum(num):
    list = []
    flag = 0
    for i in range(2,num):
        while num%i==0:
            num = num/i
            list.append(i)
            flag = 1
        if flag == 0:
            print("%d是素数" %num)
    for elem in list:
        print(elem)
reduceNum(90)