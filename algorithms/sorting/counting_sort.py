from math import ceil, log2


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


def max_subarray(arr):
    max_sum = arr[0]
    temp_sum = max_sum
    for i in range (1, len(arr)):
        temp_sum = max(arr[i], arr[i] + temp_sum)
        max_sum = max(temp_sum, max_sum)

    return max_sum


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return [-1, -1]

    def bisect_left(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return l if nums[l] == target else -1

    return [bisect_left(nums, target), bisect_right(nums, target)]


if __name__ == '__main__':
    # arr = [2, 5, 3, 0, 2, 3, 0, 3]
    # A = [100, 40, 24, 34, 33, 12, 17]
    # counting_sort(arr)
    # print(arr)
    arr = [5, 5, 5, 7, 7, 7, 7, 8, 8, 8, 10]
    # print(max_subarray(arr))
    # print(searchRange(arr, target=5))
    n = 3
    print(getMoneyAmountdp(n))
