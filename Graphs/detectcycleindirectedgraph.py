l=[]
ans=False
def dfsUtil(g,N,Visited,i,v1):
    global l,ans
    Visited[i]=True
    v1[i]=True
    l.append(i)
    for j in g[i]:
        if(not Visited[j]):
            dfsUtil(g,N,Visited,j,v1)
        elif (v1[j]):
            ans=True
    v1[i]=False
def dfs(g,N):
    global l,ans
    ans=False
    l=[]
    Visited=[False]*N
    for i in range(N):
        if(not Visited[i]):
            v1=[False]*N
            dfsUtil(g,N,Visited,i,v1)
            if(ans):
                break
    return ans
def isCyclic(n, graph):
    # print(graph,n)
    return dfs(graph,n)