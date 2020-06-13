from algorithms.search import depth_first_search


def topological_sort(G):
    depth_first_search(G)


def canJump(nums):
    _max = 0
    for i, num in enumerate(nums):
        if i > _max:
            return False
        _max = max(_max, i+num)
    return True


if __name__ == '__main__':
    l = [3, 2, 1, 0, 4]
    l = [2, 3, 1, 1, 4]
    l = [2, 3, 1, 1, 0, 4]
    print(canJump(l))
