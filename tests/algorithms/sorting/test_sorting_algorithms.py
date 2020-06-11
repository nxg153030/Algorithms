from algorithms.sorting import bubble_sort, bucket_sort, counting_sort, heapsort, merge_sort, Quicksort, radix_sort
import pytest


input_arr = [[50, 10, 40, 30, 60, 70], [10, 5, 3, 1, 6, 4, 7, 8, 9, 2]]


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_bubble_sort(test_input, expected):
    bubble_sort(test_input)
    # print(input_data)
    assert test_input == expected


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_bucket_sort(test_input, expected):
    assert bucket_sort(test_input) == expected


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_counting_sort(test_input, expected):
    counting_sort(test_input)
    assert test_input == expected


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_heapsort(test_input, expected):
    heapsort(test_input)
    assert test_input == expected


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_merge_sort(test_input, expected):
    merge_sort(test_input, 0, len(test_input))
    assert test_input == expected


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_quicksort(test_input, expected):
    assert Quicksort(test_input).arr == expected


@pytest.mark.parametrize("test_input, expected",
                         [(input_arr[0], sorted(input_arr[0])), (input_arr[1], sorted(input_arr[1]))])
def test_radix_sort(test_input, expected):
    radix_sort(test_input, d=2)
    assert test_input == expected
