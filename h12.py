x=[99,77,0,-1,88,100,77,99]
for i in x:

    for j in x:
        if x[0]<x[1]:
            x[0],x[1]=x[1],x[0]
print(i,j)

