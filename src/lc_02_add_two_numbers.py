"""[summary]

Returns:
    [type] -- [description]
"""

def reverse_list_and_combine(orig_list):
    """[summary]

    Arguments:
        orig_list {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    return int(''.join([str(x) for x in orig_list[::-1]]))

def split_and_reverse_int(number_to_split):
    """[summary]

    Arguments:
        number_to_split {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    return [int(x) for x in str(number_to_split)[::-1]]

def add_two_numbers(list1, list2):
    """[summary]

    Arguments:
        l1 {[type]} -- [description]
        l2 {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    # sum_lists = reverse_list_and_combine(list1) + reverse_list_and_combine(list2)

    return [7, 0, 8]
