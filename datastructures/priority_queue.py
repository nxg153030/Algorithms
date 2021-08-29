from typing import List
from datastructures import Heap
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class PriorityQueue(Heap):
    def __init__(self, A: List):
        super(PriorityQueue, self).__init__(A)

    def heap_maximum(self):
        return self.A[0]

    def heap_minimum(self):
        return self.A[0]

    def heap_extract_min(self):
        """
        returns the max element of the heap, i.e, the root
        :return:
        """
        if self.heap_size < 1:
            raise Exception('Heap underflow')
        _min = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.min_heapify(0)
        return _min

    def heap_extract_max(self):
        """
        returns the max element of the heap, i.e, the root
        :return:
        """
        if self.heap_size < 1:
            raise Exception('Heap underflow')
        _max = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return _max

    def heap_decrease_key(self, i, key):
        """
       :param i: index of the heap element whose value will be decreased
       :param key: new value of the heap element at index i
       :return: None
        """
        if key > self.A[i]:
            raise Exception('new key is bigger than current key')

        self.A[i] = key
        while i > 0 and self.A[self.parent(i)] > self.A[i]:
            self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
            i = self.parent(i)

    def heap_increase_key(self, i, key):
        """
        :param i: index of the heap element whose value will be increased
        :param key: new value of the heap element at index i
        :return: None
        """
        if key < self.A[i]:
            raise Exception('new key is smaller than current key')

        self.A[i] = key
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            LOGGER.debug(f'parent(A[{i}]) = A[{self.parent(i)}] = {self.A[self.parent(i)]}')
            self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
            i = self.parent(i)

    def min_heap_insert(self, key):
        """
        Implements the INSERT operation of the min priority queue
        :param key: value of element to be inserted
        :return: None
         """
        self.heap_size += 1
        self.A.append(np.inf)
        self.heap_decrease_key(self.heap_size - 1, key)

    def max_heap_insert(self, key):
        """
        Implements the INSERT operation of the max priority queue
        :param key: value of element to be inserted
        :return: None
        """
        self.heap_size += 1
        self.A.append(-np.inf)
        self.heap_increase_key(self.heap_size - 1, key)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    queue = PriorityQueue(l)
    # queue.build_max_heap()
    queue.build_min_heap()
    LOGGER.debug((str(queue)))
    # queue.max_heap_insert(key=100)
    queue.min_heap_insert(key=100)
    LOGGER.debug('After inserting a new element to heap.')
    LOGGER.debug(str(queue))
    # queue.heap_increase_key(4, 17)
    queue.heap_decrease_key(7, 0.5)
    # LOGGER.debug('After increasing the value of A[4]')
    LOGGER.debug('After decreasing the value of A[7]')
    LOGGER.debug(str(queue))