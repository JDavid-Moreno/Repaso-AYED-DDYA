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

    ## Funciones Adicionales
    def append_position(self, data, position):
        node = Node(data)
        if position == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head
        cont = 0
        while cont < position - 1 and current:
            current = current.next
            cont += 1
        if current is None:
            return

        node.next = current.next
        current.next = node

    def size(self):
        cont = 0
        current = self.head

        while current:
            cont += 1
            current = current.next
        return cont

    def get(self, position):
        cont = 0
        current = self.head

        while current:
            if cont == position:
                return current.data
            current = current.next
            cont += 1

        return None

    def last(self):
        if self.head is None:
            return None
        current = self.head

        while current.next:
            current = current.next
        return current.data

    def update(self, old, new):
        current = self.head

        while current:
            if current.data == old:
                current.data = new
                return
            current = current.next

    def count(self, value):
        total = 0
        current = self.head

        while current:
            if current.data == value:
                total += 1
            current = current.next
        return total

    def max(self):
        maximum = 0
        current = self.head

        while current:
            if maximum < current.data:
                maximum = current.data
            current = current.next
        return maximum

    def min(self):
        current = self.head
        minimum = current.data

        while current:
            if minimum > current.data:
                minimum = current.data
            current = current.next
        return minimum

    def clear(self):
        self.head = None


def main():
    array = LinkedList()
    array.append(1)
    array.append(3)
    array.append(4)
    array.append_position(2,1)

    print(array.size())
    print(array.get(1))
    print(array.last())
    print(array.max())
    print(array.min())


main()
