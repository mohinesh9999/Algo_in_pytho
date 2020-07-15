l=[]
ans=False
def dfsUtil(g,N,Visited,i,parent):
    global l,ans
    Visited[i]=True
    for j in g[i]:
        if(not Visited[j]):
            if(dfsUtil(g,N,Visited,j,i)):
                return True
        elif(parent!=j):
            return True
    return False
def dfs(g,N):
    global l,ans
    ans=False
    Visited=[False]*N
    for i in range(N):
        if(not Visited[i]):
            if(dfsUtil(g,N,Visited,i,-1)):
                return True
    return False
def isCyclic(g,n):
    return ('1' if(dfs(g,n)) else '0')