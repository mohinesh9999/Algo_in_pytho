def construct(arr,s,e,i,farr):
    if(e==s):
        return arr[s]
    ind=(s+e)//2+(s+e)%2
    farr[i]=construct(arr,s,ind,i+1,farr)+construct(arr,ind+1,e,i,farr)
    return farr[i]