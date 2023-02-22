m, n = [int(x) for x in input().split(' ')]
grid = []
for _ in range(m):
    grid.append([int(x) for x in input().split(' ')])

def isOtok(i, j):
    if i < 0 or j < 0 or i >= m or j >= n:
        return
    elif grid[i][j] == 1:
        grid[i][j] = 0
        isOtok(i, j+1)
        isOtok(i, j-1)
        isOtok(i+1, j)
        isOtok(i-1, j)
    else:
        return
    
numOtoka = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            numOtoka += 1
            isOtok(i, j)

print(numOtoka)

'''
input:
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Output: 3
'''