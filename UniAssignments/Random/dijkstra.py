from queue import PriorityQueue

class Graph:
    def __init__(self, n):
        self.v = n
        self.edges = [[-1 for i in range(n)] for j in range(n)]
        self.visited = []

    def add_edge(self, i, j, w):
        self.edges[i][j] = w
        self.edges[j][i] = w

def dijkstra(graph, start):
    sp = {v:float('inf') for v in range(graph.v)}
    sp[start]=0

    pq=PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, current) = pq.get()
        graph.visited.append(current)

        # za svakog susjeda 
        for nbor in range(graph.v):
            # ako nije -1
            if graph.edges[current][nbor] != -1:
                # sta je onda
                distance = graph.edges[current][nbor]
                # ako nije vec posjecen
                if nbor not in graph.visited:
                    # stari podatak u sp za tog susjeda
                    old = sp[nbor]
                    # novi je jednak cvoru + distanic
                    new = sp[current] + distance
                    # ako je novi manji
                    if new < old:
                        # dodaj novu distancu i susjeda u pq
                        pq.put((new, nbor))
                        # nova vrijednost u sp za to susjeda
                        sp[nbor] = new

    return sp