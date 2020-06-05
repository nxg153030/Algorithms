from typing import List
from datastructures import Heap


def heapsort(A: List):
    heap = Heap(A)
    heap.build_max_heap()
    for i in reversed(range(1, heap.heap_size)):
        heap[0], heap[i] = heap[i], heap[0]
        heap.heap_size -= 1
        heap.max_heapify(0)
    return str(heap)


if __name__ == '__main__':
    A = [20, 1, 34, 23, 15, 10, 5, 6, 3, 9]
    print(heapsort(A))