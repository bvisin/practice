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
    dummy = ListNode(0)
    current = dummy
    primary = list1
    secondary = list2
    carry = 0

    while primary or secondary:
        added_sum = (primary.val if primary else 0) + (secondary.val if secondary else 0) + carry
        mod = int(added_sum % 10)
        current.next = ListNode(mod)
        current = current.next
        carry = int(int(added_sum) / 10)
        primary = (primary.next if primary else None)
        secondary = (secondary.next if secondary else None)

    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next
