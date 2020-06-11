from typing import List


def counting_sort(arr: List):
    """
    Counting sort assumes that the input consists on integers in a small range.
    :param arr: input array
    :return:
    """
    k = max(arr)
    C = [0] * (k + 1) # temp array
    B = [0] * len(arr)
    for j in range(len(arr)):
        C[arr[j]] += 1 # C[i] now contains the no. of elements = i

    for i in range(1, k + 1):
        C[i] += C[i - 1]  # C[i] now contains the no. of elements <= i

    for j in range(len(arr) - 1, -1, -1):
        B[C[arr[j]] - 1] = arr[j]
        C[arr[j]] -= 1

    arr[:] = B


if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    # A = [100, 40, 24, 34, 33, 12, 17]
    counting_sort(A)
    print(A)
