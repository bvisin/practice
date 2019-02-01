from src.bv_selection_sort import selection_sort

def test_selection_sort1():
    unsorted_array = [6,5,4,3,2,1]
    assert selection_sort(unsorted_array) == [1,2,3,4,5,6]

def test_selection_sort2():
    unsorted_array = [55,22,75,24,10,100,5000,48,1,5]
    assert selection_sort(unsorted_array) == [1,5,10,22,24,48,55,75,100,5000]
