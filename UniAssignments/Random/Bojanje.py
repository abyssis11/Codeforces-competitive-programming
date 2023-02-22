inp = [int(x) for x in input().split(' ')]
pupils = inp[0]
friednships = inp[1]
visited = [0] * pupils
team1 = []
team2 = []
adjList = {}
for i in range(1, pupils+1):
    adjList[i] = []

for i in range(friednships):
    inp = [int(x) for x in input().split(' ')]
    adjList[inp[0]].append(inp[1])
    adjList[inp[1]].append(inp[0])

# bojanje grafa
c = {}
for key in adjList.keys():
    c.update({key: 1})

for node, nbor in adjList.items():
    for nb in nbor:
        if c[node] == c[nb]:
            c[nb] += 1

print(' '.join(str(x) for x in c.values()))
        