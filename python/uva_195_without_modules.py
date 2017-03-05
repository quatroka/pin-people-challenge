from itertools import permutations

def get_permutation_list(letters_sequence):
    letters_sequence = list(letters_sequence)

    list_of_permutaions = list(permutations(letters_sequence))
    list_of_permutaions = list(map(lambda x: ''.join(x), list_of_permutaions))
    list_of_permutaions = list(set(list_of_permutaions))
    list_of_permutaions.sort()

    return list_of_permutaions


def is_movable(lista, item):
    index_item = lista[0].index(item)
    movimento = lista[1][index_item]

    if movimento == 'L' and index_item == 0:
        return False
    elif movimento == 'R' and index_item == (len(lista[0]) - 1):
        return  False

    return True


def move_right(lista, item):
    item_index = lista[0].index(item)
    lista[0][item_index], lista[0][item_index + 1] = lista[0][item_index + 1], lista[0][item_index]
    lista[1][item_index], lista[1][item_index + 1] = lista[1][item_index + 1], lista[1][item_index]

    return lista


def move_left(lista, item):
    item_index = lista[0].index(item)
    lista[0][item_index], lista[0][item_index - 1] = lista[0][item_index - 1], lista[0][item_index]
    lista[1][item_index], lista[1][item_index - 1] = lista[1][item_index - 1], lista[1][item_index]

    return lista


def scan_movable_largest(lista):
    max_item = max(lista[0])
    if is_movable(lista, max_item):
        return max_item
    return False


def flip(item):
    if item is 'L':
        return 'R'
    return 'L'


def scan_flip(lista, item_moved):
    item_index = lista[0].index(item_moved)
    if is_movable(lista, item_moved) is False:
        lista[1][item_index] = flip(lista[1][item_index])
    return lista


def generator(lista):
    maior_item = scan_movable_largest(lista)
    if is_movable(lista, maior_item):
        item_index = lista[0].index(maior_item)
        if lista[1][item_index] == 'L':
            lista = move_left(lista, maior_item)
            lista = scan_flip(lista, maior_item)
        elif lista[1][item_index] == 'R':
            lista = move_right(lista, maior_item)
            lista = scan_flip(lista, maior_item)

    return lista

#gerar lista para fazer as permutações
# stringa = list(input())
# lista = []
# lista.append(stringa)
# lista.append([])

# for i in range(0, len(stringa)):
#     lista[1].append('L')



# lista = get_permutation_list('abcdef')
# count = 0
# for item in lista:
#     index = item.index('a')
#     if index == 0:
#         count += 1

# print(count)
