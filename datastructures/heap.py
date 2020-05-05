from typing import List
from math import floor
from heapq import heapify


class OffsetList(list):
    def __init__(self, init=[], offset=-1):
        super(OffsetList, self).__init__(init)
        self.offset = offset

    def __setitem__(self, key, value):
        return super(OffsetList, self).__setitem__(key + self.offset, value)

    def __getitem__(self, key):
        return super(OffsetList, self).__getitem__(key + self.offset)

    def __delitem__(self, key):
        return super(OffsetList, self).__delitem__(key + self.offset)

    def index(self, *args):
        return super(OffsetList, self).index(*args) - self.offset


class Heap:
    def __init__(self, A: List):
        self.A = A
        self.heap_size = len(self.A)

    def __len__(self):
        return len(self.A)

    def __str__(self):
        return str(self.A)

    def __setitem__(self, idx, data):
        self.A[idx] = data

    def __getitem__(self, idx):
        return self.A[idx]

    def parent(self, i):
        return floor(i / 2)

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
            temp = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = temp
            self.max_heapify(largest)

    def build_max_heap(self):
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
        for i in range(floor(len(self.A) / 2), -1, -1):
            self.min_heapify(i)


if __name__ == "__main__":
    A = OffsetList([10, 20, 30, 40, 50, 60])
    A = [-10, -20, -30, -40, -50, -60]
    A = [-1, -2, -3, -4, -7, -8, -9, -10, -14, -16]
    heapify(A)
    print(A)
    A = [10, 20, 30, 40, 50, 60]
    A = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    # A = OffsetList([1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
    heap = Heap(A)
    heap.build_max_heap()
    print(str(heap))
    heap.build_min_heap()
    print(str(heap))