class Node:
    def __init__(self, parent, children=None):
        self.parent = parent
        self.children = children
        self.left = None
        self.right = None


class FibonacciHeap:
    def __init__(self):
        self.root_list = []
        self.min = None
        self.n = 0

    def make_heap(self):
        return FibonacciHeap()

    def insert(self, x):
        x.degree = 0
        x.parent = None
        x.children = None
        x.mark = False
        if not self.root_list:
            self.root_list.append(x)
            self.min = x
        else:
            self.root_list.append(x)
            if x.val < self.min.val:
                self.min = x
        self.n += 1

    def minimum(self):
        return self.min

    def extract_min(self):
        z = self.min
        if not z:
            for child in z.children:
                self.root_list.append(child)
                child.parent = None
            self.root_list.remove(z)
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return z

    def union(self, heap1, heap2):
        merged_heap = self.make_heap()
        merged_heap.min = heap1.min
        merged_heap.root_list = merged_heap.root_list + heap2.root_list
        if not heap1.min or (heap2.min is not None and heap2.min.val < heap1.min.val):
            merged_heap.min = heap2.min
        merged_heap.n = heap1.n + heap2.n

        return merged_heap

    def consolidate(self):
        pass

    def decrease_key(self):
        pass

    def delete(self):
        pass