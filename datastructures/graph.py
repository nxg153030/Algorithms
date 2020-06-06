from typing import List
from enum import Enum


class Graph:
    def __init__(self, adjacency_list: List):
        self.adjacency_list = adjacency_list

    class Node:
        def __init__(self, color: Enum, predecessor=None, distance=0):
            self.color = color
            self.predecessor = predecessor
            self.distance = distance


