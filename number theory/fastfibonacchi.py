n=int(input())
def mul(a,b):
    w=[[0]*len(a) for i in range(len(a))]
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
def pow(a,n):
    if(n==0 or n==1):
        return 
    pow(a,n//2)
    mul(a,a)
    if(n%2==1):
        mul(a,[[1,1],[1,0]])
def fib(n):
    if(n<=2):
        return n-1
    a=[[1,1],[1,0]]
    pow(a,n-2)
    return a[0][0]
print(fib(n))