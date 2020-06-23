from algorithms.search import binary_search
import pytest


input_data = [([10, 20, 30, 40, 70, 80, 100], 20)]


@pytest.mark.parametrize("test_input, expected",
                         [(input_data[0], input_data[0][0].index(input_data[0][1]))])
def test_binary_search(test_input, expected):
    assert binary_search(test_input[0], test_input[1]) == expected
