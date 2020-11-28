import numpy as np


class NegativeWeightCycleException(Exception):
    def __init__(self, message=None, errors=None):
        message = "Negative weight cycle detected, no solution exists." if message is not None else message
        super().__init__(message)
        self.errors = errors


class Node:
    def __init__(self, node_id: int, distance: float, predecessor):
        self.id = node_id
        self.distance = distance  # distance from source node represented as a float
        self.path = []
        self.predecessor = predecessor


class Graph:
    def __init__(self, adj_matrix, weight_matrix):
        self.weight_matrix = weight_matrix
        self.adj_matrix = adj_matrix
        self.nodes = []


class BellmanFord:
    def __init__(self, adj_matrix, weight_matrix):
        """
        Solves the single source shortest path problem for graphs
        in which edge weights may be negative
        """
        self.num_vertices = len(adj_matrix)
        self.graph = Graph(adj_matrix, weight_matrix)
        self.shortest_path = []

    def initialize_single_source(self):
        self.graph.nodes = [Node(node_id=i, distance=np.inf, predecessor=None) for i in range(self.num_vertices)]
        self.graph.nodes[0].distance = 0
        self.graph.nodes[0].path.append(0)

    def relax(self, u, v):
        if self.graph.nodes[v].distance > self.graph.nodes[u].distance + self.graph.weight_matrix[u][v]:
            self.graph.nodes[v].distance = self.graph.nodes[u].distance + self.graph.weight_matrix[u][v]
            self.graph.nodes[v].predecessor = u

    def print_shortest_path(self):
        for i in range(self.num_vertices):
            print(f'Predecessor of Node {i}: {self.graph.nodes[i].predecessor}')

    def run(self):
        self.initialize_single_source()
        for _ in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if self.graph.adj_matrix[i][j] == 1:
                        self.relax(i, j)

        # negative cycle check
        for i in range(1, self.num_vertices):
            for j in range(self.num_vertices):
                # triangle inequality check
                if self.graph.adj_matrix[i][j] == 1 and (self.graph.nodes[j].distance >
                                                         self.graph.nodes[i].distance + self.graph.weight_matrix[i][j]):
                    raise NegativeWeightCycleException()


if __name__ == '__main__':
    w_matrix = np.array([[0, 6, 0, 0, 7],
                         [0, 0, 5, -4, 8],
                         [0, -2, 0, 0, 0],
                         [2, 0, 7, 0, 0],
                         [0, 0, -3, 9, 0]])

    a_matrix = np.array([[0, 1, 0, 0, 1],
                         [0, 0, 1, 1, 1],
                         [0, 1, 0, 0, 0],
                         [1, 0, 1, 0, 0],
                         [0, 0, 1, 1, 0]])
    bellman_ford = BellmanFord(adj_matrix=a_matrix, weight_matrix=w_matrix)
    bellman_ford.run()
    bellman_ford.print_shortest_path()
