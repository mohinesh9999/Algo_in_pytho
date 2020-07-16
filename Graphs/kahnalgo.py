#cycle detection
from collections import deque,defaultdict
def kahn(g,n):
    indegree=[0]*n
    d=deque([])
    for i in range(n):
        for j in g[i]:
            indegree[j]+=1
        if(indegree[i]==0):
            d.append(i)
    c=0
    while(d):
        x=d.popleft()
        #print(x) u will get topological sort
        c+=1
        for i in g[x]:
            indegree[i]-=1
            if(indegree[i]==0):
                deque.append(i)
    return c!=n