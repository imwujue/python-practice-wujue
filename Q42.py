num = 1

def autofunc():
    num = 0
    print('autofunc num: %d' %num)
    num += 1
for i in range(3):
    print('num: %d' %num)
    num += 1
    autofunc()