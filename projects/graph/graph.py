"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

            for next_vert in self.get_neighbors(v):
                if next_vert not in visited:
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)
                visited.add(v)

            for next_vert in self.get_neighbors(v):
                if next_vert not in visited:
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in visited:
            return

        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.vertices[starting_vertex]:
            self.dft_recursive(v)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v[-1] not in visited:
                if v[0] == starting_vertex and v[-1] == destination_vertex:
                    return v
                visited.add(v[-1])

            for next_vert in self.vertices[v[-1]]:
                v_list = list(v)
                v_list.append(next_vert)
                q.enqueue(v_list)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v[-1] not in visited:
                if v[0] == starting_vertex and v[-1] == destination_vertex:
                    return v
                visited.add(v[-1])

            for next_vert in self.vertices[v[-1]]:
                v_list = list(v)
                v_list.append(next_vert)
                s.push(v_list)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        result = None

        if len(path) == 0:
            path.append(starting_vertex)

        if path[0] == starting_vertex and path[-1] == destination_vertex:
            return path

        next_vertex = path[-1]

        for v in self.vertices[next_vertex]:
            if v not in path:
                new_path = list(path)
                new_path.append(v)

                found = self.dfs_recursive(
                    starting_vertex, destination_vertex, new_path
                )

                if not result:
                    result = found
                elif len(result) > len(found):
                    result = found

        return result


# g = Graph()
# g.add_vertex(99)
# g.add_vertex(3)
# g.add_vertex(3490)
# g.add_edge(99, 3)
# g.add_edge(99, 3490)
# g.add_edge(3, 99)

# print(g.get_neighbors(99))

# g.add_edge("0", "4") # raises an exception

"""Breadth-First Traversal"""

# g.bft(3490)
# g.bft(99)
# g.bft(3)

"""Depth-First Traversal"""

# g.dft(3490)
# g.dft(99)
# g.dft(3)

"""Depth-First Traversal Recursive"""

# g.dft_recursive(3490)
# g.dft_recursive(99)
# g.dft_recursive(3)

"""---**----***----**---"""

"""Breadth-First Search"""

# g.bfs(3, 3490)

"""Depth-First Search"""

# g.dfs(3490)

"""Depth-First Search Recursive"""

# g.dfs_recursive(3490)


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    # graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    # graph.dft(1)
    # graph.dft_recursive(1)

    # """
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # """
    # print(graph.bfs(1, 6))

    # """
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # """
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
