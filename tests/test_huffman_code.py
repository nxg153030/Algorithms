import pytest
from algorithms.huffman_code import huffman, get_codeword, Character

data = [([Character(key='f', freq=5), Character(key='e', freq=9), Character(key='c', freq=12),
         Character(key='b', freq=13), Character(key='d', freq=16), Character(key='a', freq=45)])]


@pytest.mark.parametrize("test_input", data)
def test_huffman_code(test_input):
    root = huffman(test_input)
    assert get_codeword(root, 'f') == '1100'
    assert get_codeword(root, 'a') == '0'
    assert get_codeword(root, 'b') == '101'
    assert get_codeword(root, 'c') == '100'
    assert get_codeword(root, 'e') == '1101'
