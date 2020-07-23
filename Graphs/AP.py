#articulation point
def APUtil(graph,i, visited, ap, parent, low, disc):
    
def AP(graph,V):
    visited = [False] * (V) 
    disc = [float("Inf")] * (V) 
    low = [float("Inf")] * (V) 
    parent = [-1] * (V) 
    ap = [False] * (V)
    for i in range(V):
        if(not visited[i]):
            APUtil(graph,i, visited, ap, parent, low, disc)