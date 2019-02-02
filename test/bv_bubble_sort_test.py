import pytest
from src.bv_bubble_sort import bubble_sort


def test_bubble_sort1():
    unsorted_array = [6, 5, 4, 3, 2, 1]
    assert bubble_sort(unsorted_array) == [1, 2, 3, 4, 5, 6]


def test_bubble_sort2():
    unsorted_array = [55, 22, 75, 24, 10, 100, 5000, 48, 1, 5]
    assert bubble_sort(unsorted_array) == [
        1, 5, 10, 22, 24, 48, 55, 75, 100, 5000]


def test_bubble_sort_already_sorted_array():
    unsorted_array = [1, 2, 3, 4, 5]
    assert bubble_sort(unsorted_array) == [1, 2, 3, 4, 5]

def test_bubble_sort_partially_sorted_array():
    unsorted_array = [2, 3, 1, 4, 5]
    assert bubble_sort(unsorted_array) == [1, 2, 3, 4, 5]
