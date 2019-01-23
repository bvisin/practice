import pytest

from src.lc_02_add_two_numbers import add_two_numbers
from src.lc_02_add_two_numbers import reverse_list_and_combine
from src.lc_02_add_two_numbers import split_and_reverse_int

def test_add_two_numbers():

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    rtn = [7, 0, 8]
    assert add_two_numbers(l1, l2) == rtn

def test_add_two_lists_of_nonequal_length():

    l1 = [0, 1]
    l2 = [0, 1, 2]
    rtn = [0, 2, 2]
    assert add_two_numbers(l1, l2) == rtn

def test_add_two_lists_where_one_is_empty():

    l1 = [0, 1, 2]
    l2 = []
    rtn = [0, 1, 2]
    assert add_two_numbers(l1, l2) == rtn

def test_add_two_lists_extra_cary():

    l1 = [9, 9]
    l2 = [1]
    rtn = [0, 0, 1]
    assert add_two_numbers(l1, l2) == rtn

def test_add_two_lists_where_two_is_empty():

    l1 = []
    l2 = [0, 1, 2]
    rtn = [0, 1, 2]
    assert add_two_numbers(l1, l2) == rtn

def test_reverse_list_and_combine():
    l1 = [2, 4, 3]
    rtn = 342

    assert reverse_list_and_combine(l1) == rtn

def test_split_and_reverse_int():
    test_input = 807
    test_output = [7,0,8]

    assert split_and_reverse_int(test_input) == test_output
