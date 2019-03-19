
n = int(input("num:"))

a = int(n/10000)
b = int(n%10000/1000)
c = int(n%1000/100)
d = int(n%100/10)
e = int(n%10)

if a!=0:
    print('5位数：%d %d %d %d %d' %(e,d,c,b,a))
elif b!=0:
    print('4位数：%d %d %d %d' % (e, d, c, b))
elif c!=0:
    print('3位数：%d %d %d' % (e, d, c))
elif d!=0:
    print('2位数：%d %d' % (e, d))
else:
    print('1位数：%d' % (e))