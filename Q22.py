list = ['a','b','c','x','y','z']
total = []

def perm(list, begin, end):
    if begin >= end:
        tmp = list.copy()
        total.append(tmp)
        # print(list)
    else:
        i = begin
        for num in range(begin, end):
            list[i], list[num] = list[num], list[i]
            perm(list,begin+1,end)
            list[i], list[num] = list[num], list[i]


perm(list,0,len(list))

new_total = []

for elem in total:
    if elem[0] != 'a':
        continue
    if elem[1] != 'b':
        continue
    if elem[2] != 'c':
        continue
    if elem[3] == 'x':
        continue
    if elem[5] == 'x' or elem[5] == 'z':
        continue
    tmp = elem.copy()
    new_total.append(elem)

print(new_total)

