l=[]
def dfsUtil(g,N,Visited,i):
    global l
    Visited[i]=True
    l.append(i)
    for j in g[i]:
        if(not Visited[j]):
            dfsUtil(g,N,Visited,j)
    return l
def dfs(g,N):
    global l
    l=[]
    Visited=[False]*N
    return dfsUtil(g,N,Visited,0)