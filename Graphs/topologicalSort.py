from collections import deque
l=[]
def dfsUtil(g,N,Visited,i):
    global l
    Visited[i]=True
    for j in g[i]:
        if(not Visited[j]):
            dfsUtil(g,N,Visited,j)
    l.append(i)
def dfs(g,N):
    global l
    l=[]
    x=deque([])
    Visited=[False]*N
    for i in range(N):
        if(not Visited[i]):
            dfsUtil(g,N,Visited,0)
            l=l[::-1]
            while(l):
                x.appendleft(l.pop())
            l=[]
    return x
def topoSort(n, adj):
    return dfs(adj,n)