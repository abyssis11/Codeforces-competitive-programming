with open('Competitive-programming/UniAssignments/Graphs/input/OkruzeneRegije.txt') as f:
    m = [int(x) for x in f.readline().split(' ')][0]
    grid = [x for x in [x.split(' ') for x in f.read().split('\n')]]

def osvoji(i, j):
    if i < 0 or j < 0 or i >= m or j >= m:
        return
    elif grid[i][j] == 'O':
        grid[i][j] = '#'
        osvoji(i, j+1)
        osvoji(i, j-1)
        osvoji(i+1, j)
        osvoji(i-1, j)

for i in range(m):
    for j in range(m):
        if grid[i][j] == 'O' and (i == 0 or j == 0 or i == m-1 or j == m-1):
            osvoji(i, j)

for i in range(m):
    for j in range(m):
        if grid[i][j] == 'O':
            grid[i][j] = 'X'
        elif grid[i][j] == '#':
            grid[i][j] = 'O'

for row in grid:
    print(' '.join(x for x in row))