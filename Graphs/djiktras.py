import heapq
def dijkstra(src, V, g):
    distance=[10**9]*V
    distance[src]=0
    pq=[(0,src)]
    s=set()
    while(pq):
        # print(pq,V)
        wt,i=heapq.heappop(pq)
        s.add(i)
        # s.discard(i)
        for j in range(V):
            # print('g')
            if(g[i][j]>0 and j not in s and distance[j]>distance[i]+g[i][j]):
                distance[j]=distance[i]+g[i][j]
                heapq.heappush(pq,(distance[j],j))
                # s.add(j)
    return distance