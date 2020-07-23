def find(arr,x):
    if(arr[x]==x):
        return x
    return find(arr,arr[x])


def union(arr,x,y,rank):
    x1,y1=find(x),find(y)
    if(x1==y1):
        return
    if(rank[x1]<rank[y1]):
        arr[x1]=y1
    elif(rank[x1]>rank[y1]):
        arr[y1]=x1
    else:
        arr[x1]=y1
        rank[y1]+=1