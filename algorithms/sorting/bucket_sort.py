from math import floor
from itertools import chain
from typing import List


def insertion_sort(arr: List):
    for i in range(1, len(arr)):
        key = A[i]
        j = i - 1
        # insert A[i] into the sorted sequence A[0..i-1]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j+1] = key


def bucket_sort(arr):
    """
    Bucket sort assumes that the input is drawn from a uniform distribution
    and has an average case runtime of O(n)

    :return:
    """
    max_val = max(arr)
    buckets = [[] for _ in range(0, len(arr))]
    n = len(arr)
    for num in arr:
        idx = floor(num / max_val)
        buckets[idx].append(num)

    for i in range(0, n):
        insertion_sort(buckets[i])

    return list(chain(*buckets))


if __name__ == '__main__':
    A = [10, 5, 2, 3, 1, 7, 8, 9, 6, 4]
    output = bucket_sort(A)
    print(output)