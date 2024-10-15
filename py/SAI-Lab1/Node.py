import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations


class Node:
    "Узел в дереве поиска"
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action,
                             path_cost=path_cost)

    def __repr__(self): return '<{}>'.format(self.state)

    def __len__(self): return 0 if self.parent is None else (1 +
                                                             len(self.parent))

    def __lt__(self, other): return self.path_cost < other.path_cost

failure = Node('failure', path_cost=math.inf) # Алгоритм не смог найти решение.
cutoff = Node('cutoff', path_cost=math.inf) # Указывает на то, что поиск с итеративным углублением был прерван.


def expand(problem, node):
    "Раскрываем узел, создав дочерние узлы."
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)


def path_actions(node):
    "Последовательность действий, чтобы добраться до этого узла."
    if node.parent is None:
        return []
    return path_actions(node.parent) + [node.action]


def path_states(node):
    "Последовательность состояний, чтобы добраться до этого узла"
    if node in (cutoff, failure, None):
        return []
    return path_states(node.parent) + [node.state]