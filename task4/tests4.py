from unittest import TestCase

from task4 import getArray, arithmeticMean, makeMove, equalityTest


class TestEqualityTest(TestCase):
    def test_equalityTest(self):
        self.assertTrue(equalityTest([2, 2, 2]))
        self.assertFalse(equalityTest([1, 2, 3, 4]))


class TestArithmeticMean(TestCase):
    def test_arithmeticMean(self):
        self.assertEqual(2.5, arithmeticMean([1, 2, 3, 4]))


class TestMakeMove(TestCase):
    def test_makeMove(self):
        self.assertEqual([1, 2, 3, 3], makeMove([1, 2, 3, 4], 2.5))
        self.assertEqual([2, 2, 3, 3], makeMove([1, 2, 3, 3], 2.25))
        self.assertEqual([2, 2, 3, 2], makeMove([2, 2, 3, 3], 2.5))
        self.assertEqual([2, 2, 2, 2], makeMove([2, 2, 2, 3], 2.25))


class TestGetArray(TestCase):
    def test_getArray(self):
        self.assertEqual([1, 10, 2, 9], getArray(
            '/home/user_dmitrii/dev/test/Performance-Lab/task4/file.txt'))
