from typing import List


class Quicksort:
    """Quicksort implementation. Divide-and-conquer paradigm"""
    def __init__(self, arr: List, ascending: bool = True):
        self.arr = arr
        self.ascending = ascending

    def __str__(self):
        self._quicksort(0, len(self.arr) - 1)
        if not self.ascending:
            self.arr = self.arr[::-1]
        return str(self.arr)

    def partition(self, p, r):
        pivot = self.arr[r] # pivot element
        i = p - 1
        for j in range(p, r):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[r] = self.arr[r], self.arr[i + 1]
        # print(self.arr)
        return i + 1

    def _quicksort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self._quicksort(p, q - 1)
            self._quicksort(q + 1, r)


if __name__ == '__main__':
    A = [10, 5, 12, 13, 4, 2, 20, 18, 25, 30]
    print(A)
    print(str(Quicksort(A, ascending=True)))
    # quicksort(A, 0, len(A) - 1)
    # print(A)