X = [[1,2,3],
     [4,5,6],
     [7,8,9]]
Y = [[1,2,3],
     [4,5,6],
     [7,8,9]]
res = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        res[i][j] = X[i][j] + Y[i][j]

print(res)