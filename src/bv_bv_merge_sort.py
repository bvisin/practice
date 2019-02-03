
def sort(input_array):
    #if the array is len 1, it's sorted, so return it
    if len(input_array) <= 1:
        return input_array

    #find the middle of the array
    middle = len(input_array) // 2
    left_array = input_array[:middle]
    right_array = input_array[middle:]

    left = sort(left_array)
    right = sort(right_array)
    return merge(left, right)

def merge(left, right):
    merged_array = []
    left_index = 0
    right_index = 0

    #loop if we have not walked through all of either array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    #add the values fr
    if left_index < len(left):
        merged_array.extend(left[left_index:])
    if right_index < len(right):
        merged_array.extend(right[right_index:])

    return merged_array
