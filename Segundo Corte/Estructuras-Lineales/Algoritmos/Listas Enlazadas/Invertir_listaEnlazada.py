class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

def main():
    array = LinkedList()
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    array.append(5)
    array.append(6)

    array.display()

    array.reverse()
    array.display()


main()
