from typing import List
from datastructures import Heap


def heapsort(arr: List):
    heap = Heap(arr)
    heap.build_max_heap()
    for i in reversed(range(1, heap.heap_size)):
        heap[0], heap[i] = heap[i], heap[0]
        heap.heap_size -= 1
        heap.max_heapify(0)


if __name__ == '__main__':
    A = [20, 1, 34, 23, 15, 10, 5, 6, 3, 9]
    heapsort(A)
    print(A)