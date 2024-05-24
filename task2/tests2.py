from unittest import TestCase

from task2 import getXYR, getPoints, is_point_inside_circle


class TestTask2(TestCase):
    path_XYR: str = "/home/user_dmitrii/dev/test/Performance-Lab/task2/file_XYR.txt"
    path_points: str = "/home/user_dmitrii/dev/test/Performance-Lab/task2/file_points.txt"

    def test_getXYR(self):
        self.assertEqual(getXYR(self.path_XYR), [1, 1, 5])

    def test_getPoints(self):
        self.assertEqual(getPoints(self.path_points), [(0, 0), (1, 6), (6, 6)])

    def test_is_point_inside_circle(self):
        self.assertEqual(is_point_inside_circle(1, 1, 5, 0, 0), 1)
        self.assertEqual(is_point_inside_circle(1, 1, 5, 1, 6), 0)
        self.assertEqual(is_point_inside_circle(1, 1, 5, 6, 6), 2)
