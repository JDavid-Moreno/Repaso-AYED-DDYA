class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

    def add_edge(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append((v2, weight))

    def has_vertex(self, v):
        return v in self.adjacency_list

    def get_neighbors(self, v):
        if not self.has_vertex(v):
            return []
        return self.adjacency_list[v]

    def has_edge(self, v1, v2):
        for neighborn, weight in self.adjacency_list.get(v1, []):
            if neighborn == v2:
                return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list:
            new_list = []
            for n, w in self.adjacency_list[v1]:
                if n != v2:
                    new_list.append((n, w))
            self.adjacency_list[v1] = new_list

    def remove_vertex(self, v):
        if v in self.adjacency_list:
            self.adjacency_list.pop(v)
            for vertex in self.adjacency_list:
                new_list = []
                for n, w in self.adjacency_list[vertex]:
                    if n != v:
                        new_list.append((n, w))
                self.adjacency_list[vertex] = new_list

    def vertex_count(self):
        return len(self.adjacency_list)

    def edge_count(self):
        total = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return total

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor, weight in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def get_weight(self, v1, v2):
        for neighbor, weight in self.adjacency_list.get(v1, []):
            if neighbor == v2:
                return weight
        return None

def main():
    g = Graph()
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 3)
    print(g.adjacency_list)
    g.remove_vertex("A")
    print(g.adjacency_list)


main()
