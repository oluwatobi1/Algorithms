def bfs(s, adj):
    level={s:0}
    parent = {s:None}
    i=1
    frontier = [s]
    while frontier:
        nexti = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    nexti.append(v)
        frontier = nexti
        i+=1