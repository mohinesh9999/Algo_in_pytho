def find(arr,x):
    if(arr[x]==x):
        return x
    return find(arr,arr[x])


def union(arr,x,y):
    x1,y1=find(x),find(y)
    if(x1==y1):
        return
    else:
        arr[y1]=x1
        