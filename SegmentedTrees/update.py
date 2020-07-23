def update(qi,s,e,si,diff,tree):
    if(s<=qi<=e):
        tree[si]+=diff
    elif(1):
        return 
    if(e>s):
        mid=(s+e)//2+(s+e)%2
        update(qi,s,mid,si*2+1,diff,tree)
        update(qi,mid+1,e,si*2+2,diff,tree)
