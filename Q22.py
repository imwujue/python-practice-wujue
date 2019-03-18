list1 = ['a','b','c']
list2 = ['x','y','z']
dict = {}
list3 = []
list4 = []

# for i in list1:
    # for j in list2:
        # print("first:",i, j)

        # if i == 'a' and j == 'x':
        #     continue
        # if i == 'c' and j == 'x':
        #     continue
        # if i == 'c' and j == 'z':
        #     continue
        # print(i,j)

def permutation(list1, list2):
    for i in list2:
        list3.append(list1[0])
        list4.append(i)
        list1.remove(list1[0])
        list2.remove(i)
        if list1.__len__()!=0:
            permutation(list1,list2)

permutation(list1,list2)
print(list3)
print(list4)