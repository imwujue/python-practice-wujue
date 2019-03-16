for num in range(100,1000):
    a = int(num/100)
    b = int(num/10%10)
    c = num%10
    # print(num,a,b,c)
    if num == a**3 + b**3 +c**3:
        print(num)