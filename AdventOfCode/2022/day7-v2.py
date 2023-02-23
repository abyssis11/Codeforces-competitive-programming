class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = []
        self.children = []
    
    def addFile(self, size):
        self.files.append(size)

    def addChildren(self, child):
        self.children.append(child)

    def getSize(self):
        if len(self.children) != 0:
            for c in self.children:
                c.getSize()

            for c in self.children:
                self.size += c.size
            
            self.size += sum(self.files)
        else:
            self.size = sum(self.files)

root = Dir('//', None)
currentDir = root
with open("Competitive-programming/AdventOfCode/2022/input/Day7.txt") as f:
    inp = [x for x in f.read().split('\n')]

for line in inp:
    line = [x for x in line.split(' ')]
    
    if line[1] == 'cd' and line[2] == '..':
        # up
        currentDir = currentDir.parent
    elif line[1] == 'cd':
        # in
        newDir = Dir(line[2], currentDir)
        currentDir.addChildren(newDir)
        currentDir = newDir
    else:
        if line[0].isdigit():
            currentDir.addFile(int(line[0]))
        

root.getSize()
suma = 0
visited = []
def DFS(dir):
    global suma
    if dir in visited:
        return
    visited.append(dir)
    for d in dir.children:
        if d.size <= 100000:
            suma += d.size
        DFS(d)

DFS(root)
print(suma)

neededSpace = 30000000
freeSpace = 70000000 - root.size
spaceToFree = neededSpace - freeSpace
dirToDelete = float('inf')

visited = []
def DFS2(dir):
    global dirToDelete
    if dir in visited:
        return
    visited.append(dir)
    for d in dir.children:
        if d.size >= spaceToFree:
            dirToDelete = min(dirToDelete, d.size)
        DFS2(d)

DFS2(root)
print(dirToDelete)
