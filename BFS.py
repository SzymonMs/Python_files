import queue
def BFS(s,g,graph):
    visited = set()
    visited.add(s)
    parent = {n: None for n in graph}
    q = queue.Queue()
    q.put(s)
    parent[s] = s
    while q.empty() == False:
        cur_n = q.get()
        if cur_n == g:
            break
        for nh in graph[cur_n]:
            if nh not in visited:
                parent[nh] = cur_n
                visited.add(nh)
                q.put(nh)
    path = []
    cur_n = g
    while cur_n != s:
        path.append(cur_n)
        cur_n = parent[cur_n]
    path.append(s)
    path.reverse()
    return path

s = 2
g = 7
graph = {1: [2,3],2:[1,5],3:[1,4],4:[3,6],5:[2,6,8],6:[4,5,7,8],7:[6],8:[5,6]}
print(BFS(s,g,graph))