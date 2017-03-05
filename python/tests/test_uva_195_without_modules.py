""" Test File for UVa problem 195 - Anagram """

from unittest import TestCase, main
from uva_195_without_modules import is_movable, scan_movable_largest
from uva_195_without_modules import move_left, move_right, flip
from uva_195_without_modules import scan_flip
class TestPermutation(TestCase):
    """ Test class for testing permutations. """

    def test_is_movable(self):
        self.assertEqual(False, is_movable([[0, 1, 2], ['L', 'L', 'L']], 0))
        self.assertEqual(True, is_movable([[0, 1, 2], ['L', 'L', 'L']], 2))
        self.assertEqual(True, is_movable([[0, 1, 2], ['R', 'L', 'R']], 1))
        self.assertEqual(False, is_movable([[0, 1, 2], ['L', 'L', 'R']], 2))

    def test_move_right(self):
        self.assertEqual([['a', 'c', 'b'], ['L', 'L', 'R']], move_right([['a', 'b', 'c'], ['L', 'R', 'L']], 'b'))
        self.assertEqual([[2, 1, 3], ['L', 'R', 'L']], move_right([[1, 2, 3], ['R', 'L', 'L']], 1))

    def test_move_left(self):
        self.assertEqual([['a', 'c', 'b'], ['L', 'L', 'R']], move_left([['a', 'b', 'c'], ['L', 'R', 'L']], 'c'))
        self.assertEqual([[2, 1, 3], ['L', 'R', 'L']], move_left([[1, 2, 3], ['R', 'L', 'L']], 2))

    def test_scan_movable_largest(self):
        self.assertEqual(3, scan_movable_largest([[1, 2, 3], ['L', 'L', 'L']]))
        self.assertEqual(3, scan_movable_largest([[3, 2, 1], ['R', 'L', 'L']]))
        self.assertEqual(False, scan_movable_largest([[2, 1, 3], ['L', 'L', 'R']]))


    def test_flip(self):
        self.assertEqual('L', flip('R'))
        self.assertEqual('R', flip('L'))


    def test_scan_flip(self):
        self.assertEqual([[3, 2, 1], ['R', 'L', 'L']], scan_flip([[3, 2, 1], ['L', 'L', 'L']], 3))

if __name__ == '__main__':
    main()
