def buildTree(a):
    n=len(a)
    bitTree=[0]*(len(a)+1)
    for i in range(n):
        update(bitTree,i,a[i])
    return bitTree
def update(a,i,v):
    i+=1
    while(i<=len(a)-1):
        print(i)
        a[i]+=v
        i+=(i&-i)
def getsum(a,i):
    s=0
    i+=1
    while(i>0):
        print(i)
        s+=a[i]
        i-=(i&-i)
    return s
l=list(map(int,input().split()))
b=buildTree(l)
print(b)
for i in range(6):
    a,b1,c=list(map(int,input().split()))
    if(a==0):
        update(b,b1,c-l[b1])
        print(b)
        l[b1]=c
    else:
        print(getsum(b,b1))