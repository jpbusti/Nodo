class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # referencia al siguiente nodo

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"
