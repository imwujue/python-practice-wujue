def solve(n):
    sum = 0.0
    while True:
        sum += 1/n
        # print(1/n)
        # print(sum)
        if n == 1 or n == 2:
            break
        else:
            n -= 2
    return sum

n = int(input("n:"))
print('sum:%lf' %solve(n))