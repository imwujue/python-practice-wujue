num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))

def swap(x,y):
    if x>y:
        return y,x
    else:
        return x,y

if __name__ == '__main__':
    num1,num2 = swap(num1,num2)
    num1,num3 = swap(num1,num3)
    num2,num3 = swap(num2,num3)
    print(num1,num2,num3)