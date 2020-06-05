from math import floor


def merge(A, start, mid, end):
    left = A[start:mid]
    right = A[mid:end]
    i = 0
    j = 0
    for k in range(start, end):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        mid = floor((p + r) / 2)
        merge_sort(A, p, mid)
        merge_sort(A, mid + 1, r)
        merge(A, p, mid, r)


if __name__ == '__main__':
    A = [20, 10, 30, 5, 6, 12]
    merge_sort(A, 0, len(A))
    print(A)

