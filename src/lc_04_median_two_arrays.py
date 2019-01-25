"""[summary]
"""

import math

def solution(nums1, nums2):
    """[summary]
    """
    combined_array = nums1 + nums2
    combined_array.sort()
    print(combined_array)
    median_index = math.floor((len(combined_array)-1)/2)

    return combined_array[median_index]
