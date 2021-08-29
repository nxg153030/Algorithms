from datastructures import PriorityQueue
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class Node:
    def __init__(self, left=None, right=None, freq=0):
        self.left = left
        self.right = right
        self.freq = freq

    def __lt__(self, node):
        return self.freq < node.freq

    def __gt__(self, node):
        return self.freq > node.freq


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
    Huffman codes compress data.
    greedy algorithm, optimal substructure
    If we assign a 3 bit codeword to each character, it takes 300k bits to encode a 100k character file
    What if we use variable length codes?
    prefix codes => no codeword is also a prefix of another codeword.
    :param C: list of characters
    :return:
    I can build my own file zipping algorithms! :O

    Should i build a separate tree?
    create a class for huffman codes..??
    Also want to make sure my priority queue can sort by freq
    """
    n = len(C)
    queue = PriorityQueue(C)  # create a leaf node for each character, and add them to the priority queue
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
    l = [Character(key='f', freq=5), Character(key='e', freq=9), Character(key='c', freq=12),
         Character(key='b', freq=13), Character(key='d', freq=16), Character(key='a', freq=45)]
    print(huffman(l))
