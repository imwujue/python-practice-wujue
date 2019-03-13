i = int(input("input:"))
arr=[0,100000,200000,400000,600000,1000000]
rat=[0.1,0.075,0.05,0.03,0.015,0.01]
res=0
for idx in range(5,-1,-1):
    if i>arr[idx]:
        # print("idx",idx)
        # print("res",res)
        res=res+(i-arr[idx])*rat[idx]
        # print("res", res)
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(res)