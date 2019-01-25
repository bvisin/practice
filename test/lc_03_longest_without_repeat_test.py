import pytest

from src.lc_03_longest_without_repeating import solution

def test_example_1():

    test_in = "abcabcbb"
    test_out = 3
    assert solution(test_in) == test_out

def test_example_2():

    test_in = "bbbbb"
    test_out = 1
    assert solution(test_in) == test_out

def test_example_3():

    test_in = "pwwkew"
    test_out = 3
    assert solution(test_in) == test_out