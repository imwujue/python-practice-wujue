def square(x):
    return x*x

if __name__ == '__main__':
    again = 1
    while again:
        num = int(input("num:"))
        res = square(num)
        print('res: %d' %res)
        if res >= 50:
            again = 1
        else:
            again = 0