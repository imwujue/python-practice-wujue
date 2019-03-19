
n = int(input("num:"))
a = int(n/10000)
b = int(n%10000/1000)
c = int(n%1000/100)
d = int(n%100/10)
e = int(n%10)

if a == e and b == d:
    print("是回文数")
else:
    print("不是回文数")