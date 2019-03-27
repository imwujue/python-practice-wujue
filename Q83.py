n = int(input("n:"))
def nums(n):
    if n == 1:
        return 4
    if n == 2:
        return 7*4
    else:
        return 7*pow(8,n-2)*4