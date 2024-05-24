from unittest import TestCase

from task4 import getArray, getMedian, steps


class TestGetArray(TestCase):
    def test_getArray(self):
        self.assertEqual([1, 10, 2, 9], getArray(
            '/home/user_dmitrii/dev/test/Performance-Lab/task4/file.txt'))


class TestGetMedian(TestCase):
    def test_two_identical_elements(self):
        self.assertEqual(getMedian([5, 5]), 5)

    def test_two_different_elements(self):
        self.assertEqual(getMedian([1, 3]), 2)

    def test_two_negative_elements(self):
        self.assertEqual(getMedian([-5, -3]), -4)

    def test_positive_and_negative_elements(self):
        self.assertEqual(getMedian([-1, 1]), 0)

    def test_two_large_elements(self):
        self.assertEqual(getMedian([1000000, 1000002]), 1000001)


class TestStepsFunction(TestCase):
    def test_steps_with_positive_integers(self):
        nums = [1, 2, 3, 4, 5]
        median = 3
        self.assertEqual(steps(nums, median), 6)

    def test_steps_with_negative_integers(self):
        nums = [-5, -4, -3, -2, -1]
        median = -3
        self.assertEqual(steps(nums, median), 6)

    def test_steps_with_mixed_integers(self):
        nums = [-1, 0, 1]
        median = 0
        self.assertEqual(steps(nums, median), 2)

    def test_steps_with_single_element(self):
        nums = [10]
        median = 10
        self.assertEqual(steps(nums, median), 0)

    def test_steps_with_identical_elements(self):
        nums = [5, 5, 5, 5]
        median = 5
        self.assertEqual(steps(nums, median), 0)

    def test_steps_with_float_median(self):
        nums = [4, 4, 5, 5]
        median = 4.5
        self.assertEqual(steps(nums, median), 2)
