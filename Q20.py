def height(n):
    h = 100
    total = 0
    for i in range(1,n+1):
        total += h
        ground = total
        h = h/2
        total += h
    print('ground:%f' %ground)
    print('h:%f' %h)

height(10)