class Graph: 
    def __init__(self, n):
        self.vertices = n
        self.edges = [[0 for i in range(n)] for j in range(n)]
        self.visited = []

    def add_edge(self, i, j, w):
        self.edges[i][j] = w
        self.edges[j][i] = w

inp = [int(x) for x in input().split(' ')]
cities = inp[0]
roads = inp[1]
g = Graph(cities)
selected = [0] * cities
n_edges = 0
INF = 9999999

for i in range(roads):
    inp = [int(x) for x in input().split(' ')]
    g.add_edge(inp[0]-1, inp[1]-1, inp[2])
    g.add_edge(inp[1]-1, inp[0]-1, inp[2])

selected[0] = 1
cost = 0
while (n_edges < cities-1):
    minimum = INF
    x = 0
    y = 0
    
    for i in range(cities):
        if selected[i]:
            for j in range(cities):
                if ((not selected[j]) and g.edges[i][j]):
                    if minimum > g.edges[i][j]:
                        minimum = g.edges[i][j]
                        x = i
                        y = j
    cost += g.edges[x][y]
    selected[y] = 1
    n_edges+=1

if sum(selected) < cities:
    print('IMPOSSIBLE')
else:
    print(cost)