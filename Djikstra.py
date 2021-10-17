import queue

def Djikstra(s,g,graph):
    visited = set()
    cost = {n: float('inf') for n in graph}
    parent = {s: None}
    q = queue.PriorityQueue()
    q.put((0, s))
    cost[s] = 0
    while not q.empty():
        (_, cur_n) = q.get()
        if cur_n in visited == False:
            break
        visited.add(cur_n)
        if cur_n == g:
            break
        for (nh, distance) in graph[cur_n]:
            if nh in visited:
                continue
            old_cost = cost[nh]
            new_cost = cost[cur_n] + distance
            if new_cost < old_cost:
                cost[nh] = new_cost
                parent[nh] = cur_n
                q.put((new_cost, nh))
    path = []
    cur_n = g
    while cur_n is not None:
        path.append(cur_n)
        cur_n = parent[cur_n]
    path.reverse()
    return path

s=1
g=8
graph = {1: [(2,1),(3,1)],2:[(1,1),(5,7)],3:[(1,1),(4,2)],4:[(3,2),(6,1)],
         5:[(2,7),(6,3),(8,2)],6:[(4,1),(5,3),(7,5),(8,6)],
         7:[(6,5)],8:[(5,2),(6,6)]}
print(Djikstra(s,g,graph))

