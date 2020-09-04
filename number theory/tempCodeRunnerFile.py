def mul(a,b):
    w=[[0 for i in range(len(a))] for i in range(len(a))]
    b=list(zip(*b))
    for i in range(len(a)):
        for j in range(len(a)):
            s=0
            for k in range(len(a)):
                s+=a[i][k]*b[j][k]
            w[i][j]=s
    for i in range(len(a)):
        for j in range(len(a)):
            a[i][j]=w[i][j]
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
mul(a,b)
print(a,b)