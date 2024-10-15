import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations


FIFOQueue = deque
LIFOQueue = list
class PriorityQueue:
    """Очередь, в которой элемент с минимальным значением f(item) всегда
    выгружается первым."""
    def __init__(self, items=(), key=lambda x: x):
        self.key = key
        self.items = [] # a heap of (score, item) pairs
        for item in items:
            self.add(item)

    def add(self, item):
        """Добавляем элемент в очередь."""
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        """Достаем и возвращаем элемент с минимальным значением
        f(item)."""
        return heapq.heappop(self.items)[1]

    def top(self): return self.items[0][1]

    def __len__(self): return len(self.items)