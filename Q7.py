a = [1,2,3]
print(id(a))
b = a.copy()
print(id(b))
b[:] = a[:]
print(id(b))