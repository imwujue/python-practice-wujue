
filename = input("filename:")
fp = open(filename,'w')
ch = input('strings:')
while ch != '#':
    fp.write(ch)
    ch = input('')
fp.close()