class Directed_graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append(v2)

    def has_vertex(self, v):
        return v in self.adjacency_list

    def get_neighbors(self, v):
        if not self.has_vertex(v):
            return []
        return self.adjacency_list[v]

    def has_edge(self, v1, v2):
        if not self.has_vertex(v1) or not self.has_vertex(v2):
            return False
        return v2 in self.adjacency_list[v1]

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list[v1]:
            self.adjacency_list[v1].remove(v2)

    def remove_vertex(self, v):
        if v in self.adjacency_list:
            self.adjacency_list.pop(v)
            for vertex in self.adjacency_list:
                if v in self.adjacency_list[vertex]:
                    self.adjacency_list[vertex].remove(v)

    def vertex_count(self):
        return len(self.adjacency_list)

    def edge_count(self):
        total = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return total

    def dfs(self, start):
        if start not in self.adjacency_list:
            return False
        visited = set()
        stack = [start]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

def main():
    g = Directed_graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "A")

    g.remove_vertex("A")
    print(g.adjacency_list)
main()
