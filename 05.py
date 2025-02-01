import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = None
        self.id = str(uuid.uuid4())

    def add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2**layer
                pos[node.left.id] = (l, y - 1)
                l = self.add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2**layer
                pos[node.right.id] = (r, y - 1)
                r = self.add_edges(
                    graph, node.right, pos, x=r, y=y - 1, layer=layer + 1
                )
        return graph

    def depth_first_traversal(self, colors, visited):
        if self is not None and self.id not in visited:
            visited.add(self.id)
            current_index = len(visited) - 1
            self.color = colors[current_index]

            if self.left:
                self.left.depth_first_traversal(colors, visited)
            if self.right:
                self.right.depth_first_traversal(colors, visited)

    def breadth_first_traversal(self, colors, visited):
        if not self:
            return

        queue = [(self, 0)]  # (node, level)
        visit_count = 0
        i = 0 # color index
        while queue:
            node, level = queue.pop(0)

            if node.id not in visited:
                visited.add(node.id)
                node.color = colors[i]
                self.color = node.color
                visit_count += 1

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))


    def draw_tree(self, traversal_type):
        tree = nx.DiGraph()
        pos = {self.id: (0, 0)}
        tree = self.add_edges(tree, self, pos)

        colors = []
        for i in range(15):
            colors.append((i / 15, i / 15, i / 15))

        if traversal_type == "depth":
            self.depth_first_traversal(colors, set())
            
        elif traversal_type == "breadth":
            self.breadth_first_traversal(colors, set())

        labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
        
        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=colors,
            font_color="red",
        )
        plt.show()


def main():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    root.right.right.left = Node(13)
    root.right.right.right = Node(14)

    # Відображення дерева з обходом у глибину
    root.draw_tree(traversal_type="depth")

    # Відображення дерева з обходом в ширину
    root.draw_tree(traversal_type="breadth")


if __name__ == "__main__":
    main()
