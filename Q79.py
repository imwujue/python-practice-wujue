str_list = []
def sortStr(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]
    return list
for i in range(3):
    str = input("string:")
    str_list.append(str)
list = sortStr(str_list)
print(list)