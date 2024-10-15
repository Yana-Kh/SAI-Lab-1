import heapq
import math
import time
from Problem import Problem
from Node import Node, failure, expand, path_actions, path_states
from Queue import PriorityQueue
from collections import deque

# Обновленный список городов и расстояний между ними
distances = {
    ('Красный Маныч', 'Новокучерлинский'): 11.8,
    ('Красный Маныч', 'Сабан-Антуста'): 10.9,
    ('Красный Маныч', 'Голубиный'): 2.3,
    ('Красный Маныч', 'Каменная Балка'): 13.8,
    ('Новокучерлинский', 'Ясный'): 20.3,
    ('Сабан-Антуста', 'Каменная Балка'): 15.3,
    ('Сабан-Антуста', 'Кендже-Кулак'): 7.1,
    ('Голубиный', 'Каменная Балка'): 11.1,
    ('Кендже-Кулак', 'Шарахалсун'): 12.9,
    ('Шарахалсун', 'Кучерла'): 7.2,
    ('Кучерла', 'Мирное'): 14.9,
    ('Кучерла', 'Таврический'): 13.2,
    ('Куликовы Копани', 'Маштак-Кулак'): 14.9,
    ('Маштак-Кулак', 'Летняя Ставка'): 9.0,
    ('Летняя Ставка', 'Ясный'): 26.1,
    ('Чур', 'Овощи'): 12.8,
    ('Овощи', 'Горный'): 21.9,
    ('Камбулат', 'Малые Ягуры'): 9.8,
    ('Малые Ягуры', 'Казгулак'): 19.3,
    ('Казгулак', 'Ясный'): 40.9,
}



# Функция для получения расстояния между городами
def get_distance(city1, city2):
    return distances.get((city1, city2)) or distances.get((city2, city1), float('inf'))


class TSPProblem(Problem):
    """Класс для решения задачи коммивояжёра."""

    def __init__(self, initial, goal):
        super().__init__(initial=initial, goal=goal)
        self.cities = list(distances.keys())
        print(self.cities)

    def actions(self, state):
        """Возвращает возможные действия - соседние города."""
        return [city for city in distances.keys() if state in city]

    def result(self, state, action):
        """Возвращает следующий город, в который переходит коммивояжер."""
        return action[1] if state == action[0] else action[0]

    def action_cost(self, state, action, result):
        """Возвращает стоимость перехода между городами."""
        return get_distance(state, result)


# Инициализация задачи
problem = TSPProblem(initial='Кучерла', goal='Ясный')


# Поиск решения методом полного перебора
def search_tsp(problem):
    frontier = PriorityQueue([Node(problem.initial)])  # Исправление: удален лишний кортеж
    explored = set()

    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return path_states(node), node.path_cost

        explored.add(node.state)
        for child in expand(problem, node):
            if child.state not in explored:
                frontier.add(child)

    return failure


# Замер времени выполнения
start_time = time.time()

# Запуск поиска
route, distance = search_tsp(problem)

# Вывод результатов
end_time = time.time()
execution_time = end_time - start_time

print(f"Минимальный маршрут: {route}")
print(f"Расстояние: {distance} км")
print(f"Время выполнения программы: {execution_time:.4f} секунд")