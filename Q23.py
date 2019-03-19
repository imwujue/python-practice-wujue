for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print("")
for i in range(5,8):
    for j in range(i-4):
        print(" ",end="")
    for j in range(15-2*i):
        print("*",end="")
    print("")
