class GraphMatrix:
    def __init__(self):
        self.vertex = []
        self.index = {}
        self.matrix = []

    def add_vertex(self, v):
        if v in self.index:
            return

        self.index[v] = len(self.vertex)
        self.vertex.append(v)

        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * len(self.vertex))

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)

        i, j = self.index[v1], self.index[v2]
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def has_edge(self, v1, v2):
        if v1 not in self.index or v2 not in self.index:
            return False
        i, j = self.index[v1], self.index[v2]
        return self.matrix[i][j] == 1

def main():
    g = GraphMatrix()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")

    for fila in g.matrix:
        print(fila)
main()
