from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, c1, c2):
        self.graph[c1].append(c2)
        self.graph[c2].append(c1)

n, m = [int(x) for x in input().split(' ')]
g = Graph()
for _ in range(m):
    c1, c2 = [x for x in input().split(' ')]
    g.addEdge(c1, c2)

visited = []
stack = []

def DFS(vertex):
    visited.append(vertex)
    for v in g.graph[vertex]:
        if v not in visited:
            DFS(v)
    stack.append(vertex)

for vertex in g.graph:
    if vertex not in visited:
        DFS(vertex)

print(' '.join(x for x in stack[::-1]))