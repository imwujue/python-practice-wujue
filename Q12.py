from math import sqrt

leap = 1
count = 0
for m in range(101,200):
    k = int(sqrt(m+1))
    for i in range(2,k+1):
        if m%i == 0:
            leap = 0
            break
    if leap == 1:
            print(m)
            count += 1
    leap = 1
print("count = %d" %count)