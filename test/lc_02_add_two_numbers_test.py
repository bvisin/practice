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


def test_add_two_numbers_not_equal_length_lists():

    l1 = ListNode(0)
    l1.next = ListNode(1)

    l2 = ListNode(0)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)

    rtn = add_two_numbers(l1, l2)

    assert rtn.val == 0
    assert rtn.next.val == 2
    assert rtn.next.next.val == 2

def test_add_two_lists_where_two_is_empty():

    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)

    l2 = None

    rtn = add_two_numbers(l1, l2)

    assert rtn.val == 0
    assert rtn.next.val == 1
    assert rtn.next.next.val == 2

def test_add_two_lists_extra_cary():

    l1 = ListNode(9)
    l1.next = ListNode(9)

    l2 = ListNode(1)

    rtn = add_two_numbers(l1, l2)

    assert rtn.val == 0
    assert rtn.next.val == 0
    assert rtn.next.next.val == 1

def test_add_two_lists_where_one_is_empty():

    l1 = None

    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)

    rtn = add_two_numbers(l1, l2)

    assert rtn.val == 1
    assert rtn.next.val == 1
    assert rtn.next.next.val == 2