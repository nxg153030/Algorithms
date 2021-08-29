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
        if hasattr(node, 'freq'):
            return self.freq < node.freq
        else:
            return self.freq < node

    def __gt__(self, node):
        if hasattr(node, 'freq'):
            return self.freq > node.freq
        else:
            return self.freq > node

    def __str__(self):
        return f'Character: {self.key}, freq: {self.freq}'


def huffman(characters):
    """
    Huffman codes compress data.
    greedy algorithm, optimal substructure
    If we assign a 3 bit codeword to each character, it takes 300k bits to encode a 100k character file
    What if we use variable length codes?
    prefix codes => no codeword is also a prefix of another codeword.
    :param characters: list of characters
    :return:
    """
    n = len(characters)
    queue = PriorityQueue(characters)
    queue.build_min_heap()
    for i in range(0, n-1):
        new_node = Character()
        new_node.left = queue.heap_extract_min()
        new_node.right = queue.heap_extract_min()
        new_node.freq = new_node.left.freq + new_node.right.freq
        queue.min_heap_insert(new_node)

    return queue.heap_extract_min()


if __name__ == '__main__':
    l = [Character(key='f', freq=5), Character(key='e', freq=9), Character(key='c', freq=12),
         Character(key='b', freq=13), Character(key='d', freq=16), Character(key='a', freq=45)]
    print(huffman(l))
