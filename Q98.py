fp = open("test.txt",'w')
strs = input("")
strs = strs.upper()
fp.write(strs)
fp.close()

fp = open("test.txt",'r')
print(fp.read())
fp.close()