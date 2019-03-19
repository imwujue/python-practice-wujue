def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
sum = 0.0
for i in range(1,21):
    num1 = fib(i+2)
    num2 = fib(i+1)
    sum += num1/num2
print(sum)