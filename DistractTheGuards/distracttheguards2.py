class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __eq__(self, other):
        if type(other) == Vertex:
            return self.value == other.value
        else:
            return self.value == other

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w
    
    def other(self, v):
        if v == self.v:
            return self.w
        elif v == self.w:
            return self.v
        else:
            return None

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.size = 0

    def add_vertex(self, v):
        self.vertices.append(v)
        self.size = len(self.vertices)

    def add_edge(self, v, w):
        edge = Edge(v, w)
        v.edges.append(w)
        w.edges.append(v)
        self.edges.append(edge)

    def greedy_matching(self, initial_matching=None):
        matching = {}
        if initial_matching:
            for i in initial_matching:
                matching[i] = initial_matching[i]
        
        avail = {}
        has_edge = False
        for vertex in self.vertices:
            if vertex not in matching:
                avail[v] = {}
                for w in v.edges:
                    if w not in matching:
                        avail[v][w] = (v, w)
                        has_edge = True
                if not avail[v]:
                    del avail[v]
        if not has_edge:
            return matching

        deg1 = {v for v in avail if len(avail[v]) == 1}
        deg2 = {v for v in avail if len(avail[v]) == 2}
        d2edges = []

        def update_degree(v):
            if v in deg1:
                deg1.remove(v)
            elif v in deg2:
                deg2.remove(v)
            
            if len(avail[v]) == 0:
                del avail[v]
            elif len(avail[v]) == 1:
                deg1.add(v)
            elif len(avail[v]) == 2:
                deg2.add(v)

        def add_match(v, w):
            p, q = avail[v][w]
            matching[p] = q
            matching[q] = p

            for i in avail[v].keys():
                if i != w:
                    del avail[i][v]
                    update_degree(i)
            for i in avail[w].keys():
                if i != v:
                    del avail[i][w]
                    update_degree(i)
            avail[v] = avail[w] = {}
            update_degree(v)
            update_degree(w)

        def contract(v):
            u, w = avail[v]
            d2edges.extend([avail[v][u], avail[v][w]])
            del avail[u][v]
            del avail[w][v]

            if len(avail[u]) > len(avail[w]):
                u, w = w, u
            
            for i in avail[u].keys():
                del avail[i][u]
                if i in avail[w]:
                    update_degree(i)
                elif i != w:
                    avail[i][w] = avail[w][i] = avail[u][i]
            avail[u] = avail[v] = {}
            update_degree(u)
            update_degree(v)
            update_degree(w)
        
        while avail:
            if deg1:
                v = arbitrary_item(deg1)
                
    
    def matching(self, initial_matching = None):
        pass


def is_perfect(v, w):
    n = v.value + w.value

    while n % 2 == 0:
        n = n / 2

    return (v.value % n) != 0

def solution(banana_list):
    banana_graph = Graph()
    for i in range(len(banana_list)):
        vertex = Vertex(banana_list[i])
        banana_graph.add_vertex(vertex)
    
    for i in range(banana_graph.size):
        for j in range(i + 1, banana_graph.size):
            v, w = banana_graph.vertices[i], banana_graph.vertices[j]
            if is_perfect(v, w):
                banana_graph.add_edge(v, w)
                pass

if __name__ == "__main__":
    solution([1, 7, 3, 21, 12, 19])