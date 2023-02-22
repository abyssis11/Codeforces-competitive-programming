n, m = [int(x) for x in input().split(' ')]
grid = [[0]*n for x in range(n)]
INF = 99999
for _ in range(m):
    g1, g2, w = [int(x) for x in input().split(' ')]
    grid[g1-1][g2-1] = w
    grid[g2-1][g1-1] = w

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0 and i != j:
            grid[i][j] = INF

selected = [0] * n
Nedges = 0
cost = 0
selected[0] = 1

while(Nedges < n-1):
    minimum = INF
    x = 0
    y = 0
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and grid[i][j] != 0:
                    if minimum > grid[i][j]:
                        minimum = grid[i][j]
                        x = i
                        y = j
    Nedges += 1
    selected[y] = True
    cost += grid[x][y]

if sum(selected) < n:
    print('IMPOSSIBLE')
else:
    print(cost)
    


