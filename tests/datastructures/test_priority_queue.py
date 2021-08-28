import copy
import pytest
from datastructures.priority_queue import PriorityQueue

data = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16])]


@pytest.mark.parametrize("test_input", data)
def test_priority_queue_extract_min(test_input):
    queue = PriorityQueue(copy.deepcopy(test_input))
    queue.build_min_heap()
    # assert queue.heap_extract_min() == 1
    for _min in sorted(test_input):
        extracted_min = queue.heap_extract_min()
        assert extracted_min == _min


@pytest.mark.parametrize("test_input", data)
def test_priority_queue_extract_max(test_input):
    queue = PriorityQueue(copy.deepcopy(test_input))
    queue.build_max_heap()
    # assert queue.heap_extract_max() == 16
    # assert queue.heap_extract_max() == 14
    # assert queue.heap_extract_max() == 10
    for _max in sorted(test_input, reverse=True):
        extracted_max = queue.heap_extract_max()
        assert extracted_max == _max


@pytest.mark.parametrize("test_input", data)
def test_max_priority_queue_insert(test_input):
    queue = PriorityQueue(copy.deepcopy(test_input))
    queue.build_max_heap()
    queue.max_heap_insert(100)
    assert queue.heap_extract_max() == 100


@pytest.mark.parametrize("test_input", data)
def test_min_priority_queue_insert(test_input):
    queue = PriorityQueue(copy.deepcopy(test_input))
    queue.build_min_heap()
    queue.min_heap_insert(0)
    assert queue.heap_extract_min() == 0






