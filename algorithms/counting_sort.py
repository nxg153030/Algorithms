def counting_sort(A, B, k):
    """
    :param A: input array
    :param B: sorted array
    :param k: All elements are integers in the range 0 to k
    :return:
    """
    C = [0] * (k + 1) # temp array
    for j in range(len(A)):
        C[A[j]] += 1 # C[i] now contains the no. of elements = i

    for i in range(1, k + 1):
        C[i] += C[i - 1]  # C[i] now contains the no. of elements <= i

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1


if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    # A = [100, 40, 24, 34, 33, 12, 17]
    k = 5
    B = [0] * len(A)
    counting_sort(A, B, k)
    print(B)
