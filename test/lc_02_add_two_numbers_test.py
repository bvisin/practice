import pytest

from src.lc_02_add_two_numbers import add_two_numbers
from src.lc_02_add_two_numbers import reverse_list_and_combine
from src.lc_02_add_two_numbers import split_and_reverse_int

def test_add_two_numbers():

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    rtn = [7, 0, 8]
    assert add_two_numbers(l1, l2) == rtn

def test_reverse_list_and_combine():
    l1 = [2, 4, 3]
    rtn = 342

    assert reverse_list_and_combine(l1) == rtn

def test_split_and_reverse_int():
    test_input = 807
    test_output = [7,0,8]

    assert split_and_reverse_int(test_input) == test_output
