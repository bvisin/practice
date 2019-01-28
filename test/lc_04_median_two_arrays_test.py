from src.lc_04_median_two_arrays import solution

def test_solution():

    nums1 = [1, 3]
    nums2 = [2]

    assert solution(nums1, nums2) == 2.0

def test_solution_two():

    nums1 = [1, 2]
    nums2 = [3, 4]

    assert solution(nums1, nums2) == 2.5
