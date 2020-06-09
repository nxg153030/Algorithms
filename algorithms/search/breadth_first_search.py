from datastructures import Graph
import numpy as np


def breadth_first_search(G, source):
    for v in G.vertices:
        v.color = 'white'
        v.distance = np.inf
        v.predecessor = None

    source.color = 'gray'
    source.distance = 0
    source.predecessor = None
    queue = list()
    queue.append(source)
    while queue:
        curr_node = queue.pop()
        for node in G.adjacency_list[curr_node]:
            if node.color == 'white':
                node.color = 'gray'
                node.distance = curr_node.distance + 1
                node.predecessor = curr_node
                queue.insert(0, node)
        curr_node.color = 'black'


def print_path(G, source, target):
    if source.id == target.id:
        print(source)
    elif target.predecessor is None:
        print(f'No path from {str(source)} to {str(target)} exists.')
    else:
        print_path(G, source, target.predecessor)
        print(target)


if __name__ == '__main__':
    adjacency_list = []
    graph = Graph(adjacency_list)
