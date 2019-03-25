max = lambda x,y: (x>=y)*x + (x<y)*y
min = lambda x,y: (x<=y)*x + (x>y)*y

x = int(input("x:"))
y = int(input("y:"))

print("max",max(x,y))
print("min",min(x,y))