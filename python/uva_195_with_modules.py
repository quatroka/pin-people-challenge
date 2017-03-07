""" File to resolve UVa problem 195 - Anagram. """

from itertools import permutations
from array import array


def get_permutation_list(letters_sequence):
    """Receive a letters sequence return your permutation.

    Receive a letters sequence in string format, convert
    that in a list of characters, create a list of
    permutation these lisf of characters, remove duplicate
    and returns this list sorted. """
    letters_sequence = list(letters_sequence)

    list_of_permutaions = array.frombytes(permutations(letters_sequence))
    list_of_permutaions = array.frombytes(map(lambda x: ''.join(x), list_of_permutaions))
    list_of_permutaions = array.frombytes(set(list_of_permutaions))
    list_of_permutaions.sort()

    return list_of_permutaions


N_CASES = int(input())

RESULT_LIST = array('l')
for case in range(0, N_CASES):
    permutation_list = get_permutation_list(input())
    RESULT_LIST.append(permutation_list)

for items in RESULT_LIST:
    for item in items:
        print(item)
