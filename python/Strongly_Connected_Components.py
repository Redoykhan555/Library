def SCC(graph):
    T = 0
    index = {k:-1 for k in graph}
    mlink = {k:99999999999 for k in graph}
    stack = []
    ANS = []
    def findaSCC(v):
        nonlocal T
        T+=1
        index[v] = T
        mlink[v] = T        
        stack.append(v)
        for ch in graph[v]:
            if index[ch]==-1:
                findaSCC(ch)
                mlink[v] = min(mlink[ch],mlink[v])

            elif ch in stack: #WARNING:O(N)
                mlink[v] = min(mlink[v],index[ch])

        if mlink[v]==index[v]:
            ans = [stack.pop()]
            while ans[-1]!=v: ans.append(stack.pop())
            ANS.append(ans)
            print(v,index[v],mlink[v])

    for v in graph:
        if index[v]==-1:
            findaSCC(v)

    return ANS


graph = {
    'a': ['b','d'],
    'b': ['c'],
    'c': ['a'],
    'd':['e'],
    'e':['d']
}

print(SCC(graph))
