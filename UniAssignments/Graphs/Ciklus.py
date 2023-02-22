n, m = [int(x) for x in input().split(' ')]
adjList = {}
for i in range(1, n+1):
    adjList[i] = []

for _ in range(m):
    c1, c2, w =[int(x) for x in input().split(' ')]
    adjList[c1].append([c2, w])

visted = []
ciklus = []
#isCiklus

def DFS(vertex, cw = 0):
    #if vertex in ciklus:
        #ciklus.append(vertex)
    #if vertex in visted:
        #if vertex == visted[0]:
            #print(vertex)
            #visted.append(vertex)
        #return
    #ciklus.append(vertex)
    visted.append(vertex)
    for v in adjList[vertex]:
        DFS(v[0])


for i in range(1, n+1):
    DFS(i)
    print(visted)
    visted = []