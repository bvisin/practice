import pytest

from src.lc_02_add_two_numbers import add_two_numbers

def test_add_two_numbers():

    l1 = [2, 4, 3]
    l2 = [6, 6, 4]
    rtn = [7, 0, 8]
    assert add_two_numbers(l1, l2) == rtn


