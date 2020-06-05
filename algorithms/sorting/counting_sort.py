def counting_sort(A):
    """
    Counting sort assumes that the input consists on integers in a small range.
    :param A: input array
    :return:
    """
    k = max(A)
    C = [0] * (k + 1) # temp array
    B = [0] * len(A)
    for j in range(len(A)):
        C[A[j]] += 1 # C[i] now contains the no. of elements = i

    for i in range(1, k + 1):
        C[i] += C[i - 1]  # C[i] now contains the no. of elements <= i

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    A[:] = B


if __name__ == '__main__':
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    # A = [100, 40, 24, 34, 33, 12, 17]
    counting_sort(arr)
    print(arr)
