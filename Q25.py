def mult(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

sum = 0
for i in range(1,21):
    sum += mult(i)
    print(mult(i),sum)