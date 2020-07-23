def getsum(qs,qe,ss,se,si,tree):
    if(qs>se or ss>qe):
        return 0
    elif(ss<=qs<=qe<=se):
        return tree[si]
    mid=(s+e)//2+(s+e)%2
    return getsum(qs,qe,ss,mid,2*si+1,tree)+getsum(qs,qe,mid+1,se,2*si+2,tree)