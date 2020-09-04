import math
def sieve(n):
    prime=[True]*(n+1)
    for i in range(2,n+1):
        if(prime[i]):
            for j in range(i*i,n+1,i):
                prime[j]=False
    s=set()
    for i in range(2,n+1):
        if(prime[i]):
            s.add(i)
    return sorted(list(s))
def segmentedSieve(l,r,primes):
    a=[True]*(r-l+1)
    
    i=2
    for i in primes:
        if(i*i<=r):
                low=(l//i)*i
                if(low<l):
                    low+=i
                for j in range(low,r+1,i):
                    if(j!=i):
                        a[j-l]=False
        else:
            break
    s=1
    for i in range(r-l+1):
        if(a[i]):
            s=(s*(i+l))%(10**9+7)
    return s
w=sieve(10**6+1)
for _ in range(int(input())):
    l,r=list(map(int,input().split()))
    print(segmentedSieve(l,r,w))