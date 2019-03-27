def inverseList(list):
    newList = []
    for i in range(len(list)-1,-1,-1):
        newList.append(list[i])
    return newList

if __name__ == '__main__':
    list = [1,2,3,4,5]
    list = inverseList(list)
    print(list)

