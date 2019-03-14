
for i in range(1,168):
    if 168%i == 0:
        j = 168/i;
        if i>j:
            m = (i+j)/2
            n = (i-j)/2
            if m*m-268 == n*n-100 and (i+j)%2==0 and (i-j)%2==0:
                x=m*m-268
                print(x)