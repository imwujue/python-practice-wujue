def exchange(a,b):
    a,b = b,a
    return (a,b)

if __name__ == '__main__':
    x = int(input("x:"))
    y = int(input("y:"))
    x,y = exchange(x,y)
    print(x,y)