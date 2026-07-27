class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        current = self.head

        while current.next != self.head:
            current = current.next
        current.next = node
        node.next = self.head

    def search(self, value):
        current = self.head

        while True:
            if current.data == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next != self.head:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break
        print("head")

def main():
    array = CircularLinkedList()
    array.append(1)
    array.append(2)
    array.append(3)

    array.display()

main()
