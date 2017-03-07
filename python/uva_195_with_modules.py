""" File to resolve UVa problem 195 - Anagram. """
""" https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=131 """

from itertools import permutations


def get_permutation_list(letters_sequence):
    """Receive a letters sequence return your permutation.

    Receive a letters sequence in string format, convert
    that in a list of characters, create a list of
    permutation these lisf of characters, remove duplicate
    and returns this list sorted. """
    letters_sequence = list(letters_sequence)

    list_of_permutaions = list(permutations(letters_sequence))
    list_of_permutaions = list(map(lambda x: ''.join(x), list_of_permutaions))
    list_of_permutaions = list(set(list_of_permutaions))
    list_of_permutaions.sort()

    return list_of_permutaions


N_CASES = int(input())

RESULT_LIST = []
for case in range(0, N_CASES):
    permutation_list = get_permutation_list(input())
    RESULT_LIST.append(permutation_list)

for items in RESULT_LIST:
    for item in items:
        print(item)
