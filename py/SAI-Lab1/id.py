import time
from collections import defaultdict
from Problem import Problem
from Node import Node, failure, path_states
from Queue import PriorityQueue


# Список городов и расстояний между ними (без повторов)
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
    ('Летняя Ставка', 'Овощи'): 10.2,
    ('Чур', 'Овощи'): 12.8,
    ('Овощи', 'Горный'): 21.9,
    ('Камбулат', 'Малые Ягуры'): 9.8,
    ('Малые Ягуры', 'Казгулак'): 19.3,
    ('Казгулак', 'Ясный'): 40.9,
}


class TSP(Problem):
    """Класс для решения задачи коммивояжера."""

    def __init__(self, start, finish):
        super().__init__(initial=start, goal=finish)
        self.graph = self.build_graph()

    def build_graph(self):
        """Построение графа городов на основе списка расстояний."""
        graph = defaultdict(list)
        for (city1, city2), dist in distances.items():
            graph[city1].append((city2, dist))
            graph[city2].append((city1, dist))  # Двусторонняя связь
        return graph

    def actions(self, state):
        """Возвращает соседние города и расстояние до них."""
        #print('action', self.graph[state], state)
        return self.graph[state]


    def result(self, state, action):
        """Переход в следующий город."""
        return action[0]

    def action_cost(self, state, action, result):
        """Возвращает стоимость перехода."""
        return action[1]


# Функция для поиска решения задачи коммивояжера
def search_TSP(problem):
    border = PriorityQueue([Node(problem.initial)])  # Очередь с приоритетом
    path = set()

    while border:
        node = border.pop()
        if problem.is_goal(node.state):
            return path_states(node), node.path_cost

        path.add(node.state)

        for city, cost in problem.actions(node.state):
            child = Node(city, node, path_cost=node.path_cost + cost)
            if child.state not in path:
                border.add(child)

    return failure


# Инициализация задачи
problem = TSP('Красный Маныч','Чур')

# Запуск поиска и замер времени
start_time = time.time()
route, total_distance = search_TSP(problem)
end_time = time.time()

# Вывод результатов
if route:
    print(f"Минимальный маршрут: {' -> '.join(route)}")
    print(f"Общее расстояние: {total_distance} км")
else:
    print("Маршрут не найден.")

print(f"Время выполнения: {end_time - start_time:.4f} секунд")
