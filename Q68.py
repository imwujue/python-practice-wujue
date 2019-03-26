n = int(input("n:"))
m = int(input("m:"))

x = pow(10,m)
y = int(n/x)
z = n%x
str1 = str(n)
n = z*pow(10,len(str1)-m) + y
print(n)