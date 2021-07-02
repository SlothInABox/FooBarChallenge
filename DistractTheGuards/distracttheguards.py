class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if other is Vertex:
            return self.value == other.value
        else:
            return self.value == other

    def __hash__(self):
        return hash(self.value)

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
    
    def __str__(self):
        return "[%s, %s]" % (self.v, self.w)

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def __getitem__(self, *v):
        if len(v) == 1:
            v = v[0]
            for vertex in self.vertices:
                if vertex == v:
                    return vertex
            return None
        elif len(v) == 2:
            w = v[1]
            v = v[0]
            if w in v.edges:
                return v.edges[w]
            else:
                return None
        else:
            return None
    
    def add_edge(self, v, w):
        edge = self[v, w]
        if not edge:
            edge = Edge(v, w)
            v.edges[w] = edge
            w.edges[v] = edge
            self.edges.append(edge)

    def add_vertex(self, v):
        self.vertices.append(v)

    def __str__(self):
        vertex_string = []
        for vertex in self.vertices:
            edge_str = str(vertex) + ": " + ", ".join(str(edge) for edge in vertex.edges.values())
            vertex_string.append(edge_str)
        return "\n".join(vertex_string)

    def max_match(self, vertex, best_edges, marked):
        for other in vertex.edges.keys():
            if other not in marked:
                marked.append(other)

                if other not in best_edges.keys() or self.max_match(best_edges[other].other(other), best_edges, marked):
                    best_edges[other] = vertex.edges[other]
                    return True
        return False

def is_perfect(x, y):
    n = x + y
    n_prime = n

    while n_prime % 2 == 0:
        n_prime = n_prime / 2
    return(x% n_prime) != 0

def solution(banana_list):
    graph = Graph()
    for k in banana_list:
        vertex = Vertex(k)
        graph.add_vertex(vertex)

    for i in range(len(graph.vertices)):
        for j in range(i + 1, len(graph.vertices)):
            v = graph.vertices[i]
            w = graph.vertices[j]

            if is_perfect(v.value, w.value):
                graph.add_edge(v, w)

    best_edges = {}
    n_pairs = 0
    for vertex in graph.vertices:
        marked = []
        if graph.max_match(vertex, best_edges, marked):
            n_pairs += 1

    return len(banana_list) - n_pairs

if __name__ == "__main__":
    # solution([1, 7, 3, 21, 13, 19])
    print(solution([1,1]))
    print(solution([1, 7, 3, 21, 12, 19]))