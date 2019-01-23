import unittest
import pytest
from src import lc_01_two_sums


class TwoSumsBruteForce(unittest.TestCase):

    def test_two_sums(self):
        nums = [2, 7, 11, 15]
        target = 9
        assert lc_01_two_sums.two_sums_brute_force(nums, target) == [0, 1]

    def test_two_sums_exception(self):
        nums = [2, 7, 11, 15]
        target = 10
        self.assertRaises(Exception, lc_01_two_sums.two_sums_brute_force, nums, target)


    def test_two_sums_expanded(self):
        nums = [1, 3, 4, 5, 2, 7, 11, 15]
        target = 16
        assert lc_01_two_sums.two_sums_brute_force(nums, target) == [0, 7]

class TwoSumsDict(unittest.TestCase):

    def test_two_sums(self):
        nums = [2, 7, 11, 15]
        target = 9
        assert lc_01_two_sums.two_sums_compliment(nums, target) == [0, 1]

    def test_two_sums_exception(self):
        nums = [2, 7, 11, 15]
        target = 10
        with pytest.raises(Exception):
            lc_01_two_sums.two_sums_compliment(nums, target)


    def test_two_sums_expanded(self):
        nums = [1, 3, 4, 5, 2, 7, 11, 15]
        target = 16
        assert lc_01_two_sums.two_sums_compliment(nums, target) == [0, 7]

