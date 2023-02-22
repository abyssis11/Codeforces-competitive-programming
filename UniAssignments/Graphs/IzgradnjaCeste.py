n, m =  [int(x) for x in input().split(' ')]

adjList = {}
for i in range(1, n+1):
    adjList[i] = []

for _ in range(m):
    g1, g2 = [int(x) for x in input().split(' ')]
    adjList[g1].append(g2)
    adjList[g2].append(g1)

visited = []
edgeRoads = []

def DFS(vertex):
    if vertex in visited:
        return
    visited.append(vertex)
    for n in adjList[vertex]:
        DFS(n)

for i in range(1, n+1):
    if i not in visited:
        edgeRoads.append(i)
        DFS(i)

print(len(edgeRoads)-1)
for i in range(len(edgeRoads)-1):
    print(str(edgeRoads[i]) + ' ' + str(edgeRoads[i+1]))