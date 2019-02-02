def bubble_sort(unsorted_array):
    is_sorted = False
    for index, _ in enumerate(unsorted_array):
        #break out of the sort early if we have already sorted the array
        if is_sorted:
            break
        is_sorted = True
        for sub_index, _ in enumerate(unsorted_array):
            #we assume it has been sorted
            if sub_index >= len(unsorted_array) - index - 1:
                break
            if unsorted_array[sub_index + 1] < unsorted_array[sub_index]:
                #this made a swap, so it was not sorted...we need to do another iteration to confirm it was sorted
                is_sorted = False
                current_num = unsorted_array[sub_index]
                unsorted_array[sub_index] = unsorted_array[sub_index + 1]
                unsorted_array[sub_index + 1] = current_num


    return unsorted_array
