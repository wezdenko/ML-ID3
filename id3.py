from math import log
from random import choice
from tree import Node, Leaf, Edge

# Y = []    / zbiór klas
# U = []    / zbiór par uczących
# D = []    / zbiór atrybutów wejściowych


# U = [ {'x': [x1, x2, x3, ...], 'y': y1}, ... ]
# D = [ {'index': 0, 'values': [x11, x12, x13, ...]} ]


def id3(Y, D, U):
    # zwrócenie liścia gdy jest jedna klasa
    if _is_one_class(U):
        if len(U) != 0:
            return Leaf(U[0]['y'])
        return Leaf(choice(Y))

    # zwrócenie liścia gdy nie ma decyzji do rozpatrzenia
    if len(D) == 0:
        return Leaf(_most_common_class(U))

    # wybranie decyzji dla której entropia zbiorów jest największa
    d = max(D, key=lambda d: _Inf_gain(d, U))
    U = _divide_set(d, U)
    D.remove(d)

    # zwrócenie korzenia drzewa z pozostałymi decyzjami
    return Node(
        d,
        [Edge(d['values'][i], id3(Y, D, U[i])) for i in range(len(U))]
    )


def get_decisions(U):
    D = []
    num = len(U[0]['x'])

    for i in range(num):
        d = {'index': i, 'values': []}
        for u in U:
            if u['x'][i] not in d['values']:
                d['values'].append(u['x'][i])
        D.append(d)
    return D


def get_classes(U):
    Y = []
    for u in U:
        if u['y'] not in Y:
            Y.append(u['y'])
    return Y


def result(tree, data):
    if tree.__class__.__name__ == 'Leaf':
        return tree.result

    answer = data['x'][tree.d['index']]
    for edge in tree.children:
        if edge.decision == answer:
            return result(edge.child, data)


### funkcje prywatne ###

def _is_one_class(U):
    one_class = None
    for i in U:
        if one_class is None:
            one_class = i['y']
        if i['y'] != one_class:
            return False
    return True


def _count_classes(U):
    Y = []
    for i in U:
        if i['y'] not in [i['class'] for i in Y]:
            count = [j['y'] for j in U].count(i['y'])
            Y.append({'class': i['y'], 'count': count})
    return Y


def _most_common_class(U):
    return max(_count_classes(U), key=lambda i: i['count'])['class']


def _divide_set(d, U):
    Y = []
    for value in d['values']:
        Y.append([i for i in U if i['x'][d['index']] == value])
    return Y


def _Inf_gain(d, U):
    x = _I(U) - _Inf(d, U)
    return x


def _Inf(d, U):
    Y = _divide_set(d, U)
    return sum([(len(Uj) / len(U)) * _I(Uj) for Uj in Y])


def _I(U):
    Y = _count_classes(U)
    s = sum([i['count'] for i in Y])
    Y = map(lambda i: i['count'] / s, Y)
    return -sum([i * log(i) for i in Y])


def gini_index(d, U):
    Y = _divide_set(d, U)
    return sum([(len(Uj) / len(U)) * gini(Uj) for Uj in Y])

def gini(U):
    pass


U = [
    {'x': ['Sunny', 'Hot', 'High', 'Weak'], 'y': 'No'},
    {'x': ['Sunny', 'Hot', 'High', 'Strong'], 'y': 'No'},
    {'x': ['Overcast', 'Hot', 'High', 'Weak'], 'y': 'Yes'},
    {'x': ['Rainy', 'Mild', 'High', 'Weak'], 'y': 'Yes'},
    {'x': ['Rainy', 'Cool', 'Normal', 'Weak'], 'y': 'Yes'},
    {'x': ['Rainy', 'Cool', 'Normal', 'Strong'], 'y': 'No'},
    {'x': ['Overcast', 'Cool', 'Normal', 'Strong'], 'y': 'Yes'},
    {'x': ['Sunny', 'Mild', 'High', 'Weak'], 'y': 'No'},
    {'x': ['Sunny', 'Cool', 'Normal', 'Weak'], 'y': 'Yes'},
    {'x': ['Rainy', 'Mild', 'Normal', 'Weak'], 'y': 'Yes'},
    {'x': ['Sunny', 'Mild', 'Normal', 'Strong'], 'y': 'Yes'},
    {'x': ['Overcast', 'Mild', 'High', 'Strong'], 'y': 'Yes'},
    {'x': ['Overcast', 'Hot', 'Normal', 'Weak'], 'y': 'Yes'},
    {'x': ['Rainy', 'Mild', 'High', 'Strong'], 'y': 'No'},
]

D = [
    {'index': 0, 'values': ['Sunny', 'Overcast', 'Rainy']},
    {'index': 1, 'values': ['Hot', 'Mild', 'Cool']},
    {'index': 2, 'values': ['High', 'Normal']},
    {'index': 3, 'values': ['Weak', 'Strong']}
]

x = [
    ['Sunny', 'Mild', 'High', 'Strong'],
    ['Overcast', 'Mild', 'High', 'Weak'],
    ['Sunny', 'Mild', 'High', 'String']
]
