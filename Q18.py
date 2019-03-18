a = int(input("a:"))
n = int(input("n:"))
list = []
res = a
b = a
for i in range(0,n):
    list.append(res)
    a = b*10**(i+1)
    res = res +a
print(list)
sum = 0
for elem in list:
    sum +=elem
print(sum)