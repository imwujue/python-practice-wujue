
def peach(res,n):
    res = 1
    count = 0
    for i in range(n-1):
        count = (res+1)*2
        res = count
    return count

print(peach(1,10))