""" Test File for UVa problem 195 - Anagram """

from unittest import TestCase, main
from uva_195_with_modules import get_permutation_list

class TestPermutation(TestCase):
    """ Test class for testing permutations. """

    def test_get_amount_results(self):
        """ Test if method get_amount_results returns the
        correct permutation amount. """
        self.assertEqual(6, len(get_permutation_list('abc')))
        self.assertEqual(24, len(get_permutation_list('abcd')))
        self.assertEqual(1, len(get_permutation_list('aaa')))
        self.assertEqual(3, len(get_permutation_list('aab')))


    def test_permutation_list(self):
        """ Test if method get_permutation_list returns the
        permutation list corretily."""
        self.assertEqual(['aaa'], get_permutation_list('aaa'))
        self.assertEqual(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],
                         get_permutation_list('abc'))


if __name__ == '__main__':
    main()
