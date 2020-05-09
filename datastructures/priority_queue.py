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
    queue.build_max_heap()
    LOGGER.debug((str(queue)))
    queue.max_heap_insert(key=100)
    LOGGER.debug('After inserting a new element to heap.')
    LOGGER.debug(str(queue))
    queue.heap_increase_key(4, 17)
    LOGGER.debug('After increasing the value of A[4]')
    LOGGER.debug(str(queue))