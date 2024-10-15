import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations


class Problem:
    """Абстрактный класс для формальной задачи. Новый домен
специализирует этот класс,
переопределяя `actions` и `results`, и, возможно, другие методы.
Эвристика по умолчанию равна 0, а стоимость действия по умолчанию
равна 1 для всех состояний.
Когда вы создаете экземпляр подкласса, укажите `начальное` и
`целевое` состояния
(или задайте метод `is_goal`) и, возможно, другие ключевые слова для
подкласса."""

    def __init__(self, initial=None, goal=None, **kwds):
        self.__dict__.update(initial=initial, goal=goal, **kwds)

    def actions(self, state):        raise NotImplementedError

    def result(self, state, action): raise NotImplementedError

    def is_goal(self, state):        return state == self.goal

    def action_cost(self, s, a, s1): return 1

    def h(self, node):               return 0

    def __str__(self):
        return '{}({!r}, {!r})'.format(
            type(self).__name__, self.initial, self.goal)