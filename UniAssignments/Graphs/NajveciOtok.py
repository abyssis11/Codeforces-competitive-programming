grid = []
with open('Competitive-programming/UniAssignments/Graphs/input/NajveciOtok.txt') as f:
    m, n = [int(x) for x in f.readline().split(' ')]
    for line in f:
        grid.append([int(x) for x in line.split(' ')])

otokSizes = []
acc = 0

def isOtok(i, j, acc):
    if i < 0 or j < 0 or i >= m or j >= n:
        return
    elif grid[i][j] == 1:
        otokSizes[acc] += 1
        grid[i][j] = '0'
        isOtok(i, j+1, acc)
        isOtok(i, j-1, acc)
        isOtok(i+1, j, acc)
        isOtok(i-1, j, acc)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            otokSizes.append(0)
            isOtok(i, j, acc)
            acc += 1

print(max(otokSizes))

