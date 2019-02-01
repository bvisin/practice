from src.bv_selection_sort import selection_sort

def test_selection_sort1():
    unsorted_array = [6,5,4,3,2,1]
    assert selection_sort(unsorted_array) == [1,2,3,4,5,6]