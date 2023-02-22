# maximum recursion depth
inp = [int(x) for x in input().split(' ')]
cities = inp[0]
roads = inp[1]
adjList = {}
visited = [0] * (cities+1)
bridges = []
for i in range(1, cities+1):
    adjList[i] = []

for i in range(roads):
    inp = [int(x) for x in input().split(' ')]
    adjList[inp[0]].append(inp[1])
    adjList[inp[1]].append(inp[0])

def DFS(i):
    if visited[i]:
        return
    visited[i] = 1
    for node in adjList[i]:
        DFS(node)


for i in range(1, cities+1):
    if not visited[i]:
        bridges.append(i)
        DFS(i)

print(len(bridges) - 1)
for i in range(len(bridges)-1):
    print(bridges[i], bridges[i+1])
