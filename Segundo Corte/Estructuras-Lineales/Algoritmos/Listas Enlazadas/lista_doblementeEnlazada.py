class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = node
        node.prev = current

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data)
            current = current.prev
        print(None)

def main():
    array = DoublyLinkedList()
    array.append(1)
    array.append(2)
    array.append(3)

    array.display_backward()

main()
