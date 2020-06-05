from datastructures import Heap, PriorityQueue


class Character:
    def __init__(self, freq: int):
        self.freq = freq


def huffman(C):
    """
    :param C: set of characters
    :return:
    """
    n = len(C)
    queue = PriorityQueue(list(C))
    queue.build_min_heap()
    for i in range(0, n-1):
        new_node =
