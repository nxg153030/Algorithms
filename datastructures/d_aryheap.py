from typing import List
from math import floor
import time
import logging

logging.basicConfig(level=logging.DEBUG)
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


if __name__ == "__main__":
    # A = [-10, -20, -30, -40, -50, -60]
    # A = [-1, -2, -3, -4, -7, -8, -9, -10, -14, -16]
    # A = random.sample(range(10,1000), 10)
    # start = time.time()
    # heapify(A)
    # print(A)
    # end = time.time()
    # print(f'Time taken to heapify list of {len(A)} elements: {end-start} seconds')
    # A = OffsetList([1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
    A = [20, 1, 34, 23, 15, 10, 5, 6, 3, 9]
    A = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    start = time.time()
    heap = DHeap(A, num_children=5)
    heap.build_min_heap()
    LOGGER.debug(str(heap))
    end = time.time()
    LOGGER.debug(f'Time taken to heapify list of {len(A)} elements: {end - start} seconds')