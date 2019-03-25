def compare(x,y):
    if x >y:
        print("x is larger than y")
    elif x == y:
        print("x is equal to y")
    else:
        print("x is smaller than y")

if __name__ == '__main__':
    x = int(input("x:"))
    y = int(input("y:"))
    compare(x,y)