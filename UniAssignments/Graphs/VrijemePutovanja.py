grid = []
with open('Competitive-programming/UniAssignments/Graphs/input/VrijemePutovanja.txt') as f:
    n, m = [int(x) for x in f.readline().split(' ')]
    for row in f.readlines():
        grid.append([int(x) for x in row.replace('\n','').split(' ')])

for i in range(m):
    for j in range(m):
        if grid[i][j] == 0 and i != j:
            grid[i][j] = 1000

for k in range(m):
    for i in range(m):
        for j in range(m):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

for row in grid:
    print(' '.join(str(x) for x in row))