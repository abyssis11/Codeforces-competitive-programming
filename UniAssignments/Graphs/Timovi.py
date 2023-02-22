""" adjList = {}
with open('Competitive-programming/UniAssignments/Graphs/input/Timovi.txt') as f:
    n, m =  [int(x) for x in f.readline().split(' ')]
    for i in range(1, n+1):
        adjList[i] = []
    for line in f:
        g1, g2 = [int(x) for x in line.split(' ')]
        adjList[g1].append(g2)
        adjList[g2].append(g1) """

adjList = {}
n, m = [int(x) for x in input().split(' ')]
for i in range(1, n+1):
    adjList[i] = []

for _ in range(m):
    f1, f2 = [int(x) for x in input().split(' ')]
    adjList[f1].append(f2)
    adjList[f2].append(f1)

team= [True] * n
visted = []
possible = True

def DFS(vertex, p = 0):
    global possible
    for v in adjList[vertex]:
        if v != p:
            if v not in visted:
                team[v-1] = not team[vertex-1]
                visted.append(v)
                DFS(v, vertex)
            else:
                if team[v-1] == team[vertex-1]:
                    possible = False

for i in range(1, n+1):
    if not possible:
        break
    if i not in visted:
        visted.append(i)
        DFS(i)

if possible:
    print(' '.join('1' if i else '2' for i in team))
else:
    print('IMPOSSIBLE')
            