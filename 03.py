import heapq
import random


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if weight is None:
            weight = 0
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))

    def dijkstra(self, start):
        distances = {vertex: float("infinity") for vertex in self.vertices}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            cur_dist, cur_vert = heapq.heappop(priority_queue)

            if cur_dist > distances[cur_vert]:
                continue

            for neighbor, weight in self.vertices[cur_vert]:
                distance = cur_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def main():
    my_G = Graph()

    # Додамо 12 вершин
    vertices = [f"Vertex {i}" for i in range(1, 13)]
    for vertex in vertices:
        my_G.add_vertex(vertex)

    # Додамо ребра між вершинами випадковим чином у кількості від 1 до 3
    # ваги також додаємо випадковим чином значеннями від 1 до 5
    for i in range(len(vertices)):
        connections = random.sample(range(len(vertices)), random.randint(1, 3))
        for j in connections:
            if i != j:
                weight = random.randint(1, 5)
                my_G.add_edge(vertices[i], vertices[j], weight)

    # Тестування Дейкстри з випадковою вершиною для старту
    start = "Vertex " + str(random.randint(1, 12))
    shortest_distances = my_G.dijkstra(start)

    print(f"Для вершини '{start}' найкоротші відстані наступні: ")
    for i in shortest_distances:
        print(f"├─ '{i}'\t{shortest_distances[i]}")


if __name__ == "__main__":
    main()
