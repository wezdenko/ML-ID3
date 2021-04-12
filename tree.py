
class Node:

    def __init__(self, d, edges=[]):
        self.d = d
        self.children = edges


class Leaf:

    def __init__(self, result=None):
        self.result = result


class Edge:

    def __init__(self, decision, child):
        self.decision = decision
        self.child = child
