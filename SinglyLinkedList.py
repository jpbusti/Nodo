import Node
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def prepend(self, data):
        new_node = Node.Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_tail(self, data):
        node = Node(data)
        if self.tail is None:  # lista vacía
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def pop_first(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    
    def pop(self):  # eliminar cola
        if self.is_empty():
            raise IndexError("lista vacía")
        if self._size == 1:
            return self.pop_first()
        prev = self._node_at(self._size - 2)
        data = prev.next.data
        prev.next = None
        self.tail = prev
        self._size -= 1
        return data
    
    def find(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1
    def insert(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("índice fuera de rango")
        if index == 0:
            return self.prepend(data)
        if index == self._size:
            return self.append(data)
        prev = self._node_at(index - 1)
        node = Node.Node(data, prev.next)
        prev.next = node
        self._size += 1

sll= SinglyLinkedList()
sll.prepend(1)
sll.prepend(1)
sll.prepend(2)
sll.prepend(3)
sll.prepend(5)
print(sll.traverse())

sll.insert(2,8)