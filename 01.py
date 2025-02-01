import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.sorted = False

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.sorted = False

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.sorted = False

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.sorted = False

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list_v2(self):
        current = self.head
        while current:
            print(f"{str(current.data)}", end=" > " if current.next else "")
            current = current.next
        print()

    # РЕВЕРС СПИСКУ
    # Зберігаємо посилання на наступний вузол
    # Змінюємо посилання на попередній вузол
    # Пересуваємо вказівники на наступний вузол
    # Новий початок списку - останній оброблений вузол
    def reverse_linked_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # СОРТУВАННЯ ВСТАВКАМИ
    def list_sort_insertion(self):
        head = self.head
        if self is None or head.next is None:
            return self

        sorted_head = None

        while head:
            next_node = head.next

            # Вставка поточного вузла у відсортований список
            sorted_head = self.add_in_sorted(sorted_head, head)

            head = next_node

        self.head = sorted_head
        self.sorted = True

    def add_in_sorted(self, sorted_head, node):
        if sorted_head is None or node.data <= sorted_head.data:
            node.next = sorted_head
            return node

        current = sorted_head

        while current.next and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node

        return sorted_head

    # ОБ'ЄДНАННЯ ДВОХ СПИСКІВ
    def merge_sorted_lists(self, external_list):
        current = LinkedList()

        if not self.sorted:
            self.list_sort_insertion()
        if not external_list.sorted:
            external_list.list_sort_insertion()

        list1 = self
        list2 = external_list

        while list1.head and list2.head:
            if list1.head.data < list2.head.data:
                current.insert_at_end(list1.head.data)
                list1.head = list1.head.next
            else:
                current.insert_at_end(list2.head.data)
                list2.head = list2.head.next

        if list1.head:
            current.insert_at_end(list1.head.data)
        elif list2.head:
            current.insert_at_end(list2.head.data)

        return current


# test
def main():
    llist = LinkedList()

    for _ in range(8):
        random_value = random.randint(1, 100)
        llist.insert_at_end(random_value)
    print(f"Оригінальний список:")
    llist.print_list_v2()

    llist.reverse_linked_list()
    print(f"\nРеверсивний список:")
    llist.print_list_v2()

    print("\nСписок посортований вставками:")
    llist.list_sort_insertion()
    llist.print_list_v2()

    llist2 = LinkedList()
    for _ in range(8):
        random_value = random.randint(1, 100)
        llist2.insert_at_end(random_value)
    print(f"\nДругий список:")
    llist2.print_list_v2()

    print("\nОб'єднання із сортуванням двох списків:")
    merged_list = llist.merge_sorted_lists(llist2)
    merged_list.print_list_v2()


if __name__ == "__main__":
    main()
