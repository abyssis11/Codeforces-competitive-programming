import random
def make_adj_dict(n):
    g = {}
    for i in range(0, n):
        neighbours = random.sample(range(0, n), random.randint(1, n//4)) # 
        neighbours = [str(x) for x in neighbours]
        g.update({str(i): neighbours})
    return g

def BFS(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([i for i in graph[vertex] if i not in list(visited)])
    
    return visited

g = make_adj_dict(50)

# ako postoji cvor do svih cvorova
all_nodes = set(g.keys())
centralni_nod = []
for node in g.keys():
    visited = BFS(g, node)
    if visited == all_nodes:
        centralni_nod.append(node)

print(centralni_nod)
