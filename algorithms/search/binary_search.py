from typing import List


def binary_search(arr: List[int], target: int):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    l = [10, 20, 30, 40, 50, 60]
    target_index = binary_search(l, target=51)
    print(target_index)