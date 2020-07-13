from collections import defaultdict
class Graph:
    def __init__(self, *args, **kwargs):
        self.graph=defaultdict(list)
    def addNode(self,u,v):
        self.graph[u].append(v)
    def printg(self):
        print(self.graph)
g=Graph()
for i in range(10):
    u,v=list(map(int,input().split()))
    g.addNode(u,v)
g.printg()