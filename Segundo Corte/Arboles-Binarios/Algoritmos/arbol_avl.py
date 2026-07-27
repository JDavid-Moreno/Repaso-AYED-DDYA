class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)

        elif value > node.value:
            node.right = self._insert(node.right, value)

        else:
            return node

        return self.rebalance(node)

    def search(self, value):
        current = self.root
        while True:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
            return False

    def inorder(self):
        self._inorder(self.root)

    #función auxiliar
    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)

    # función auxiliar
    def _preorder(self, node):
        if node is None:
            return
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    # función auxiliar
    def _postorder(self, node):
        if node is None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        if node is None:
            return node

        return self.rebalance(node)

    def find_min(self, node):

        while node.left:
            node = node.left

        return node

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self):
        return self._get_balance(self.root)

    def _get_balance(self, node):
        if node is None:
            return 0

        return self._get_height(node.left) - self._get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def rebalance(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

def main():
    tree = BinaryTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(9)
    tree.insert(10)
    tree.insert(13)
    tree.inorder()

main()