from typing import List
from math import floor
from heapq import heapify
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class Heap:
    def __init__(self, A: List):
        self.A = A
        self.heap_size = len(self.A)

    def __len__(self):
        return len(self.A)

    def __str__(self):
        return str(self.A[:self.heap_size])

    def __setitem__(self, idx, data):
        self.A[idx] = data

    def __getitem__(self, idx):
        return self.A[idx]

    def parent(self, i):
        return floor((i - 1) / 2)

    def left(self, i):
        return (2 * i) + 1

    def right(self, i):
        return (2 * i) + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
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
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.A[r] < self.A[smallest]:
            smallest = r
        if smallest != i:
            temp = self.A[i]
            self.A[i] = self.A[smallest]
            self.A[smallest] = temp
            self.min_heapify(smallest)

    def build_min_heap(self):
        """
        converts a list into a min binary heap
        """
        for i in range(floor(len(self.A) / 2), -1, -1):
            self.min_heapify(i)


if __name__ == "__main__":
    A = [-10, -20, -30, -40, -50, -60]
    A = [-1, -2, -3, -4, -7, -8, -9, -10, -14, -16]
    # A = random.sample(range(10,1000), 10)
    # start = time.time()
    # heapify(A)
    # print(A)
    # end = time.time()
    # print(f'Time taken to heapify list of {len(A)} elements: {end-start} seconds')
    # A = OffsetList([1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
    A = [20, 1, 34, 23, 15, 10, 5, 6, 3, 9]
    start = time.time()
    heap = Heap(A)
    heap.build_max_heap()
    for elem in heap:
        print(elem)
    LOGGER.debug(str(heap))
    end = time.time()
    LOGGER.debug(f'Time taken to heapify list of {len(A)} elements: {end - start} seconds')