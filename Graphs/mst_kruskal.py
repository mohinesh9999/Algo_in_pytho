#undirected graph
class Edge:
    def __init__(self, *args, **kwargs):
        self.u=args[0]
        self.v=args[1]
        self.w=args[2]
def kruskal(edges,v):
    edges.sort(key=lambda x:x.wt)
    parent,rank,res=[i for i in range(v)],[0]*v,0#initialization
    i,s=0,0
    while(s<v-1):
        e=edges[i]
        x,y=find(e.u,parent),find(e.v,parent)
        if(x!=y):
            res+=e.w 
            union(e.u,e.v,parent,rank)
            s+=1
        i+=1
    return res
def find(vertex,parent):
    if(parent[vertex]==vertex):
        return vertex
    return find(parent[vertex],parent)
def union(u,v,parent,rank):
    x,y=find(u,parent),find(v,parent)
    if(rank[x]>rank[y]):
        parent[y]=x
    elif(rank[y]>rank[x]):
        parent[x]=y
    else:
        rank[x]+=1
        parent[y]=x