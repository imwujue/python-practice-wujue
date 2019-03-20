from math import sqrt
lower = int(input("min:"))
upper = int(input("max:"))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,int(sqrt(num+1)+1)):
            if num % i == 0:
                break
        else:
            print(num)