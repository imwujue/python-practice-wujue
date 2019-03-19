def output(s,l):
    if l == 0:
        return
    else:
        print(s[l-1],end="")
        output(s,l-1)

s = input("raw_string:")
l = len(s)
print("inverse_string:",end="")
output(s,l)