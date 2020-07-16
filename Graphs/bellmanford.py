#[[u,v,w],....]
def bellmanford(graph,source,n):
    d=[10**9]*n
    d[source]=0
    for i in range(n-1):
        for j in graph:
            if(d[j[1]]>d[j[0]]+j[2]):
                d[j[1]]=d[j[0]]+j[2]
    for j in graph:
            if(d[j[1]]>d[j[0]]+j[2]):
                print('negative cycyle detected')
    return d