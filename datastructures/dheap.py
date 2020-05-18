from typing import List
from math import floor, ceil, log2
import time
import logging
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class DHeap:
    """
    Generalized implementation of a heap, where all non-leaf nodes have d children
    """
    def __init__(self, A: List, num_children):
        self.A = A
        self.num_children = num_children
        self.heap_size = len(self.A)

    def __len__(self):
        return len(self.A)

    def __str__(self):
        return str(self.A[:self.heap_size])

    def __setitem__(self, idx, data):
        self.A[idx] = data

    def __getitem__(self, idx):
        return self.A[idx]

    @staticmethod
    def parent(i, num_children):
        return floor((i - 1) / num_children)

    @staticmethod
    def height(heap_size, num_children, node_idx):
        if (2 * node_idx) + 1 >= heap_size:
            return 0
        for n in range(num_children):
            if (2 * node_idx) + (n + 1) < heap_size:
                return 1 + DHeap.height(heap_size, num_children, (2 * node_idx) + (n + 1))

    @staticmethod
    def depth(node_idx, num_children):
        if node_idx == 0:
            return 0
        return 1 + DHeap.depth(DHeap.parent(node_idx, num_children), num_children)

    def max_heapify(self, i):
        current_node_level_dict = {}
        for n in range(self.num_children):
            if (2 * i) + (n + 1) < self.heap_size:
                current_node_level_dict.update({(2 * i) + (n + 1): self.A[(2 * i) + (n + 1)]})
        current_node_level_dict.update({i: self.A[i]})
        largest = max(current_node_level_dict, key=current_node_level_dict.get)
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        converts a list into a max binary heap
        """
        for i in range(floor(len(self.A) / 2), -1, -1):
            self.max_heapify(i)

    def min_heapify(self, i):
        current_node_level_dict = {}
        for n in range(self.num_children):
            if (2 * i) + (n + 1) < self.heap_size:
                current_node_level_dict.update({(2 * i) + (n + 1): self.A[(2 * i) + (n + 1)]})
        current_node_level_dict.update({i: self.A[i]})
        smallest = min(current_node_level_dict, key=current_node_level_dict.get)
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        """
        converts a list into a min binary heap
        """
        for i in range(floor(len(self.A) / 2), -1, -1):
            self.min_heapify(i)

    @staticmethod
    def visualize_heap(heap):
        G = nx.Graph()
        # get the depth for all the nodes
        # then plot the nodes by depth
        node_depth_mappings = [[] for _ in range(ceil(log2(len(heap))))]
        print(node_depth_mappings)
        for i in range(len(heap)):
            depth = DHeap.depth(i, heap.num_children)
            node_depth_mappings[depth].append(heap[i])
        print(node_depth_mappings)
        x, y = (10, 15)
        for depth, mapping in enumerate(node_depth_mappings):
            if len(mapping) > 0:
                for node_idx, node in enumerate(mapping):
                    if depth > 0 and node_idx == 0:
                        x -= 0.5
                    G.add_node(node, pos=(x, y))
                    x += 0.5
                y -= 0.5

        for i, elem in enumerate(heap):
            for n in range(heap.num_children):
                if (heap.num_children * i) + (n + 1) < heap.heap_size:
                    print(f'Adding edge between {elem} and {heap[(heap.num_children * i) + (n + 1)]}')
                    G.add_edge(elem, heap[(heap.num_children * i) + (n + 1)])

        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G, pos, with_labels=True)
        plt.show()

    @staticmethod
    def _visualize_heap(heap):
        G = nx.Graph()
        x, y = (5, 8)
        for i in range(heap.heap_size):
            # node_height = DHeap.height(heap.heap_size, heap.num_children, i)
            # if node_height == 3:
            #     y = 9
            #     x = 5
            if i == 0:
                G.add_node(heap[i], pos=(x, y))
                G.add_node(heap[(2 * i) + 1], pos=(4.5, 7.5))
                G.add_node(heap[(2 * i) + 2], pos=(5.5, 7.5))
            elif i == 1:
                G.add_node(heap[(2 * i) + 1], pos=(3, 7))
                G.add_node(heap[(2 * i) + 2], pos=(4, 7))
            elif i == 2:
                G.add_node(heap[(2 * i) + 1], pos=(5, 7))
                G.add_node(heap[(2 * i) + 2], pos=(6, 7))
            elif i == 3:
                G.add_node(heap[(2 * i) + 1], pos=(1, 6.5))
                G.add_node(heap[(2 * i) + 2], pos=(2, 6.5))
            elif i == 4:
                G.add_node(heap[(2 * i) + 1], pos=(3, 6.5))

        for i, elem in enumerate(heap):
            for n in range(heap.num_children):
                if (2 * i) + (n + 1) < heap.heap_size:
                    print(f'Adding edge between {elem} and {heap[(2 * i) + (n + 1)]}')
                    G.add_edge(elem, heap[(2 * i) + (n + 1)])

        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx(G, pos, with_labels=True)
        plt.show()


if __name__ == "__main__":
    A = [1, 2, 3, 4, 7, 5, 6, 10, 9, 8, 15, 20, 35, 44]
    start = time.time()
    dheap = DHeap(A, num_children=5)
    dheap.build_min_heap()
    print(f'max {dheap.num_children}-heap: {str(dheap)}')
    LOGGER.debug(str(dheap))
    end = time.time()
    LOGGER.debug(f'Time taken to heapify list of {len(A)} elements: {end - start} seconds')
    DHeap.visualize_heap(dheap)