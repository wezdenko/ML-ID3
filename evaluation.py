from id3 import id3, get_decisions, get_classes, result
from random import shuffle


# walidacja krzyżowa na zbiorze "U" z "k" podziałami
def evaluate(U, k):
    D = get_decisions(U)
    Y = get_classes(U)

    shuffle(U)
    U = divide(U, k)

    evaluation = []
    for i in range(k):
        tree = id3(Y, D, substract(U, U[i]))
        evaluation.append(avg_loss(tree, U[i]))

    return sum(evaluation) / k


def divide(U, k):
    Y = [[] for i in range(k)]

    for i, elm in enumerate(U):
        Y[i % k].append(elm)
    return Y


def substract(U1, U2):
    U = []
    for i in U1:
        if i != U2:
            U += i
    return U


def avg_loss(tree, U):
    results = []
    for i in U:
        if result(tree, i) == i['y']:
            results.append(1)
        else:
            results.append(0)

    return sum(results) / len(results)
