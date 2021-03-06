"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

def two_sums_brute_force(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for numx in nums:
        for numy in nums:
            if numx + numy == target:
                return [nums.index(numx), nums.index(numy)]

    raise Exception("No two sum solution")

def two_sums_compliment(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    compliments = {}
    for index, num in enumerate(nums):
        #disable=no-else-return
        if num in compliments:
            return [compliments[num], index]
        else:
            compliments[target - num] = index

    raise Exception("No two sum solution")
