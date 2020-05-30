

def counting_sort(A, place):
    k = max(A)
    C = [0] * (k + 1)  # temp array
    sorted_arr = [0] * len(A)
    for j in range(len(A)):
        C[((A[j] // place) % 10)] += 1  # C[i] now contains the no. of elements = i

    for i in range(1, k + 1):
        C[i] += C[i - 1]  # C[i] now contains the no. of elements <= i

    for j in range(len(A) - 1, -1, -1):
        sorted_arr[C[(A[j] // place) % 10] - 1] = A[j]
        C[(A[j] // place) % 10] -= 1

    # copy sorted_arr contents to input array
    for i in range(len(A)):
        A[i] = sorted_arr[i]


def radix_sort(A, d):
    """
    Radix sort sorts an array by sorting on the least significant digit first.
    It makes use of a stable sort algorithm, in this case, counting sort to sort the array on the digit.
    """
    place = 1
    for _ in range(0, d):
        counting_sort(A, place=place)
        place *= 10


if __name__ == '__main__':
    A = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(A, d=3)
    print(A)
