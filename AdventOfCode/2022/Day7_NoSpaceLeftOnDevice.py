with open("AdventOfCode\/2022\input\Day7.txt") as file:
    lista = [x for x in file.read().split('\n')]

adj_list = {}
mylist = []

class Node():
    def __init__(self, name, parent=None, size=0):
        self.name=name
        self.parent=parent
        self.size=size
        if parent == None:
            self.key = name
        else:
            self.key = parent.key+self.name

    def updateSize(self, data):
        self.size+=data

def add_node(currentDirName, parentNode):
    key=parentNode.key+currentDirName
    if not any(obj.key == key for obj in mylist):
        newNode = Node(currentDirName, parentNode)
        mylist.append(newNode)
        return newNode
    else:
        for i in range(len(mylist)):
            if mylist[i].key == key:
                return mylist[i]

def add_edge(node1, node2):
  temp = []
  if node1 in mylist and node2 in mylist:
    if node1 not in adj_list:
      temp.append(node2)
      adj_list[node1] = temp
   
    elif node1 in adj_list:
      temp.extend(adj_list[node1])
      temp.append(node2)
      adj_list[node1] = temp

root = lista[0][lista[0].find(' ',3)+1:]
root = Node(root)
parent = root
ls = False
currentDir=''
for l in lista:
    if l == '$ cd ..':
        #print('$ cd ..')
        currentDir = currentDir.parent

    elif l.startswith('$ cd'):
        #print('$ cd')
        if currentDir != '':
            parent=currentDir
        ls = False
        currentDirName = l[l.find(' ',3)+1:]
        currentDir = add_node(currentDirName, parent)

    elif l == '$ ls':
        #print('$ ls')
        ls = True

    elif ls and l.startswith('dir '):
        #print('dir')
        childDirName = l.replace('dir ','')
        childDir = add_node(childDirName, currentDir)
        add_edge(currentDir, childDir)

    elif ls:
        #print('file')
        size = l.split()[0]
        currentDir.updateSize(int(size)) 


keys=list(adj_list.keys())
for i in range(len(adj_list)-1, -1, -1):
    node=keys[i]
    acc=0
    for n in adj_list[node]:
        acc+=n.size
    node.updateSize(acc)

def p1():
    acc=0
    for dir in mylist:
        if dir.size <= 100000:
            acc += dir.size
    return acc

def p2():
    freeSpace = 70000000 - mylist[0].size
    neededSpace = 30000000 - freeSpace
    acc=[]
    for dir in mylist:
        if dir.size >= neededSpace:
            acc.append(dir.size)
    return min(acc)

print(p1())
print(p2())
