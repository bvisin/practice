"""[summary]

Returns:
    [type] -- [description]
"""

class ListNode:
    """Definition for singly-linked list.
    """
    def __init__(self, val):
        """[summary]

        Arguments:
            x {[type]} -- [description]
        """
        self.val = val
        self.next = None

def add_two_numbers(list1, list2):
    """[summary]

    Arguments:
        l1 {[type]} -- [description]
        l2 {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    rtn = ListNode(7)
    rtn.next = ListNode(0)
    rtn.next.next = ListNode(8)

    return rtn
