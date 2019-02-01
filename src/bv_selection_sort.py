"""[summary]

Returns:
    [type] -- [description]
"""


def selection_sort(unsorted_array):
    """[summary]

    Arguments:
        unsorted_array {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    for index, _ in enumerate(unsorted_array):

        smallest_index = index
        for next_index, _ in enumerate(unsorted_array[index:]):

            if unsorted_array[next_index + index] < unsorted_array[smallest_index]:
                smallest_index = next_index + index

        if smallest_index != index:
            current_num = unsorted_array[index]
            unsorted_array[index] = unsorted_array[smallest_index]
            unsorted_array[smallest_index] = current_num

    return unsorted_array
