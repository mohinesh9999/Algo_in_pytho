a,b,c,m=list(map(int,input().split()))
# def pow1(a,b,m):
#     if(b==0):
#         return 1
#     x=pow1((a*a)%m,b//2,m)
#     if(b%2==1):
#         return (((x)%m)*a)%m
#     return (x)%m
def pow1(a,b,m):
    if(b==0):
        return 1
    i,ans,s=0,a,1
    while(i<32):
        if(1<<i&b !=0 ):
            s=(s*ans)%m
        ans=(ans*ans)%m
        i+=1
    return s
def modInv1(c,m):
    return pow1(c,m-2,m)
def extendedEuclid(c,m):
    if(m==0):
        return [c,1,0]
    a=extendedEuclid(m,c%m)
    w=[a[0]]
    w.append(a[2])
    w.append(a[1]-c//m*a[2])
    return w
def modInv2(c,m):
    return extendedEuclid(c,m)[1]%m
print((pow1(a,b,m)*modInv2(c,m))%m)