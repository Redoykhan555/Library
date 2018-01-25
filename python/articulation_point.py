class Node:
    def __init__(self,v):
        self.v=v
        self.mates = set()
        self.vis = False
        self.num = -1
        self.low = 999999999999
        self.art = False

    def __repr__(self):
        x = str(self.par.v) if self.par else "root"
        return str(self.v)

T = 1

def dfs(v):
    global T
    v.num = T
    T+=1
    v.vis = True

    v.low = v.num
    childs_lows = []
    
    for m in v.mates:
        if not m.vis:
            childs_lows.append(dfs(m))
        else:
            v.low = min(v.low,m.num)

    v.low = min(childs_lows+[v.low])

    if v.num==1: v.art = len(childs_lows)>1 #root
    elif childs_lows and max(childs_lows)>=v.num:v.art = True
    return v.low

#-------Test----------------------------------

graph = [Node(i) for i in range(7)]
es = [(0,1),(0,3),(1,2),(2,3),(3,4),(3,5),(2,6)]
for i,j in es:
    graph[i].mates.add(graph[j])
    graph[j].mates.add(graph[i])


dfs(graph[0])
print([i.art for i in graph])
