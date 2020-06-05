from math import floor
import numpy as np
from itertools import chain


def insertion_sort(arr):
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
    n = arr.shape[0]
    buckets = [[] for _ in range(0, n)]

    for i in range(1, n):
        buckets[floor(n * arr[i])].append(arr[i])

    for i in range(0, n):
        insertion_sort(buckets[i])

    return list(chain(*buckets))


if __name__ == '__main__':
    A = np.random.uniform(0, 1, 10)
    print(A.shape[0])
    bucket_sort(A)
    print(A)