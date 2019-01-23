import pytest

from src.lc_02_add_two_numbers import ListNode
from src.lc_02_add_two_numbers import add_two_numbers

def test_add_two_numbers():

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    rtn = add_two_numbers(l1, l2)

    assert rtn.val == 7
    assert rtn.next.val == 0
    assert rtn.next.next.val == 8

# def test_add_two_lists_of_nonequal_length():

#     l1 = [0, 1]
#     l2 = [0, 1, 2]
#     rtn = [0, 2, 2]
#     l1 = ListNode(0, ListNode(1))
#     l2 = ListNode(0, ListNode(1, ListNode(2)))
#     rtn = ListNode(7, ListNode(0, ListNode(8)))
#     assert add_two_numbers(l1, l2) == rtn

# def test_add_two_lists_where_one_is_empty():

#     l1 = [0, 1, 2]
#     l2 = []
#     rtn = [0, 1, 2]
#     assert add_two_numbers(l1, l2) == rtn

# def test_add_two_lists_extra_cary():

#     l1 = [9, 9]
#     l2 = [1]
#     rtn = [0, 0, 1]
#     assert add_two_numbers(l1, l2) == rtn

# def test_add_two_lists_where_two_is_empty():

#     l1 = []
#     l2 = [0, 1, 2]
#     rtn = [0, 1, 2]
#     assert add_two_numbers(l1, l2) == rtn

# def test_reverse_list_and_combine():
#     l1 = [2, 4, 3]
#     rtn = 342

#     assert reverse_list_and_combine(l1) == rtn

# def test_split_and_reverse_int():
#     test_input = 807
#     test_output = [7,0,8]

#     assert split_and_reverse_int(test_input) == test_output
