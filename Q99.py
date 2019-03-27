
fp1 = open("test1.txt",'w')
fp1.write("alice richard jack")
fp1 = open("test1.txt",'r')
a = fp1.read()
print(a)
fp1.close()

fp2 = open("test2.txt",'w')
fp2.write("bob mary lily")
fp2 = open("test2.txt",'r')
b = fp2.read()
print(b)
fp2.close()

c = list(b+a)
c.sort()
print(c)
s = ''
s = s.join(c)
print(s)

fp3 = open("test3.txt",'w')
fp3.write(s)
fp3 = open("test3.txt",'r')
print(fp3.read())
fp3.close()