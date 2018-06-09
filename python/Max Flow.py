from queue import Queue

def bfs(RG,src,sink):
    parent = {v:None for v in RG}
    dist = {v:None for v in RG}
    
    que = Queue()
    que.put(src)
    dist[src] = 0
    while not que.empty():
        u = que.get()
        if u==sink: break
        for v in RG[u]:
            if RG[u][v]==0: continue
            if dist[v]==None:
                que.put(v)
                dist[v] = dist[u]+1
                parent[v] = u
                
    if dist[sink]==None: return -1
    ans = []
    while parent[sink]!=None:
        ans.append((parent[sink],sink))
        sink = parent[sink]
    return ans

def maxFlow(G,src,sink):
    RG = {v:{} for v in G}
    for u in G:
        for v in G[u]:
            RG[u][v] = G[u][v]
            RG[v][u] = 0
    
    while True:
        path = bfs(RG,src,sink)
        if path==-1: break
        cf = min(RG[u][v] for u,v in path)
        for (u,v) in path:
            RG[u][v] -= cf
            RG[v][u] += cf
    
    return {(u,v):G[u][v]-RG[u][v] for u in G for v in G[u]} #sum(G[0][v]-RG[0][v] for v in G[0])

G = {
    0:{1:16,2:13},
    1:{3:12},
    2:{1:4,4:14},
    3:{2:9,5:20},
    4:{3:7,5:4},
    5:{},
    }
"""
G = {
    0:{1:7,2:14,3:9},
    1:{2:10,5:15},
    2:{4:13},
    3:{2:3,4:6},
    4:{1:8,6:11},
    5:{6:18},
    6:{}
    }"""

print(maxFlow(G,0,5))














