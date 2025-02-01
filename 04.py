import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def __lt__(self, other):
        return self.val < other.val


# перероблена базова функція для додавання ребер, але тепер вже в купу
def add_edges_in_heap(graph, heap, pos, index=0, x=0, y=0, layer=1):
    if index < len(heap):
        node = heap[index]
        left = 2 * index + 1
        right = 2 * index + 2

        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла

        if left < len(heap):
            graph.add_edge(node.id, heap[left].id)
            l = x - 1 / 2**layer
            pos[heap[left].id] = (l, y - 1)
            add_edges_in_heap(graph, heap, pos, left, x=l, y=y - 1, layer=layer + 1)

        if right < len(heap):
            graph.add_edge(node.id, heap[right].id)
            r = x + 1 / 2**layer
            pos[heap[right].id] = (r, y - 1)
            add_edges_in_heap(graph, heap, pos, right, x=r, y=y - 1, layer=layer + 1)


# перероблена базова функція для відображення дерева на відображення купи
def draw_heap(heap):
    heap_in_graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    add_edges_in_heap(heap_in_graph, heap, pos)

    colors = [node[1]["color"] for node in heap_in_graph.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in heap_in_graph.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_in_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def main():
    # Створення дерева
    # використовуємо значення для вузлів з базового коду:
    # 0, 4, 5, 10, 1, 3
    # та зберігаємо у наш масив з езкземплярами класу Node з цими значеннями
    # сторюємо купу з такої структури
    my_heap = [Node(0), Node(4), Node(5), Node(10), Node(1), Node(3)]
    heapq.heapify(my_heap)

    # Відображення купи
    draw_heap(my_heap)


if __name__ == "__main__":
    main()
