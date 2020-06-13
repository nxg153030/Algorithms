from datastructures import PriorityQueue
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class Character:
    def __init__(self, key: str = '', freq: int = 0):
        self.key = key
        self.freq = freq

    def __lt__(self, node):
        return self.freq < node.freq

    def __gt__(self, node):
        return self.freq > node.freq

    def __str__(self):
        return f'Character: {self.key}, freq: {self.freq}'


def huffman(C):
    """
    :param C: list of characters
    :return:
    """
    n = len(C)
    queue = PriorityQueue(C) # create a leaf node for each character, and add them to the priority queue
    queue.build_min_heap()
    for i in range(0, n-1):
        new_node = Character()
        new_node.left = queue.heap_extract_min()
        new_node.right = queue.heap_extract_min()
        new_node.freq = new_node.left.freq + new_node.right.freq
        queue.min_heap_insert(new_node)

    return queue.heap_extract_min()


if __name__ == '__main__':
    # TODO: figure out how to pass the list of characters into the algorithm
    # TODO: What am i trying to output?
    l = [Character(key='a', freq=5), Character(key='b', freq=10), Character(key='c', freq=15), Character(key='d', freq=4)]
    print(huffman(l))
