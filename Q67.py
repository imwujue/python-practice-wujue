n = int(input("n:"))
list = []
def inputnum(n):
    for i in range(n):
        a = int(input("nums:"))
        list.append(a)

if __name__ == '__main__':
    inputnum(n)
    maxnum = list[0]
    minnum = list[0]
    for i in range(len(list)):
        maxnum = max(list[i],maxnum)
        minnum = min(list[i],minnum)
    for i in range(len(list)):
        if list[i] == maxnum:
            list[0],list[i]=list[i],list[0]
        if list[i] == minnum:
            list[len(list)-1],list[i]=list[i],list[len(list)-1]
    print(list)