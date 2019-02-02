def sort(unsorted_array):

    for index in range(1, len(unsorted_array)):
        key = unsorted_array[index]

        position = index-1
        while position >= 0 and key < unsorted_array[position]:
            unsorted_array[position+1] = unsorted_array[position]
            position -= 1
        unsorted_array[position+1] = key

    return unsorted_array
