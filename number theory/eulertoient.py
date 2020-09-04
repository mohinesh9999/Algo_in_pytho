import math
def phi(n):
    ans=n
    for i in range(2,math.floor(math.sqrt(n))+1):
        if(n%i==0):
            while(n%i==0):
                n//=i
            ans*=(i-1)/i
    if(n>1):
        ans*=(n-1)/n
    return int(ans)
def eulerToitent(n):
    phi=[i for i in range(n+1)]
    for i in range(2,n+1):
        if(phi[i]==i): 
            phi[i]-=1
            for j in range(2*i,n+1,i):
                phi[j]*=((i-1)/i)
    return int(phi[-1])
n=int(input())
print(eulerToitent(n))