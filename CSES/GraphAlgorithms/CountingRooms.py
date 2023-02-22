# maximum recursion depth
inp =  [int(x) for x in input().split(' ')]
height = inp[0]
width = inp[1]
grid = []
visited = [[0]*width for i in range(height)]
neigborI = [1, -1, 0, 0]
neigborY = [0, 0, 1, -1]

for x in range(height):
    row = [x for x in input()]
    grid.append(row)

def isRoom(i, j):
    if i<0 or j<0 or i>=height or j>=width:
        return False
    if grid[i][j] == '#':
        return False
    return True

def DFS (i, j):
    visited[i][j] = 1
    for n in range(4):
        newI = i + neigborI[n]
        newJ = j + neigborY[n]
        if isRoom(newI, newJ) and visited[newI][newJ] == 0:
            DFS(newI, newJ)
        
    
NumOfRooms=0

for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
        if grid[i][j] == '.' and visited[i][j] == 0:
            DFS(i, j)
            NumOfRooms +=1

print(NumOfRooms)