class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

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
        return node

    def find_min(self, node):

        while node.left:
            node = node.left

        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1

        return self._count_leaves(node.left) + self ._count_leaves(node.right)

    def min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def invert_tree(self):
        return self._invert_tree(self.root)

    def _invert_tree(self, node):
        if node is None:
            return

        node.left, node.right = node.right, node.left

        self._invert_tree(node.left)
        self._invert_tree(node.right)

def main():
    tree = BinaryTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(9)

    #tree.inorder()
    #tree.preorder()
    #tree.postorder()

    #print(tree.height())
    #print(tree.count_nodes())
    #print(tree.count_leaves())
    #print(tree.min())
    #print(tree.max())
    tree.invert_tree()
    tree.inorder()


main()

