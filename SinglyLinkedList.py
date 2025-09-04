import Nodo
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Nodo.Node(data)
        new_node.next = self.head
        self.head = new_node

sll= SinglyLinkedList()
sll.prepend(1)
sll.prepend(2)
print(sll)