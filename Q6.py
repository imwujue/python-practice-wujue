# 递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# 非递归
def fib1(n):
    a,b = 0,1
    for i in range(0,n-1):
        a,b = b,a+b
    return b

print(fib(10))
print(fib1(10))