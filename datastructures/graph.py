from typing import List
from enum import Enum
import numpy as np


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class Graph:
    def __init__(self, adjacency_list: List):
        self.adjacency_list = adjacency_list
        self.vertices = list()
        self._create_graph()

    def __iter__(self):
        pass

    class Vertex:
        def __init__(self, _id: int, color: Enum, predecessor=None, distance=0):
            self.id = _id
            self.color = color
            self.predecessor = predecessor
            self.distance = distance

        def __str__(self):
            return f'Node({self.id})'

    def _create_graph(self):
        for i in range(len(self.adjacency_list)):
            self.vertices.append(Graph.Vertex(_id=i+1, color=Color.WHITE, predecessor=None, distance=np.inf))

