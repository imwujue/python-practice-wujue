n = int(input("n:"))
flag = 1
res = 9
while flag:
    if res%n == 0:
        flag = 0
        print(res)
    else:
        res = res*10+9
