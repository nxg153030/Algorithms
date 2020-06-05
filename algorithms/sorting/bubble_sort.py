from typing import List


def bubble_sort(arr: List):
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                # print(arr)


if __name__ == '__main__':
    a = [15, 20, 30, 10, 50, 40]
    bubble_sort(a)
    print(a)