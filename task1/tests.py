from unittest import TestCase
from .task1 import findCircularPath, getIndex


def getIndex(index: int, current_index: int, length: int) -> int:
    return (length + current_index) % index - 1


class TestGetIndex(TestCase):
    def test_getIndex(self):
        # self.assertEqual(0, getIndex(0, 5))
        self.assertEqual(-1, getIndex(1, 0, 5))

        self.assertEqual(0, getIndex(2, 0, 5))

        self.assertEqual(1, getIndex(3, 0, 5))
        self.assertEqual(-1, getIndex(3, 1, 5))
        self.assertEqual(0, getIndex(3, -1, 5))

        self.assertEqual(0, getIndex(4, 0, 5))

        self.assertEqual(4, getIndex(6, 0, 5))
        self.assertEqual(2, getIndex(6, 4, 5))
        self.assertEqual(0, getIndex(6, 2, 5))

        self.assertEqual(3, getIndex(5, 0, 4))
        self.assertEqual(1, getIndex(5, 3, 4))
        self.assertEqual(-1, getIndex(5, 1, 4))
        self.assertEqual(2, getIndex(5, -1, 4))
        self.assertEqual(0, getIndex(5, 2, 4))

    def test_findCircularPath(self):
        self.assertEqual('1', findCircularPath(1, 5))
        self.assertEqual('14253.', findCircularPath(5, 4))
        self.assertEqual('13', findCircularPath(4, 3))
