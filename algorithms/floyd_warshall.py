import numpy as np
import copy


class FloydWarshall:
    def __init__(self, adj_matrix, weight_matrix):
        """
        The Floyd-Warshall algorithm solves the all pairs shortest path problem in O(V^3).
        It assumes that there are no negative weight cycles.
        :param adj_matrix:
        :param weight_matrix:
        """
        self.adj_matrix = adj_matrix
        self.weight_matrix = weight_matrix
        self.num_vertices = len(self.adj_matrix)
        self.shortest_path_matrix = copy.deepcopy(weight_matrix)
        self.init_shortest_path_matrix()
        # predecessor_matrix[i][j] holds the id of the last vertex in the shortest path
        # that connects vertex i to vertex j
        self.predecessor_matrix = np.zeros((self.num_vertices, self.num_vertices))
        self.init_predecessor_matrix()

    def init_shortest_path_matrix(self):
        for i in range(len(self.weight_matrix)):
            for j in range(len(self.weight_matrix)):
                if i != j and self.weight_matrix[i][j] == 0:
                    self.shortest_path_matrix[i][j] = np.inf

    def init_predecessor_matrix(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if self.adj_matrix[i][j] == 1:
                    self.predecessor_matrix[i][j] = i + 1  # add 1 for vertex index
                else:
                    self.predecessor_matrix[i][j] = None

    def run(self):
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    self.shortest_path_matrix[i][j] = min(self.shortest_path_matrix[i][j],
                                                          self.shortest_path_matrix[i][k] +
                                                          self.shortest_path_matrix[k][j])


if __name__ == '__main__':
    a_matrix = np.array([[0, 1, 1, 0, 1],
                         [0, 0, 0, 1, 1],
                         [0, 1, 0, 0, 0],
                         [1, 0, 1, 0, 0],
                         [0, 0, 0, 1, 0]])

    w_matrix = np.array([[0.0, 3.0, 8.0, 0.0, -4.0],
                         [0.0, 0.0, 0.0, 1.0, 7.0],
                         [0.0, 4.0, 0.0, 0.0, 0.0],
                         [2.0, 0.0, -5.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 6.0, 0.0]])

    floyd_warshall = FloydWarshall(a_matrix, w_matrix)
    # print(floyd_warshall.predecessor_matrix)
    floyd_warshall.run()
    print(floyd_warshall.shortest_path_matrix)
