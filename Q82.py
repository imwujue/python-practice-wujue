num = input("num:")
res = 0
for i in range(len(num)):
    res = res*8 + ord(num[i]) - ord('0')
print(res)