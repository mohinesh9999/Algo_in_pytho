from collections import deque,defaultdict
from collections import deque
def bfs(g,N):
    d=deque([0])
    v=[False]*N
    l=[]
    while(d):
        x=d.popleft()
        if(not v[x]):
            l.append(x)
        v[x]=True
        for i in g[x]:
            if(not v[i]):
                d.append(i)
    return l
    # code here

G=defaultdict(list)
for i in range(5):
    u,v=list(map(int,input().split()))
    G[u].append(v)