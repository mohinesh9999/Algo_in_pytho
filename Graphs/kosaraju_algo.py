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
    Visited=[False]*N
    for i in range(N):
        if(not Visited[i]):
            dfsUtil(g,N,Visited,i)
from collections import defaultdict
def countSCCs (adj, V):
    # print(adj)
    global l
    dfs(adj,V)
    x=l
    l=[]
    d=defaultdict(list)
    for i in adj:
        for j in adj[i]:
            d[j].append(i)
    visited=[False]*V
    c=0
    x=x[::-1]
    # print(x)
    for i in x:
        if(not visited[i]):
            dfsUtil(d,V,visited,i)
            c+=1
    return c 